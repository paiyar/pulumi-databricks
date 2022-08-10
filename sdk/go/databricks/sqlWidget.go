// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type SqlWidget struct {
	pulumi.CustomResourceState

	DashboardId     pulumi.StringOutput           `pulumi:"dashboardId"`
	Description     pulumi.StringPtrOutput        `pulumi:"description"`
	Parameters      SqlWidgetParameterArrayOutput `pulumi:"parameters"`
	Position        SqlWidgetPositionPtrOutput    `pulumi:"position"`
	Text            pulumi.StringPtrOutput        `pulumi:"text"`
	Title           pulumi.StringPtrOutput        `pulumi:"title"`
	VisualizationId pulumi.StringPtrOutput        `pulumi:"visualizationId"`
	WidgetId        pulumi.StringOutput           `pulumi:"widgetId"`
}

// NewSqlWidget registers a new resource with the given unique name, arguments, and options.
func NewSqlWidget(ctx *pulumi.Context,
	name string, args *SqlWidgetArgs, opts ...pulumi.ResourceOption) (*SqlWidget, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DashboardId == nil {
		return nil, errors.New("invalid value for required argument 'DashboardId'")
	}
	var resource SqlWidget
	err := ctx.RegisterResource("databricks:index/sqlWidget:SqlWidget", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSqlWidget gets an existing SqlWidget resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSqlWidget(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SqlWidgetState, opts ...pulumi.ResourceOption) (*SqlWidget, error) {
	var resource SqlWidget
	err := ctx.ReadResource("databricks:index/sqlWidget:SqlWidget", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SqlWidget resources.
type sqlWidgetState struct {
	DashboardId     *string              `pulumi:"dashboardId"`
	Description     *string              `pulumi:"description"`
	Parameters      []SqlWidgetParameter `pulumi:"parameters"`
	Position        *SqlWidgetPosition   `pulumi:"position"`
	Text            *string              `pulumi:"text"`
	Title           *string              `pulumi:"title"`
	VisualizationId *string              `pulumi:"visualizationId"`
	WidgetId        *string              `pulumi:"widgetId"`
}

type SqlWidgetState struct {
	DashboardId     pulumi.StringPtrInput
	Description     pulumi.StringPtrInput
	Parameters      SqlWidgetParameterArrayInput
	Position        SqlWidgetPositionPtrInput
	Text            pulumi.StringPtrInput
	Title           pulumi.StringPtrInput
	VisualizationId pulumi.StringPtrInput
	WidgetId        pulumi.StringPtrInput
}

func (SqlWidgetState) ElementType() reflect.Type {
	return reflect.TypeOf((*sqlWidgetState)(nil)).Elem()
}

type sqlWidgetArgs struct {
	DashboardId     string               `pulumi:"dashboardId"`
	Description     *string              `pulumi:"description"`
	Parameters      []SqlWidgetParameter `pulumi:"parameters"`
	Position        *SqlWidgetPosition   `pulumi:"position"`
	Text            *string              `pulumi:"text"`
	Title           *string              `pulumi:"title"`
	VisualizationId *string              `pulumi:"visualizationId"`
	WidgetId        *string              `pulumi:"widgetId"`
}

// The set of arguments for constructing a SqlWidget resource.
type SqlWidgetArgs struct {
	DashboardId     pulumi.StringInput
	Description     pulumi.StringPtrInput
	Parameters      SqlWidgetParameterArrayInput
	Position        SqlWidgetPositionPtrInput
	Text            pulumi.StringPtrInput
	Title           pulumi.StringPtrInput
	VisualizationId pulumi.StringPtrInput
	WidgetId        pulumi.StringPtrInput
}

func (SqlWidgetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sqlWidgetArgs)(nil)).Elem()
}

type SqlWidgetInput interface {
	pulumi.Input

	ToSqlWidgetOutput() SqlWidgetOutput
	ToSqlWidgetOutputWithContext(ctx context.Context) SqlWidgetOutput
}

func (*SqlWidget) ElementType() reflect.Type {
	return reflect.TypeOf((**SqlWidget)(nil)).Elem()
}

func (i *SqlWidget) ToSqlWidgetOutput() SqlWidgetOutput {
	return i.ToSqlWidgetOutputWithContext(context.Background())
}

func (i *SqlWidget) ToSqlWidgetOutputWithContext(ctx context.Context) SqlWidgetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SqlWidgetOutput)
}

