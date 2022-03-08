// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// > **Note** Please switch to Grants with Unity Catalog to manage data access, which provides better and faster way for managing data security. `Grants` resource *doesn't require a technical cluster to perform operations*. `SqlPermissions` will be removed, once Unity Catalog is Generally Available.
//
// This resource manages data object access control lists in Databricks workspaces for things like tables, views, databases, and [more](https://docs.databricks.com/security/access-control/table-acls/object-privileges.html). In order to enable Table Access control, you have to login to the workspace as administrator, go to `Admin Console`, pick `Access Control` tab, click on `Enable` button in `Table Access Control` section, and click `Confirm`. The security guarantees of table access control **will only be effective if cluster access control is also turned on**. Please make sure that no users can create clusters in your workspace and all Cluster have approximately the following configuration:
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
// 		_, err := databricks.NewCluster(ctx, "clusterWithTableAccessControl", &databricks.ClusterArgs{
// 			SparkConf: pulumi.AnyMap{
// 				"spark.databricks.acl.dfAclsEnabled":     pulumi.Any("true"),
// 				"spark.databricks.repl.allowedLanguages": pulumi.Any("python,sql"),
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
// It could be combined with creation of High-Concurrency and Single-Node clusters - in this case it should have corresponding `customTags` and `spark.databricks.cluster.profile` in Spark configuration as described in documentation for `Cluster` resource.
//
// The created cluster could be referred to by providing its ID as `clusterId` property.
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
// 		_, err := databricks.NewSqlPermissions(ctx, "fooTable", &databricks.SqlPermissionsArgs{
// 			ClusterId: pulumi.Any(databricks_cluster.Cluster_name.Id),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Example Usage
//
// The following resource definition will enforce access control on a table by executing the following SQL queries on a special auto-terminating cluster it would create for this operation:
//
// * ``` SHOW GRANT ON TABLE `default`.`foo`  ```
// * ```REVOKE ALL PRIVILEGES ON TABLE `default`.`foo` FROM ... every group and user that has access to it ...```
// * ``` GRANT MODIFY, SELECT ON TABLE `default`.`foo` TO `serge@example.com`  ```
// * ``` GRANT SELECT ON TABLE `default`.`foo` TO `special group`  ```
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
// 		_, err := databricks.NewSqlPermissions(ctx, "fooTable", &databricks.SqlPermissionsArgs{
// 			PrivilegeAssignments: SqlPermissionsPrivilegeAssignmentArray{
// 				&SqlPermissionsPrivilegeAssignmentArgs{
// 					Principal: pulumi.String("serge@example.com"),
// 					Privileges: pulumi.StringArray{
// 						pulumi.String("SELECT"),
// 						pulumi.String("MODIFY"),
// 					},
// 				},
// 				&SqlPermissionsPrivilegeAssignmentArgs{
// 					Principal: pulumi.String("special group"),
// 					Privileges: pulumi.StringArray{
// 						pulumi.String("SELECT"),
// 					},
// 				},
// 			},
// 			Table: pulumi.String("foo"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ## Related Resources
//
// The following resources are often used in the same context:
//
// * End to end workspace management guide.
// * Group to manage [groups in Databricks Workspace](https://docs.databricks.com/administration-guide/users-groups/groups.html) or [Account Console](https://accounts.cloud.databricks.com/) (for AWS deployments).
// * Grants to manage data access in Unity Catalog.
// * Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
// * User to [manage users](https://docs.databricks.com/administration-guide/users-groups/users.html), that could be added to Group within the workspace.
//
// ## Import
//
// The resource can be imported using a synthetic identifier. Examples of valid synthetic identifiers are* `table/default.foo` - table `foo` in a `default` database. Database is always mandatory. * `view/bar.foo` - view `foo` in `bar` database. * `database/bar` - `bar` database. * `catalog/` - entire catalog. `/` suffix is mandatory. * `any file/` - direct access to any file. `/` suffix is mandatory. * `anonymous function/` - anonymous function. `/` suffix is mandatory. bash
//
// ```sh
//  $ pulumi import databricks:index/sqlPermissions:SqlPermissions foo /<object-type>/<object-name>
// ```
type SqlPermissions struct {
	pulumi.CustomResourceState

	// If this access control for using anonymous function. Defaults to `false`.
	AnonymousFunction pulumi.BoolPtrOutput `pulumi:"anonymousFunction"`
	// If this access control for reading any file. Defaults to `false`.
	AnyFile pulumi.BoolPtrOutput `pulumi:"anyFile"`
	// If this access control for the entire catalog. Defaults to `false`.
	Catalog   pulumi.BoolPtrOutput `pulumi:"catalog"`
	ClusterId pulumi.StringOutput  `pulumi:"clusterId"`
	// Name of the database. Has default value of `default`.
	Database             pulumi.StringPtrOutput                       `pulumi:"database"`
	PrivilegeAssignments SqlPermissionsPrivilegeAssignmentArrayOutput `pulumi:"privilegeAssignments"`
	// Name of the table. Can be combined with `database`.
	Table pulumi.StringPtrOutput `pulumi:"table"`
	// Name of the view. Can be combined with `database`.
	View pulumi.StringPtrOutput `pulumi:"view"`
}

