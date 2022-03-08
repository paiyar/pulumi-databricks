// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetTables(ctx *pulumi.Context, args *GetTablesArgs, opts ...pulumi.InvokeOption) (*GetTablesResult, error) {
	var rv GetTablesResult
	err := ctx.Invoke("databricks:index/getTables:getTables", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTables.
type GetTablesArgs struct {
	// Name of databricks_catalog
	CatalogName string `pulumi:"catalogName"`
	// set of Table full names: *`catalog`.`schema`.`table`*
	Ids []string `pulumi:"ids"`
	// Name of databricks_schema
	SchemaName string `pulumi:"schemaName"`
}

// A collection of values returned by getTables.
type GetTablesResult struct {
	CatalogName string `pulumi:"catalogName"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// set of Table full names: *`catalog`.`schema`.`table`*
	Ids        []string `pulumi:"ids"`
	SchemaName string   `pulumi:"schemaName"`
}

func GetTablesOutput(ctx *pulumi.Context, args GetTablesOutputArgs, opts ...pulumi.InvokeOption) GetTablesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetTablesResult, error) {
			args := v.(GetTablesArgs)
			r, err := GetTables(ctx, &args, opts...)
			return *r, err
		}).(GetTablesResultOutput)
}

// A collection of arguments for invoking getTables.
type GetTablesOutputArgs struct {
	// Name of databricks_catalog
	CatalogName pulumi.StringInput `pulumi:"catalogName"`
	// set of Table full names: *`catalog`.`schema`.`table`*
	Ids pulumi.StringArrayInput `pulumi:"ids"`
	// Name of databricks_schema
	SchemaName pulumi.StringInput `pulumi:"schemaName"`
}

func (GetTablesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTablesArgs)(nil)).Elem()
}

// A collection of values returned by getTables.
type GetTablesResultOutput struct{ *pulumi.OutputState }

func (GetTablesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTablesResult)(nil)).Elem()
}

func (o GetTablesResultOutput) ToGetTablesResultOutput() GetTablesResultOutput {
	return o
}

func (o GetTablesResultOutput) ToGetTablesResultOutputWithContext(ctx context.Context) GetTablesResultOutput {
	return o
}

func (o GetTablesResultOutput) CatalogName() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesResult) string { return v.CatalogName }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetTablesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesResult) string { return v.Id }).(pulumi.StringOutput)
}

// set of Table full names: *`catalog`.`schema`.`table`*
func (o GetTablesResultOutput) Ids() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetTablesResult) []string { return v.Ids }).(pulumi.StringArrayOutput)
}

func (o GetTablesResultOutput) SchemaName() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesResult) string { return v.SchemaName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetTablesResultOutput{})
}
