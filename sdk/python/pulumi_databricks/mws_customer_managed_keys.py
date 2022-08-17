# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['MwsCustomerManagedKeysArgs', 'MwsCustomerManagedKeys']

@pulumi.input_type
class MwsCustomerManagedKeysArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 aws_key_info: pulumi.Input['MwsCustomerManagedKeysAwsKeyInfoArgs'],
                 use_cases: pulumi.Input[Sequence[pulumi.Input[str]]],
                 creation_time: Optional[pulumi.Input[int]] = None,
                 customer_managed_key_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MwsCustomerManagedKeys resource.
        :param pulumi.Input[str] account_id: Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        :param pulumi.Input['MwsCustomerManagedKeysAwsKeyInfoArgs'] aws_key_info: This field is a block and is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_cases: *(since v0.3.4)* List of use cases for which this key will be used. *If you've used the resource before, please add `use_cases = ["MANAGED_SERVICES"]` to keep the previous behaviour.* Possible values are:
        :param pulumi.Input[int] creation_time: (Integer) Time in epoch milliseconds when the customer key was created.
        :param pulumi.Input[str] customer_managed_key_id: (String) ID of the encryption key configuration object.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "aws_key_info", aws_key_info)
        pulumi.set(__self__, "use_cases", use_cases)
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if customer_managed_key_id is not None:
            pulumi.set(__self__, "customer_managed_key_id", customer_managed_key_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="awsKeyInfo")
    def aws_key_info(self) -> pulumi.Input['MwsCustomerManagedKeysAwsKeyInfoArgs']:
        """
        This field is a block and is documented below.
        """
        return pulumi.get(self, "aws_key_info")

    @aws_key_info.setter
    def aws_key_info(self, value: pulumi.Input['MwsCustomerManagedKeysAwsKeyInfoArgs']):
        pulumi.set(self, "aws_key_info", value)

    @property
    @pulumi.getter(name="useCases")
    def use_cases(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        *(since v0.3.4)* List of use cases for which this key will be used. *If you've used the resource before, please add `use_cases = ["MANAGED_SERVICES"]` to keep the previous behaviour.* Possible values are:
        """
        return pulumi.get(self, "use_cases")

    @use_cases.setter
    def use_cases(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "use_cases", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        """
        (Integer) Time in epoch milliseconds when the customer key was created.
        """
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter(name="customerManagedKeyId")
    def customer_managed_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        (String) ID of the encryption key configuration object.
        """
        return pulumi.get(self, "customer_managed_key_id")

    @customer_managed_key_id.setter
    def customer_managed_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_managed_key_id", value)


@pulumi.input_type
class _MwsCustomerManagedKeysState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 aws_key_info: Optional[pulumi.Input['MwsCustomerManagedKeysAwsKeyInfoArgs']] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 customer_managed_key_id: Optional[pulumi.Input[str]] = None,
                 use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering MwsCustomerManagedKeys resources.
        :param pulumi.Input[str] account_id: Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        :param pulumi.Input['MwsCustomerManagedKeysAwsKeyInfoArgs'] aws_key_info: This field is a block and is documented below.
        :param pulumi.Input[int] creation_time: (Integer) Time in epoch milliseconds when the customer key was created.
        :param pulumi.Input[str] customer_managed_key_id: (String) ID of the encryption key configuration object.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_cases: *(since v0.3.4)* List of use cases for which this key will be used. *If you've used the resource before, please add `use_cases = ["MANAGED_SERVICES"]` to keep the previous behaviour.* Possible values are:
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if aws_key_info is not None:
            pulumi.set(__self__, "aws_key_info", aws_key_info)
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if customer_managed_key_id is not None:
            pulumi.set(__self__, "customer_managed_key_id", customer_managed_key_id)
        if use_cases is not None:
            pulumi.set(__self__, "use_cases", use_cases)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="awsKeyInfo")
    def aws_key_info(self) -> Optional[pulumi.Input['MwsCustomerManagedKeysAwsKeyInfoArgs']]:
        """
        This field is a block and is documented below.
        """
        return pulumi.get(self, "aws_key_info")

    @aws_key_info.setter
    def aws_key_info(self, value: Optional[pulumi.Input['MwsCustomerManagedKeysAwsKeyInfoArgs']]):
        pulumi.set(self, "aws_key_info", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        """
        (Integer) Time in epoch milliseconds when the customer key was created.
        """
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter(name="customerManagedKeyId")
    def customer_managed_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        (String) ID of the encryption key configuration object.
        """
        return pulumi.get(self, "customer_managed_key_id")

    @customer_managed_key_id.setter
    def customer_managed_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_managed_key_id", value)

    @property
    @pulumi.getter(name="useCases")
    def use_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        *(since v0.3.4)* List of use cases for which this key will be used. *If you've used the resource before, please add `use_cases = ["MANAGED_SERVICES"]` to keep the previous behaviour.* Possible values are:
        """
        return pulumi.get(self, "use_cases")

    @use_cases.setter
    def use_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "use_cases", value)


