from aws_cdk import (core,
                     aws_ec2 as ec2,
                     aws_batch as batch,
                     aws_iam as iam
                     )
from typing import Union, TypeVar


class AwsBatchPocStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # subnet_id = ec2.CfnSubnet(self, id='vpc-d22ed2b9', cidr_block='172.31.0.0/16', vpc_id='vpc-d22ed2b9')
        # print(subnet_id)

        vpc_id = ec2.Vpc.from_lookup(self, id='vpc-d22ed2b9', vpc_id='vpc-d22ed2b9')

        print(vpc_id)
        
        iam_sr = iam.Role.from_role_arn(self, id='arn:aws:iam::340444537094:role/POC_LUSID_BATCH_SR', role_arn='arn:aws:iam::340444537094:role/POC_LUSID_BATCH_SR') 

        managed_batch_resources = batch.ComputeResources(vpc=vpc_id, allocation_strategy=None, bid_percentage=None,
                                                         compute_resources_tags=None, desiredv_cpus=None,
                                                         ec2_key_pair=None, image=None, instance_role=None,
                                                         instance_types=None, launch_template=None, maxv_cpus=None,
                                                         minv_cpus=None, placement_group=None, security_groups=None,
                                                         spot_fleet_role=None, type=None, vpc_subnets=None)

        print(type(managed_batch_resources))

        managed_batch = batch.ComputeEnvironment(self,
                                                 id='managed_compute_batch_lusid_poc',
                                                 service_role=iam_sr,
                                                 managed=True,
                                                 compute_environment_name='managed_compute_batch_lusid_poc',
                                                 compute_resources=managed_batch_resources,
                                                 enabled=False
                                                 )
