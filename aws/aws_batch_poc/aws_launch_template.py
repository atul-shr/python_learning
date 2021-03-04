from aws_cdk import (core,
                     aws_ec2 as ec2,
                     aws_batch as batch,
                     aws_iam as iam
                     )


class CdwLaunchTemplate:
    def __init__(self):
        self.var_launch_template = None 


    def get_luanch_template(self):
        return ec2.LaunchTemplate(self, id='sample_poc', block_devices=None, cpu_credits=None,
                                                       detailed_monitoring=None, disable_api_termination=None,
                                                       ebs_optimized=None, hibernation_configured=None,
                                                       instance_initiated_shutdown_behavior=None, instance_type=None,
                                                       key_name=None, launch_template_name=None, machine_image=None,
                                                       nitro_enclave_enabled=None, role=None, security_group=None,
                                                       spot_options=None, user_data=None)