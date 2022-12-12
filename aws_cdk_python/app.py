#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk_python.aws_cdk_python_stack import AwsCdkPythonStack

app = cdk.App()

env = cdk.Environment(region="us-west-2",account="123456789101")

AwsCdkPythonStack(app, "aws-cdk-python", env=env)

app.synth()