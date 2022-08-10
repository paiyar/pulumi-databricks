// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class SecretAcl extends pulumi.CustomResource {
    /**
     * Get an existing SecretAcl resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecretAclState, opts?: pulumi.CustomResourceOptions): SecretAcl {
        return new SecretAcl(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/secretAcl:SecretAcl';

    /**
     * Returns true if the given object is an instance of SecretAcl.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SecretAcl {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SecretAcl.__pulumiType;
    }

    public readonly permission!: pulumi.Output<string>;
    public readonly principal!: pulumi.Output<string>;
    public readonly scope!: pulumi.Output<string>;

    /**
     * Create a SecretAcl resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SecretAclArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SecretAclArgs | SecretAclState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SecretAclState | undefined;
            resourceInputs["permission"] = state ? state.permission : undefined;
            resourceInputs["principal"] = state ? state.principal : undefined;
            resourceInputs["scope"] = state ? state.scope : undefined;
        } else {
            const args = argsOrState as SecretAclArgs | undefined;
            if ((!args || args.permission === undefined) && !opts.urn) {
                throw new Error("Missing required property 'permission'");
            }
            if ((!args || args.principal === undefined) && !opts.urn) {
                throw new Error("Missing required property 'principal'");
            }
            if ((!args || args.scope === undefined) && !opts.urn) {
                throw new Error("Missing required property 'scope'");
            }
            resourceInputs["permission"] = args ? args.permission : undefined;
            resourceInputs["principal"] = args ? args.principal : undefined;
            resourceInputs["scope"] = args ? args.scope : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(SecretAcl.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SecretAcl resources.
 */
export interface SecretAclState {
    permission?: pulumi.Input<string>;
    principal?: pulumi.Input<string>;
    scope?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SecretAcl resource.
 */
export interface SecretAclArgs {
    permission: pulumi.Input<string>;
    principal: pulumi.Input<string>;
    scope: pulumi.Input<string>;
}
