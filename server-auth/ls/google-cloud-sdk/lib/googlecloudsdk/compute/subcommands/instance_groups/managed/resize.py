# Copyright 2015 Google Inc. All Rights Reserved.
"""Command for setting size of instance group manager."""
from googlecloudsdk.compute.lib import base_classes
from googlecloudsdk.compute.lib import utils


class Resize(base_classes.BaseAsyncMutator):
  """Set size of instance group manager."""

  @staticmethod
  def Args(parser):
    parser.add_argument('instance_group_manager',
                        help='Instance group manager name.')
    parser.add_argument(
        '--size',
        required=True,
        type=int,
        help=('The number of instances in the instance group manged by the '
              'instance group manager.'))
    utils.AddZoneFlag(
        parser,
        resource_type='instance group manager',
        operation_type='resize')

  def method(self):
    return 'Resize'

  @property
  def service(self):
    return self.compute.instanceGroupManagers

  @property
  def resource_type(self):
    return 'instanceGroupManagers'

  def CreateRequests(self, args):
    ref = self.CreateZonalReference(args.instance_group_manager, args.zone)
    return [(self.method(),
             self.messages.ComputeInstanceGroupManagersResizeRequest(
                 instanceGroupManager=ref.Name(),
                 size=args.size,
                 project=self.project,
                 zone=ref.zone,))]


Resize.detailed_help = {
    'brief': 'Set size for instance group manager.',
    'DESCRIPTION': """
        *{command}* resize a managed instance group to a provided size.

       If you resize down, the Instance Group Manager service deletes instances
       from the group until the group reaches the desired size. To understand
       what order the instances will be deleted in, please see the API
       documentation.

       If you resize up, the service adds instances to the group using the most
       current instance template until the group reaches the desired size.
        """,
}
