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

__all__ = ['InstancePoolArgs', 'InstancePool']

@pulumi.input_type
class InstancePoolArgs:
    def __init__(__self__, *,
                 idle_instance_autotermination_minutes: pulumi.Input[int],
                 instance_pool_name: pulumi.Input[str],
                 aws_attributes: Optional[pulumi.Input['InstancePoolAwsAttributesArgs']] = None,
                 azure_attributes: Optional[pulumi.Input['InstancePoolAzureAttributesArgs']] = None,
                 custom_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 disk_spec: Optional[pulumi.Input['InstancePoolDiskSpecArgs']] = None,
                 enable_elastic_disk: Optional[pulumi.Input[bool]] = None,
                 gcp_attributes: Optional[pulumi.Input['InstancePoolGcpAttributesArgs']] = None,
                 instance_pool_fleet_attributes: Optional[pulumi.Input['InstancePoolInstancePoolFleetAttributesArgs']] = None,
                 instance_pool_id: Optional[pulumi.Input[str]] = None,
                 max_capacity: Optional[pulumi.Input[int]] = None,
                 min_idle_instances: Optional[pulumi.Input[int]] = None,
                 node_type_id: Optional[pulumi.Input[str]] = None,
                 preloaded_docker_images: Optional[pulumi.Input[Sequence[pulumi.Input['InstancePoolPreloadedDockerImageArgs']]]] = None,
                 preloaded_spark_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a InstancePool resource.
        """
        pulumi.set(__self__, "idle_instance_autotermination_minutes", idle_instance_autotermination_minutes)
        pulumi.set(__self__, "instance_pool_name", instance_pool_name)
        if aws_attributes is not None:
            pulumi.set(__self__, "aws_attributes", aws_attributes)
        if azure_attributes is not None:
            pulumi.set(__self__, "azure_attributes", azure_attributes)
        if custom_tags is not None:
            pulumi.set(__self__, "custom_tags", custom_tags)
        if disk_spec is not None:
            pulumi.set(__self__, "disk_spec", disk_spec)
        if enable_elastic_disk is not None:
            pulumi.set(__self__, "enable_elastic_disk", enable_elastic_disk)
        if gcp_attributes is not None:
            pulumi.set(__self__, "gcp_attributes", gcp_attributes)
        if instance_pool_fleet_attributes is not None:
            pulumi.set(__self__, "instance_pool_fleet_attributes", instance_pool_fleet_attributes)
        if instance_pool_id is not None:
            pulumi.set(__self__, "instance_pool_id", instance_pool_id)
        if max_capacity is not None:
            pulumi.set(__self__, "max_capacity", max_capacity)
        if min_idle_instances is not None:
            pulumi.set(__self__, "min_idle_instances", min_idle_instances)
        if node_type_id is not None:
            pulumi.set(__self__, "node_type_id", node_type_id)
        if preloaded_docker_images is not None:
            pulumi.set(__self__, "preloaded_docker_images", preloaded_docker_images)
        if preloaded_spark_versions is not None:
            pulumi.set(__self__, "preloaded_spark_versions", preloaded_spark_versions)

    @property
    @pulumi.getter(name="idleInstanceAutoterminationMinutes")
    def idle_instance_autotermination_minutes(self) -> pulumi.Input[int]:
        return pulumi.get(self, "idle_instance_autotermination_minutes")

    @idle_instance_autotermination_minutes.setter
    def idle_instance_autotermination_minutes(self, value: pulumi.Input[int]):
        pulumi.set(self, "idle_instance_autotermination_minutes", value)

    @property
    @pulumi.getter(name="instancePoolName")
    def instance_pool_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instance_pool_name")

    @instance_pool_name.setter
    def instance_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_pool_name", value)

    @property
    @pulumi.getter(name="awsAttributes")
    def aws_attributes(self) -> Optional[pulumi.Input['InstancePoolAwsAttributesArgs']]:
        return pulumi.get(self, "aws_attributes")

    @aws_attributes.setter
    def aws_attributes(self, value: Optional[pulumi.Input['InstancePoolAwsAttributesArgs']]):
        pulumi.set(self, "aws_attributes", value)

    @property
    @pulumi.getter(name="azureAttributes")
    def azure_attributes(self) -> Optional[pulumi.Input['InstancePoolAzureAttributesArgs']]:
        return pulumi.get(self, "azure_attributes")

    @azure_attributes.setter
    def azure_attributes(self, value: Optional[pulumi.Input['InstancePoolAzureAttributesArgs']]):
        pulumi.set(self, "azure_attributes", value)

    @property
    @pulumi.getter(name="customTags")
    def custom_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "custom_tags")

    @custom_tags.setter
    def custom_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "custom_tags", value)

    @property
    @pulumi.getter(name="diskSpec")
    def disk_spec(self) -> Optional[pulumi.Input['InstancePoolDiskSpecArgs']]:
        return pulumi.get(self, "disk_spec")

    @disk_spec.setter
    def disk_spec(self, value: Optional[pulumi.Input['InstancePoolDiskSpecArgs']]):
        pulumi.set(self, "disk_spec", value)

    @property
    @pulumi.getter(name="enableElasticDisk")
    def enable_elastic_disk(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_elastic_disk")

    @enable_elastic_disk.setter
    def enable_elastic_disk(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_elastic_disk", value)

    @property
    @pulumi.getter(name="gcpAttributes")
    def gcp_attributes(self) -> Optional[pulumi.Input['InstancePoolGcpAttributesArgs']]:
        return pulumi.get(self, "gcp_attributes")

    @gcp_attributes.setter
    def gcp_attributes(self, value: Optional[pulumi.Input['InstancePoolGcpAttributesArgs']]):
        pulumi.set(self, "gcp_attributes", value)

    @property
    @pulumi.getter(name="instancePoolFleetAttributes")
    def instance_pool_fleet_attributes(self) -> Optional[pulumi.Input['InstancePoolInstancePoolFleetAttributesArgs']]:
        return pulumi.get(self, "instance_pool_fleet_attributes")

    @instance_pool_fleet_attributes.setter
    def instance_pool_fleet_attributes(self, value: Optional[pulumi.Input['InstancePoolInstancePoolFleetAttributesArgs']]):
        pulumi.set(self, "instance_pool_fleet_attributes", value)

    @property
    @pulumi.getter(name="instancePoolId")
    def instance_pool_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "instance_pool_id")

    @instance_pool_id.setter
    def instance_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_pool_id", value)

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_capacity")

    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_capacity", value)

    @property
    @pulumi.getter(name="minIdleInstances")
    def min_idle_instances(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "min_idle_instances")

    @min_idle_instances.setter
    def min_idle_instances(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_idle_instances", value)

    @property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "node_type_id")

    @node_type_id.setter
    def node_type_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_type_id", value)

    @property
    @pulumi.getter(name="preloadedDockerImages")
    def preloaded_docker_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstancePoolPreloadedDockerImageArgs']]]]:
        return pulumi.get(self, "preloaded_docker_images")

    @preloaded_docker_images.setter
    def preloaded_docker_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstancePoolPreloadedDockerImageArgs']]]]):
        pulumi.set(self, "preloaded_docker_images", value)

    @property
    @pulumi.getter(name="preloadedSparkVersions")
    def preloaded_spark_versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "preloaded_spark_versions")

    @preloaded_spark_versions.setter
    def preloaded_spark_versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "preloaded_spark_versions", value)


@pulumi.input_type
class _InstancePoolState:
    def __init__(__self__, *,
                 aws_attributes: Optional[pulumi.Input['InstancePoolAwsAttributesArgs']] = None,
                 azure_attributes: Optional[pulumi.Input['InstancePoolAzureAttributesArgs']] = None,
                 custom_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 disk_spec: Optional[pulumi.Input['InstancePoolDiskSpecArgs']] = None,
                 enable_elastic_disk: Optional[pulumi.Input[bool]] = None,
                 gcp_attributes: Optional[pulumi.Input['InstancePoolGcpAttributesArgs']] = None,
                 idle_instance_autotermination_minutes: Optional[pulumi.Input[int]] = None,
                 instance_pool_fleet_attributes: Optional[pulumi.Input['InstancePoolInstancePoolFleetAttributesArgs']] = None,
                 instance_pool_id: Optional[pulumi.Input[str]] = None,
                 instance_pool_name: Optional[pulumi.Input[str]] = None,
                 max_capacity: Optional[pulumi.Input[int]] = None,
                 min_idle_instances: Optional[pulumi.Input[int]] = None,
                 node_type_id: Optional[pulumi.Input[str]] = None,
                 preloaded_docker_images: Optional[pulumi.Input[Sequence[pulumi.Input['InstancePoolPreloadedDockerImageArgs']]]] = None,
                 preloaded_spark_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering InstancePool resources.
        """
        if aws_attributes is not None:
            pulumi.set(__self__, "aws_attributes", aws_attributes)
        if azure_attributes is not None:
            pulumi.set(__self__, "azure_attributes", azure_attributes)
        if custom_tags is not None:
            pulumi.set(__self__, "custom_tags", custom_tags)
        if disk_spec is not None:
            pulumi.set(__self__, "disk_spec", disk_spec)
        if enable_elastic_disk is not None:
            pulumi.set(__self__, "enable_elastic_disk", enable_elastic_disk)
        if gcp_attributes is not None:
            pulumi.set(__self__, "gcp_attributes", gcp_attributes)
        if idle_instance_autotermination_minutes is not None:
            pulumi.set(__self__, "idle_instance_autotermination_minutes", idle_instance_autotermination_minutes)
        if instance_pool_fleet_attributes is not None:
            pulumi.set(__self__, "instance_pool_fleet_attributes", instance_pool_fleet_attributes)
        if instance_pool_id is not None:
            pulumi.set(__self__, "instance_pool_id", instance_pool_id)
        if instance_pool_name is not None:
            pulumi.set(__self__, "instance_pool_name", instance_pool_name)
        if max_capacity is not None:
            pulumi.set(__self__, "max_capacity", max_capacity)
        if min_idle_instances is not None:
            pulumi.set(__self__, "min_idle_instances", min_idle_instances)
        if node_type_id is not None:
            pulumi.set(__self__, "node_type_id", node_type_id)
        if preloaded_docker_images is not None:
            pulumi.set(__self__, "preloaded_docker_images", preloaded_docker_images)
        if preloaded_spark_versions is not None:
            pulumi.set(__self__, "preloaded_spark_versions", preloaded_spark_versions)

    @property
    @pulumi.getter(name="awsAttributes")
    def aws_attributes(self) -> Optional[pulumi.Input['InstancePoolAwsAttributesArgs']]:
        return pulumi.get(self, "aws_attributes")

    @aws_attributes.setter
    def aws_attributes(self, value: Optional[pulumi.Input['InstancePoolAwsAttributesArgs']]):
        pulumi.set(self, "aws_attributes", value)

    @property
    @pulumi.getter(name="azureAttributes")
    def azure_attributes(self) -> Optional[pulumi.Input['InstancePoolAzureAttributesArgs']]:
        return pulumi.get(self, "azure_attributes")

    @azure_attributes.setter
    def azure_attributes(self, value: Optional[pulumi.Input['InstancePoolAzureAttributesArgs']]):
        pulumi.set(self, "azure_attributes", value)

    @property
    @pulumi.getter(name="customTags")
    def custom_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "custom_tags")

    @custom_tags.setter
    def custom_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "custom_tags", value)

    @property
    @pulumi.getter(name="diskSpec")
    def disk_spec(self) -> Optional[pulumi.Input['InstancePoolDiskSpecArgs']]:
        return pulumi.get(self, "disk_spec")

    @disk_spec.setter
    def disk_spec(self, value: Optional[pulumi.Input['InstancePoolDiskSpecArgs']]):
        pulumi.set(self, "disk_spec", value)

    @property
    @pulumi.getter(name="enableElasticDisk")
    def enable_elastic_disk(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_elastic_disk")

    @enable_elastic_disk.setter
    def enable_elastic_disk(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_elastic_disk", value)

    @property
    @pulumi.getter(name="gcpAttributes")
    def gcp_attributes(self) -> Optional[pulumi.Input['InstancePoolGcpAttributesArgs']]:
        return pulumi.get(self, "gcp_attributes")

    @gcp_attributes.setter
    def gcp_attributes(self, value: Optional[pulumi.Input['InstancePoolGcpAttributesArgs']]):
        pulumi.set(self, "gcp_attributes", value)

    @property
    @pulumi.getter(name="idleInstanceAutoterminationMinutes")
    def idle_instance_autotermination_minutes(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "idle_instance_autotermination_minutes")

    @idle_instance_autotermination_minutes.setter
    def idle_instance_autotermination_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "idle_instance_autotermination_minutes", value)

    @property
    @pulumi.getter(name="instancePoolFleetAttributes")
    def instance_pool_fleet_attributes(self) -> Optional[pulumi.Input['InstancePoolInstancePoolFleetAttributesArgs']]:
        return pulumi.get(self, "instance_pool_fleet_attributes")

    @instance_pool_fleet_attributes.setter
    def instance_pool_fleet_attributes(self, value: Optional[pulumi.Input['InstancePoolInstancePoolFleetAttributesArgs']]):
        pulumi.set(self, "instance_pool_fleet_attributes", value)

    @property
    @pulumi.getter(name="instancePoolId")
    def instance_pool_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "instance_pool_id")

    @instance_pool_id.setter
    def instance_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_pool_id", value)

    @property
    @pulumi.getter(name="instancePoolName")
    def instance_pool_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "instance_pool_name")

    @instance_pool_name.setter
    def instance_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_pool_name", value)

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_capacity")

    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_capacity", value)

    @property
    @pulumi.getter(name="minIdleInstances")
    def min_idle_instances(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "min_idle_instances")

    @min_idle_instances.setter
    def min_idle_instances(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_idle_instances", value)

    @property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "node_type_id")

    @node_type_id.setter
    def node_type_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_type_id", value)

    @property
    @pulumi.getter(name="preloadedDockerImages")
    def preloaded_docker_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstancePoolPreloadedDockerImageArgs']]]]:
        return pulumi.get(self, "preloaded_docker_images")

    @preloaded_docker_images.setter
    def preloaded_docker_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstancePoolPreloadedDockerImageArgs']]]]):
        pulumi.set(self, "preloaded_docker_images", value)

    @property
    @pulumi.getter(name="preloadedSparkVersions")
    def preloaded_spark_versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "preloaded_spark_versions")

    @preloaded_spark_versions.setter
    def preloaded_spark_versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "preloaded_spark_versions", value)


