# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['WorkspaceConfArgs', 'WorkspaceConf']

@pulumi.input_type
class WorkspaceConfArgs:
    def __init__(__self__, *,
                 custom_config: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a WorkspaceConf resource.
        """
        if custom_config is not None:
            pulumi.set(__self__, "custom_config", custom_config)

    @property
    @pulumi.getter(name="customConfig")
    def custom_config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "custom_config")

    @custom_config.setter
    def custom_config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "custom_config", value)


@pulumi.input_type
class _WorkspaceConfState:
    def __init__(__self__, *,
                 custom_config: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering WorkspaceConf resources.
        """
        if custom_config is not None:
            pulumi.set(__self__, "custom_config", custom_config)

    @property
    @pulumi.getter(name="customConfig")
    def custom_config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "custom_config")

    @custom_config.setter
    def custom_config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "custom_config", value)


class WorkspaceConf(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        Create a WorkspaceConf resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[WorkspaceConfArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a WorkspaceConf resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param WorkspaceConfArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceConfArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
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
            __props__ = WorkspaceConfArgs.__new__(WorkspaceConfArgs)

            __props__.__dict__["custom_config"] = custom_config
        super(WorkspaceConf, __self__).__init__(
            'databricks:index/workspaceConf:WorkspaceConf',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom_config: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'WorkspaceConf':
        """
        Get an existing WorkspaceConf resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkspaceConfState.__new__(_WorkspaceConfState)

        __props__.__dict__["custom_config"] = custom_config
        return WorkspaceConf(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customConfig")
    def custom_config(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "custom_config")

