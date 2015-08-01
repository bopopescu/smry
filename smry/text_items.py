"""
Text Items
    W. R. Emanuel, University of Maryland, College Park
    E-Mail: wemanuel@umd.edu
    Gmail: wemanuel@gmail.com
"""

import os
import logging

import markdown

from smry.models import TextItem

# Create a logging service.
# smrylogger = logging.getLogger("smry")
# smrylogger.setLevel(logging.WARNING)

def get_txt_html(view, name, number=None, replace=None):
    """
    get_txt_html(view, name, number=None, replace=None)
    """
    txt_obj = text_item_filter(view, name, number=number)
    html = process_txt_itm(txt_obj.text, replace=replace)
    txt_obj = None
    return html

def process_txt_itm(txt_itm, replace=None):
    """
    process_txt_itm(txt_itm, replace=None)
    
    Process a text string, potentially containing markdown
    into html. The replace option is a dictionary mapping
    text to replace to corresponding replacement text.
    
    Example usage:
    html = process_txt_itm(sample_text, replace = {"<p>": ""})
    """
    # Process markdown.
    html = markdown.markdown(txt_itm)

    # Replace specified strings.
    if replace:
        for key in replace.keys():
            html = html.replace(key, replace[key])

#     smrylogger.debug("process_txt_itm( )|html: %s", html[0 : 80])         
        
    return html

def text_item_filter(view, name, number=None):
    """
    text_item_filter(view, name, number=None)

    Filter text items with respect to the specified view,
    name, and number.

    text_item_filter() return a text_item_object.
    """
#     log_str = "text_item_filter|name: %s, view: %s, number: %d"
#     smrylogger.debug(log_str, name, view, number)

    # Filter for view and name.
    txt_objs = TextItem.objects.filter(view__contains=view)

    txt_objs = txt_objs.filter(name__contains = name)

    if number:    
        # Filter for number.
        txt_objs = txt_objs.filter(number__contains=number)

    text_item_obj = txt_objs[0]

    return text_item_obj
