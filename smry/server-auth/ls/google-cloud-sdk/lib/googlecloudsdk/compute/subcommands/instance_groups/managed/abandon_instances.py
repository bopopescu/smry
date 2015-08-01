# Copyright 2015 Google Inc. All Rights Reserved.
"""Command for abandoning instances managed by the instance group manager."""

from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.compute.lib import base_classes
from googlecloudsdk.compute.lib import utils


class AbandonInstances(base_classes.BaseAsyncMutator):
  """Abandon instances managed by instance group manager."""

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
        help='Names of instances to abandon.')
    utils.AddZoneFlag(
        parser,
        resource_type='instance group manager',
        operation_type='abandon instances')

  def method(self):
    return 'AbandonInstances'

  @property
  def service(self):
    return self.compute.instanceGroupManagers

  @property
  def resource_type(self):
    return 'instanceGroupManagers'

  def CreateRequests(self, args):
    zone_ref = self.CreateZonalReference(args.instance_group_manager, args.zone)
    instance_refs = self.CreateZonalReferences(
        args.instances,
        zone_ref.zone,
        resource_type='instances')
    instances = [instance_ref.SelfLink() for instance_ref in instance_refs]
    return [(self.method(),
             self.messages.ComputeInstanceGroupManagersAbandonInstancesRequest(
                 instanceGroupManager=zone_ref.Name(),
                 instanceGroupManagersAbandonInstancesRequest=(
                     self.messages.InstanceGroupManagersAbandonInstancesRequest(
                         instances=instances,
                     )
                 ),
                 project=self.project,
                 zone=zone_ref.zone,
             ),),]


AbandonInstances.detailed_help = {
    'brief': 'Abandon instances managed by instance group manager.',
    'DESCRIPTION': """
        *{command}* abandons one or more instances from a managed instance
        group, thereby reducing the intendedSize of the group. Once the
        instances have been abandoned, the currentSize of the group is
        automatically reduced as well to reflect the changes.

       If you would like to delete the underlying virtual machines instead of
       only moving them out of the managed instance group, use the
       delete-instances command instead.
        """,
}
