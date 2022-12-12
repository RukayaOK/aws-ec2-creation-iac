from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)

class AwsCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.instance_ami = "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20221201"
        self.instance_type = "t3.micro"
        self.vpc_id = "vpc-04f6fe67c88e555ef"
        self.security_group_id = "sg-083ed0694a6575fbc"
        self.key_name = "my-aws-cdk-created-key-pair"
        self.key_type = "rsa"

        cfn_key_pair = ec2.CfnKeyPair(
            self
            , "MyCfnKeyPair"
            , key_name=self.key_name
            , key_type=self.key_type
        )

        vpc = ec2.Vpc.from_lookup(
            self
            , "vpc"
            , vpc_id=self.vpc_id
        )

        security_group = ec2.SecurityGroup.from_lookup_by_id(
            self
            , "security_group"
            , security_group_id=self.security_group_id
        )

        instance = ec2.Instance(
            self
            , "Instance"
            , instance_type=ec2.InstanceType(self.instance_type)
            , machine_image=ec2.MachineImage().lookup(name=self.instance_ami)
            , vpc = vpc
            , security_group = security_group
            , key_name= cfn_key_pair.key_name
        )