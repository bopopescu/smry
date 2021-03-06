# Copyright 2014 Google Inc. All Rights Reserved.
"""Command for deleting HTTP health checks."""
from googlecloudsdk.compute.lib import base_classes


class Delete(base_classes.GlobalDeleter):
  """Delete HTTP health checks."""

  @staticmethod
  def Args(parser):
    cli = Delete.GetCLIGenerator()
    base_classes.GlobalDeleter.Args(parser, 'compute.httpHealthChecks', cli,
                                    'compute.http-health-checks')

  @property
  def service(self):
    return self.compute.httpHealthChecks

  @property
  def resource_type(self):
    return 'httpHealthChecks'


Delete.detailed_help = {
    'brief': 'Delete HTTP health checks',
    'DESCRIPTION': """\
        *{command}* deletes one or more Google Compute Engine
        HTTP health checks.
        """,
}
