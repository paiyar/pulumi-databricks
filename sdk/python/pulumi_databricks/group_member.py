# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['GroupMemberArgs', 'GroupMember']

@pulumi.input_type
class GroupMemberArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 member_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a GroupMember resource.
        :param pulumi.Input[str] group_id: This is the id of the group resource.
        :param pulumi.Input[str] member_id: This is the id of the group or user.
        """
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "member_id", member_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        This is the id of the group resource.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Input[str]:
        """
        This is the id of the group or user.
        """
        return pulumi.get(self, "member_id")

    @member_id.setter
    def member_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "member_id", value)


@pulumi.input_type
class _GroupMemberState:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 member_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GroupMember resources.
        :param pulumi.Input[str] group_id: This is the id of the group resource.
        :param pulumi.Input[str] member_id: This is the id of the group or user.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if member_id is not None:
            pulumi.set(__self__, "member_id", member_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        This is the id of the group resource.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional[pulumi.Input[str]]:
        """
        This is the id of the group or user.
        """
        return pulumi.get(self, "member_id")

    @member_id.setter
    def member_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member_id", value)


class GroupMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 member_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to attach users and groups as group members.

        ## Example Usage

        After the following example, Bradley would have direct membership in group B and transitive membership in group A.

        ```python
        import pulumi
        import pulumi_databricks as databricks

        group = databricks.Group("group", display_name="A")
        index_group_group = databricks.Group("index/groupGroup", display_name="B")
        ab = databricks.GroupMember("ab",
            group_id=group.id,
            member_id=index / group_group["id"])
        bradley = databricks.User("bradley", user_name="bradley@example.com")
        bb = databricks.GroupMember("bb",
            group_id=index / group_group["id"],
            member_id=bradley.id)
        ```
        ## Related Resources

        The following resources are often used in the same context:

        * End to end workspace management guide.
        * Group to manage [groups in Databricks Workspace](https://docs.databricks.com/administration-guide/users-groups/groups.html) or [Account Console](https://accounts.cloud.databricks.com/) (for AWS deployments).
        * Group data to retrieve information about Group members, entitlements and instance profiles.
        * GroupInstanceProfile to attach InstanceProfile (AWS) to databricks_group.
        * IpAccessList to allow access from [predefined IP ranges](https://docs.databricks.com/security/network/ip-access-list.html).
        * User to [manage users](https://docs.databricks.com/administration-guide/users-groups/users.html), that could be added to Group within the workspace.
        * User data to retrieves information about databricks_user.
        * UserInstanceProfile to attach InstanceProfile (AWS) to databricks_user.

        ## Import

        -> **Note** Importing this resource is not currently supported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: This is the id of the group resource.
        :param pulumi.Input[str] member_id: This is the id of the group or user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to attach users and groups as group members.

        ## Example Usage

        After the following example, Bradley would have direct membership in group B and transitive membership in group A.

        ```python
        import pulumi
        import pulumi_databricks as databricks

        group = databricks.Group("group", display_name="A")
        index_group_group = databricks.Group("index/groupGroup", display_name="B")
        ab = databricks.GroupMember("ab",
            group_id=group.id,
            member_id=index / group_group["id"])
        bradley = databricks.User("bradley", user_name="bradley@example.com")
        bb = databricks.GroupMember("bb",
            group_id=index / group_group["id"],
            member_id=bradley.id)
        ```
        ## Related Resources

        The following resources are often used in the same context:

        * End to end workspace management guide.
        * Group to manage [groups in Databricks Workspace](https://docs.databricks.com/administration-guide/users-groups/groups.html) or [Account Console](https://accounts.cloud.databricks.com/) (for AWS deployments).
        * Group data to retrieve information about Group members, entitlements and instance profiles.
        * GroupInstanceProfile to attach InstanceProfile (AWS) to databricks_group.
        * IpAccessList to allow access from [predefined IP ranges](https://docs.databricks.com/security/network/ip-access-list.html).
        * User to [manage users](https://docs.databricks.com/administration-guide/users-groups/users.html), that could be added to Group within the workspace.
        * User data to retrieves information about databricks_user.
        * UserInstanceProfile to attach InstanceProfile (AWS) to databricks_user.

        ## Import

        -> **Note** Importing this resource is not currently supported.

        :param str resource_name: The name of the resource.
        :param GroupMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 member_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = GroupMemberArgs.__new__(GroupMemberArgs)

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            if member_id is None and not opts.urn:
                raise TypeError("Missing required property 'member_id'")
            __props__.__dict__["member_id"] = member_id
        super(GroupMember, __self__).__init__(
            'databricks:index/groupMember:GroupMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            member_id: Optional[pulumi.Input[str]] = None) -> 'GroupMember':
        """
        Get an existing GroupMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: This is the id of the group resource.
        :param pulumi.Input[str] member_id: This is the id of the group or user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupMemberState.__new__(_GroupMemberState)

        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["member_id"] = member_id
        return GroupMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        This is the id of the group resource.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Output[str]:
        """
        This is the id of the group or user.
        """
        return pulumi.get(self, "member_id")

