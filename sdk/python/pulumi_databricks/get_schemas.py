# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetSchemasResult',
    'AwaitableGetSchemasResult',
    'get_schemas',
    'get_schemas_output',
]

@pulumi.output_type
class GetSchemasResult:
    """
    A collection of values returned by getSchemas.
    """
    def __init__(__self__, catalog_name=None, id=None, ids=None):
        if catalog_name and not isinstance(catalog_name, str):
            raise TypeError("Expected argument 'catalog_name' to be a str")
        pulumi.set(__self__, "catalog_name", catalog_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> str:
        return pulumi.get(self, "catalog_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        return pulumi.get(self, "ids")


class AwaitableGetSchemasResult(GetSchemasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSchemasResult(
            catalog_name=self.catalog_name,
            id=self.id,
            ids=self.ids)


def get_schemas(catalog_name: Optional[str] = None,
                ids: Optional[Sequence[str]] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSchemasResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['catalogName'] = catalog_name
    __args__['ids'] = ids
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('databricks:index/getSchemas:getSchemas', __args__, opts=opts, typ=GetSchemasResult).value

    return AwaitableGetSchemasResult(
        catalog_name=__ret__.catalog_name,
        id=__ret__.id,
        ids=__ret__.ids)


@_utilities.lift_output_func(get_schemas)
def get_schemas_output(catalog_name: Optional[pulumi.Input[str]] = None,
                       ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSchemasResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
