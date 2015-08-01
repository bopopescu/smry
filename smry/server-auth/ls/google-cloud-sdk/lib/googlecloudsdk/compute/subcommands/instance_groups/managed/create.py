# Copyright 2015 Google Inc. All Rights Reserved.
"""Command for creating instance group managers."""
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.compute.lib import base_classes
from googlecloudsdk.compute.lib import utils
from googlecloudsdk.compute.lib import zone_utils


class Create(base_classes.BaseAsyncCreator, zone_utils.ZoneResourceFetcher):
  """Create Google Compute Engine instance group managers."""

  @staticmethod
  def Args(parser):
    parser.add_argument('name', help='Instance group manager name.')
    parser.add_argument(
        '--template',
        required=True,
        help=('Compute Engine instance template resource to be used.'))
    parser.add_argument(
        '--base-instance-name',
        required=True,
        help=('The base name to use for the Compute Engine instances that will '
              'be created with the instance group manager.'))
    parser.add_argument(
        '--size',
        required=True,
        help=('Initial number of instances in the instance group managed by '
              'the instance group manager.'))
    parser.add_argument(
        '--description',
        help='Instance group manager description.')
    parser.add_argument(
        '--target-pool',
        type=arg_parsers.ArgList(),
        action=arg_parsers.FloatingListValuesCatcher(),
        metavar='TARGET_POOL',
        help=('Compute Engine Target Pools to add the instances to. '
              'Target Pools must can specified by name or by URL. Example: '
              '--target-pools target-pool-1 target-pool-2'))
    utils.AddZoneFlag(
        parser,
        resource_type='instance group manager',
        operation_type='create')

  @property
  def service(self):
    return self.compute.instanceGroupManagers

  @property
  def method(self):
    return 'Insert'

  @property
  def resource_type(self):
    return 'instanceGroupManagers'

  def CreateRequests(self, args):
    """Creates and returns an instanceGroupManagers.Insert request.

    Args:
      args: the argparse arguments that this command was invoked with.

    Returns:
      request: a singleton list containing
               ComputeManagedInstanceGroupsInsertRequest message object.
    """
    group_ref = self.CreateZonalReference(args.name, args.zone)
    self.WarnForZonalCreation([group_ref])
    template_ref = self.CreateGlobalReference(args.template,
                                              resource_type='instanceTemplates')
    if args.target_pool:
      region = utils.ZoneNameToRegionName(group_ref.zone)
      pool_refs = self.CreateRegionalReferences(
          args.target_pool, region, resource_type='targetPools')
      pools = [pool_ref.SelfLink() for pool_ref in pool_refs]
    else:
      pools = []

    instance_group_manager = self.messages.InstanceGroupManager(
        name=group_ref.Name(),
        zone=group_ref.zone,
        baseInstanceName=args.base_instance_name,
        description=args.description,
        instanceTemplate=template_ref.SelfLink(),
        targetPools=pools,
        targetSize=int(args.size))
    request = self.messages.ComputeInstanceGroupManagersInsertRequest(
        instanceGroupManager=instance_group_manager,
        project=self.project,
        zone=group_ref.zone,
    )

    return [request]

Create.detailed_help = {
    'brief': 'Create a Compute Engine instance group manager',
    'DESCRIPTION': """\
        *{command}* creates of Google Compute Engine instance group managers.
        For example, running:

          $ {command} example-instance-group-manager --zone us-central1-a

        will create one instance group manager called 'example-instance-group'
        in the ``us-central1-a'' zone.
        """,
}
