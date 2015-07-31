# Copyright 2015 Google Inc. All Rights Reserved.
"""Command for describing instance group managers."""
from googlecloudsdk.compute.lib import autoscaler_util
from googlecloudsdk.compute.lib import base_classes


class Describe(base_classes.ZonalDescriber):
  """Describe an instance group manager."""

  @staticmethod
  def Args(parser):
    base_classes.ZonalDescriber.Args(parser)
    base_classes.AddFieldsFlag(parser, 'instanceGroupManagers')

  @property
  def service(self):
    return self.compute.instanceGroupManagers

  @property
  def resource_type(self):
    return 'instanceGroupManagers'

  def ComputeDynamicProperties(self, args, items):
    """Add Autoscaler information if Autoscaler is defined for the item."""
    # Items are expected to be IGMs.
    return autoscaler_util.AddAutoscalersToMigs(
        migs_iterator=items,
        project=self.project,
        compute=self.compute,
        http=self.http,
        batch_url=self.batch_url,
        fail_when_api_not_supported=False)


Describe.detailed_help = {
    'brief': 'Describe an instance group manager',
    'DESCRIPTION': """\
        *{command}* displays all data associated with a Google Compute
        Engine instance group manager.
        """,
}
