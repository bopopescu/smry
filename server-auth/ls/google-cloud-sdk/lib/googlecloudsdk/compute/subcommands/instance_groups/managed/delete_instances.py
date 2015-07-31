# Copyright 2015 Google Inc. All Rights Reserved.
"""Command for deleting instances managed by instance group manager."""

from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.compute.lib import base_classes
from googlecloudsdk.compute.lib import utils


class DeleteInstances(base_classes.BaseAsyncMutator):
  """Delete instances managed by instance group manager."""

  @staticmethod
  def Args(parser):
    parser.add_argument('instance_group_manager',
                        help='Instance group manager name.')
    parser.add_argument(
        '--instances',
        type=arg_parsers.ArgList(min_length=1),
        action=arg_parsers.FloatingListValuesCatcher(),
        metavar='INSTANCE',
        required=True,
        help='Names of instances to delete.')
    utils.AddZoneFlag(
        parser,
        resource_type='instance group manager',
        operation_type='delete instances')

  def method(self):
    return 'DeleteInstances'

  @property
  def service(self):
    return self.compute.instanceGroupManagers

  @property
  def resource_type(self):
    return 'instanceGroupManagers'

  def CreateRequests(self, args):
    ref = self.CreateZonalReference(args.instance_group_manager, args.zone)
    instances_ref = self.CreateZonalReferences(
        args.instances,
        ref.zone,
        resource_type='instances')
    instances = [instance_ref.SelfLink() for instance_ref in instances_ref]
    return [(self.method(),
             self.messages.ComputeInstanceGroupManagersDeleteInstancesRequest(
                 instanceGroupManager=ref.Name(),
                 instanceGroupManagersDeleteInstancesRequest=(
                     self.messages.InstanceGroupManagersDeleteInstancesRequest(
                         instances=instances,
                     )
                 ),
                 project=self.project,
                 zone=ref.zone,
             ))]


DeleteInstances.detailed_help = {
    'brief': 'Delete instances managed by instance group manager.',
    'DESCRIPTION': """
        *{command}* is used to deletes one or more instances from a managed
        instance group. Once the instances have finished deleting, the size of
        the group is automatically reduced to reflect the changes.

       If you would like to keep the underlying virtual machines but still
       remove them from the managed instance group, use the abandon-instances
       command instead.
        """,
}
