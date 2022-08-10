// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Example Usage
//
// Allows specification of custom configuration properties for expert usage:
//
//  * `enableIpAccessLists` - enables the use of IpAccessList resources
//  * `maxTokenLifetimeDays` - (string) Maximum token lifetime of new tokens in days, as an integer. If zero, new tokens are permitted to have no lifetime limit. Negative numbers are unsupported. **WARNING:** This limit only applies to new tokens, so there may be tokens with lifetimes longer than this value, including unlimited lifetime. Such tokens may have been created before the current maximum token lifetime was set.
//  * `enableTokensConfig` - (boolean) Enable or disable personal access tokens for this workspace.
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
// 		_, err := databricks.NewWorkspaceConf(ctx, "this", &databricks.WorkspaceConfArgs{
// 			CustomConfig: pulumi.AnyMap{
// 				"enableIpAccessLists": pulumi.Any(true),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// -> **Note** Importing this resource is not currently supported.
type WorkspaceConf struct {
	pulumi.CustomResourceState

	// Key-value map of strings that represent workspace configuration. Upon resource deletion, properties that start with `enable` or `enforce` will be reset to `false` value, regardless of initial default one.
	CustomConfig pulumi.MapOutput `pulumi:"customConfig"`
}

// NewWorkspaceConf registers a new resource with the given unique name, arguments, and options.
func NewWorkspaceConf(ctx *pulumi.Context,
	name string, args *WorkspaceConfArgs, opts ...pulumi.ResourceOption) (*WorkspaceConf, error) {
	if args == nil {
		args = &WorkspaceConfArgs{}
	}

	var resource WorkspaceConf
	err := ctx.RegisterResource("databricks:index/workspaceConf:WorkspaceConf", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWorkspaceConf gets an existing WorkspaceConf resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWorkspaceConf(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WorkspaceConfState, opts ...pulumi.ResourceOption) (*WorkspaceConf, error) {
	var resource WorkspaceConf
	err := ctx.ReadResource("databricks:index/workspaceConf:WorkspaceConf", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WorkspaceConf resources.
type workspaceConfState struct {
	// Key-value map of strings that represent workspace configuration. Upon resource deletion, properties that start with `enable` or `enforce` will be reset to `false` value, regardless of initial default one.
	CustomConfig map[string]interface{} `pulumi:"customConfig"`
}

type WorkspaceConfState struct {
	// Key-value map of strings that represent workspace configuration. Upon resource deletion, properties that start with `enable` or `enforce` will be reset to `false` value, regardless of initial default one.
	CustomConfig pulumi.MapInput
}

func (WorkspaceConfState) ElementType() reflect.Type {
	return reflect.TypeOf((*workspaceConfState)(nil)).Elem()
}

type workspaceConfArgs struct {
	// Key-value map of strings that represent workspace configuration. Upon resource deletion, properties that start with `enable` or `enforce` will be reset to `false` value, regardless of initial default one.
	CustomConfig map[string]interface{} `pulumi:"customConfig"`
}

// The set of arguments for constructing a WorkspaceConf resource.
type WorkspaceConfArgs struct {
	// Key-value map of strings that represent workspace configuration. Upon resource deletion, properties that start with `enable` or `enforce` will be reset to `false` value, regardless of initial default one.
	CustomConfig pulumi.MapInput
}

func (WorkspaceConfArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*workspaceConfArgs)(nil)).Elem()
}

type WorkspaceConfInput interface {
	pulumi.Input

	ToWorkspaceConfOutput() WorkspaceConfOutput
	ToWorkspaceConfOutputWithContext(ctx context.Context) WorkspaceConfOutput
}

func (*WorkspaceConf) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkspaceConf)(nil)).Elem()
}

func (i *WorkspaceConf) ToWorkspaceConfOutput() WorkspaceConfOutput {
	return i.ToWorkspaceConfOutputWithContext(context.Background())
}

func (i *WorkspaceConf) ToWorkspaceConfOutputWithContext(ctx context.Context) WorkspaceConfOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceConfOutput)
}

// WorkspaceConfArrayInput is an input type that accepts WorkspaceConfArray and WorkspaceConfArrayOutput values.
// You can construct a concrete instance of `WorkspaceConfArrayInput` via:
//
//          WorkspaceConfArray{ WorkspaceConfArgs{...} }
type WorkspaceConfArrayInput interface {
	pulumi.Input

	ToWorkspaceConfArrayOutput() WorkspaceConfArrayOutput
	ToWorkspaceConfArrayOutputWithContext(context.Context) WorkspaceConfArrayOutput
}

