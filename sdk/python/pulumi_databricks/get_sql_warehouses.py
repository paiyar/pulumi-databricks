# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetSqlWarehousesResult',
    'AwaitableGetSqlWarehousesResult',
    'get_sql_warehouses',
    'get_sql_warehouses_output',
]

@pulumi.output_type
class GetSqlWarehousesResult:
    """
    A collection of values returned by getSqlWarehouses.
    """
    def __init__(__self__, id=None, ids=None, warehouse_name_contains=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if warehouse_name_contains and not isinstance(warehouse_name_contains, str):
            raise TypeError("Expected argument 'warehouse_name_contains' to be a str")
        pulumi.set(__self__, "warehouse_name_contains", warehouse_name_contains)

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

    @property
    @pulumi.getter(name="warehouseNameContains")
    def warehouse_name_contains(self) -> Optional[str]:
        return pulumi.get(self, "warehouse_name_contains")


class AwaitableGetSqlWarehousesResult(GetSqlWarehousesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlWarehousesResult(
            id=self.id,
            ids=self.ids,
            warehouse_name_contains=self.warehouse_name_contains)


def get_sql_warehouses(ids: Optional[Sequence[str]] = None,
                       warehouse_name_contains: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlWarehousesResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['warehouseNameContains'] = warehouse_name_contains
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('databricks:index/getSqlWarehouses:getSqlWarehouses', __args__, opts=opts, typ=GetSqlWarehousesResult).value

    return AwaitableGetSqlWarehousesResult(
        id=__ret__.id,
        ids=__ret__.ids,
        warehouse_name_contains=__ret__.warehouse_name_contains)


@_utilities.lift_output_func(get_sql_warehouses)
def get_sql_warehouses_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                              warehouse_name_contains: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlWarehousesResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
