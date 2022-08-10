# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetAwsCrossaccountPolicyResult',
    'AwaitableGetAwsCrossaccountPolicyResult',
    'get_aws_crossaccount_policy',
    'get_aws_crossaccount_policy_output',
]

@pulumi.output_type
class GetAwsCrossaccountPolicyResult:
    """
    A collection of values returned by getAwsCrossaccountPolicy.
    """
    def __init__(__self__, id=None, json=None, pass_roles=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if pass_roles and not isinstance(pass_roles, list):
            raise TypeError("Expected argument 'pass_roles' to be a list")
        pulumi.set(__self__, "pass_roles", pass_roles)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def json(self) -> str:
        """
        AWS IAM Policy JSON document
        """
        return pulumi.get(self, "json")

    @property
    @pulumi.getter(name="passRoles")
    def pass_roles(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "pass_roles")


class AwaitableGetAwsCrossaccountPolicyResult(GetAwsCrossaccountPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAwsCrossaccountPolicyResult(
            id=self.id,
            json=self.json,
            pass_roles=self.pass_roles)


def get_aws_crossaccount_policy(pass_roles: Optional[Sequence[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAwsCrossaccountPolicyResult:
    """
    > **Note** This resource has an evolving API, which may change in future versions of the provider. Please always consult [latest documentation](https://docs.databricks.com/administration-guide/account-api/iam-role.html#language-Your%C2%A0VPC,%C2%A0default) in case of any questions.

    This data source constructs necessary AWS cross-account policy for you, which is based on [official documentation](https://docs.databricks.com/administration-guide/account-api/iam-role.html#language-Your%C2%A0VPC,%C2%A0default).

    ## Example Usage

    For more detailed usage please see get_aws_assume_role_policy or AwsS3Mount pages.

    ```python
    import pulumi
    import pulumi_databricks as databricks

    this = databricks.get_aws_crossaccount_policy()
    ```
    ## Related Resources

    The following resources are used in the same context:

    * Provisioning AWS Databricks E2 with a Hub & Spoke firewall for data exfiltration protection guide
    * get_aws_assume_role_policy data to construct the necessary AWS STS assume role policy.
    * get_aws_bucket_policy data to configure a simple access policy for AWS S3 buckets, so that Databricks can access data in it.
    * InstanceProfile to manage AWS EC2 instance profiles that users can launch Cluster and access data, like databricks_mount.


    :param Sequence[str] pass_roles: List of Data IAM role ARNs that are explicitly granted `iam:PassRole` action.
    """
    __args__ = dict()
    __args__['passRoles'] = pass_roles
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('databricks:index/getAwsCrossaccountPolicy:getAwsCrossaccountPolicy', __args__, opts=opts, typ=GetAwsCrossaccountPolicyResult).value

    return AwaitableGetAwsCrossaccountPolicyResult(
        id=__ret__.id,
        json=__ret__.json,
        pass_roles=__ret__.pass_roles)


@_utilities.lift_output_func(get_aws_crossaccount_policy)
def get_aws_crossaccount_policy_output(pass_roles: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAwsCrossaccountPolicyResult]:
    """
    > **Note** This resource has an evolving API, which may change in future versions of the provider. Please always consult [latest documentation](https://docs.databricks.com/administration-guide/account-api/iam-role.html#language-Your%C2%A0VPC,%C2%A0default) in case of any questions.

    This data source constructs necessary AWS cross-account policy for you, which is based on [official documentation](https://docs.databricks.com/administration-guide/account-api/iam-role.html#language-Your%C2%A0VPC,%C2%A0default).

    ## Example Usage

    For more detailed usage please see get_aws_assume_role_policy or AwsS3Mount pages.

    ```python
    import pulumi
    import pulumi_databricks as databricks

    this = databricks.get_aws_crossaccount_policy()
    ```
    ## Related Resources

    The following resources are used in the same context:

    * Provisioning AWS Databricks E2 with a Hub & Spoke firewall for data exfiltration protection guide
    * get_aws_assume_role_policy data to construct the necessary AWS STS assume role policy.
    * get_aws_bucket_policy data to configure a simple access policy for AWS S3 buckets, so that Databricks can access data in it.
    * InstanceProfile to manage AWS EC2 instance profiles that users can launch Cluster and access data, like databricks_mount.


    :param Sequence[str] pass_roles: List of Data IAM role ARNs that are explicitly granted `iam:PassRole` action.
    """
    ...