class MwsCustomerManagedKeys(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 aws_key_info: Optional[pulumi.Input[pulumi.InputType['MwsCustomerManagedKeysAwsKeyInfoArgs']]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 customer_managed_key_id: Optional[pulumi.Input[str]] = None,
                 use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        > **Note** If you've used the resource before, please add `use_cases = ["MANAGED_SERVICES"]` to keep the previous behaviour.
        ### Customer-managed key for managed services

        You must configure this during workspace creation

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_databricks as databricks

        config = pulumi.Config()
        databricks_account_id = config.require_object("databricksAccountId")
        current = aws.get_caller_identity()
        databricks_managed_services_cmk = aws.iam.get_policy_document(version="2012-10-17",
            statements=[
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Enable IAM User Permissions",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=[current.account_id],
                    )],
                    actions=["kms:*"],
                    resources=["*"],
                ),
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Allow Databricks to use KMS key for control plane managed services",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=["arn:aws:iam::414351767826:root"],
                    )],
                    actions=[
                        "kms:Encrypt",
                        "kms:Decrypt",
                    ],
                    resources=["*"],
                ),
            ])
        managed_services_customer_managed_key = aws.kms.Key("managedServicesCustomerManagedKey", policy=databricks_managed_services_cmk.json)
        managed_services_customer_managed_key_alias = aws.kms.Alias("managedServicesCustomerManagedKeyAlias", target_key_id=managed_services_customer_managed_key.key_id)
        managed_services = databricks.MwsCustomerManagedKeys("managedServices",
            account_id=databricks_account_id,
            aws_key_info=databricks.MwsCustomerManagedKeysAwsKeyInfoArgs(
                key_arn=managed_services_customer_managed_key.arn,
                key_alias=managed_services_customer_managed_key_alias.name,
            ),
            use_cases=["MANAGED_SERVICES"])
        ```
        ### Customer-managed key for workspace storage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_databricks as databricks

        config = pulumi.Config()
        databricks_account_id = config.require_object("databricksAccountId")
        databricks_cross_account_role = config.require_object("databricksCrossAccountRole")
        databricks_storage_cmk = aws.iam.get_policy_document(version="2012-10-17",
            statements=[
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Enable IAM User Permissions",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=[data["aws_caller_identity"]["current"]["account_id"]],
                    )],
                    actions=["kms:*"],
                    resources=["*"],
                ),
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Allow Databricks to use KMS key for DBFS",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=["arn:aws:iam::414351767826:root"],
                    )],
                    actions=[
                        "kms:Encrypt",
                        "kms:Decrypt",
                        "kms:ReEncrypt*",
                        "kms:GenerateDataKey*",
                        "kms:DescribeKey",
                    ],
                    resources=["*"],
                ),
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Allow Databricks to use KMS key for DBFS (Grants)",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=["arn:aws:iam::414351767826:root"],
                    )],
                    actions=[
                        "kms:CreateGrant",
                        "kms:ListGrants",
                        "kms:RevokeGrant",
                    ],
                    resources=["*"],
                    conditions=[aws.iam.GetPolicyDocumentStatementConditionArgs(
                        test="Bool",
                        variable="kms:GrantIsForAWSResource",
                        values=["true"],
                    )],
                ),
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Allow Databricks to use KMS key for EBS",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=[databricks_cross_account_role],
                    )],
                    actions=[
                        "kms:Decrypt",
                        "kms:GenerateDataKey*",
                        "kms:CreateGrant",
                        "kms:DescribeKey",
                    ],
                    resources=["*"],
                    conditions=[aws.iam.GetPolicyDocumentStatementConditionArgs(
                        test="ForAnyValue:StringLike",
                        variable="kms:ViaService",
                        values=["ec2.*.amazonaws.com"],
                    )],
                ),
            ])
        storage_customer_managed_key = aws.kms.Key("storageCustomerManagedKey", policy=databricks_storage_cmk.json)
        storage_customer_managed_key_alias = aws.kms.Alias("storageCustomerManagedKeyAlias", target_key_id=storage_customer_managed_key.key_id)
        storage = databricks.MwsCustomerManagedKeys("storage",
            account_id=databricks_account_id,
            aws_key_info=databricks.MwsCustomerManagedKeysAwsKeyInfoArgs(
                key_arn=storage_customer_managed_key.arn,
                key_alias=storage_customer_managed_key_alias.name,
            ),
            use_cases=["STORAGE"])
        ```
        ## Related Resources

        The following resources are used in the same context:

        * Provisioning Databricks on AWS guide.
        * MwsCredentials to configure the cross-account role for creation of new workspaces within AWS.
        * MwsLogDelivery to configure delivery of [billable usage logs](https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html) and [audit logs](https://docs.databricks.com/administration-guide/account-settings/audit-logs.html).
        * MwsNetworks to [configure VPC](https://docs.databricks.com/administration-guide/cloud-configurations/aws/customer-managed-vpc.html) & subnets for new workspaces within AWS.
        * MwsStorageConfigurations to configure root bucket new workspaces within AWS.
        * MwsWorkspaces to set up [workspaces in E2 architecture on AWS](https://docs.databricks.com/getting-started/overview.html#e2-architecture-1).

        ## Import

        -> **Note** Importing this resource is not currently supported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        :param pulumi.Input[pulumi.InputType['MwsCustomerManagedKeysAwsKeyInfoArgs']] aws_key_info: This field is a block and is documented below.
        :param pulumi.Input[int] creation_time: (Integer) Time in epoch milliseconds when the customer key was created.
        :param pulumi.Input[str] customer_managed_key_id: (String) ID of the encryption key configuration object.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_cases: *(since v0.3.4)* List of use cases for which this key will be used. *If you've used the resource before, please add `use_cases = ["MANAGED_SERVICES"]` to keep the previous behaviour.* Possible values are:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MwsCustomerManagedKeysArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        > **Note** If you've used the resource before, please add `use_cases = ["MANAGED_SERVICES"]` to keep the previous behaviour.
        ### Customer-managed key for managed services

        You must configure this during workspace creation

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_databricks as databricks

        config = pulumi.Config()
        databricks_account_id = config.require_object("databricksAccountId")
        current = aws.get_caller_identity()
        databricks_managed_services_cmk = aws.iam.get_policy_document(version="2012-10-17",
            statements=[
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Enable IAM User Permissions",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=[current.account_id],
                    )],
                    actions=["kms:*"],
                    resources=["*"],
                ),
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Allow Databricks to use KMS key for control plane managed services",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=["arn:aws:iam::414351767826:root"],
                    )],
                    actions=[
                        "kms:Encrypt",
                        "kms:Decrypt",
                    ],
                    resources=["*"],
                ),
            ])
        managed_services_customer_managed_key = aws.kms.Key("managedServicesCustomerManagedKey", policy=databricks_managed_services_cmk.json)
        managed_services_customer_managed_key_alias = aws.kms.Alias("managedServicesCustomerManagedKeyAlias", target_key_id=managed_services_customer_managed_key.key_id)
        managed_services = databricks.MwsCustomerManagedKeys("managedServices",
            account_id=databricks_account_id,
            aws_key_info=databricks.MwsCustomerManagedKeysAwsKeyInfoArgs(
                key_arn=managed_services_customer_managed_key.arn,
                key_alias=managed_services_customer_managed_key_alias.name,
            ),
            use_cases=["MANAGED_SERVICES"])
        ```
        ### Customer-managed key for workspace storage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_databricks as databricks

        config = pulumi.Config()
        databricks_account_id = config.require_object("databricksAccountId")
        databricks_cross_account_role = config.require_object("databricksCrossAccountRole")
        databricks_storage_cmk = aws.iam.get_policy_document(version="2012-10-17",
            statements=[
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Enable IAM User Permissions",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=[data["aws_caller_identity"]["current"]["account_id"]],
                    )],
                    actions=["kms:*"],
                    resources=["*"],
                ),
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Allow Databricks to use KMS key for DBFS",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=["arn:aws:iam::414351767826:root"],
                    )],
                    actions=[
                        "kms:Encrypt",
                        "kms:Decrypt",
                        "kms:ReEncrypt*",
                        "kms:GenerateDataKey*",
                        "kms:DescribeKey",
                    ],
                    resources=["*"],
                ),
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Allow Databricks to use KMS key for DBFS (Grants)",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=["arn:aws:iam::414351767826:root"],
                    )],
                    actions=[
                        "kms:CreateGrant",
                        "kms:ListGrants",
                        "kms:RevokeGrant",
                    ],
                    resources=["*"],
                    conditions=[aws.iam.GetPolicyDocumentStatementConditionArgs(
                        test="Bool",
                        variable="kms:GrantIsForAWSResource",
                        values=["true"],
                    )],
                ),
                aws.iam.GetPolicyDocumentStatementArgs(
                    sid="Allow Databricks to use KMS key for EBS",
                    effect="Allow",
                    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                        type="AWS",
                        identifiers=[databricks_cross_account_role],
                    )],
                    actions=[
                        "kms:Decrypt",
                        "kms:GenerateDataKey*",
                        "kms:CreateGrant",
                        "kms:DescribeKey",
                    ],
                    resources=["*"],
                    conditions=[aws.iam.GetPolicyDocumentStatementConditionArgs(
                        test="ForAnyValue:StringLike",
                        variable="kms:ViaService",
                        values=["ec2.*.amazonaws.com"],
                    )],
                ),
            ])
        storage_customer_managed_key = aws.kms.Key("storageCustomerManagedKey", policy=databricks_storage_cmk.json)
        storage_customer_managed_key_alias = aws.kms.Alias("storageCustomerManagedKeyAlias", target_key_id=storage_customer_managed_key.key_id)
        storage = databricks.MwsCustomerManagedKeys("storage",
            account_id=databricks_account_id,
            aws_key_info=databricks.MwsCustomerManagedKeysAwsKeyInfoArgs(
                key_arn=storage_customer_managed_key.arn,
                key_alias=storage_customer_managed_key_alias.name,
            ),
            use_cases=["STORAGE"])
        ```
        ## Related Resources

        The following resources are used in the same context:

        * Provisioning Databricks on AWS guide.
        * MwsCredentials to configure the cross-account role for creation of new workspaces within AWS.
        * MwsLogDelivery to configure delivery of [billable usage logs](https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html) and [audit logs](https://docs.databricks.com/administration-guide/account-settings/audit-logs.html).
        * MwsNetworks to [configure VPC](https://docs.databricks.com/administration-guide/cloud-configurations/aws/customer-managed-vpc.html) & subnets for new workspaces within AWS.
        * MwsStorageConfigurations to configure root bucket new workspaces within AWS.
        * MwsWorkspaces to set up [workspaces in E2 architecture on AWS](https://docs.databricks.com/getting-started/overview.html#e2-architecture-1).

        ## Import

        -> **Note** Importing this resource is not currently supported.

        :param str resource_name: The name of the resource.
        :param MwsCustomerManagedKeysArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MwsCustomerManagedKeysArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 aws_key_info: Optional[pulumi.Input[pulumi.InputType['MwsCustomerManagedKeysAwsKeyInfoArgs']]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 customer_managed_key_id: Optional[pulumi.Input[str]] = None,
                 use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MwsCustomerManagedKeysArgs.__new__(MwsCustomerManagedKeysArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            if aws_key_info is None and not opts.urn:
                raise TypeError("Missing required property 'aws_key_info'")
            __props__.__dict__["aws_key_info"] = aws_key_info
            __props__.__dict__["creation_time"] = creation_time
            __props__.__dict__["customer_managed_key_id"] = customer_managed_key_id
            if use_cases is None and not opts.urn:
                raise TypeError("Missing required property 'use_cases'")
            __props__.__dict__["use_cases"] = use_cases
        super(MwsCustomerManagedKeys, __self__).__init__(
            'databricks:index/mwsCustomerManagedKeys:MwsCustomerManagedKeys',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            aws_key_info: Optional[pulumi.Input[pulumi.InputType['MwsCustomerManagedKeysAwsKeyInfoArgs']]] = None,
            creation_time: Optional[pulumi.Input[int]] = None,
            customer_managed_key_id: Optional[pulumi.Input[str]] = None,
            use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'MwsCustomerManagedKeys':
        """
        Get an existing MwsCustomerManagedKeys resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        :param pulumi.Input[pulumi.InputType['MwsCustomerManagedKeysAwsKeyInfoArgs']] aws_key_info: This field is a block and is documented below.
        :param pulumi.Input[int] creation_time: (Integer) Time in epoch milliseconds when the customer key was created.
        :param pulumi.Input[str] customer_managed_key_id: (String) ID of the encryption key configuration object.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_cases: *(since v0.3.4)* List of use cases for which this key will be used. *If you've used the resource before, please add `use_cases = ["MANAGED_SERVICES"]` to keep the previous behaviour.* Possible values are:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MwsCustomerManagedKeysState.__new__(_MwsCustomerManagedKeysState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["aws_key_info"] = aws_key_info
        __props__.__dict__["creation_time"] = creation_time
        __props__.__dict__["customer_managed_key_id"] = customer_managed_key_id
        __props__.__dict__["use_cases"] = use_cases
        return MwsCustomerManagedKeys(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="awsKeyInfo")
    def aws_key_info(self) -> pulumi.Output['outputs.MwsCustomerManagedKeysAwsKeyInfo']:
        """
        This field is a block and is documented below.
        """
        return pulumi.get(self, "aws_key_info")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        """
        (Integer) Time in epoch milliseconds when the customer key was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="customerManagedKeyId")
    def customer_managed_key_id(self) -> pulumi.Output[str]:
        """
        (String) ID of the encryption key configuration object.
        """
        return pulumi.get(self, "customer_managed_key_id")

    @property
    @pulumi.getter(name="useCases")
    def use_cases(self) -> pulumi.Output[Sequence[str]]:
        """
        *(since v0.3.4)* List of use cases for which this key will be used. *If you've used the resource before, please add `use_cases = ["MANAGED_SERVICES"]` to keep the previous behaviour.* Possible values are:
        """
        return pulumi.get(self, "use_cases")

