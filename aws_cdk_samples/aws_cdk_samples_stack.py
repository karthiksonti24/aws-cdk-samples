from aws_cdk import core as cdk
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_s3 as s3

class AwsCdkSamplesStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "VpcFromCDK", cidr="10.0.0.0/16")

        cdk.CfnOutput(self, 'vpcId', value=vpc.vpc_id)

        s3Bucket = s3.Bucket(self, "S3FromCDK", versioned=True, removal_policy=cdk.RemovalPolicy.DESTROY, auto_delete_objects=True)

        cdk.CfnOutput(self , 'bucketName', value=s3Bucket.bucket_name)