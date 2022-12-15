// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// > **Note** This resource has an evolving API, which may change in future versions of the provider. Please always consult [latest documentation](https://docs.databricks.com/administration-guide/account-api/iam-role.html#language-Your%C2%A0VPC,%C2%A0default) in case of any questions.
//
// This data source constructs necessary AWS cross-account policy for you, which is based on [official documentation](https://docs.databricks.com/administration-guide/account-api/iam-role.html#language-Your%C2%A0VPC,%C2%A0default).
//
// ## Example Usage
//
// For more detailed usage please see getAwsAssumeRolePolicy or AwsS3Mount pages.
//
// ```go
// package main
//
// import (
// 	"github.com/paiyar/pulumi-databricks/sdk/go/databricks"
// 	"github.com/pulumi/pulumi-databricks/sdk/go/databricks"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := databricks.GetAwsCrossaccountPolicy(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ## Related Resources
//
// The following resources are used in the same context:
//
// * Provisioning AWS Databricks E2 with a Hub & Spoke firewall for data exfiltration protection guide
// * getAwsAssumeRolePolicy data to construct the necessary AWS STS assume role policy.
// * getAwsBucketPolicy data to configure a simple access policy for AWS S3 buckets, so that Databricks can access data in it.
// * InstanceProfile to manage AWS EC2 instance profiles that users can launch Cluster and access data, like databricks_mount.
func GetAwsCrossaccountPolicy(ctx *pulumi.Context, args *GetAwsCrossaccountPolicyArgs, opts ...pulumi.InvokeOption) (*GetAwsCrossaccountPolicyResult, error) {
	var rv GetAwsCrossaccountPolicyResult
	err := ctx.Invoke("databricks:index/getAwsCrossaccountPolicy:getAwsCrossaccountPolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAwsCrossaccountPolicy.
type GetAwsCrossaccountPolicyArgs struct {
	// List of Data IAM role ARNs that are explicitly granted `iam:PassRole` action.
	PassRoles []string `pulumi:"passRoles"`
}

// A collection of values returned by getAwsCrossaccountPolicy.
type GetAwsCrossaccountPolicyResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// AWS IAM Policy JSON document
	Json      string   `pulumi:"json"`
	PassRoles []string `pulumi:"passRoles"`
}

func GetAwsCrossaccountPolicyOutput(ctx *pulumi.Context, args GetAwsCrossaccountPolicyOutputArgs, opts ...pulumi.InvokeOption) GetAwsCrossaccountPolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetAwsCrossaccountPolicyResult, error) {
			args := v.(GetAwsCrossaccountPolicyArgs)
			r, err := GetAwsCrossaccountPolicy(ctx, &args, opts...)
			var s GetAwsCrossaccountPolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetAwsCrossaccountPolicyResultOutput)
}

// A collection of arguments for invoking getAwsCrossaccountPolicy.
type GetAwsCrossaccountPolicyOutputArgs struct {
	// List of Data IAM role ARNs that are explicitly granted `iam:PassRole` action.
	PassRoles pulumi.StringArrayInput `pulumi:"passRoles"`
}

func (GetAwsCrossaccountPolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAwsCrossaccountPolicyArgs)(nil)).Elem()
}

// A collection of values returned by getAwsCrossaccountPolicy.
type GetAwsCrossaccountPolicyResultOutput struct{ *pulumi.OutputState }

func (GetAwsCrossaccountPolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAwsCrossaccountPolicyResult)(nil)).Elem()
}

func (o GetAwsCrossaccountPolicyResultOutput) ToGetAwsCrossaccountPolicyResultOutput() GetAwsCrossaccountPolicyResultOutput {
	return o
}

func (o GetAwsCrossaccountPolicyResultOutput) ToGetAwsCrossaccountPolicyResultOutputWithContext(ctx context.Context) GetAwsCrossaccountPolicyResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetAwsCrossaccountPolicyResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetAwsCrossaccountPolicyResult) string { return v.Id }).(pulumi.StringOutput)
}

// AWS IAM Policy JSON document
func (o GetAwsCrossaccountPolicyResultOutput) Json() pulumi.StringOutput {
	return o.ApplyT(func(v GetAwsCrossaccountPolicyResult) string { return v.Json }).(pulumi.StringOutput)
}

func (o GetAwsCrossaccountPolicyResultOutput) PassRoles() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetAwsCrossaccountPolicyResult) []string { return v.PassRoles }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetAwsCrossaccountPolicyResultOutput{})
}
