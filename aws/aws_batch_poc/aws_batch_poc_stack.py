from aws_cdk import (core,
    aws_ec2 as ec2,
    aws_batch as batch
)
from typing import Union,TypeVar

class AwsBatchPocStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # The code that defines your stack goes here
        
        subnet_id = ec2.CfnSubnet(self, id='vpc-d22ed2b9', cidr_block='172.31.0.0/16', vpc_id='vpc-d22ed2b9')
        print(subnet_id)
        
        managed_batch_resources = batch.CfnComputeEnvironment.ComputeResourcesProperty(maxv_cpus=32, 
                                                                                subnets=subnet_id, 
                                                                                type='MANAGED', 
                                                                                allocation_strategy=None, 
                                                                                bid_percentage=None, 
                                                                                desiredv_cpus=None, 
                                                                                ec2_configuration=None, 
                                                                                ec2_key_pair=None, 
                                                                                image_id=None, 
                                                                                instance_role=None, 
                                                                                instance_types=None, 
                                                                                launch_template=None, 
                                                                                minv_cpus=None, 
                                                                                placement_group=None, 
                                                                                security_group_ids=None, 
                                                                                spot_iam_fleet_role=None, 
                                                                                tags=None)
        
        print(managed_batch_resources)
        
        managed_batch = batch.CfnComputeEnvironment(self, 
                                                    id='managed_compute_batch_lusid_poc',
                                                    service_role='managed_compute_batch_lusid_poc_sr',
                                                    type='MANAGED',
                                                    compute_environment_name='managed_compute_batch_lusid_poc',
                                                    compute_resources=['', managed_batch_resources, None],
                                                    state='DISABLED'
                                                    )
        
