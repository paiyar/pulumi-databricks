// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Secret extends pulumi.CustomResource {
    /**
     * Get an existing Secret resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecretState, opts?: pulumi.CustomResourceOptions): Secret {
        return new Secret(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/secret:Secret';

    /**
     * Returns true if the given object is an instance of Secret.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Secret {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Secret.__pulumiType;
    }

    public readonly key!: pulumi.Output<string>;
    public /*out*/ readonly lastUpdatedTimestamp!: pulumi.Output<number>;
    public readonly scope!: pulumi.Output<string>;
    public readonly stringValue!: pulumi.Output<string>;

    /**
     * Create a Secret resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SecretArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SecretArgs | SecretState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SecretState | undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["lastUpdatedTimestamp"] = state ? state.lastUpdatedTimestamp : undefined;
            resourceInputs["scope"] = state ? state.scope : undefined;
            resourceInputs["stringValue"] = state ? state.stringValue : undefined;
        } else {
            const args = argsOrState as SecretArgs | undefined;
            if ((!args || args.key === undefined) && !opts.urn) {
                throw new Error("Missing required property 'key'");
            }
            if ((!args || args.scope === undefined) && !opts.urn) {
                throw new Error("Missing required property 'scope'");
            }
            if ((!args || args.stringValue === undefined) && !opts.urn) {
                throw new Error("Missing required property 'stringValue'");
            }
            resourceInputs["key"] = args ? args.key : undefined;
            resourceInputs["scope"] = args ? args.scope : undefined;
            resourceInputs["stringValue"] = args ? args.stringValue : undefined;
            resourceInputs["lastUpdatedTimestamp"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Secret.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Secret resources.
 */
export interface SecretState {
    key?: pulumi.Input<string>;
    lastUpdatedTimestamp?: pulumi.Input<number>;
    scope?: pulumi.Input<string>;
    stringValue?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Secret resource.
 */
export interface SecretArgs {
    key: pulumi.Input<string>;
    scope: pulumi.Input<string>;
    stringValue: pulumi.Input<string>;
}
