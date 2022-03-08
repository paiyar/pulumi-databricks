// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * > **Private Preview** This feature is in [Private Preview](https://docs.databricks.com/release-notes/release-types.html). Contact your Databricks representative to request access.
 *
 * Within a metastore, Unity Catalog provides a 3-level namespace for organizing data: Catalogs, Databases (also called Schemas), and Tables / Views.
 *
 * A `databricks.Schema` is contained within databricks.Catalog and can contain tables & views.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as databricks from "@pulumi/databricks";
 *
 * const sandbox = new databricks.Catalog("sandbox", {
 *     metastoreId: databricks_metastore["this"].id,
 *     comment: "this catalog is managed by terraform",
 *     properties: {
 *         purpose: "testing",
 *     },
 * });
 * const things = new databricks.Schema("things", {
 *     catalogName: sandbox.id,
 *     comment: "this database is managed by terraform",
 *     properties: {
 *         kind: "various",
 *     },
 * });
 * ```
 * ## Related Resources
 *
 * The following resources are used in the same context:
 *
 * * databricks.Table data to list tables within Unity Catalog.
 * * databricks.Schema data to list schemas within Unity Catalog.
 * * databricks.Catalog data to list catalogs within Unity Catalog.
 *
 * ## Import
 *
 * This resource can be imported by namebash
 *
 * ```sh
 *  $ pulumi import databricks:index/schema:Schema this <name>
 * ```
 */
export class Schema extends pulumi.CustomResource {
    /**
     * Get an existing Schema resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SchemaState, opts?: pulumi.CustomResourceOptions): Schema {
        return new Schema(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/schema:Schema';

    /**
     * Returns true if the given object is an instance of Schema.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Schema {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Schema.__pulumiType;
    }

    /**
     * Name of parent catalog
     */
    public readonly catalogName!: pulumi.Output<string>;
    /**
     * User-supplied free-form text.
     */
    public readonly comment!: pulumi.Output<string | undefined>;
    public readonly metastoreId!: pulumi.Output<string>;
    /**
     * Name of Schema relative to parent catalog. Change forces creation of a new resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Username/groupname of schema owner. Currently this field can only be changed after the resource is created.
     */
    public readonly owner!: pulumi.Output<string>;
    /**
     * Extensible Schema properties.
     */
    public readonly properties!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a Schema resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SchemaArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SchemaArgs | SchemaState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SchemaState | undefined;
            resourceInputs["catalogName"] = state ? state.catalogName : undefined;
            resourceInputs["comment"] = state ? state.comment : undefined;
            resourceInputs["metastoreId"] = state ? state.metastoreId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["owner"] = state ? state.owner : undefined;
            resourceInputs["properties"] = state ? state.properties : undefined;
        } else {
            const args = argsOrState as SchemaArgs | undefined;
            if ((!args || args.catalogName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'catalogName'");
            }
            resourceInputs["catalogName"] = args ? args.catalogName : undefined;
            resourceInputs["comment"] = args ? args.comment : undefined;
            resourceInputs["metastoreId"] = args ? args.metastoreId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["owner"] = args ? args.owner : undefined;
            resourceInputs["properties"] = args ? args.properties : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Schema.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Schema resources.
 */
export interface SchemaState {
    /**
     * Name of parent catalog
     */
    catalogName?: pulumi.Input<string>;
    /**
     * User-supplied free-form text.
     */
    comment?: pulumi.Input<string>;
    metastoreId?: pulumi.Input<string>;
    /**
     * Name of Schema relative to parent catalog. Change forces creation of a new resource.
     */
    name?: pulumi.Input<string>;
    /**
     * Username/groupname of schema owner. Currently this field can only be changed after the resource is created.
     */
    owner?: pulumi.Input<string>;
    /**
     * Extensible Schema properties.
     */
    properties?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a Schema resource.
 */
export interface SchemaArgs {
    /**
     * Name of parent catalog
     */
    catalogName: pulumi.Input<string>;
    /**
     * User-supplied free-form text.
     */
    comment?: pulumi.Input<string>;
    metastoreId?: pulumi.Input<string>;
    /**
     * Name of Schema relative to parent catalog. Change forces creation of a new resource.
     */
    name?: pulumi.Input<string>;
    /**
     * Username/groupname of schema owner. Currently this field can only be changed after the resource is created.
     */
    owner?: pulumi.Input<string>;
    /**
     * Extensible Schema properties.
     */
    properties?: pulumi.Input<{[key: string]: any}>;
}
