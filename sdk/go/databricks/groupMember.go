// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This resource allows you to attach users, service_principal, and groups as group members.
//
// To attach members to groups in the Databricks account, the provider must be configured with `host = "https://accounts.cloud.databricks.com"` on AWS deployments or `host = "https://accounts.azuredatabricks.net"` and authenticate using AAD tokens on Azure deployments
//
// ## Example Usage
//
// After the following example, Bradley would have direct membership in group B and transitive membership in group A.
//
// ```go
// package main
//
// import (
// 	"github.com/paiyar/pulumi-databricks/sdk/go/databricks"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		group, err := databricks.NewGroup(ctx, "group", &databricks.GroupArgs{
// 			DisplayName: pulumi.String("A"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = databricks.NewGroup(ctx, "index/groupGroup", &databricks.GroupArgs{
// 			DisplayName: pulumi.String("B"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = databricks.NewGroupMember(ctx, "ab", &databricks.GroupMemberArgs{
// 			GroupId:  group.ID(),
// 			MemberId: index / groupGroup.Id,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		bradley, err := databricks.NewUser(ctx, "bradley", &databricks.UserArgs{
// 			UserName: pulumi.String("bradley@example.com"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = databricks.NewGroupMember(ctx, "bb", &databricks.GroupMemberArgs{
// 			GroupId:  index / groupGroup.Id,
// 			MemberId: bradley.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ## Related Resources
//
// The following resources are often used in the same context:
//
// * End to end workspace management guide.
// * Group to manage [groups in Databricks Workspace](https://docs.databricks.com/administration-guide/users-groups/groups.html) or [Account Console](https://accounts.cloud.databricks.com/) (for AWS deployments).
// * Group data to retrieve information about Group members, entitlements and instance profiles.
// * GroupInstanceProfile to attach InstanceProfile (AWS) to databricks_group.
// * IpAccessList to allow access from [predefined IP ranges](https://docs.databricks.com/security/network/ip-access-list.html).
// * ServicePrincipal to grant access to a workspace to an automation tool or application.
// * User to [manage users](https://docs.databricks.com/administration-guide/users-groups/users.html), that could be added to Group within the workspace.
// * User data to retrieve information about databricks_user.
// * UserInstanceProfile to attach InstanceProfile (AWS) to databricks_user.
//
// ## Import
//
// -> **Note** Importing this resource is not currently supported.
type GroupMember struct {
	pulumi.CustomResourceState

	// This is the id of the group resource.
	GroupId pulumi.StringOutput `pulumi:"groupId"`
	// This is the id of the group, service principal, or user.
	MemberId pulumi.StringOutput `pulumi:"memberId"`
}

// NewGroupMember registers a new resource with the given unique name, arguments, and options.
func NewGroupMember(ctx *pulumi.Context,
	name string, args *GroupMemberArgs, opts ...pulumi.ResourceOption) (*GroupMember, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.GroupId == nil {
		return nil, errors.New("invalid value for required argument 'GroupId'")
	}
	if args.MemberId == nil {
		return nil, errors.New("invalid value for required argument 'MemberId'")
	}
	var resource GroupMember
	err := ctx.RegisterResource("databricks:index/groupMember:GroupMember", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGroupMember gets an existing GroupMember resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGroupMember(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GroupMemberState, opts ...pulumi.ResourceOption) (*GroupMember, error) {
	var resource GroupMember
	err := ctx.ReadResource("databricks:index/groupMember:GroupMember", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GroupMember resources.
type groupMemberState struct {
	// This is the id of the group resource.
	GroupId *string `pulumi:"groupId"`
	// This is the id of the group, service principal, or user.
	MemberId *string `pulumi:"memberId"`
}

type GroupMemberState struct {
	// This is the id of the group resource.
	GroupId pulumi.StringPtrInput
	// This is the id of the group, service principal, or user.
	MemberId pulumi.StringPtrInput
}

func (GroupMemberState) ElementType() reflect.Type {
	return reflect.TypeOf((*groupMemberState)(nil)).Elem()
}

type groupMemberArgs struct {
	// This is the id of the group resource.
	GroupId string `pulumi:"groupId"`
	// This is the id of the group, service principal, or user.
	MemberId string `pulumi:"memberId"`
}

// The set of arguments for constructing a GroupMember resource.
type GroupMemberArgs struct {
	// This is the id of the group resource.
	GroupId pulumi.StringInput
	// This is the id of the group, service principal, or user.
	MemberId pulumi.StringInput
}

func (GroupMemberArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*groupMemberArgs)(nil)).Elem()
}

type GroupMemberInput interface {
	pulumi.Input

	ToGroupMemberOutput() GroupMemberOutput
	ToGroupMemberOutputWithContext(ctx context.Context) GroupMemberOutput
}

func (*GroupMember) ElementType() reflect.Type {
	return reflect.TypeOf((**GroupMember)(nil)).Elem()
}

func (i *GroupMember) ToGroupMemberOutput() GroupMemberOutput {
	return i.ToGroupMemberOutputWithContext(context.Background())
}

func (i *GroupMember) ToGroupMemberOutputWithContext(ctx context.Context) GroupMemberOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMemberOutput)
}

