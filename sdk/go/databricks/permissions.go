// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// The resource permissions can be imported using the object id bash
//
// ```sh
//  $ pulumi import databricks:index/permissions:Permissions this /<object type>/<object id>
// ```
type Permissions struct {
	pulumi.CustomResourceState

	AccessControls PermissionsAccessControlArrayOutput `pulumi:"accessControls"`
	// either [`tokens`](https://docs.databricks.com/administration-guide/access-control/tokens.html) or [`passwords`](https://docs.databricks.com/administration-guide/users-groups/single-sign-on/index.html#configure-password-permission).
	Authorization pulumi.StringPtrOutput `pulumi:"authorization"`
	// cluster id
	ClusterId pulumi.StringPtrOutput `pulumi:"clusterId"`
	// cluster policy id
	ClusterPolicyId pulumi.StringPtrOutput `pulumi:"clusterPolicyId"`
	// directory id
	DirectoryId pulumi.StringPtrOutput `pulumi:"directoryId"`
	// path of directory
	DirectoryPath pulumi.StringPtrOutput `pulumi:"directoryPath"`
	ExperimentId  pulumi.StringPtrOutput `pulumi:"experimentId"`
	// instance pool id
	InstancePoolId pulumi.StringPtrOutput `pulumi:"instancePoolId"`
	// job id
	JobId pulumi.StringPtrOutput `pulumi:"jobId"`
	// ID of notebook within workspace
	NotebookId pulumi.StringPtrOutput `pulumi:"notebookId"`
	// path of notebook
	NotebookPath pulumi.StringPtrOutput `pulumi:"notebookPath"`
	// type of permissions.
	ObjectType        pulumi.StringOutput    `pulumi:"objectType"`
	RegisteredModelId pulumi.StringPtrOutput `pulumi:"registeredModelId"`
	// repo id
	RepoId pulumi.StringPtrOutput `pulumi:"repoId"`
	// path of databricks repo directory(`/Repos/<username>/...`)
	RepoPath       pulumi.StringPtrOutput `pulumi:"repoPath"`
	SqlAlertId     pulumi.StringPtrOutput `pulumi:"sqlAlertId"`
	SqlDashboardId pulumi.StringPtrOutput `pulumi:"sqlDashboardId"`
	SqlEndpointId  pulumi.StringPtrOutput `pulumi:"sqlEndpointId"`
	SqlQueryId     pulumi.StringPtrOutput `pulumi:"sqlQueryId"`
}

