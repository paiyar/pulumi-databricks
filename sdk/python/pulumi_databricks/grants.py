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

__all__ = ['GrantsArgs', 'Grants']

@pulumi.input_type
class GrantsArgs:
    def __init__(__self__, *,
                 grants: pulumi.Input[Sequence[pulumi.Input['GrantsGrantArgs']]],
                 catalog: Optional[pulumi.Input[str]] = None,
                 external_location: Optional[pulumi.Input[str]] = None,
                 metastore: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 storage_credential: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Grants resource.
        """
        pulumi.set(__self__, "grants", grants)
        if catalog is not None:
            pulumi.set(__self__, "catalog", catalog)
        if external_location is not None:
            pulumi.set(__self__, "external_location", external_location)
        if metastore is not None:
            pulumi.set(__self__, "metastore", metastore)
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if storage_credential is not None:
            pulumi.set(__self__, "storage_credential", storage_credential)
        if table is not None:
            pulumi.set(__self__, "table", table)
        if view is not None:
            pulumi.set(__self__, "view", view)

    @property
    @pulumi.getter
    def grants(self) -> pulumi.Input[Sequence[pulumi.Input['GrantsGrantArgs']]]:
        return pulumi.get(self, "grants")

    @grants.setter
    def grants(self, value: pulumi.Input[Sequence[pulumi.Input['GrantsGrantArgs']]]):
        pulumi.set(self, "grants", value)

    @property
    @pulumi.getter
    def catalog(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "catalog")

    @catalog.setter
    def catalog(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog", value)

    @property
    @pulumi.getter(name="externalLocation")
    def external_location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "external_location")

    @external_location.setter
    def external_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_location", value)

    @property
    @pulumi.getter
    def metastore(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metastore")

    @metastore.setter
    def metastore(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metastore", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="storageCredential")
    def storage_credential(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage_credential")

    @storage_credential.setter
    def storage_credential(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_credential", value)

    @property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table", value)

    @property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "view")

    @view.setter
    def view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "view", value)


@pulumi.input_type
class _GrantsState:
    def __init__(__self__, *,
                 catalog: Optional[pulumi.Input[str]] = None,
                 external_location: Optional[pulumi.Input[str]] = None,
                 grants: Optional[pulumi.Input[Sequence[pulumi.Input['GrantsGrantArgs']]]] = None,
                 metastore: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 storage_credential: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Grants resources.
        """
        if catalog is not None:
            pulumi.set(__self__, "catalog", catalog)
        if external_location is not None:
            pulumi.set(__self__, "external_location", external_location)
        if grants is not None:
            pulumi.set(__self__, "grants", grants)
        if metastore is not None:
            pulumi.set(__self__, "metastore", metastore)
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if storage_credential is not None:
            pulumi.set(__self__, "storage_credential", storage_credential)
        if table is not None:
            pulumi.set(__self__, "table", table)
        if view is not None:
            pulumi.set(__self__, "view", view)

    @property
    @pulumi.getter
    def catalog(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "catalog")

    @catalog.setter
    def catalog(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog", value)

    @property
    @pulumi.getter(name="externalLocation")
    def external_location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "external_location")

    @external_location.setter
    def external_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_location", value)

    @property
    @pulumi.getter
    def grants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GrantsGrantArgs']]]]:
        return pulumi.get(self, "grants")

    @grants.setter
    def grants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GrantsGrantArgs']]]]):
        pulumi.set(self, "grants", value)

    @property
    @pulumi.getter
    def metastore(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metastore")

    @metastore.setter
    def metastore(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metastore", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="storageCredential")
    def storage_credential(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage_credential")

    @storage_credential.setter
    def storage_credential(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_credential", value)

    @property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table", value)

    @property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "view")

    @view.setter
    def view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "view", value)


class Grants(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog: Optional[pulumi.Input[str]] = None,
                 external_location: Optional[pulumi.Input[str]] = None,
                 grants: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GrantsGrantArgs']]]]] = None,
                 metastore: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 storage_credential: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Grants resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GrantsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Grants resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param GrantsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GrantsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog: Optional[pulumi.Input[str]] = None,
                 external_location: Optional[pulumi.Input[str]] = None,
                 grants: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GrantsGrantArgs']]]]] = None,
                 metastore: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 storage_credential: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GrantsArgs.__new__(GrantsArgs)

            __props__.__dict__["catalog"] = catalog
            __props__.__dict__["external_location"] = external_location
            if grants is None and not opts.urn:
                raise TypeError("Missing required property 'grants'")
            __props__.__dict__["grants"] = grants
            __props__.__dict__["metastore"] = metastore
            __props__.__dict__["schema"] = schema
            __props__.__dict__["storage_credential"] = storage_credential
            __props__.__dict__["table"] = table
            __props__.__dict__["view"] = view
        super(Grants, __self__).__init__(
            'databricks:index/grants:Grants',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            catalog: Optional[pulumi.Input[str]] = None,
            external_location: Optional[pulumi.Input[str]] = None,
            grants: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GrantsGrantArgs']]]]] = None,
            metastore: Optional[pulumi.Input[str]] = None,
            schema: Optional[pulumi.Input[str]] = None,
            storage_credential: Optional[pulumi.Input[str]] = None,
            table: Optional[pulumi.Input[str]] = None,
            view: Optional[pulumi.Input[str]] = None) -> 'Grants':
        """
        Get an existing Grants resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GrantsState.__new__(_GrantsState)

        __props__.__dict__["catalog"] = catalog
        __props__.__dict__["external_location"] = external_location
        __props__.__dict__["grants"] = grants
        __props__.__dict__["metastore"] = metastore
        __props__.__dict__["schema"] = schema
        __props__.__dict__["storage_credential"] = storage_credential
        __props__.__dict__["table"] = table
        __props__.__dict__["view"] = view
        return Grants(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def catalog(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "catalog")

    @property
    @pulumi.getter(name="externalLocation")
    def external_location(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "external_location")

    @property
    @pulumi.getter
    def grants(self) -> pulumi.Output[Sequence['outputs.GrantsGrant']]:
        return pulumi.get(self, "grants")

    @property
    @pulumi.getter
    def metastore(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "metastore")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="storageCredential")
    def storage_credential(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "storage_credential")

    @property
    @pulumi.getter
    def table(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "table")

    @property
    @pulumi.getter
    def view(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "view")

