from aws_cdk import (core,
                     aws_ec2 as ec2,
                     aws_batch as batch,
                     aws_iam as iam,
                     aws_ecs as ecs
                     )
import json
import os

print(os.getcwd())

with open('/home/ec2-user/environment/aws-batch-poc/aws_batch_poc/stack_config.json') as f:
    cfg_data = json.load(f)


# print(cfg_data["vpc_id"])

class AwsBatchPocStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # subnet_id = ec2.CfnSubnet(self, id='vpc-d22ed2b9', cidr_block='172.31.0.0/16', vpc_id='vpc-d22ed2b9')
        # print(subnet_id)

        ecs_img = ecs.EcsOptimizedImage.amazon_linux2()
        print(ecs_img)

        ins_class_c5 = ec2.InstanceClass.COMPUTE5
        ins_class_m5 = ec2.InstanceClass.MEMORY5
        ins_class_r5 = ec2.InstanceClass.STANDARD5
        ins_size_m = ec2.InstanceSize.MEDIUM

        ins_typ_c5 = ec2.InstanceType.of(ins_class_c5, ins_size_m)
        ins_typ_m5 = ec2.InstanceType.of(ins_class_m5, ins_size_m)
        ins_typ_r5 = ec2.InstanceType.of(ins_class_r5, ins_size_m)

        vpc_id = ec2.Vpc.from_lookup(self, id=cfg_data["vpc_id"], vpc_id=cfg_data["vpc_id"])

        print(vpc_id)

        iam_sr = iam.Role.from_role_arn(self, id=cfg_data["service_role"],
                                        role_arn=cfg_data["service_role"])

        sec_grp = ec2.SecurityGroup(self,
                                    id=cfg_data["security_group_name"],
                                    vpc=vpc_id,
                                    allow_all_outbound=True,
                                    description=cfg_data["security_group_name"],
                                    security_group_name=cfg_data["security_group_name"]
                                    )

        sec_grp.add_ingress_rule(peer=ec2.Peer.ipv4("10.166.233.0/24"), connection=ec2.Port.tcp(22),
                                 description=cfg_data["security_ingress1"])
        sec_grp.add_ingress_rule(peer=ec2.Peer.ipv4("10.166.232.0/24"), connection=ec2.Port.tcp(22),
                                 description=cfg_data["security_ingress2"])
        # sec_grp.add_egress_rule(peer=ec2.Peer.ipv4("0.0.0.0/0"), connection=ec2.Port.all_traffic(),
        #                         description=cfg_data["security_egress"])

        obj_block_device = ec2.BlockDevice(device_name="/dev/xvda",
                                                                               volume=ec2.BlockDeviceVolume(
                                                                                   ebs_device=ec2.EbsDeviceProps(
                                                                                       delete_on_termination=True,
                                                                                       volume_size=75,
                                                                                       volume_type=ec2.EbsDeviceVolumeType.GP2
                                                                                   )
                                                                               )
                                                                               )
                                                                               
        print(obj_block_device)                    
        
        obj_user_data = ec2.UserData.add_commands("echo yes")

        obj_launch_template = ec2.LaunchTemplate(self,
                                                 id=cfg_data["luanch_template_name"],
                                                 block_devices=None,
                                                 cpu_credits=None,
                                                 detailed_monitoring=None,
                                                 disable_api_termination=None,
                                                 ebs_optimized=None,
                                                 hibernation_configured=None,
                                                 instance_initiated_shutdown_behavior=None,
                                                 instance_type=None,
                                                 key_name=None,
                                                 launch_template_name=cfg_data["luanch_template_name"],
                                                 machine_image=None,
                                                 nitro_enclave_enabled=None,
                                                 role=None,
                                                 security_group=None,
                                                 spot_options=None,
                                                 user_data=None)

        managed_batch_resources = batch.ComputeResources(vpc=vpc_id,
                                                         allocation_strategy=None,
                                                         bid_percentage=None,
                                                         compute_resources_tags=None,
                                                         desiredv_cpus=None,
                                                         ec2_key_pair="batch-compute",
                                                         image=ecs_img,
                                                         instance_role=None,
                                                         instance_types=[ins_typ_c5, ins_typ_m5, ins_typ_r5],
                                                         launch_template=None,
                                                         maxv_cpus=cfg_data["max_cpus"],
                                                         minv_cpus=cfg_data["min_cpus"],
                                                         placement_group=None,
                                                         security_groups=None,
                                                         spot_fleet_role=None,
                                                         type=batch.ComputeResourceType.ON_DEMAND,
                                                         vpc_subnets=None)

        print(type(managed_batch_resources))

        managed_batch = batch.ComputeEnvironment(self,
                                                 id=cfg_data["stack_name"],
                                                 service_role=iam_sr,
                                                 managed=True,
                                                 compute_environment_name=cfg_data["stack_name"],
                                                 compute_resources=managed_batch_resources,
                                                 enabled=True
                                                 )
