# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['MwsCredentialsArgs', 'MwsCredentials']

@pulumi.input_type
class MwsCredentialsArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 credentials_name: pulumi.Input[str],
                 role_arn: pulumi.Input[str]):
        """
        The set of arguments for constructing a MwsCredentials resource.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "credentials_name", credentials_name)
        pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="credentialsName")
    def credentials_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "credentials_name")

    @credentials_name.setter
    def credentials_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "credentials_name", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)


@pulumi.input_type
class _MwsCredentialsState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 credentials_id: Optional[pulumi.Input[str]] = None,
                 credentials_name: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MwsCredentials resources.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if credentials_id is not None:
            pulumi.set(__self__, "credentials_id", credentials_id)
        if credentials_name is not None:
            pulumi.set(__self__, "credentials_name", credentials_name)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter(name="credentialsId")
    def credentials_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "credentials_id")

    @credentials_id.setter
    def credentials_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credentials_id", value)

    @property
    @pulumi.getter(name="credentialsName")
    def credentials_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "credentials_name")

    @credentials_name.setter
    def credentials_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credentials_name", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)


class MwsCredentials(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 credentials_name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a MwsCredentials resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MwsCredentialsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a MwsCredentials resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MwsCredentialsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MwsCredentialsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 credentials_name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MwsCredentialsArgs.__new__(MwsCredentialsArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            if credentials_name is None and not opts.urn:
                raise TypeError("Missing required property 'credentials_name'")
            __props__.__dict__["credentials_name"] = credentials_name
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["credentials_id"] = None
            __props__.__dict__["external_id"] = None
        super(MwsCredentials, __self__).__init__(
            'databricks:index/mwsCredentials:MwsCredentials',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            creation_time: Optional[pulumi.Input[int]] = None,
            credentials_id: Optional[pulumi.Input[str]] = None,
            credentials_name: Optional[pulumi.Input[str]] = None,
            external_id: Optional[pulumi.Input[str]] = None,
            role_arn: Optional[pulumi.Input[str]] = None) -> 'MwsCredentials':
        """
        Get an existing MwsCredentials resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MwsCredentialsState.__new__(_MwsCredentialsState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["creation_time"] = creation_time
        __props__.__dict__["credentials_id"] = credentials_id
        __props__.__dict__["credentials_name"] = credentials_name
        __props__.__dict__["external_id"] = external_id
        __props__.__dict__["role_arn"] = role_arn
        return MwsCredentials(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="credentialsId")
    def credentials_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "credentials_id")

    @property
    @pulumi.getter(name="credentialsName")
    def credentials_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "credentials_name")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role_arn")