type WorkspaceConfArray []WorkspaceConfInput

func (WorkspaceConfArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WorkspaceConf)(nil)).Elem()
}

func (i WorkspaceConfArray) ToWorkspaceConfArrayOutput() WorkspaceConfArrayOutput {
	return i.ToWorkspaceConfArrayOutputWithContext(context.Background())
}

func (i WorkspaceConfArray) ToWorkspaceConfArrayOutputWithContext(ctx context.Context) WorkspaceConfArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceConfArrayOutput)
}

// WorkspaceConfMapInput is an input type that accepts WorkspaceConfMap and WorkspaceConfMapOutput values.
// You can construct a concrete instance of `WorkspaceConfMapInput` via:
//
//          WorkspaceConfMap{ "key": WorkspaceConfArgs{...} }
type WorkspaceConfMapInput interface {
	pulumi.Input

	ToWorkspaceConfMapOutput() WorkspaceConfMapOutput
	ToWorkspaceConfMapOutputWithContext(context.Context) WorkspaceConfMapOutput
}

type WorkspaceConfMap map[string]WorkspaceConfInput

func (WorkspaceConfMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WorkspaceConf)(nil)).Elem()
}

func (i WorkspaceConfMap) ToWorkspaceConfMapOutput() WorkspaceConfMapOutput {
	return i.ToWorkspaceConfMapOutputWithContext(context.Background())
}

func (i WorkspaceConfMap) ToWorkspaceConfMapOutputWithContext(ctx context.Context) WorkspaceConfMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceConfMapOutput)
}

type WorkspaceConfOutput struct{ *pulumi.OutputState }

func (WorkspaceConfOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkspaceConf)(nil)).Elem()
}

func (o WorkspaceConfOutput) ToWorkspaceConfOutput() WorkspaceConfOutput {
	return o
}

func (o WorkspaceConfOutput) ToWorkspaceConfOutputWithContext(ctx context.Context) WorkspaceConfOutput {
	return o
}

// Key-value map of strings that represent workspace configuration. Upon resource deletion, properties that start with `enable` or `enforce` will be reset to `false` value, regardless of initial default one.
func (o WorkspaceConfOutput) CustomConfig() pulumi.MapOutput {
	return o.ApplyT(func(v *WorkspaceConf) pulumi.MapOutput { return v.CustomConfig }).(pulumi.MapOutput)
}

type WorkspaceConfArrayOutput struct{ *pulumi.OutputState }

func (WorkspaceConfArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WorkspaceConf)(nil)).Elem()
}

func (o WorkspaceConfArrayOutput) ToWorkspaceConfArrayOutput() WorkspaceConfArrayOutput {
	return o
}

func (o WorkspaceConfArrayOutput) ToWorkspaceConfArrayOutputWithContext(ctx context.Context) WorkspaceConfArrayOutput {
	return o
}

func (o WorkspaceConfArrayOutput) Index(i pulumi.IntInput) WorkspaceConfOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *WorkspaceConf {
		return vs[0].([]*WorkspaceConf)[vs[1].(int)]
	}).(WorkspaceConfOutput)
}

type WorkspaceConfMapOutput struct{ *pulumi.OutputState }

func (WorkspaceConfMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WorkspaceConf)(nil)).Elem()
}

func (o WorkspaceConfMapOutput) ToWorkspaceConfMapOutput() WorkspaceConfMapOutput {
	return o
}

func (o WorkspaceConfMapOutput) ToWorkspaceConfMapOutputWithContext(ctx context.Context) WorkspaceConfMapOutput {
	return o
}

func (o WorkspaceConfMapOutput) MapIndex(k pulumi.StringInput) WorkspaceConfOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *WorkspaceConf {
		return vs[0].(map[string]*WorkspaceConf)[vs[1].(string)]
	}).(WorkspaceConfOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WorkspaceConfInput)(nil)).Elem(), &WorkspaceConf{})
	pulumi.RegisterInputType(reflect.TypeOf((*WorkspaceConfArrayInput)(nil)).Elem(), WorkspaceConfArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*WorkspaceConfMapInput)(nil)).Elem(), WorkspaceConfMap{})
	pulumi.RegisterOutputType(WorkspaceConfOutput{})
	pulumi.RegisterOutputType(WorkspaceConfArrayOutput{})
	pulumi.RegisterOutputType(WorkspaceConfMapOutput{})
}