// NewPermissions registers a new resource with the given unique name, arguments, and options.
func NewPermissions(ctx *pulumi.Context,
	name string, args *PermissionsArgs, opts ...pulumi.ResourceOption) (*Permissions, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AccessControls == nil {
		return nil, errors.New("invalid value for required argument 'AccessControls'")
	}
	var resource Permissions
	err := ctx.RegisterResource("databricks:index/permissions:Permissions", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPermissions gets an existing Permissions resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPermissions(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PermissionsState, opts ...pulumi.ResourceOption) (*Permissions, error) {
	var resource Permissions
	err := ctx.ReadResource("databricks:index/permissions:Permissions", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Permissions resources.
type permissionsState struct {
	AccessControls []PermissionsAccessControl `pulumi:"accessControls"`
	// either [`tokens`](https://docs.databricks.com/administration-guide/access-control/tokens.html) or [`passwords`](https://docs.databricks.com/administration-guide/users-groups/single-sign-on/index.html#configure-password-permission).
	Authorization *string `pulumi:"authorization"`
	// cluster id
	ClusterId *string `pulumi:"clusterId"`
	// cluster policy id
	ClusterPolicyId *string `pulumi:"clusterPolicyId"`
	// directory id
	DirectoryId *string `pulumi:"directoryId"`
	// path of directory
	DirectoryPath *string `pulumi:"directoryPath"`
	ExperimentId  *string `pulumi:"experimentId"`
	// instance pool id
	InstancePoolId *string `pulumi:"instancePoolId"`
	// job id
	JobId *string `pulumi:"jobId"`
	// ID of notebook within workspace
	NotebookId *string `pulumi:"notebookId"`
	// path of notebook
	NotebookPath *string `pulumi:"notebookPath"`
	// type of permissions.
	ObjectType        *string `pulumi:"objectType"`
	RegisteredModelId *string `pulumi:"registeredModelId"`
	// repo id
	RepoId *string `pulumi:"repoId"`
	// path of databricks repo directory(`/Repos/<username>/...`)
	RepoPath       *string `pulumi:"repoPath"`
	SqlAlertId     *string `pulumi:"sqlAlertId"`
	SqlDashboardId *string `pulumi:"sqlDashboardId"`
	SqlEndpointId  *string `pulumi:"sqlEndpointId"`
	SqlQueryId     *string `pulumi:"sqlQueryId"`
}

type PermissionsState struct {
	AccessControls PermissionsAccessControlArrayInput
	// either [`tokens`](https://docs.databricks.com/administration-guide/access-control/tokens.html) or [`passwords`](https://docs.databricks.com/administration-guide/users-groups/single-sign-on/index.html#configure-password-permission).
	Authorization pulumi.StringPtrInput
	// cluster id
	ClusterId pulumi.StringPtrInput
	// cluster policy id
	ClusterPolicyId pulumi.StringPtrInput
	// directory id
	DirectoryId pulumi.StringPtrInput
	// path of directory
	DirectoryPath pulumi.StringPtrInput
	ExperimentId  pulumi.StringPtrInput
	// instance pool id
	InstancePoolId pulumi.StringPtrInput
	// job id
	JobId pulumi.StringPtrInput
	// ID of notebook within workspace
	NotebookId pulumi.StringPtrInput
	// path of notebook
	NotebookPath pulumi.StringPtrInput
	// type of permissions.
	ObjectType        pulumi.StringPtrInput
	RegisteredModelId pulumi.StringPtrInput
	// repo id
	RepoId pulumi.StringPtrInput
	// path of databricks repo directory(`/Repos/<username>/...`)
	RepoPath       pulumi.StringPtrInput
	SqlAlertId     pulumi.StringPtrInput
	SqlDashboardId pulumi.StringPtrInput
	SqlEndpointId  pulumi.StringPtrInput
	SqlQueryId     pulumi.StringPtrInput
}

func (PermissionsState) ElementType() reflect.Type {
	return reflect.TypeOf((*permissionsState)(nil)).Elem()
}

type permissionsArgs struct {
	AccessControls []PermissionsAccessControl `pulumi:"accessControls"`
	// either [`tokens`](https://docs.databricks.com/administration-guide/access-control/tokens.html) or [`passwords`](https://docs.databricks.com/administration-guide/users-groups/single-sign-on/index.html#configure-password-permission).
	Authorization *string `pulumi:"authorization"`
	// cluster id
	ClusterId *string `pulumi:"clusterId"`
	// cluster policy id
	ClusterPolicyId *string `pulumi:"clusterPolicyId"`
	// directory id
	DirectoryId *string `pulumi:"directoryId"`
	// path of directory
	DirectoryPath *string `pulumi:"directoryPath"`
	ExperimentId  *string `pulumi:"experimentId"`
	// instance pool id
	InstancePoolId *string `pulumi:"instancePoolId"`
	// job id
	JobId *string `pulumi:"jobId"`
	// ID of notebook within workspace
	NotebookId *string `pulumi:"notebookId"`
	// path of notebook
	NotebookPath *string `pulumi:"notebookPath"`
	// type of permissions.
	ObjectType        *string `pulumi:"objectType"`
	RegisteredModelId *string `pulumi:"registeredModelId"`
	// repo id
	RepoId *string `pulumi:"repoId"`
	// path of databricks repo directory(`/Repos/<username>/...`)
	RepoPath       *string `pulumi:"repoPath"`
	SqlAlertId     *string `pulumi:"sqlAlertId"`
	SqlDashboardId *string `pulumi:"sqlDashboardId"`
	SqlEndpointId  *string `pulumi:"sqlEndpointId"`
	SqlQueryId     *string `pulumi:"sqlQueryId"`
}

// The set of arguments for constructing a Permissions resource.
type PermissionsArgs struct {
	AccessControls PermissionsAccessControlArrayInput
	// either [`tokens`](https://docs.databricks.com/administration-guide/access-control/tokens.html) or [`passwords`](https://docs.databricks.com/administration-guide/users-groups/single-sign-on/index.html#configure-password-permission).
	Authorization pulumi.StringPtrInput
	// cluster id
	ClusterId pulumi.StringPtrInput
	// cluster policy id
	ClusterPolicyId pulumi.StringPtrInput
	// directory id
	DirectoryId pulumi.StringPtrInput
	// path of directory
	DirectoryPath pulumi.StringPtrInput
	ExperimentId  pulumi.StringPtrInput
	// instance pool id
	InstancePoolId pulumi.StringPtrInput
	// job id
	JobId pulumi.StringPtrInput
	// ID of notebook within workspace
	NotebookId pulumi.StringPtrInput
	// path of notebook
	NotebookPath pulumi.StringPtrInput
	// type of permissions.
	ObjectType        pulumi.StringPtrInput
	RegisteredModelId pulumi.StringPtrInput
	// repo id
	RepoId pulumi.StringPtrInput
	// path of databricks repo directory(`/Repos/<username>/...`)
	RepoPath       pulumi.StringPtrInput
	SqlAlertId     pulumi.StringPtrInput
	SqlDashboardId pulumi.StringPtrInput
	SqlEndpointId  pulumi.StringPtrInput
	SqlQueryId     pulumi.StringPtrInput
}

func (PermissionsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*permissionsArgs)(nil)).Elem()
}

type PermissionsInput interface {
	pulumi.Input

	ToPermissionsOutput() PermissionsOutput
	ToPermissionsOutputWithContext(ctx context.Context) PermissionsOutput
}

func (*Permissions) ElementType() reflect.Type {
	return reflect.TypeOf((**Permissions)(nil)).Elem()
}

func (i *Permissions) ToPermissionsOutput() PermissionsOutput {
	return i.ToPermissionsOutputWithContext(context.Background())
}

func (i *Permissions) ToPermissionsOutputWithContext(ctx context.Context) PermissionsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionsOutput)
}

