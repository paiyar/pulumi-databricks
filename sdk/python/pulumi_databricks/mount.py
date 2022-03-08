# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['MountArgs', 'Mount']

@pulumi.input_type
class MountArgs:
    def __init__(__self__, *,
                 abfs: Optional[pulumi.Input['MountAbfsArgs']] = None,
                 adl: Optional[pulumi.Input['MountAdlArgs']] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[str]] = None,
                 extra_configs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 gs: Optional[pulumi.Input['MountGsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input['MountS3Args']] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 wasb: Optional[pulumi.Input['MountWasbArgs']] = None):
        """
        The set of arguments for constructing a Mount resource.
        """
        if abfs is not None:
            pulumi.set(__self__, "abfs", abfs)
        if adl is not None:
            pulumi.set(__self__, "adl", adl)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if encryption_type is not None:
            pulumi.set(__self__, "encryption_type", encryption_type)
        if extra_configs is not None:
            pulumi.set(__self__, "extra_configs", extra_configs)
        if gs is not None:
            pulumi.set(__self__, "gs", gs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if s3 is not None:
            pulumi.set(__self__, "s3", s3)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)
        if wasb is not None:
            pulumi.set(__self__, "wasb", wasb)

    @property
    @pulumi.getter
    def abfs(self) -> Optional[pulumi.Input['MountAbfsArgs']]:
        return pulumi.get(self, "abfs")

    @abfs.setter
    def abfs(self, value: Optional[pulumi.Input['MountAbfsArgs']]):
        pulumi.set(self, "abfs", value)

    @property
    @pulumi.getter
    def adl(self) -> Optional[pulumi.Input['MountAdlArgs']]:
        return pulumi.get(self, "adl")

    @adl.setter
    def adl(self, value: Optional[pulumi.Input['MountAdlArgs']]):
        pulumi.set(self, "adl", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "encryption_type")

    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_type", value)

    @property
    @pulumi.getter(name="extraConfigs")
    def extra_configs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "extra_configs")

    @extra_configs.setter
    def extra_configs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "extra_configs", value)

    @property
    @pulumi.getter
    def gs(self) -> Optional[pulumi.Input['MountGsArgs']]:
        return pulumi.get(self, "gs")

    @gs.setter
    def gs(self, value: Optional[pulumi.Input['MountGsArgs']]):
        pulumi.set(self, "gs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input['MountS3Args']]:
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: Optional[pulumi.Input['MountS3Args']]):
        pulumi.set(self, "s3", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter
    def wasb(self) -> Optional[pulumi.Input['MountWasbArgs']]:
        return pulumi.get(self, "wasb")

    @wasb.setter
    def wasb(self, value: Optional[pulumi.Input['MountWasbArgs']]):
        pulumi.set(self, "wasb", value)


@pulumi.input_type
class _MountState:
    def __init__(__self__, *,
                 abfs: Optional[pulumi.Input['MountAbfsArgs']] = None,
                 adl: Optional[pulumi.Input['MountAdlArgs']] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[str]] = None,
                 extra_configs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 gs: Optional[pulumi.Input['MountGsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input['MountS3Args']] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 wasb: Optional[pulumi.Input['MountWasbArgs']] = None):
        """
        Input properties used for looking up and filtering Mount resources.
        :param pulumi.Input[str] source: (String) HDFS-compatible url
        """
        if abfs is not None:
            pulumi.set(__self__, "abfs", abfs)
        if adl is not None:
            pulumi.set(__self__, "adl", adl)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if encryption_type is not None:
            pulumi.set(__self__, "encryption_type", encryption_type)
        if extra_configs is not None:
            pulumi.set(__self__, "extra_configs", extra_configs)
        if gs is not None:
            pulumi.set(__self__, "gs", gs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if s3 is not None:
            pulumi.set(__self__, "s3", s3)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)
        if wasb is not None:
            pulumi.set(__self__, "wasb", wasb)

    @property
    @pulumi.getter
    def abfs(self) -> Optional[pulumi.Input['MountAbfsArgs']]:
        return pulumi.get(self, "abfs")

    @abfs.setter
    def abfs(self, value: Optional[pulumi.Input['MountAbfsArgs']]):
        pulumi.set(self, "abfs", value)

    @property
    @pulumi.getter
    def adl(self) -> Optional[pulumi.Input['MountAdlArgs']]:
        return pulumi.get(self, "adl")

    @adl.setter
    def adl(self, value: Optional[pulumi.Input['MountAdlArgs']]):
        pulumi.set(self, "adl", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "encryption_type")

    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_type", value)

    @property
    @pulumi.getter(name="extraConfigs")
    def extra_configs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "extra_configs")

    @extra_configs.setter
    def extra_configs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "extra_configs", value)

    @property
    @pulumi.getter
    def gs(self) -> Optional[pulumi.Input['MountGsArgs']]:
        return pulumi.get(self, "gs")

    @gs.setter
    def gs(self, value: Optional[pulumi.Input['MountGsArgs']]):
        pulumi.set(self, "gs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input['MountS3Args']]:
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: Optional[pulumi.Input['MountS3Args']]):
        pulumi.set(self, "s3", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        (String) HDFS-compatible url
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter
    def wasb(self) -> Optional[pulumi.Input['MountWasbArgs']]:
        return pulumi.get(self, "wasb")

    @wasb.setter
    def wasb(self, value: Optional[pulumi.Input['MountWasbArgs']]):
        pulumi.set(self, "wasb", value)


class Mount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 abfs: Optional[pulumi.Input[pulumi.InputType['MountAbfsArgs']]] = None,
                 adl: Optional[pulumi.Input[pulumi.InputType['MountAdlArgs']]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[str]] = None,
                 extra_configs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 gs: Optional[pulumi.Input[pulumi.InputType['MountGsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input[pulumi.InputType['MountS3Args']]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 wasb: Optional[pulumi.Input[pulumi.InputType['MountWasbArgs']]] = None,
                 __props__=None):
        """
        ## Import

        -> **Note** Importing this resource is not currently supported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[MountArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        -> **Note** Importing this resource is not currently supported.

        :param str resource_name: The name of the resource.
        :param MountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 abfs: Optional[pulumi.Input[pulumi.InputType['MountAbfsArgs']]] = None,
                 adl: Optional[pulumi.Input[pulumi.InputType['MountAdlArgs']]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[str]] = None,
                 extra_configs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 gs: Optional[pulumi.Input[pulumi.InputType['MountGsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input[pulumi.InputType['MountS3Args']]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 wasb: Optional[pulumi.Input[pulumi.InputType['MountWasbArgs']]] = None,
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
            __props__ = MountArgs.__new__(MountArgs)

            __props__.__dict__["abfs"] = abfs
            __props__.__dict__["adl"] = adl
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["encryption_type"] = encryption_type
            __props__.__dict__["extra_configs"] = extra_configs
            __props__.__dict__["gs"] = gs
            __props__.__dict__["name"] = name
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["s3"] = s3
            __props__.__dict__["uri"] = uri
            __props__.__dict__["wasb"] = wasb
            __props__.__dict__["source"] = None
        super(Mount, __self__).__init__(
            'databricks:index/mount:Mount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            abfs: Optional[pulumi.Input[pulumi.InputType['MountAbfsArgs']]] = None,
            adl: Optional[pulumi.Input[pulumi.InputType['MountAdlArgs']]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            encryption_type: Optional[pulumi.Input[str]] = None,
            extra_configs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            gs: Optional[pulumi.Input[pulumi.InputType['MountGsArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_id: Optional[pulumi.Input[str]] = None,
            s3: Optional[pulumi.Input[pulumi.InputType['MountS3Args']]] = None,
            source: Optional[pulumi.Input[str]] = None,
            uri: Optional[pulumi.Input[str]] = None,
            wasb: Optional[pulumi.Input[pulumi.InputType['MountWasbArgs']]] = None) -> 'Mount':
        """
        Get an existing Mount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] source: (String) HDFS-compatible url
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MountState.__new__(_MountState)

        __props__.__dict__["abfs"] = abfs
        __props__.__dict__["adl"] = adl
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["encryption_type"] = encryption_type
        __props__.__dict__["extra_configs"] = extra_configs
        __props__.__dict__["gs"] = gs
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_id"] = resource_id
        __props__.__dict__["s3"] = s3
        __props__.__dict__["source"] = source
        __props__.__dict__["uri"] = uri
        __props__.__dict__["wasb"] = wasb
        return Mount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def abfs(self) -> pulumi.Output[Optional['outputs.MountAbfs']]:
        return pulumi.get(self, "abfs")

    @property
    @pulumi.getter
    def adl(self) -> pulumi.Output[Optional['outputs.MountAdl']]:
        return pulumi.get(self, "adl")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "encryption_type")

    @property
    @pulumi.getter(name="extraConfigs")
    def extra_configs(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "extra_configs")

    @property
    @pulumi.getter
    def gs(self) -> pulumi.Output[Optional['outputs.MountGs']]:
        return pulumi.get(self, "gs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def s3(self) -> pulumi.Output[Optional['outputs.MountS3']]:
        return pulumi.get(self, "s3")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        """
        (String) HDFS-compatible url
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter
    def wasb(self) -> pulumi.Output[Optional['outputs.MountWasb']]:
        return pulumi.get(self, "wasb")

