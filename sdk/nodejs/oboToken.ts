// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Import
 *
 * -> **Note** Importing this resource is not currently supported.
 */
export class OboToken extends pulumi.CustomResource {
    /**
     * Get an existing OboToken resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OboTokenState, opts?: pulumi.CustomResourceOptions): OboToken {
        return new OboToken(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/oboToken:OboToken';

    /**
     * Returns true if the given object is an instance of OboToken.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OboToken {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OboToken.__pulumiType;
    }

    /**
     * Application ID of databricks.ServicePrincipal to create a PAT token for.
     */
    public readonly applicationId!: pulumi.Output<string>;
    /**
     * Comment that describes the purpose of the token.
     */
    public readonly comment!: pulumi.Output<string>;
    /**
     * The number of seconds before the token expires. Token resource is re-created when it expires.
     */
    public readonly lifetimeSeconds!: pulumi.Output<number>;
    /**
     * **Sensitive** value of the newly-created token.
     */
    public /*out*/ readonly tokenValue!: pulumi.Output<string>;

    /**
     * Create a OboToken resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OboTokenArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OboTokenArgs | OboTokenState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as OboTokenState | undefined;
            resourceInputs["applicationId"] = state ? state.applicationId : undefined;
            resourceInputs["comment"] = state ? state.comment : undefined;
            resourceInputs["lifetimeSeconds"] = state ? state.lifetimeSeconds : undefined;
            resourceInputs["tokenValue"] = state ? state.tokenValue : undefined;
        } else {
            const args = argsOrState as OboTokenArgs | undefined;
            if ((!args || args.applicationId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'applicationId'");
            }
            if ((!args || args.comment === undefined) && !opts.urn) {
                throw new Error("Missing required property 'comment'");
            }
            if ((!args || args.lifetimeSeconds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'lifetimeSeconds'");
            }
            resourceInputs["applicationId"] = args ? args.applicationId : undefined;
            resourceInputs["comment"] = args ? args.comment : undefined;
            resourceInputs["lifetimeSeconds"] = args ? args.lifetimeSeconds : undefined;
            resourceInputs["tokenValue"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(OboToken.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering OboToken resources.
 */
export interface OboTokenState {
    /**
     * Application ID of databricks.ServicePrincipal to create a PAT token for.
     */
    applicationId?: pulumi.Input<string>;
    /**
     * Comment that describes the purpose of the token.
     */
    comment?: pulumi.Input<string>;
    /**
     * The number of seconds before the token expires. Token resource is re-created when it expires.
     */
    lifetimeSeconds?: pulumi.Input<number>;
    /**
     * **Sensitive** value of the newly-created token.
     */
    tokenValue?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a OboToken resource.
 */
export interface OboTokenArgs {
    /**
     * Application ID of databricks.ServicePrincipal to create a PAT token for.
     */
    applicationId: pulumi.Input<string>;
    /**
     * Comment that describes the purpose of the token.
     */
    comment: pulumi.Input<string>;
    /**
     * The number of seconds before the token expires. Token resource is re-created when it expires.
     */
    lifetimeSeconds: pulumi.Input<number>;
}