// PermissionsArrayInput is an input type that accepts PermissionsArray and PermissionsArrayOutput values.
// You can construct a concrete instance of `PermissionsArrayInput` via:
//
//          PermissionsArray{ PermissionsArgs{...} }
type PermissionsArrayInput interface {
	pulumi.Input

	ToPermissionsArrayOutput() PermissionsArrayOutput
	ToPermissionsArrayOutputWithContext(context.Context) PermissionsArrayOutput
}

type PermissionsArray []PermissionsInput

func (PermissionsArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Permissions)(nil)).Elem()
}

func (i PermissionsArray) ToPermissionsArrayOutput() PermissionsArrayOutput {
	return i.ToPermissionsArrayOutputWithContext(context.Background())
}

func (i PermissionsArray) ToPermissionsArrayOutputWithContext(ctx context.Context) PermissionsArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionsArrayOutput)
}

// PermissionsMapInput is an input type that accepts PermissionsMap and PermissionsMapOutput values.
// You can construct a concrete instance of `PermissionsMapInput` via:
//
//          PermissionsMap{ "key": PermissionsArgs{...} }
type PermissionsMapInput interface {
	pulumi.Input

	ToPermissionsMapOutput() PermissionsMapOutput
	ToPermissionsMapOutputWithContext(context.Context) PermissionsMapOutput
}

type PermissionsMap map[string]PermissionsInput

func (PermissionsMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Permissions)(nil)).Elem()
}

func (i PermissionsMap) ToPermissionsMapOutput() PermissionsMapOutput {
	return i.ToPermissionsMapOutputWithContext(context.Background())
}

func (i PermissionsMap) ToPermissionsMapOutputWithContext(ctx context.Context) PermissionsMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionsMapOutput)
}

type PermissionsOutput struct{ *pulumi.OutputState }

func (PermissionsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Permissions)(nil)).Elem()
}

func (o PermissionsOutput) ToPermissionsOutput() PermissionsOutput {
	return o
}

func (o PermissionsOutput) ToPermissionsOutputWithContext(ctx context.Context) PermissionsOutput {
	return o
}

type PermissionsArrayOutput struct{ *pulumi.OutputState }

func (PermissionsArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Permissions)(nil)).Elem()
}

func (o PermissionsArrayOutput) ToPermissionsArrayOutput() PermissionsArrayOutput {
	return o
}

func (o PermissionsArrayOutput) ToPermissionsArrayOutputWithContext(ctx context.Context) PermissionsArrayOutput {
	return o
}

func (o PermissionsArrayOutput) Index(i pulumi.IntInput) PermissionsOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Permissions {
		return vs[0].([]*Permissions)[vs[1].(int)]
	}).(PermissionsOutput)
}

type PermissionsMapOutput struct{ *pulumi.OutputState }

func (PermissionsMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Permissions)(nil)).Elem()
}

func (o PermissionsMapOutput) ToPermissionsMapOutput() PermissionsMapOutput {
	return o
}

func (o PermissionsMapOutput) ToPermissionsMapOutputWithContext(ctx context.Context) PermissionsMapOutput {
	return o
}

func (o PermissionsMapOutput) MapIndex(k pulumi.StringInput) PermissionsOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Permissions {
		return vs[0].(map[string]*Permissions)[vs[1].(string)]
	}).(PermissionsOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PermissionsInput)(nil)).Elem(), &Permissions{})
	pulumi.RegisterInputType(reflect.TypeOf((*PermissionsArrayInput)(nil)).Elem(), PermissionsArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PermissionsMapInput)(nil)).Elem(), PermissionsMap{})
	pulumi.RegisterOutputType(PermissionsOutput{})
	pulumi.RegisterOutputType(PermissionsArrayOutput{})
	pulumi.RegisterOutputType(PermissionsMapOutput{})
}
