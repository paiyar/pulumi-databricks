# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DbfsFileArgs', 'DbfsFile']

@pulumi.input_type
class DbfsFileArgs:
    def __init__(__self__, *,
                 path: pulumi.Input[str],
                 content_base64: Optional[pulumi.Input[str]] = None,
                 md5: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DbfsFile resource.
        """
        pulumi.set(__self__, "path", path)
        if content_base64 is not None:
            pulumi.set(__self__, "content_base64", content_base64)
        if md5 is not None:
            pulumi.set(__self__, "md5", md5)
        if source is not None:
            pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "content_base64")

    @content_base64.setter
    def content_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_base64", value)

    @property
    @pulumi.getter
    def md5(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "md5")

    @md5.setter
    def md5(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "md5", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)


@pulumi.input_type
class _DbfsFileState:
    def __init__(__self__, *,
                 content_base64: Optional[pulumi.Input[str]] = None,
                 dbfs_path: Optional[pulumi.Input[str]] = None,
                 file_size: Optional[pulumi.Input[int]] = None,
                 md5: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DbfsFile resources.
        """
        if content_base64 is not None:
            pulumi.set(__self__, "content_base64", content_base64)
        if dbfs_path is not None:
            pulumi.set(__self__, "dbfs_path", dbfs_path)
        if file_size is not None:
            pulumi.set(__self__, "file_size", file_size)
        if md5 is not None:
            pulumi.set(__self__, "md5", md5)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if source is not None:
            pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "content_base64")

    @content_base64.setter
    def content_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_base64", value)

    @property
    @pulumi.getter(name="dbfsPath")
    def dbfs_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "dbfs_path")

    @dbfs_path.setter
    def dbfs_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dbfs_path", value)

    @property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "file_size")

    @file_size.setter
    def file_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "file_size", value)

    @property
    @pulumi.getter
    def md5(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "md5")

    @md5.setter
    def md5(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "md5", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)


class DbfsFile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_base64: Optional[pulumi.Input[str]] = None,
                 md5: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a DbfsFile resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DbfsFileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DbfsFile resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DbfsFileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DbfsFileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_base64: Optional[pulumi.Input[str]] = None,
                 md5: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
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
            __props__ = DbfsFileArgs.__new__(DbfsFileArgs)

            __props__.__dict__["content_base64"] = content_base64
            __props__.__dict__["md5"] = md5
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
            __props__.__dict__["source"] = source
            __props__.__dict__["dbfs_path"] = None
            __props__.__dict__["file_size"] = None
        super(DbfsFile, __self__).__init__(
            'databricks:index/dbfsFile:DbfsFile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            content_base64: Optional[pulumi.Input[str]] = None,
            dbfs_path: Optional[pulumi.Input[str]] = None,
            file_size: Optional[pulumi.Input[int]] = None,
            md5: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[str]] = None) -> 'DbfsFile':
        """
        Get an existing DbfsFile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DbfsFileState.__new__(_DbfsFileState)

        __props__.__dict__["content_base64"] = content_base64
        __props__.__dict__["dbfs_path"] = dbfs_path
        __props__.__dict__["file_size"] = file_size
        __props__.__dict__["md5"] = md5
        __props__.__dict__["path"] = path
        __props__.__dict__["source"] = source
        return DbfsFile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "content_base64")

    @property
    @pulumi.getter(name="dbfsPath")
    def dbfs_path(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dbfs_path")

    @property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> pulumi.Output[int]:
        return pulumi.get(self, "file_size")

    @property
    @pulumi.getter
    def md5(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "md5")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source")

