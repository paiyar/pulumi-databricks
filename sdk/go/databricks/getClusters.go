// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetClusters(ctx *pulumi.Context, args *GetClustersArgs, opts ...pulumi.InvokeOption) (*GetClustersResult, error) {
	var rv GetClustersResult
	err := ctx.Invoke("databricks:index/getClusters:getClusters", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getClusters.
type GetClustersArgs struct {
	ClusterNameContains *string `pulumi:"clusterNameContains"`
}

// A collection of values returned by getClusters.
type GetClustersResult struct {
	ClusterNameContains *string `pulumi:"clusterNameContains"`
	// The provider-assigned unique ID for this managed resource.
	Id  string   `pulumi:"id"`
	Ids []string `pulumi:"ids"`
}

func GetClustersOutput(ctx *pulumi.Context, args GetClustersOutputArgs, opts ...pulumi.InvokeOption) GetClustersResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetClustersResult, error) {
			args := v.(GetClustersArgs)
			r, err := GetClusters(ctx, &args, opts...)
			return *r, err
		}).(GetClustersResultOutput)
}

// A collection of arguments for invoking getClusters.
type GetClustersOutputArgs struct {
	ClusterNameContains pulumi.StringPtrInput `pulumi:"clusterNameContains"`
}

func (GetClustersOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetClustersArgs)(nil)).Elem()
}

// A collection of values returned by getClusters.
type GetClustersResultOutput struct{ *pulumi.OutputState }

func (GetClustersResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetClustersResult)(nil)).Elem()
}

func (o GetClustersResultOutput) ToGetClustersResultOutput() GetClustersResultOutput {
	return o
}

func (o GetClustersResultOutput) ToGetClustersResultOutputWithContext(ctx context.Context) GetClustersResultOutput {
	return o
}

func (o GetClustersResultOutput) ClusterNameContains() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetClustersResult) *string { return v.ClusterNameContains }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetClustersResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetClustersResultOutput) Ids() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetClustersResult) []string { return v.Ids }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetClustersResultOutput{})
}