class InstancePool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolAwsAttributesArgs']]] = None,
                 azure_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolAzureAttributesArgs']]] = None,
                 custom_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 disk_spec: Optional[pulumi.Input[pulumi.InputType['InstancePoolDiskSpecArgs']]] = None,
                 enable_elastic_disk: Optional[pulumi.Input[bool]] = None,
                 gcp_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolGcpAttributesArgs']]] = None,
                 idle_instance_autotermination_minutes: Optional[pulumi.Input[int]] = None,
                 instance_pool_fleet_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolInstancePoolFleetAttributesArgs']]] = None,
                 instance_pool_id: Optional[pulumi.Input[str]] = None,
                 instance_pool_name: Optional[pulumi.Input[str]] = None,
                 max_capacity: Optional[pulumi.Input[int]] = None,
                 min_idle_instances: Optional[pulumi.Input[int]] = None,
                 node_type_id: Optional[pulumi.Input[str]] = None,
                 preloaded_docker_images: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstancePoolPreloadedDockerImageArgs']]]]] = None,
                 preloaded_spark_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a InstancePool resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstancePoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a InstancePool resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param InstancePoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstancePoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolAwsAttributesArgs']]] = None,
                 azure_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolAzureAttributesArgs']]] = None,
                 custom_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 disk_spec: Optional[pulumi.Input[pulumi.InputType['InstancePoolDiskSpecArgs']]] = None,
                 enable_elastic_disk: Optional[pulumi.Input[bool]] = None,
                 gcp_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolGcpAttributesArgs']]] = None,
                 idle_instance_autotermination_minutes: Optional[pulumi.Input[int]] = None,
                 instance_pool_fleet_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolInstancePoolFleetAttributesArgs']]] = None,
                 instance_pool_id: Optional[pulumi.Input[str]] = None,
                 instance_pool_name: Optional[pulumi.Input[str]] = None,
                 max_capacity: Optional[pulumi.Input[int]] = None,
                 min_idle_instances: Optional[pulumi.Input[int]] = None,
                 node_type_id: Optional[pulumi.Input[str]] = None,
                 preloaded_docker_images: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstancePoolPreloadedDockerImageArgs']]]]] = None,
                 preloaded_spark_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = InstancePoolArgs.__new__(InstancePoolArgs)

            __props__.__dict__["aws_attributes"] = aws_attributes
            __props__.__dict__["azure_attributes"] = azure_attributes
            __props__.__dict__["custom_tags"] = custom_tags
            __props__.__dict__["disk_spec"] = disk_spec
            __props__.__dict__["enable_elastic_disk"] = enable_elastic_disk
            __props__.__dict__["gcp_attributes"] = gcp_attributes
            if idle_instance_autotermination_minutes is None and not opts.urn:
                raise TypeError("Missing required property 'idle_instance_autotermination_minutes'")
            __props__.__dict__["idle_instance_autotermination_minutes"] = idle_instance_autotermination_minutes
            __props__.__dict__["instance_pool_fleet_attributes"] = instance_pool_fleet_attributes
            __props__.__dict__["instance_pool_id"] = instance_pool_id
            if instance_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'instance_pool_name'")
            __props__.__dict__["instance_pool_name"] = instance_pool_name
            __props__.__dict__["max_capacity"] = max_capacity
            __props__.__dict__["min_idle_instances"] = min_idle_instances
            __props__.__dict__["node_type_id"] = node_type_id
            __props__.__dict__["preloaded_docker_images"] = preloaded_docker_images
            __props__.__dict__["preloaded_spark_versions"] = preloaded_spark_versions
        super(InstancePool, __self__).__init__(
            'databricks:index/instancePool:InstancePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            aws_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolAwsAttributesArgs']]] = None,
            azure_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolAzureAttributesArgs']]] = None,
            custom_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            disk_spec: Optional[pulumi.Input[pulumi.InputType['InstancePoolDiskSpecArgs']]] = None,
            enable_elastic_disk: Optional[pulumi.Input[bool]] = None,
            gcp_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolGcpAttributesArgs']]] = None,
            idle_instance_autotermination_minutes: Optional[pulumi.Input[int]] = None,
            instance_pool_fleet_attributes: Optional[pulumi.Input[pulumi.InputType['InstancePoolInstancePoolFleetAttributesArgs']]] = None,
            instance_pool_id: Optional[pulumi.Input[str]] = None,
            instance_pool_name: Optional[pulumi.Input[str]] = None,
            max_capacity: Optional[pulumi.Input[int]] = None,
            min_idle_instances: Optional[pulumi.Input[int]] = None,
            node_type_id: Optional[pulumi.Input[str]] = None,
            preloaded_docker_images: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstancePoolPreloadedDockerImageArgs']]]]] = None,
            preloaded_spark_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'InstancePool':
        """
        Get an existing InstancePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstancePoolState.__new__(_InstancePoolState)

        __props__.__dict__["aws_attributes"] = aws_attributes
        __props__.__dict__["azure_attributes"] = azure_attributes
        __props__.__dict__["custom_tags"] = custom_tags
        __props__.__dict__["disk_spec"] = disk_spec
        __props__.__dict__["enable_elastic_disk"] = enable_elastic_disk
        __props__.__dict__["gcp_attributes"] = gcp_attributes
        __props__.__dict__["idle_instance_autotermination_minutes"] = idle_instance_autotermination_minutes
        __props__.__dict__["instance_pool_fleet_attributes"] = instance_pool_fleet_attributes
        __props__.__dict__["instance_pool_id"] = instance_pool_id
        __props__.__dict__["instance_pool_name"] = instance_pool_name
        __props__.__dict__["max_capacity"] = max_capacity
        __props__.__dict__["min_idle_instances"] = min_idle_instances
        __props__.__dict__["node_type_id"] = node_type_id
        __props__.__dict__["preloaded_docker_images"] = preloaded_docker_images
        __props__.__dict__["preloaded_spark_versions"] = preloaded_spark_versions
        return InstancePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsAttributes")
    def aws_attributes(self) -> pulumi.Output['outputs.InstancePoolAwsAttributes']:
        return pulumi.get(self, "aws_attributes")

    @property
    @pulumi.getter(name="azureAttributes")
    def azure_attributes(self) -> pulumi.Output[Optional['outputs.InstancePoolAzureAttributes']]:
        return pulumi.get(self, "azure_attributes")

    @property
    @pulumi.getter(name="customTags")
    def custom_tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "custom_tags")

    @property
    @pulumi.getter(name="diskSpec")
    def disk_spec(self) -> pulumi.Output[Optional['outputs.InstancePoolDiskSpec']]:
        return pulumi.get(self, "disk_spec")

    @property
    @pulumi.getter(name="enableElasticDisk")
    def enable_elastic_disk(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_elastic_disk")

    @property
    @pulumi.getter(name="gcpAttributes")
    def gcp_attributes(self) -> pulumi.Output[Optional['outputs.InstancePoolGcpAttributes']]:
        return pulumi.get(self, "gcp_attributes")

    @property
    @pulumi.getter(name="idleInstanceAutoterminationMinutes")
    def idle_instance_autotermination_minutes(self) -> pulumi.Output[int]:
        return pulumi.get(self, "idle_instance_autotermination_minutes")

    @property
    @pulumi.getter(name="instancePoolFleetAttributes")
    def instance_pool_fleet_attributes(self) -> pulumi.Output[Optional['outputs.InstancePoolInstancePoolFleetAttributes']]:
        return pulumi.get(self, "instance_pool_fleet_attributes")

    @property
    @pulumi.getter(name="instancePoolId")
    def instance_pool_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_pool_id")

    @property
    @pulumi.getter(name="instancePoolName")
    def instance_pool_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_pool_name")

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="minIdleInstances")
    def min_idle_instances(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "min_idle_instances")

    @property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "node_type_id")

    @property
    @pulumi.getter(name="preloadedDockerImages")
    def preloaded_docker_images(self) -> pulumi.Output[Optional[Sequence['outputs.InstancePoolPreloadedDockerImage']]]:
        return pulumi.get(self, "preloaded_docker_images")

    @property
    @pulumi.getter(name="preloadedSparkVersions")
    def preloaded_spark_versions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "preloaded_spark_versions")

