"""This creates an entry on SSM to register this service's API URL every time it is
deployed / updated, so it can be discovered by other services.
"""
import boto3
from botocore.exceptions import ClientError


def callback(zappa_cli):
    api_gateway_url = zappa_cli.zappa.get_api_url(zappa_cli.lambda_name, zappa_cli.api_stage)

    ssm_client = boto3.client("ssm")
    name = f"/{zappa_cli.project_name}/{zappa_cli.api_stage}/api_url"

    try:
        param = ssm_client.get_parameter(Name=name)
    except ClientError:
        print(f"URL not found for {zappa_cli.project_name} on stage {zappa_cli.api_stage}.")
        param = {"Parameter": {"Value": "NOT FOUND"}}

    if param["Parameter"]["Value"] != api_gateway_url:
        print("API Gateway has a new URL.")
        ssm_client.put_parameter(
            Name=name,
            Description="API access URL.",
            Value=api_gateway_url,
            Type="String",
            Overwrite=True,
        )
    else:
        print("API Gateway has the same URL.")
