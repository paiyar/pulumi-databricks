// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// The resource global init script can be imported using script IDbash
//
// ```sh
//  $ pulumi import databricks:index/globalInitScript:GlobalInitScript this script_id
// ```
type GlobalInitScript struct {
	pulumi.CustomResourceState

	ContentBase64 pulumi.StringPtrOutput `pulumi:"contentBase64"`
	// specifies if the script is enabled for execution, or not
	Enabled pulumi.BoolPtrOutput   `pulumi:"enabled"`
	Md5     pulumi.StringPtrOutput `pulumi:"md5"`
	// - the name of the script.  It should be unique
	Name pulumi.StringOutput `pulumi:"name"`
	// - the position of a global init script, where `0` represents the first global init script to run, `1` is the second global init script to run, and so on. When omitted, the script gets the last position.
	Position pulumi.IntOutput `pulumi:"position"`
	// Path to script's source code on local filesystem. Conflicts with `contentBase64`
	Source pulumi.StringPtrOutput `pulumi:"source"`
}

// NewGlobalInitScript registers a new resource with the given unique name, arguments, and options.
func NewGlobalInitScript(ctx *pulumi.Context,
	name string, args *GlobalInitScriptArgs, opts ...pulumi.ResourceOption) (*GlobalInitScript, error) {
	if args == nil {
		args = &GlobalInitScriptArgs{}
	}

	var resource GlobalInitScript
	err := ctx.RegisterResource("databricks:index/globalInitScript:GlobalInitScript", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGlobalInitScript gets an existing GlobalInitScript resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGlobalInitScript(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GlobalInitScriptState, opts ...pulumi.ResourceOption) (*GlobalInitScript, error) {
	var resource GlobalInitScript
	err := ctx.ReadResource("databricks:index/globalInitScript:GlobalInitScript", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GlobalInitScript resources.
type globalInitScriptState struct {
	ContentBase64 *string `pulumi:"contentBase64"`
	// specifies if the script is enabled for execution, or not
	Enabled *bool   `pulumi:"enabled"`
	Md5     *string `pulumi:"md5"`
	// - the name of the script.  It should be unique
	Name *string `pulumi:"name"`
	// - the position of a global init script, where `0` represents the first global init script to run, `1` is the second global init script to run, and so on. When omitted, the script gets the last position.
	Position *int `pulumi:"position"`
	// Path to script's source code on local filesystem. Conflicts with `contentBase64`
	Source *string `pulumi:"source"`
}

type GlobalInitScriptState struct {
	ContentBase64 pulumi.StringPtrInput
	// specifies if the script is enabled for execution, or not
	Enabled pulumi.BoolPtrInput
	Md5     pulumi.StringPtrInput
	// - the name of the script.  It should be unique
	Name pulumi.StringPtrInput
	// - the position of a global init script, where `0` represents the first global init script to run, `1` is the second global init script to run, and so on. When omitted, the script gets the last position.
	Position pulumi.IntPtrInput
	// Path to script's source code on local filesystem. Conflicts with `contentBase64`
	Source pulumi.StringPtrInput
}

func (GlobalInitScriptState) ElementType() reflect.Type {
	return reflect.TypeOf((*globalInitScriptState)(nil)).Elem()
}

type globalInitScriptArgs struct {
	ContentBase64 *string `pulumi:"contentBase64"`
	// specifies if the script is enabled for execution, or not
	Enabled *bool   `pulumi:"enabled"`
	Md5     *string `pulumi:"md5"`
	// - the name of the script.  It should be unique
	Name *string `pulumi:"name"`
	// - the position of a global init script, where `0` represents the first global init script to run, `1` is the second global init script to run, and so on. When omitted, the script gets the last position.
	Position *int `pulumi:"position"`
	// Path to script's source code on local filesystem. Conflicts with `contentBase64`
	Source *string `pulumi:"source"`
}

// The set of arguments for constructing a GlobalInitScript resource.
type GlobalInitScriptArgs struct {
	ContentBase64 pulumi.StringPtrInput
	// specifies if the script is enabled for execution, or not
	Enabled pulumi.BoolPtrInput
	Md5     pulumi.StringPtrInput
	// - the name of the script.  It should be unique
	Name pulumi.StringPtrInput
	// - the position of a global init script, where `0` represents the first global init script to run, `1` is the second global init script to run, and so on. When omitted, the script gets the last position.
	Position pulumi.IntPtrInput
	// Path to script's source code on local filesystem. Conflicts with `contentBase64`
	Source pulumi.StringPtrInput
}

func (GlobalInitScriptArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*globalInitScriptArgs)(nil)).Elem()
}

type GlobalInitScriptInput interface {
	pulumi.Input

	ToGlobalInitScriptOutput() GlobalInitScriptOutput
	ToGlobalInitScriptOutputWithContext(ctx context.Context) GlobalInitScriptOutput
}

func (*GlobalInitScript) ElementType() reflect.Type {
	return reflect.TypeOf((**GlobalInitScript)(nil)).Elem()
}

func (i *GlobalInitScript) ToGlobalInitScriptOutput() GlobalInitScriptOutput {
	return i.ToGlobalInitScriptOutputWithContext(context.Background())
}

func (i *GlobalInitScript) ToGlobalInitScriptOutputWithContext(ctx context.Context) GlobalInitScriptOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GlobalInitScriptOutput)
}

// GlobalInitScriptArrayInput is an input type that accepts GlobalInitScriptArray and GlobalInitScriptArrayOutput values.
// You can construct a concrete instance of `GlobalInitScriptArrayInput` via:
//
//          GlobalInitScriptArray{ GlobalInitScriptArgs{...} }
type GlobalInitScriptArrayInput interface {
	pulumi.Input

	ToGlobalInitScriptArrayOutput() GlobalInitScriptArrayOutput
	ToGlobalInitScriptArrayOutputWithContext(context.Context) GlobalInitScriptArrayOutput
}

