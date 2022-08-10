// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupNotebook(ctx *pulumi.Context, args *LookupNotebookArgs, opts ...pulumi.InvokeOption) (*LookupNotebookResult, error) {
	var rv LookupNotebookResult
	err := ctx.Invoke("databricks:index/getNotebook:getNotebook", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNotebook.
type LookupNotebookArgs struct {
	Format     string  `pulumi:"format"`
	Language   *string `pulumi:"language"`
	ObjectId   *int    `pulumi:"objectId"`
	ObjectType *string `pulumi:"objectType"`
	Path       string  `pulumi:"path"`
}

// A collection of values returned by getNotebook.
type LookupNotebookResult struct {
	Content string `pulumi:"content"`
	Format  string `pulumi:"format"`
	// The provider-assigned unique ID for this managed resource.
	Id         string `pulumi:"id"`
	Language   string `pulumi:"language"`
	ObjectId   int    `pulumi:"objectId"`
	ObjectType string `pulumi:"objectType"`
	Path       string `pulumi:"path"`
}

func LookupNotebookOutput(ctx *pulumi.Context, args LookupNotebookOutputArgs, opts ...pulumi.InvokeOption) LookupNotebookResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNotebookResult, error) {
			args := v.(LookupNotebookArgs)
			r, err := LookupNotebook(ctx, &args, opts...)
			return *r, err
		}).(LookupNotebookResultOutput)
}

// A collection of arguments for invoking getNotebook.
type LookupNotebookOutputArgs struct {
	Format     pulumi.StringInput    `pulumi:"format"`
	Language   pulumi.StringPtrInput `pulumi:"language"`
	ObjectId   pulumi.IntPtrInput    `pulumi:"objectId"`
	ObjectType pulumi.StringPtrInput `pulumi:"objectType"`
	Path       pulumi.StringInput    `pulumi:"path"`
}

func (LookupNotebookOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNotebookArgs)(nil)).Elem()
}

// A collection of values returned by getNotebook.
type LookupNotebookResultOutput struct{ *pulumi.OutputState }

func (LookupNotebookResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNotebookResult)(nil)).Elem()
}

func (o LookupNotebookResultOutput) ToLookupNotebookResultOutput() LookupNotebookResultOutput {
	return o
}

func (o LookupNotebookResultOutput) ToLookupNotebookResultOutputWithContext(ctx context.Context) LookupNotebookResultOutput {
	return o
}

func (o LookupNotebookResultOutput) Content() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNotebookResult) string { return v.Content }).(pulumi.StringOutput)
}

func (o LookupNotebookResultOutput) Format() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNotebookResult) string { return v.Format }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupNotebookResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNotebookResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupNotebookResultOutput) Language() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNotebookResult) string { return v.Language }).(pulumi.StringOutput)
}

func (o LookupNotebookResultOutput) ObjectId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNotebookResult) int { return v.ObjectId }).(pulumi.IntOutput)
}

func (o LookupNotebookResultOutput) ObjectType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNotebookResult) string { return v.ObjectType }).(pulumi.StringOutput)
}

func (o LookupNotebookResultOutput) Path() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNotebookResult) string { return v.Path }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNotebookResultOutput{})
}
