// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class ClusterPolicy extends pulumi.CustomResource {
    /**
     * Get an existing ClusterPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterPolicyState, opts?: pulumi.CustomResourceOptions): ClusterPolicy {
        return new ClusterPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/clusterPolicy:ClusterPolicy';

    /**
     * Returns true if the given object is an instance of ClusterPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterPolicy.__pulumiType;
    }

    /**
     * Policy definition JSON document expressed in Databricks Policy Definition Language.
     */
    public readonly definition!: pulumi.Output<string | undefined>;
    /**
     * Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
     */
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly policyId!: pulumi.Output<string>;

    /**
     * Create a ClusterPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ClusterPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ClusterPolicyArgs | ClusterPolicyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ClusterPolicyState | undefined;
            resourceInputs["definition"] = state ? state.definition : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["policyId"] = state ? state.policyId : undefined;
        } else {
            const args = argsOrState as ClusterPolicyArgs | undefined;
            resourceInputs["definition"] = args ? args.definition : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["policyId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ClusterPolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ClusterPolicy resources.
 */
export interface ClusterPolicyState {
    /**
     * Policy definition JSON document expressed in Databricks Policy Definition Language.
     */
    definition?: pulumi.Input<string>;
    /**
     * Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
     */
    name?: pulumi.Input<string>;
    policyId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ClusterPolicy resource.
 */
export interface ClusterPolicyArgs {
    /**
     * Policy definition JSON document expressed in Databricks Policy Definition Language.
     */
    definition?: pulumi.Input<string>;
    /**
     * Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
     */
    name?: pulumi.Input<string>;
}
