# Copyright 2015 Google Inc. All Rights Reserved.

"""Simple console pager."""

import os
import re
import sys

from googlecloudsdk.core.console import console_attr


class Pager(object):
  """A simple console text pager.

  This pager requires the entire contents to be available. The contents are
  written one page of lines at a time. The prompt is written after each page of
  lines. A one character response is expected. See HELP_TEXT below for more
  info.

  The contents are written as is. For example, ANSI control codes will be in
  effect. This is different from pagers like more(1) which is ANSI control code
  agnostic and miscalculates line lengths, and less(1) which displays control
  character names by default.

  Attrinutes:
    _attr: The current ConsoleAttr handle.
    _clear: A string that clears the prompt when written to _out.
    _contents: The entire contents of the text lines to page.
    _height: The terminal height in characters.
    _out: The output stream, log.out (effectively) if None.
    _prompt: The page break prompt.
    _search_direction: The search direction command, n:forward, N:reverse.
    _search_pattern: The current forward/reverse search compiled RE.
    _width: The termonal width in characters.
  """

  HELP_TEXT = """
  Simple pager commands:

    b, ^B, <PAGE-UP>
      Back one page.
    f, ^F, <SPACE>, <PAGE-DOWN>
      Forward one page. Does not quit if there are no more lines.
    g, <HOME>
      Back to the first page.
    <number>g
      Go to <number> lines from the top.
    G, <END>
      Forward to the last page.
    <number>G
      Go to <number> lines from the bottom.
    h
      Print pager command help.
    j, +, <DOWN-ARROW>
      Forward one line.
    k, -, <UP-ARROW>
      Back one line.
    /pattern
      Forward search for pattern.
    ?pattern
      Backward search for pattern.
    n
      Repeat current search.
    N
      Repeat current search in the opposite direction.
    q, Q, ^C, ^D, ^Z
      Quit return to the caller.
    any other character
      Prompt again.

  Hit any key to continue:"""

  # This dict maps ANSI key codes to pager commands. For example, the ANSI
  # page up key code is <ESC>S and that corresponds to the pager b command.
  _ANSI_TO_COMMAND = {
      'A': 'k',
      'B': 'j',
      'C': 'G',
      'D': 'g',
      'F': 'G',
      'H': 'g',
      'M': 'j',
      'S': 'b',
      'T': 'f',
      '5': 'b',
      '6': 'f',
      }

  def __init__(self, contents, out=None, prompt=None):
    """Constructor.

    Args:
      contents: The entire contents of the text lines to page.
      out: The output stream, log.out (effectively) if None.
      prompt: The page break prompt, a defalt prompt is used if None..
    """
    self._contents = contents
    self._out = out or sys.stdout
    self._search_pattern = None
    self._search_direction = None

    # Initialize the console attributes.
    self._attr = console_attr.GetConsoleAttr(out=out)
    self._width, self._height = self._attr.GetTermSize()

    # Initialize the prompt and the prompt clear string.
    if not prompt:
      prompt = '{bold}--({{percent}}%)--{normal}'.format(
          bold=self._attr.GetFontCode(bold=True),
          normal=self._attr.GetFontCode())
    self._clear = '\r{0}\r'.format(' ' * (self._attr.PrintWidth(prompt) - 6))
    self._prompt = prompt

    # Initialize a list of lines with long lines split into separate display
    # lines.
    self._lines = []
    for line in contents.splitlines():
      self._lines += self._attr.SplitLine(line, self._width)

  def _GetANSIKeyCommand(self):
    """Consumes an ANSI key sequence and returns the pager equivalent command.

    The initial CSI (control sequnce indicator) has already been consumed.

    Returns:
      A command character or '' to silently ignore the ANSI key.
    """
    c = self._attr.GetRawChar()
    while True:
      if c.isalpha():
        break
      prev_c = c
      c = self._attr.GetRawChar()
      if c == '~':
        c = prev_c
        break
    # Map the control sequence command char to a pager command char.
    # Unknown keys are silently ignored via ''.
    return self._ANSI_TO_COMMAND.get(c, '')

  def _GetSearchCommand(self, c):
    """Consumes a search command and returns the equivalent pager command.

    The search pattern is an RE that is pre-compiled and cached for subsequent
    /<newline>, ?<newline>, n, or N commands.

    Args:
      c: The search command char.

    Returns:
      The pager command char.
    """
    self._out.write(c)
    buf = ''
    while True:
      p = self._attr.GetRawChar()
      if p in ('\n', '\r'):
        break
      self._out.write(p)
      buf += p
    self._out.write('\r' + ' ' * len(buf) + '\r')
    if buf:
      try:
        self._search_pattern = re.compile(buf)
      except re.error:
        # Silently ignore pattern errors.
        self._search_pattern = None
        return ''
    self._search_direction = 'n' if c == '/' else 'N'
    return 'n'

  def _Help(self):
    """Print command help and wait for any character to continue."""
    clear = self._height - (len(self.HELP_TEXT) -
                            len(self.HELP_TEXT.replace('\n', '')))
    if clear > 0:
      self._out.write('\n' * clear)
    self._out.write(self.HELP_TEXT)
    self._attr.GetRawChar()
    self._out.write(os.linesep)

  def Run(self):
    """Run the pager."""
    # No paging if the contents are small enough.
    if len(self._lines) <= self._height:
      self._out.write(self._contents)
      return

    # Save room for the prompt at the bottom of the page.
    self._height -= 1

    # Loop over all the pages.
    pos = 0
    while pos < len(self._lines):
      # Write a page of lines.
      nxt = pos + self._height
      if nxt > len(self._lines):
        nxt = len(self._lines)
        pos = nxt - self._height
      self._out.write(os.linesep.join(self._lines[pos:nxt]) + os.linesep)

      # Handle the prompt response.
      percent = self._prompt.format(percent=100 * nxt / len(self._lines))
      digits = ''
      while True:
        self._out.write(percent)
        c = self._attr.GetRawChar()
        self._out.write(self._clear)

        # Parse the command.
        if c in (None,    # EOF.
                 'q',     # Quit.
                 'Q',     # Quit.
                 '\x03',  # ^C  (unix & windows terminal interrupt)
                 '\x04',  # ^D  (unix terminal input EOF)
                 '\x1a',  # ^Z  (windows terminal input EOF)
                ):
          # Quit.
          return
        elif c == '\x1b':  # ASCII <ESC> indicating possible ANSI key sequence.
          c = self._GetANSIKeyCommand()
        elif c in ('/', '?'):
          c = self._GetSearchCommand(c)
        elif c.isdigit():
          # Collect digits for operation count.
          digits += c
          continue

        # Set the optional command count.
        if digits:
          count = int(digits)
          digits = ''
        else:
          count = 0

        # Finally commit to command c.
        if c in ('b', '\x02'):
          # Previous page.
          nxt = pos - self._height
          if nxt < 0:
            nxt = 0
        elif c in ('f', '\x06', ' '):
          # Next page.
          if nxt >= len(self._lines):
            continue
          nxt = pos + self._height
          if nxt >= len(self._lines):
            nxt = pos
        elif c in ('g', 'G'):
          # First or last page.
          if c == 'g':
            nxt = count - 1
          else:
            nxt = len(self._lines) - count
          if nxt > len(self._lines) - self._height:
            nxt = len(self._lines) - self._height
          if nxt < 0:
            nxt = 0
        elif c == 'h':
          self._Help()
          nxt = pos
          break
        elif c in ('j', '+', '\n', '\r'):
          # Next line.
          if nxt >= len(self._lines):
            continue
          nxt = pos + 1
          if nxt >= len(self._lines):
            nxt = pos
        elif c in ('k', '-'):
          # Previous line.
          nxt = pos - 1
          if nxt < 0:
            nxt = 0
        elif c in ('n', 'N'):
          # Next pattern match search.
          if not self._search_pattern:
            continue
          nxt = pos
          i = pos
          direction = 1 if c == self._search_direction else -1
          while True:
            i += direction
            if i < 0 or i >= len(self._lines):
              break
            if self._search_pattern.search(self._lines[i]):
              nxt = i
              break
        else:
          # Silently ignore everything else.
          continue
        if nxt != pos:
          break
      pos = nxt
