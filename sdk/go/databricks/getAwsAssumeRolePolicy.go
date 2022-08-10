// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetAwsAssumeRolePolicy(ctx *pulumi.Context, args *GetAwsAssumeRolePolicyArgs, opts ...pulumi.InvokeOption) (*GetAwsAssumeRolePolicyResult, error) {
	var rv GetAwsAssumeRolePolicyResult
	err := ctx.Invoke("databricks:index/getAwsAssumeRolePolicy:getAwsAssumeRolePolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAwsAssumeRolePolicy.
type GetAwsAssumeRolePolicyArgs struct {
	DatabricksAccountId *string `pulumi:"databricksAccountId"`
	ExternalId          string  `pulumi:"externalId"`
	ForLogDelivery      *bool   `pulumi:"forLogDelivery"`
}

// A collection of values returned by getAwsAssumeRolePolicy.
type GetAwsAssumeRolePolicyResult struct {
	DatabricksAccountId *string `pulumi:"databricksAccountId"`
	ExternalId          string  `pulumi:"externalId"`
	ForLogDelivery      *bool   `pulumi:"forLogDelivery"`
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Json string `pulumi:"json"`
}

func GetAwsAssumeRolePolicyOutput(ctx *pulumi.Context, args GetAwsAssumeRolePolicyOutputArgs, opts ...pulumi.InvokeOption) GetAwsAssumeRolePolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetAwsAssumeRolePolicyResult, error) {
			args := v.(GetAwsAssumeRolePolicyArgs)
			r, err := GetAwsAssumeRolePolicy(ctx, &args, opts...)
			return *r, err
		}).(GetAwsAssumeRolePolicyResultOutput)
}

// A collection of arguments for invoking getAwsAssumeRolePolicy.
type GetAwsAssumeRolePolicyOutputArgs struct {
	DatabricksAccountId pulumi.StringPtrInput `pulumi:"databricksAccountId"`
	ExternalId          pulumi.StringInput    `pulumi:"externalId"`
	ForLogDelivery      pulumi.BoolPtrInput   `pulumi:"forLogDelivery"`
}

func (GetAwsAssumeRolePolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAwsAssumeRolePolicyArgs)(nil)).Elem()
}

// A collection of values returned by getAwsAssumeRolePolicy.
type GetAwsAssumeRolePolicyResultOutput struct{ *pulumi.OutputState }

func (GetAwsAssumeRolePolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAwsAssumeRolePolicyResult)(nil)).Elem()
}

func (o GetAwsAssumeRolePolicyResultOutput) ToGetAwsAssumeRolePolicyResultOutput() GetAwsAssumeRolePolicyResultOutput {
	return o
}

func (o GetAwsAssumeRolePolicyResultOutput) ToGetAwsAssumeRolePolicyResultOutputWithContext(ctx context.Context) GetAwsAssumeRolePolicyResultOutput {
	return o
}

func (o GetAwsAssumeRolePolicyResultOutput) DatabricksAccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAwsAssumeRolePolicyResult) *string { return v.DatabricksAccountId }).(pulumi.StringPtrOutput)
}

func (o GetAwsAssumeRolePolicyResultOutput) ExternalId() pulumi.StringOutput {
	return o.ApplyT(func(v GetAwsAssumeRolePolicyResult) string { return v.ExternalId }).(pulumi.StringOutput)
}

func (o GetAwsAssumeRolePolicyResultOutput) ForLogDelivery() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v GetAwsAssumeRolePolicyResult) *bool { return v.ForLogDelivery }).(pulumi.BoolPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetAwsAssumeRolePolicyResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetAwsAssumeRolePolicyResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetAwsAssumeRolePolicyResultOutput) Json() pulumi.StringOutput {
	return o.ApplyT(func(v GetAwsAssumeRolePolicyResult) string { return v.Json }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetAwsAssumeRolePolicyResultOutput{})
}
