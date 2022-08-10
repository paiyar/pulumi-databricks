// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type UserInstanceProfile struct {
	pulumi.CustomResourceState

	InstanceProfileId pulumi.StringOutput `pulumi:"instanceProfileId"`
	UserId            pulumi.StringOutput `pulumi:"userId"`
}

// NewUserInstanceProfile registers a new resource with the given unique name, arguments, and options.
func NewUserInstanceProfile(ctx *pulumi.Context,
	name string, args *UserInstanceProfileArgs, opts ...pulumi.ResourceOption) (*UserInstanceProfile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceProfileId == nil {
		return nil, errors.New("invalid value for required argument 'InstanceProfileId'")
	}
	if args.UserId == nil {
		return nil, errors.New("invalid value for required argument 'UserId'")
	}
	var resource UserInstanceProfile
	err := ctx.RegisterResource("databricks:index/userInstanceProfile:UserInstanceProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserInstanceProfile gets an existing UserInstanceProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserInstanceProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserInstanceProfileState, opts ...pulumi.ResourceOption) (*UserInstanceProfile, error) {
	var resource UserInstanceProfile
	err := ctx.ReadResource("databricks:index/userInstanceProfile:UserInstanceProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserInstanceProfile resources.
type userInstanceProfileState struct {
	InstanceProfileId *string `pulumi:"instanceProfileId"`
	UserId            *string `pulumi:"userId"`
}

type UserInstanceProfileState struct {
	InstanceProfileId pulumi.StringPtrInput
	UserId            pulumi.StringPtrInput
}

func (UserInstanceProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*userInstanceProfileState)(nil)).Elem()
}

type userInstanceProfileArgs struct {
	InstanceProfileId string `pulumi:"instanceProfileId"`
	UserId            string `pulumi:"userId"`
}

// The set of arguments for constructing a UserInstanceProfile resource.
type UserInstanceProfileArgs struct {
	InstanceProfileId pulumi.StringInput
	UserId            pulumi.StringInput
}

func (UserInstanceProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userInstanceProfileArgs)(nil)).Elem()
}

type UserInstanceProfileInput interface {
	pulumi.Input

	ToUserInstanceProfileOutput() UserInstanceProfileOutput
	ToUserInstanceProfileOutputWithContext(ctx context.Context) UserInstanceProfileOutput
}

func (*UserInstanceProfile) ElementType() reflect.Type {
	return reflect.TypeOf((**UserInstanceProfile)(nil)).Elem()
}

func (i *UserInstanceProfile) ToUserInstanceProfileOutput() UserInstanceProfileOutput {
	return i.ToUserInstanceProfileOutputWithContext(context.Background())
}

func (i *UserInstanceProfile) ToUserInstanceProfileOutputWithContext(ctx context.Context) UserInstanceProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserInstanceProfileOutput)
}

// UserInstanceProfileArrayInput is an input type that accepts UserInstanceProfileArray and UserInstanceProfileArrayOutput values.
// You can construct a concrete instance of `UserInstanceProfileArrayInput` via:
//
//          UserInstanceProfileArray{ UserInstanceProfileArgs{...} }
type UserInstanceProfileArrayInput interface {
	pulumi.Input

	ToUserInstanceProfileArrayOutput() UserInstanceProfileArrayOutput
	ToUserInstanceProfileArrayOutputWithContext(context.Context) UserInstanceProfileArrayOutput
}

type UserInstanceProfileArray []UserInstanceProfileInput

func (UserInstanceProfileArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*UserInstanceProfile)(nil)).Elem()
}

func (i UserInstanceProfileArray) ToUserInstanceProfileArrayOutput() UserInstanceProfileArrayOutput {
	return i.ToUserInstanceProfileArrayOutputWithContext(context.Background())
}

func (i UserInstanceProfileArray) ToUserInstanceProfileArrayOutputWithContext(ctx context.Context) UserInstanceProfileArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserInstanceProfileArrayOutput)
}

// UserInstanceProfileMapInput is an input type that accepts UserInstanceProfileMap and UserInstanceProfileMapOutput values.
// You can construct a concrete instance of `UserInstanceProfileMapInput` via:
//
//          UserInstanceProfileMap{ "key": UserInstanceProfileArgs{...} }
type UserInstanceProfileMapInput interface {
	pulumi.Input

	ToUserInstanceProfileMapOutput() UserInstanceProfileMapOutput
	ToUserInstanceProfileMapOutputWithContext(context.Context) UserInstanceProfileMapOutput
}

type UserInstanceProfileMap map[string]UserInstanceProfileInput

func (UserInstanceProfileMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*UserInstanceProfile)(nil)).Elem()
}

func (i UserInstanceProfileMap) ToUserInstanceProfileMapOutput() UserInstanceProfileMapOutput {
	return i.ToUserInstanceProfileMapOutputWithContext(context.Background())
}

func (i UserInstanceProfileMap) ToUserInstanceProfileMapOutputWithContext(ctx context.Context) UserInstanceProfileMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserInstanceProfileMapOutput)
}

type UserInstanceProfileOutput struct{ *pulumi.OutputState }

func (UserInstanceProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserInstanceProfile)(nil)).Elem()
}

func (o UserInstanceProfileOutput) ToUserInstanceProfileOutput() UserInstanceProfileOutput {
	return o
}

func (o UserInstanceProfileOutput) ToUserInstanceProfileOutputWithContext(ctx context.Context) UserInstanceProfileOutput {
	return o
}

type UserInstanceProfileArrayOutput struct{ *pulumi.OutputState }

func (UserInstanceProfileArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*UserInstanceProfile)(nil)).Elem()
}

func (o UserInstanceProfileArrayOutput) ToUserInstanceProfileArrayOutput() UserInstanceProfileArrayOutput {
	return o
}

func (o UserInstanceProfileArrayOutput) ToUserInstanceProfileArrayOutputWithContext(ctx context.Context) UserInstanceProfileArrayOutput {
	return o
}

func (o UserInstanceProfileArrayOutput) Index(i pulumi.IntInput) UserInstanceProfileOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *UserInstanceProfile {
		return vs[0].([]*UserInstanceProfile)[vs[1].(int)]
	}).(UserInstanceProfileOutput)
}

type UserInstanceProfileMapOutput struct{ *pulumi.OutputState }

func (UserInstanceProfileMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*UserInstanceProfile)(nil)).Elem()
}

func (o UserInstanceProfileMapOutput) ToUserInstanceProfileMapOutput() UserInstanceProfileMapOutput {
	return o
}

func (o UserInstanceProfileMapOutput) ToUserInstanceProfileMapOutputWithContext(ctx context.Context) UserInstanceProfileMapOutput {
	return o
}

func (o UserInstanceProfileMapOutput) MapIndex(k pulumi.StringInput) UserInstanceProfileOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *UserInstanceProfile {
		return vs[0].(map[string]*UserInstanceProfile)[vs[1].(string)]
	}).(UserInstanceProfileOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserInstanceProfileInput)(nil)).Elem(), &UserInstanceProfile{})
	pulumi.RegisterInputType(reflect.TypeOf((*UserInstanceProfileArrayInput)(nil)).Elem(), UserInstanceProfileArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*UserInstanceProfileMapInput)(nil)).Elem(), UserInstanceProfileMap{})
	pulumi.RegisterOutputType(UserInstanceProfileOutput{})
	pulumi.RegisterOutputType(UserInstanceProfileArrayOutput{})
	pulumi.RegisterOutputType(UserInstanceProfileMapOutput{})
}
