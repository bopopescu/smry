# Copyright 2015 Google Inc. All Rights Reserved.
"""Commands for reading and manipulating instance group managers."""

from googlecloudsdk.calliope import base
from googlecloudsdk.compute.lib import utils


class InstanceGroupManagers(base.Group):
  """Read and manipulate Google Compute Engine instance group managers."""

InstanceGroupManagers.detailed_help = {
    'brief': (
        'Read and manipulate Google Compute Engine instance group managers'),
}
