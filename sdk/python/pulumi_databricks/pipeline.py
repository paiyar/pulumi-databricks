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

__all__ = ['PipelineArgs', 'Pipeline']

@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *,
                 allow_duplicate_names: Optional[pulumi.Input[bool]] = None,
                 channel: Optional[pulumi.Input[str]] = None,
                 clusters: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 continuous: Optional[pulumi.Input[bool]] = None,
                 development: Optional[pulumi.Input[bool]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input['PipelineFiltersArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 libraries: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 photon: Optional[pulumi.Input[bool]] = None,
                 storage: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Pipeline resource.
        """
        if allow_duplicate_names is not None:
            pulumi.set(__self__, "allow_duplicate_names", allow_duplicate_names)
        if channel is not None:
            pulumi.set(__self__, "channel", channel)
        if clusters is not None:
            pulumi.set(__self__, "clusters", clusters)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if continuous is not None:
            pulumi.set(__self__, "continuous", continuous)
        if development is not None:
            pulumi.set(__self__, "development", development)
        if edition is not None:
            pulumi.set(__self__, "edition", edition)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if libraries is not None:
            pulumi.set(__self__, "libraries", libraries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if photon is not None:
            pulumi.set(__self__, "photon", photon)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)
        if target is not None:
            pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="allowDuplicateNames")
    def allow_duplicate_names(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_duplicate_names")

    @allow_duplicate_names.setter
    def allow_duplicate_names(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_duplicate_names", value)

    @property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "channel")

    @channel.setter
    def channel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel", value)

    @property
    @pulumi.getter
    def clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]]:
        return pulumi.get(self, "clusters")

    @clusters.setter
    def clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]]):
        pulumi.set(self, "clusters", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def continuous(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "continuous")

    @continuous.setter
    def continuous(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "continuous", value)

    @property
    @pulumi.getter
    def development(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "development")

    @development.setter
    def development(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "development", value)

    @property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "edition")

    @edition.setter
    def edition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "edition", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input['PipelineFiltersArgs']]:
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input['PipelineFiltersArgs']]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def libraries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]]:
        return pulumi.get(self, "libraries")

    @libraries.setter
    def libraries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]]):
        pulumi.set(self, "libraries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def photon(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "photon")

    @photon.setter
    def photon(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "photon", value)

    @property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)


@pulumi.input_type
class _PipelineState:
    def __init__(__self__, *,
                 allow_duplicate_names: Optional[pulumi.Input[bool]] = None,
                 channel: Optional[pulumi.Input[str]] = None,
                 clusters: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 continuous: Optional[pulumi.Input[bool]] = None,
                 development: Optional[pulumi.Input[bool]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input['PipelineFiltersArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 libraries: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 photon: Optional[pulumi.Input[bool]] = None,
                 storage: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Pipeline resources.
        """
        if allow_duplicate_names is not None:
            pulumi.set(__self__, "allow_duplicate_names", allow_duplicate_names)
        if channel is not None:
            pulumi.set(__self__, "channel", channel)
        if clusters is not None:
            pulumi.set(__self__, "clusters", clusters)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if continuous is not None:
            pulumi.set(__self__, "continuous", continuous)
        if development is not None:
            pulumi.set(__self__, "development", development)
        if edition is not None:
            pulumi.set(__self__, "edition", edition)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if libraries is not None:
            pulumi.set(__self__, "libraries", libraries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if photon is not None:
            pulumi.set(__self__, "photon", photon)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)
        if target is not None:
            pulumi.set(__self__, "target", target)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="allowDuplicateNames")
    def allow_duplicate_names(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_duplicate_names")

    @allow_duplicate_names.setter
    def allow_duplicate_names(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_duplicate_names", value)

    @property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "channel")

    @channel.setter
    def channel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel", value)

    @property
    @pulumi.getter
    def clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]]:
        return pulumi.get(self, "clusters")

    @clusters.setter
    def clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]]):
        pulumi.set(self, "clusters", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def continuous(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "continuous")

    @continuous.setter
    def continuous(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "continuous", value)

    @property
    @pulumi.getter
    def development(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "development")

    @development.setter
    def development(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "development", value)

    @property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "edition")

    @edition.setter
    def edition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "edition", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input['PipelineFiltersArgs']]:
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input['PipelineFiltersArgs']]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def libraries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]]:
        return pulumi.get(self, "libraries")

    @libraries.setter
    def libraries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]]):
        pulumi.set(self, "libraries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def photon(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "photon")

    @photon.setter
    def photon(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "photon", value)

    @property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_duplicate_names: Optional[pulumi.Input[bool]] = None,
                 channel: Optional[pulumi.Input[str]] = None,
                 clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineClusterArgs']]]]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 continuous: Optional[pulumi.Input[bool]] = None,
                 development: Optional[pulumi.Input[bool]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['PipelineFiltersArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 libraries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLibraryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 photon: Optional[pulumi.Input[bool]] = None,
                 storage: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Pipeline resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PipelineArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Pipeline resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_duplicate_names: Optional[pulumi.Input[bool]] = None,
                 channel: Optional[pulumi.Input[str]] = None,
                 clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineClusterArgs']]]]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 continuous: Optional[pulumi.Input[bool]] = None,
                 development: Optional[pulumi.Input[bool]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['PipelineFiltersArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 libraries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLibraryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 photon: Optional[pulumi.Input[bool]] = None,
                 storage: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
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
            __props__ = PipelineArgs.__new__(PipelineArgs)

            __props__.__dict__["allow_duplicate_names"] = allow_duplicate_names
            __props__.__dict__["channel"] = channel
            __props__.__dict__["clusters"] = clusters
            __props__.__dict__["configuration"] = configuration
            __props__.__dict__["continuous"] = continuous
            __props__.__dict__["development"] = development
            __props__.__dict__["edition"] = edition
            __props__.__dict__["filters"] = filters
            __props__.__dict__["id"] = id
            __props__.__dict__["libraries"] = libraries
            __props__.__dict__["name"] = name
            __props__.__dict__["photon"] = photon
            __props__.__dict__["storage"] = storage
            __props__.__dict__["target"] = target
            __props__.__dict__["url"] = None
        super(Pipeline, __self__).__init__(
            'databricks:index/pipeline:Pipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_duplicate_names: Optional[pulumi.Input[bool]] = None,
            channel: Optional[pulumi.Input[str]] = None,
            clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineClusterArgs']]]]] = None,
            configuration: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            continuous: Optional[pulumi.Input[bool]] = None,
            development: Optional[pulumi.Input[bool]] = None,
            edition: Optional[pulumi.Input[str]] = None,
            filters: Optional[pulumi.Input[pulumi.InputType['PipelineFiltersArgs']]] = None,
            id: Optional[pulumi.Input[str]] = None,
            libraries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLibraryArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            photon: Optional[pulumi.Input[bool]] = None,
            storage: Optional[pulumi.Input[str]] = None,
            target: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'Pipeline':
        """
        Get an existing Pipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PipelineState.__new__(_PipelineState)

        __props__.__dict__["allow_duplicate_names"] = allow_duplicate_names
        __props__.__dict__["channel"] = channel
        __props__.__dict__["clusters"] = clusters
        __props__.__dict__["configuration"] = configuration
        __props__.__dict__["continuous"] = continuous
        __props__.__dict__["development"] = development
        __props__.__dict__["edition"] = edition
        __props__.__dict__["filters"] = filters
        __props__.__dict__["id"] = id
        __props__.__dict__["libraries"] = libraries
        __props__.__dict__["name"] = name
        __props__.__dict__["photon"] = photon
        __props__.__dict__["storage"] = storage
        __props__.__dict__["target"] = target
        __props__.__dict__["url"] = url
        return Pipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowDuplicateNames")
    def allow_duplicate_names(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "allow_duplicate_names")

    @property
    @pulumi.getter
    def channel(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter
    def clusters(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineCluster']]]:
        return pulumi.get(self, "clusters")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def continuous(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "continuous")

    @property
    @pulumi.getter
    def development(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "development")

    @property
    @pulumi.getter
    def edition(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "edition")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional['outputs.PipelineFilters']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def libraries(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineLibrary']]]:
        return pulumi.get(self, "libraries")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def photon(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "photon")

    @property
    @pulumi.getter
    def storage(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "storage")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "url")