type GlobalInitScriptArray []GlobalInitScriptInput

func (GlobalInitScriptArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GlobalInitScript)(nil)).Elem()
}

func (i GlobalInitScriptArray) ToGlobalInitScriptArrayOutput() GlobalInitScriptArrayOutput {
	return i.ToGlobalInitScriptArrayOutputWithContext(context.Background())
}

func (i GlobalInitScriptArray) ToGlobalInitScriptArrayOutputWithContext(ctx context.Context) GlobalInitScriptArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GlobalInitScriptArrayOutput)
}

// GlobalInitScriptMapInput is an input type that accepts GlobalInitScriptMap and GlobalInitScriptMapOutput values.
// You can construct a concrete instance of `GlobalInitScriptMapInput` via:
//
//          GlobalInitScriptMap{ "key": GlobalInitScriptArgs{...} }
type GlobalInitScriptMapInput interface {
	pulumi.Input

	ToGlobalInitScriptMapOutput() GlobalInitScriptMapOutput
	ToGlobalInitScriptMapOutputWithContext(context.Context) GlobalInitScriptMapOutput
}

type GlobalInitScriptMap map[string]GlobalInitScriptInput

func (GlobalInitScriptMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GlobalInitScript)(nil)).Elem()
}

func (i GlobalInitScriptMap) ToGlobalInitScriptMapOutput() GlobalInitScriptMapOutput {
	return i.ToGlobalInitScriptMapOutputWithContext(context.Background())
}

func (i GlobalInitScriptMap) ToGlobalInitScriptMapOutputWithContext(ctx context.Context) GlobalInitScriptMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GlobalInitScriptMapOutput)
}

type GlobalInitScriptOutput struct{ *pulumi.OutputState }

func (GlobalInitScriptOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GlobalInitScript)(nil)).Elem()
}

func (o GlobalInitScriptOutput) ToGlobalInitScriptOutput() GlobalInitScriptOutput {
	return o
}

func (o GlobalInitScriptOutput) ToGlobalInitScriptOutputWithContext(ctx context.Context) GlobalInitScriptOutput {
	return o
}

func (o GlobalInitScriptOutput) ContentBase64() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *GlobalInitScript) pulumi.StringPtrOutput { return v.ContentBase64 }).(pulumi.StringPtrOutput)
}

// specifies if the script is enabled for execution, or not
func (o GlobalInitScriptOutput) Enabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *GlobalInitScript) pulumi.BoolPtrOutput { return v.Enabled }).(pulumi.BoolPtrOutput)
}

func (o GlobalInitScriptOutput) Md5() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *GlobalInitScript) pulumi.StringPtrOutput { return v.Md5 }).(pulumi.StringPtrOutput)
}

// - the name of the script.  It should be unique
func (o GlobalInitScriptOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *GlobalInitScript) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// - the position of a global init script, where `0` represents the first global init script to run, `1` is the second global init script to run, and so on. When omitted, the script gets the last position.
func (o GlobalInitScriptOutput) Position() pulumi.IntOutput {
	return o.ApplyT(func(v *GlobalInitScript) pulumi.IntOutput { return v.Position }).(pulumi.IntOutput)
}

// Path to script's source code on local filesystem. Conflicts with `contentBase64`
func (o GlobalInitScriptOutput) Source() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *GlobalInitScript) pulumi.StringPtrOutput { return v.Source }).(pulumi.StringPtrOutput)
}

type GlobalInitScriptArrayOutput struct{ *pulumi.OutputState }

func (GlobalInitScriptArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GlobalInitScript)(nil)).Elem()
}

func (o GlobalInitScriptArrayOutput) ToGlobalInitScriptArrayOutput() GlobalInitScriptArrayOutput {
	return o
}

func (o GlobalInitScriptArrayOutput) ToGlobalInitScriptArrayOutputWithContext(ctx context.Context) GlobalInitScriptArrayOutput {
	return o
}

func (o GlobalInitScriptArrayOutput) Index(i pulumi.IntInput) GlobalInitScriptOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *GlobalInitScript {
		return vs[0].([]*GlobalInitScript)[vs[1].(int)]
	}).(GlobalInitScriptOutput)
}

type GlobalInitScriptMapOutput struct{ *pulumi.OutputState }

func (GlobalInitScriptMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GlobalInitScript)(nil)).Elem()
}

func (o GlobalInitScriptMapOutput) ToGlobalInitScriptMapOutput() GlobalInitScriptMapOutput {
	return o
}

func (o GlobalInitScriptMapOutput) ToGlobalInitScriptMapOutputWithContext(ctx context.Context) GlobalInitScriptMapOutput {
	return o
}

func (o GlobalInitScriptMapOutput) MapIndex(k pulumi.StringInput) GlobalInitScriptOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *GlobalInitScript {
		return vs[0].(map[string]*GlobalInitScript)[vs[1].(string)]
	}).(GlobalInitScriptOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GlobalInitScriptInput)(nil)).Elem(), &GlobalInitScript{})
	pulumi.RegisterInputType(reflect.TypeOf((*GlobalInitScriptArrayInput)(nil)).Elem(), GlobalInitScriptArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GlobalInitScriptMapInput)(nil)).Elem(), GlobalInitScriptMap{})
	pulumi.RegisterOutputType(GlobalInitScriptOutput{})
	pulumi.RegisterOutputType(GlobalInitScriptArrayOutput{})
	pulumi.RegisterOutputType(GlobalInitScriptMapOutput{})
}
