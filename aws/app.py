#!/usr/bin/env python3

from aws_cdk import core

from aws_batch_poc.aws_batch_poc_stack import AwsBatchPocStack


app = core.App()
AwsBatchPocStack(app, "aws-batch-poc")

app.synth()