// NewSqlPermissions registers a new resource with the given unique name, arguments, and options.
func NewSqlPermissions(ctx *pulumi.Context,
	name string, args *SqlPermissionsArgs, opts ...pulumi.ResourceOption) (*SqlPermissions, error) {
	if args == nil {
		args = &SqlPermissionsArgs{}
	}

	var resource SqlPermissions
	err := ctx.RegisterResource("databricks:index/sqlPermissions:SqlPermissions", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSqlPermissions gets an existing SqlPermissions resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSqlPermissions(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SqlPermissionsState, opts ...pulumi.ResourceOption) (*SqlPermissions, error) {
	var resource SqlPermissions
	err := ctx.ReadResource("databricks:index/sqlPermissions:SqlPermissions", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SqlPermissions resources.
type sqlPermissionsState struct {
	// If this access control for using anonymous function. Defaults to `false`.
	AnonymousFunction *bool `pulumi:"anonymousFunction"`
	// If this access control for reading any file. Defaults to `false`.
	AnyFile *bool `pulumi:"anyFile"`
	// If this access control for the entire catalog. Defaults to `false`.
	Catalog   *bool   `pulumi:"catalog"`
	ClusterId *string `pulumi:"clusterId"`
	// Name of the database. Has default value of `default`.
	Database             *string                             `pulumi:"database"`
	PrivilegeAssignments []SqlPermissionsPrivilegeAssignment `pulumi:"privilegeAssignments"`
	// Name of the table. Can be combined with `database`.
	Table *string `pulumi:"table"`
	// Name of the view. Can be combined with `database`.
	View *string `pulumi:"view"`
}

type SqlPermissionsState struct {
	// If this access control for using anonymous function. Defaults to `false`.
	AnonymousFunction pulumi.BoolPtrInput
	// If this access control for reading any file. Defaults to `false`.
	AnyFile pulumi.BoolPtrInput
	// If this access control for the entire catalog. Defaults to `false`.
	Catalog   pulumi.BoolPtrInput
	ClusterId pulumi.StringPtrInput
	// Name of the database. Has default value of `default`.
	Database             pulumi.StringPtrInput
	PrivilegeAssignments SqlPermissionsPrivilegeAssignmentArrayInput
	// Name of the table. Can be combined with `database`.
	Table pulumi.StringPtrInput
	// Name of the view. Can be combined with `database`.
	View pulumi.StringPtrInput
}

func (SqlPermissionsState) ElementType() reflect.Type {
	return reflect.TypeOf((*sqlPermissionsState)(nil)).Elem()
}

type sqlPermissionsArgs struct {
	// If this access control for using anonymous function. Defaults to `false`.
	AnonymousFunction *bool `pulumi:"anonymousFunction"`
	// If this access control for reading any file. Defaults to `false`.
	AnyFile *bool `pulumi:"anyFile"`
	// If this access control for the entire catalog. Defaults to `false`.
	Catalog   *bool   `pulumi:"catalog"`
	ClusterId *string `pulumi:"clusterId"`
	// Name of the database. Has default value of `default`.
	Database             *string                             `pulumi:"database"`
	PrivilegeAssignments []SqlPermissionsPrivilegeAssignment `pulumi:"privilegeAssignments"`
	// Name of the table. Can be combined with `database`.
	Table *string `pulumi:"table"`
	// Name of the view. Can be combined with `database`.
	View *string `pulumi:"view"`
}

// The set of arguments for constructing a SqlPermissions resource.
type SqlPermissionsArgs struct {
	// If this access control for using anonymous function. Defaults to `false`.
	AnonymousFunction pulumi.BoolPtrInput
	// If this access control for reading any file. Defaults to `false`.
	AnyFile pulumi.BoolPtrInput
	// If this access control for the entire catalog. Defaults to `false`.
	Catalog   pulumi.BoolPtrInput
	ClusterId pulumi.StringPtrInput
	// Name of the database. Has default value of `default`.
	Database             pulumi.StringPtrInput
	PrivilegeAssignments SqlPermissionsPrivilegeAssignmentArrayInput
	// Name of the table. Can be combined with `database`.
	Table pulumi.StringPtrInput
	// Name of the view. Can be combined with `database`.
	View pulumi.StringPtrInput
}

func (SqlPermissionsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sqlPermissionsArgs)(nil)).Elem()
}

type SqlPermissionsInput interface {
	pulumi.Input

	ToSqlPermissionsOutput() SqlPermissionsOutput
	ToSqlPermissionsOutputWithContext(ctx context.Context) SqlPermissionsOutput
}

func (*SqlPermissions) ElementType() reflect.Type {
	return reflect.TypeOf((**SqlPermissions)(nil)).Elem()
}

func (i *SqlPermissions) ToSqlPermissionsOutput() SqlPermissionsOutput {
	return i.ToSqlPermissionsOutputWithContext(context.Background())
}

func (i *SqlPermissions) ToSqlPermissionsOutputWithContext(ctx context.Context) SqlPermissionsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SqlPermissionsOutput)
}