// GroupMemberArrayInput is an input type that accepts GroupMemberArray and GroupMemberArrayOutput values.
// You can construct a concrete instance of `GroupMemberArrayInput` via:
//
//          GroupMemberArray{ GroupMemberArgs{...} }
type GroupMemberArrayInput interface {
	pulumi.Input

	ToGroupMemberArrayOutput() GroupMemberArrayOutput
	ToGroupMemberArrayOutputWithContext(context.Context) GroupMemberArrayOutput
}

type GroupMemberArray []GroupMemberInput

func (GroupMemberArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GroupMember)(nil)).Elem()
}

func (i GroupMemberArray) ToGroupMemberArrayOutput() GroupMemberArrayOutput {
	return i.ToGroupMemberArrayOutputWithContext(context.Background())
}

func (i GroupMemberArray) ToGroupMemberArrayOutputWithContext(ctx context.Context) GroupMemberArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMemberArrayOutput)
}

// GroupMemberMapInput is an input type that accepts GroupMemberMap and GroupMemberMapOutput values.
// You can construct a concrete instance of `GroupMemberMapInput` via:
//
//          GroupMemberMap{ "key": GroupMemberArgs{...} }
type GroupMemberMapInput interface {
	pulumi.Input

	ToGroupMemberMapOutput() GroupMemberMapOutput
	ToGroupMemberMapOutputWithContext(context.Context) GroupMemberMapOutput
}

type GroupMemberMap map[string]GroupMemberInput

func (GroupMemberMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GroupMember)(nil)).Elem()
}

func (i GroupMemberMap) ToGroupMemberMapOutput() GroupMemberMapOutput {
	return i.ToGroupMemberMapOutputWithContext(context.Background())
}

func (i GroupMemberMap) ToGroupMemberMapOutputWithContext(ctx context.Context) GroupMemberMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMemberMapOutput)
}

type GroupMemberOutput struct{ *pulumi.OutputState }

func (GroupMemberOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GroupMember)(nil)).Elem()
}

func (o GroupMemberOutput) ToGroupMemberOutput() GroupMemberOutput {
	return o
}

func (o GroupMemberOutput) ToGroupMemberOutputWithContext(ctx context.Context) GroupMemberOutput {
	return o
}

// This is the id of the group resource.
func (o GroupMemberOutput) GroupId() pulumi.StringOutput {
	return o.ApplyT(func(v *GroupMember) pulumi.StringOutput { return v.GroupId }).(pulumi.StringOutput)
}

// This is the id of the group, service principal, or user.
func (o GroupMemberOutput) MemberId() pulumi.StringOutput {
	return o.ApplyT(func(v *GroupMember) pulumi.StringOutput { return v.MemberId }).(pulumi.StringOutput)
}

type GroupMemberArrayOutput struct{ *pulumi.OutputState }

func (GroupMemberArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GroupMember)(nil)).Elem()
}

func (o GroupMemberArrayOutput) ToGroupMemberArrayOutput() GroupMemberArrayOutput {
	return o
}

func (o GroupMemberArrayOutput) ToGroupMemberArrayOutputWithContext(ctx context.Context) GroupMemberArrayOutput {
	return o
}

func (o GroupMemberArrayOutput) Index(i pulumi.IntInput) GroupMemberOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *GroupMember {
		return vs[0].([]*GroupMember)[vs[1].(int)]
	}).(GroupMemberOutput)
}

type GroupMemberMapOutput struct{ *pulumi.OutputState }

func (GroupMemberMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GroupMember)(nil)).Elem()
}

func (o GroupMemberMapOutput) ToGroupMemberMapOutput() GroupMemberMapOutput {
	return o
}

func (o GroupMemberMapOutput) ToGroupMemberMapOutputWithContext(ctx context.Context) GroupMemberMapOutput {
	return o
}

func (o GroupMemberMapOutput) MapIndex(k pulumi.StringInput) GroupMemberOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *GroupMember {
		return vs[0].(map[string]*GroupMember)[vs[1].(string)]
	}).(GroupMemberOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GroupMemberInput)(nil)).Elem(), &GroupMember{})
	pulumi.RegisterInputType(reflect.TypeOf((*GroupMemberArrayInput)(nil)).Elem(), GroupMemberArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GroupMemberMapInput)(nil)).Elem(), GroupMemberMap{})
	pulumi.RegisterOutputType(GroupMemberOutput{})
	pulumi.RegisterOutputType(GroupMemberArrayOutput{})
	pulumi.RegisterOutputType(GroupMemberMapOutput{})
}