// SqlWidgetArrayInput is an input type that accepts SqlWidgetArray and SqlWidgetArrayOutput values.
// You can construct a concrete instance of `SqlWidgetArrayInput` via:
//
//          SqlWidgetArray{ SqlWidgetArgs{...} }
type SqlWidgetArrayInput interface {
	pulumi.Input

	ToSqlWidgetArrayOutput() SqlWidgetArrayOutput
	ToSqlWidgetArrayOutputWithContext(context.Context) SqlWidgetArrayOutput
}

type SqlWidgetArray []SqlWidgetInput

func (SqlWidgetArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SqlWidget)(nil)).Elem()
}

func (i SqlWidgetArray) ToSqlWidgetArrayOutput() SqlWidgetArrayOutput {
	return i.ToSqlWidgetArrayOutputWithContext(context.Background())
}

func (i SqlWidgetArray) ToSqlWidgetArrayOutputWithContext(ctx context.Context) SqlWidgetArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SqlWidgetArrayOutput)
}

// SqlWidgetMapInput is an input type that accepts SqlWidgetMap and SqlWidgetMapOutput values.
// You can construct a concrete instance of `SqlWidgetMapInput` via:
//
//          SqlWidgetMap{ "key": SqlWidgetArgs{...} }
type SqlWidgetMapInput interface {
	pulumi.Input

	ToSqlWidgetMapOutput() SqlWidgetMapOutput
	ToSqlWidgetMapOutputWithContext(context.Context) SqlWidgetMapOutput
}

type SqlWidgetMap map[string]SqlWidgetInput

func (SqlWidgetMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SqlWidget)(nil)).Elem()
}

func (i SqlWidgetMap) ToSqlWidgetMapOutput() SqlWidgetMapOutput {
	return i.ToSqlWidgetMapOutputWithContext(context.Background())
}

func (i SqlWidgetMap) ToSqlWidgetMapOutputWithContext(ctx context.Context) SqlWidgetMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SqlWidgetMapOutput)
}

type SqlWidgetOutput struct{ *pulumi.OutputState }

func (SqlWidgetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SqlWidget)(nil)).Elem()
}

func (o SqlWidgetOutput) ToSqlWidgetOutput() SqlWidgetOutput {
	return o
}

func (o SqlWidgetOutput) ToSqlWidgetOutputWithContext(ctx context.Context) SqlWidgetOutput {
	return o
}

type SqlWidgetArrayOutput struct{ *pulumi.OutputState }

func (SqlWidgetArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SqlWidget)(nil)).Elem()
}

func (o SqlWidgetArrayOutput) ToSqlWidgetArrayOutput() SqlWidgetArrayOutput {
	return o
}

func (o SqlWidgetArrayOutput) ToSqlWidgetArrayOutputWithContext(ctx context.Context) SqlWidgetArrayOutput {
	return o
}

func (o SqlWidgetArrayOutput) Index(i pulumi.IntInput) SqlWidgetOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SqlWidget {
		return vs[0].([]*SqlWidget)[vs[1].(int)]
	}).(SqlWidgetOutput)
}

type SqlWidgetMapOutput struct{ *pulumi.OutputState }

func (SqlWidgetMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SqlWidget)(nil)).Elem()
}

func (o SqlWidgetMapOutput) ToSqlWidgetMapOutput() SqlWidgetMapOutput {
	return o
}

func (o SqlWidgetMapOutput) ToSqlWidgetMapOutputWithContext(ctx context.Context) SqlWidgetMapOutput {
	return o
}

func (o SqlWidgetMapOutput) MapIndex(k pulumi.StringInput) SqlWidgetOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SqlWidget {
		return vs[0].(map[string]*SqlWidget)[vs[1].(string)]
	}).(SqlWidgetOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SqlWidgetInput)(nil)).Elem(), &SqlWidget{})
	pulumi.RegisterInputType(reflect.TypeOf((*SqlWidgetArrayInput)(nil)).Elem(), SqlWidgetArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SqlWidgetMapInput)(nil)).Elem(), SqlWidgetMap{})
	pulumi.RegisterOutputType(SqlWidgetOutput{})
	pulumi.RegisterOutputType(SqlWidgetArrayOutput{})
	pulumi.RegisterOutputType(SqlWidgetMapOutput{})
}