// SqlPermissionsArrayInput is an input type that accepts SqlPermissionsArray and SqlPermissionsArrayOutput values.
// You can construct a concrete instance of `SqlPermissionsArrayInput` via:
//
//          SqlPermissionsArray{ SqlPermissionsArgs{...} }
type SqlPermissionsArrayInput interface {
	pulumi.Input

	ToSqlPermissionsArrayOutput() SqlPermissionsArrayOutput
	ToSqlPermissionsArrayOutputWithContext(context.Context) SqlPermissionsArrayOutput
}

type SqlPermissionsArray []SqlPermissionsInput

func (SqlPermissionsArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SqlPermissions)(nil)).Elem()
}

func (i SqlPermissionsArray) ToSqlPermissionsArrayOutput() SqlPermissionsArrayOutput {
	return i.ToSqlPermissionsArrayOutputWithContext(context.Background())
}

func (i SqlPermissionsArray) ToSqlPermissionsArrayOutputWithContext(ctx context.Context) SqlPermissionsArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SqlPermissionsArrayOutput)
}

// SqlPermissionsMapInput is an input type that accepts SqlPermissionsMap and SqlPermissionsMapOutput values.
// You can construct a concrete instance of `SqlPermissionsMapInput` via:
//
//          SqlPermissionsMap{ "key": SqlPermissionsArgs{...} }
type SqlPermissionsMapInput interface {
	pulumi.Input

	ToSqlPermissionsMapOutput() SqlPermissionsMapOutput
	ToSqlPermissionsMapOutputWithContext(context.Context) SqlPermissionsMapOutput
}

type SqlPermissionsMap map[string]SqlPermissionsInput

func (SqlPermissionsMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SqlPermissions)(nil)).Elem()
}

func (i SqlPermissionsMap) ToSqlPermissionsMapOutput() SqlPermissionsMapOutput {
	return i.ToSqlPermissionsMapOutputWithContext(context.Background())
}

func (i SqlPermissionsMap) ToSqlPermissionsMapOutputWithContext(ctx context.Context) SqlPermissionsMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SqlPermissionsMapOutput)
}

type SqlPermissionsOutput struct{ *pulumi.OutputState }

func (SqlPermissionsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SqlPermissions)(nil)).Elem()
}

func (o SqlPermissionsOutput) ToSqlPermissionsOutput() SqlPermissionsOutput {
	return o
}

func (o SqlPermissionsOutput) ToSqlPermissionsOutputWithContext(ctx context.Context) SqlPermissionsOutput {
	return o
}

type SqlPermissionsArrayOutput struct{ *pulumi.OutputState }

func (SqlPermissionsArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SqlPermissions)(nil)).Elem()
}

func (o SqlPermissionsArrayOutput) ToSqlPermissionsArrayOutput() SqlPermissionsArrayOutput {
	return o
}

func (o SqlPermissionsArrayOutput) ToSqlPermissionsArrayOutputWithContext(ctx context.Context) SqlPermissionsArrayOutput {
	return o
}

func (o SqlPermissionsArrayOutput) Index(i pulumi.IntInput) SqlPermissionsOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SqlPermissions {
		return vs[0].([]*SqlPermissions)[vs[1].(int)]
	}).(SqlPermissionsOutput)
}

type SqlPermissionsMapOutput struct{ *pulumi.OutputState }

func (SqlPermissionsMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SqlPermissions)(nil)).Elem()
}

func (o SqlPermissionsMapOutput) ToSqlPermissionsMapOutput() SqlPermissionsMapOutput {
	return o
}

func (o SqlPermissionsMapOutput) ToSqlPermissionsMapOutputWithContext(ctx context.Context) SqlPermissionsMapOutput {
	return o
}

func (o SqlPermissionsMapOutput) MapIndex(k pulumi.StringInput) SqlPermissionsOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SqlPermissions {
		return vs[0].(map[string]*SqlPermissions)[vs[1].(string)]
	}).(SqlPermissionsOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SqlPermissionsInput)(nil)).Elem(), &SqlPermissions{})
	pulumi.RegisterInputType(reflect.TypeOf((*SqlPermissionsArrayInput)(nil)).Elem(), SqlPermissionsArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SqlPermissionsMapInput)(nil)).Elem(), SqlPermissionsMap{})
	pulumi.RegisterOutputType(SqlPermissionsOutput{})
	pulumi.RegisterOutputType(SqlPermissionsArrayOutput{})
	pulumi.RegisterOutputType(SqlPermissionsMapOutput{})
}
