#!/usr/bin/env python3

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from aws_cdk_samples.aws_cdk_samples_stack import AwsCdkSamplesStack


app = core.App()

AwsCdkSamplesStack(app, "AwsCdkSamplesStack", env=core.Environment(account="932770550094", region="eu-west-1"))

app.synth()
