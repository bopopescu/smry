# Copyright 2014 Google Inc. All Rights Reserved.

"""The 'gcloud test android' sub-group."""

from googlecloudsdk.calliope import base


class Android(base.Group):
  """Command group for Android-specific testing."""

  @staticmethod
  def Args(parser):
    """Method called by Calliope to register flags common to this sub-group.

    Args:
      parser: An argparse parser used to add arguments that immediately follow
          this group in the CLI. Positional arguments are allowed.
    """
