// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * The following resource definition will enforce access control on a table by executing the following SQL queries on a special auto-terminating cluster it would create for this operation:
 *
 * * ``` SHOW GRANT ON TABLE `default`.`foo`  ```
 * * ```REVOKE ALL PRIVILEGES ON TABLE `default`.`foo` FROM ... every group and user that has access to it ...```
 * * ``` GRANT MODIFY, SELECT ON TABLE `default`.`foo` TO `serge@example.com`  ```
 * * ``` GRANT SELECT ON TABLE `default`.`foo` TO `special group`  ```
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as databricks from "@pulumi/databricks";
 *
 * const fooTable = new databricks.SqlPermissions("foo_table", {
 *     privilegeAssignments: [
 *         {
 *             principal: "serge@example.com",
 *             privileges: [
 *                 "SELECT",
 *                 "MODIFY",
 *             ],
 *         },
 *         {
 *             principal: "special group",
 *             privileges: ["SELECT"],
 *         },
 *     ],
 *     table: "foo",
 * });
 * ```
 * ## Related Resources
 *
 * The following resources are often used in the same context:
 *
 * * End to end workspace management guide.
 * * databricks.Group to manage [groups in Databricks Workspace](https://docs.databricks.com/administration-guide/users-groups/groups.html) or [Account Console](https://accounts.cloud.databricks.com/) (for AWS deployments).
 * * databricks.Grants to manage data access in Unity Catalog.
 * * databricks.Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
 * * databricks.User to [manage users](https://docs.databricks.com/administration-guide/users-groups/users.html), that could be added to databricks.Group within the workspace.
 *
 * ## Import
 *
 * The resource can be imported using a synthetic identifier. Examples of valid synthetic identifiers are* `table/default.foo` - table `foo` in a `default` database. Database is always mandatory. * `view/bar.foo` - view `foo` in `bar` database. * `database/bar` - `bar` database. * `catalog/` - entire catalog. `/` suffix is mandatory. * `any file/` - direct access to any file. `/` suffix is mandatory. * `anonymous function/` - anonymous function. `/` suffix is mandatory. bash
 *
 * ```sh
 *  $ pulumi import databricks:index/sqlPermissions:SqlPermissions foo /<object-type>/<object-name>
 * ```
 */
export class SqlPermissions extends pulumi.CustomResource {
    /**
     * Get an existing SqlPermissions resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SqlPermissionsState, opts?: pulumi.CustomResourceOptions): SqlPermissions {
        return new SqlPermissions(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/sqlPermissions:SqlPermissions';

    /**
     * Returns true if the given object is an instance of SqlPermissions.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SqlPermissions {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SqlPermissions.__pulumiType;
    }

    /**
     * If this access control for using anonymous function. Defaults to `false`.
     */
    public readonly anonymousFunction!: pulumi.Output<boolean | undefined>;
    /**
     * If this access control for reading any file. Defaults to `false`.
     */
    public readonly anyFile!: pulumi.Output<boolean | undefined>;
    /**
     * If this access control for the entire catalog. Defaults to `false`.
     */
    public readonly catalog!: pulumi.Output<boolean | undefined>;
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * Name of the database. Has default value of `default`.
     */
    public readonly database!: pulumi.Output<string | undefined>;
    public readonly privilegeAssignments!: pulumi.Output<outputs.SqlPermissionsPrivilegeAssignment[] | undefined>;
    /**
     * Name of the table. Can be combined with `database`.
     */
    public readonly table!: pulumi.Output<string | undefined>;
    /**
     * Name of the view. Can be combined with `database`.
     */
    public readonly view!: pulumi.Output<string | undefined>;

    /**
     * Create a SqlPermissions resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SqlPermissionsArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SqlPermissionsArgs | SqlPermissionsState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SqlPermissionsState | undefined;
            resourceInputs["anonymousFunction"] = state ? state.anonymousFunction : undefined;
            resourceInputs["anyFile"] = state ? state.anyFile : undefined;
            resourceInputs["catalog"] = state ? state.catalog : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["database"] = state ? state.database : undefined;
            resourceInputs["privilegeAssignments"] = state ? state.privilegeAssignments : undefined;
            resourceInputs["table"] = state ? state.table : undefined;
            resourceInputs["view"] = state ? state.view : undefined;
        } else {
            const args = argsOrState as SqlPermissionsArgs | undefined;
            resourceInputs["anonymousFunction"] = args ? args.anonymousFunction : undefined;
            resourceInputs["anyFile"] = args ? args.anyFile : undefined;
            resourceInputs["catalog"] = args ? args.catalog : undefined;
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["database"] = args ? args.database : undefined;
            resourceInputs["privilegeAssignments"] = args ? args.privilegeAssignments : undefined;
            resourceInputs["table"] = args ? args.table : undefined;
            resourceInputs["view"] = args ? args.view : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(SqlPermissions.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SqlPermissions resources.
 */
export interface SqlPermissionsState {
    /**
     * If this access control for using anonymous function. Defaults to `false`.
     */
    anonymousFunction?: pulumi.Input<boolean>;
    /**
     * If this access control for reading any file. Defaults to `false`.
     */
    anyFile?: pulumi.Input<boolean>;
    /**
     * If this access control for the entire catalog. Defaults to `false`.
     */
    catalog?: pulumi.Input<boolean>;
    clusterId?: pulumi.Input<string>;
    /**
     * Name of the database. Has default value of `default`.
     */
    database?: pulumi.Input<string>;
    privilegeAssignments?: pulumi.Input<pulumi.Input<inputs.SqlPermissionsPrivilegeAssignment>[]>;
    /**
     * Name of the table. Can be combined with `database`.
     */
    table?: pulumi.Input<string>;
    /**
     * Name of the view. Can be combined with `database`.
     */
    view?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SqlPermissions resource.
 */
export interface SqlPermissionsArgs {
    /**
     * If this access control for using anonymous function. Defaults to `false`.
     */
    anonymousFunction?: pulumi.Input<boolean>;
    /**
     * If this access control for reading any file. Defaults to `false`.
     */
    anyFile?: pulumi.Input<boolean>;
    /**
     * If this access control for the entire catalog. Defaults to `false`.
     */
    catalog?: pulumi.Input<boolean>;
    clusterId?: pulumi.Input<string>;
    /**
     * Name of the database. Has default value of `default`.
     */
    database?: pulumi.Input<string>;
    privilegeAssignments?: pulumi.Input<pulumi.Input<inputs.SqlPermissionsPrivilegeAssignment>[]>;
    /**
     * Name of the table. Can be combined with `database`.
     */
    table?: pulumi.Input<string>;
    /**
     * Name of the view. Can be combined with `database`.
     */
    view?: pulumi.Input<string>;
}
