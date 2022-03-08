// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * > **Private Preview** This feature is in [Private Preview](https://docs.databricks.com/release-notes/release-types.html). Contact your Databricks representative to request access.
 *
 * To work with external tables, Unity Catalog introduces two new objects to access and work with external cloud storage:
 * - databricks.StorageCredential represent authentication methods to access cloud storage (e.g. an IAM role for Amazon S3 or a service principal for Azure Storage). Storage credentials are access-controlled to determine which users can use the credential.
 * - `databricks.ExternalLocation` are objects that combine a cloud storage path with a Storage Credential that can be used to access the location.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as databricks from "@pulumi/databricks";
 *
 * const external = new databricks.StorageCredential("external", {
 *     awsIamRole: {
 *         roleArn: aws_iam_role.external_data_access.arn,
 *     },
 *     comment: "Managed by TF",
 * });
 * const someExternalLocation = new databricks.ExternalLocation("someExternalLocation", {
 *     url: `s3://${aws_s3_bucket.external.id}/some`,
 *     credentialName: external.id,
 *     comment: "Managed by TF",
 * });
 * const someGrants = new databricks.Grants("someGrants", {
 *     externalLocation: someExternalLocation.id,
 *     grants: [{
 *         principal: "Data Engineers",
 *         privileges: [
 *             "CREATE TABLE",
 *             "READ FILES",
 *         ],
 *     }],
 * });
 * ```
 *
 * ## Import
 *
 * This resource can be imported by namebash
 *
 * ```sh
 *  $ pulumi import databricks:index/externalLocation:ExternalLocation this <name>
 * ```
 */
export class ExternalLocation extends pulumi.CustomResource {
    /**
     * Get an existing ExternalLocation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ExternalLocationState, opts?: pulumi.CustomResourceOptions): ExternalLocation {
        return new ExternalLocation(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/externalLocation:ExternalLocation';

    /**
     * Returns true if the given object is an instance of ExternalLocation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ExternalLocation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ExternalLocation.__pulumiType;
    }

    /**
     * User-supplied free-form text.
     */
    public readonly comment!: pulumi.Output<string | undefined>;
    /**
     * Name of the databricks.StorageCredential to use with this External Location.
     */
    public readonly credentialName!: pulumi.Output<string>;
    public readonly metastoreId!: pulumi.Output<string>;
    /**
     * Name of External Location, which must be unique within the databricks_metastore. Change forces creation of a new resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Username/groupname of External Location owner. Currently this field can only be changed after the resource is created.
     */
    public readonly owner!: pulumi.Output<string>;
    /**
     * Path URL in cloud storage, of the form: `s3://bucket-host/[bucket-dir]` (AWS), `abfss://[user@]host/[path]` (Azure).
     */
    public readonly url!: pulumi.Output<string>;

    /**
     * Create a ExternalLocation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ExternalLocationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ExternalLocationArgs | ExternalLocationState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ExternalLocationState | undefined;
            resourceInputs["comment"] = state ? state.comment : undefined;
            resourceInputs["credentialName"] = state ? state.credentialName : undefined;
            resourceInputs["metastoreId"] = state ? state.metastoreId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["owner"] = state ? state.owner : undefined;
            resourceInputs["url"] = state ? state.url : undefined;
        } else {
            const args = argsOrState as ExternalLocationArgs | undefined;
            if ((!args || args.credentialName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'credentialName'");
            }
            if ((!args || args.url === undefined) && !opts.urn) {
                throw new Error("Missing required property 'url'");
            }
            resourceInputs["comment"] = args ? args.comment : undefined;
            resourceInputs["credentialName"] = args ? args.credentialName : undefined;
            resourceInputs["metastoreId"] = args ? args.metastoreId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["owner"] = args ? args.owner : undefined;
            resourceInputs["url"] = args ? args.url : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ExternalLocation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ExternalLocation resources.
 */
export interface ExternalLocationState {
    /**
     * User-supplied free-form text.
     */
    comment?: pulumi.Input<string>;
    /**
     * Name of the databricks.StorageCredential to use with this External Location.
     */
    credentialName?: pulumi.Input<string>;
    metastoreId?: pulumi.Input<string>;
    /**
     * Name of External Location, which must be unique within the databricks_metastore. Change forces creation of a new resource.
     */
    name?: pulumi.Input<string>;
    /**
     * Username/groupname of External Location owner. Currently this field can only be changed after the resource is created.
     */
    owner?: pulumi.Input<string>;
    /**
     * Path URL in cloud storage, of the form: `s3://bucket-host/[bucket-dir]` (AWS), `abfss://[user@]host/[path]` (Azure).
     */
    url?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ExternalLocation resource.
 */
export interface ExternalLocationArgs {
    /**
     * User-supplied free-form text.
     */
    comment?: pulumi.Input<string>;
    /**
     * Name of the databricks.StorageCredential to use with this External Location.
     */
    credentialName: pulumi.Input<string>;
    metastoreId?: pulumi.Input<string>;
    /**
     * Name of External Location, which must be unique within the databricks_metastore. Change forces creation of a new resource.
     */
    name?: pulumi.Input<string>;
    /**
     * Username/groupname of External Location owner. Currently this field can only be changed after the resource is created.
     */
    owner?: pulumi.Input<string>;
    /**
     * Path URL in cloud storage, of the form: `s3://bucket-host/[bucket-dir]` (AWS), `abfss://[user@]host/[path]` (Azure).
     */
    url: pulumi.Input<string>;
}
