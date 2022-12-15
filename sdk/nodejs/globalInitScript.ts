// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Import
 *
 * The resource global init script can be imported using script IDbash
 *
 * ```sh
 *  $ pulumi import databricks:index/globalInitScript:GlobalInitScript this script_id
 * ```
 */
export class GlobalInitScript extends pulumi.CustomResource {
    /**
     * Get an existing GlobalInitScript resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GlobalInitScriptState, opts?: pulumi.CustomResourceOptions): GlobalInitScript {
        return new GlobalInitScript(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/globalInitScript:GlobalInitScript';

    /**
     * Returns true if the given object is an instance of GlobalInitScript.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GlobalInitScript {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GlobalInitScript.__pulumiType;
    }

    public readonly contentBase64!: pulumi.Output<string | undefined>;
    /**
     * specifies if the script is enabled for execution, or not
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    public readonly md5!: pulumi.Output<string | undefined>;
    /**
     * - the name of the script.  It should be unique
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * - the position of a global init script, where `0` represents the first global init script to run, `1` is the second global init script to run, and so on. When omitted, the script gets the last position.
     */
    public readonly position!: pulumi.Output<number>;
    /**
     * Path to script's source code on local filesystem. Conflicts with `contentBase64`
     */
    public readonly source!: pulumi.Output<string | undefined>;

    /**
     * Create a GlobalInitScript resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: GlobalInitScriptArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GlobalInitScriptArgs | GlobalInitScriptState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GlobalInitScriptState | undefined;
            resourceInputs["contentBase64"] = state ? state.contentBase64 : undefined;
            resourceInputs["enabled"] = state ? state.enabled : undefined;
            resourceInputs["md5"] = state ? state.md5 : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["position"] = state ? state.position : undefined;
            resourceInputs["source"] = state ? state.source : undefined;
        } else {
            const args = argsOrState as GlobalInitScriptArgs | undefined;
            resourceInputs["contentBase64"] = args ? args.contentBase64 : undefined;
            resourceInputs["enabled"] = args ? args.enabled : undefined;
            resourceInputs["md5"] = args ? args.md5 : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["position"] = args ? args.position : undefined;
            resourceInputs["source"] = args ? args.source : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(GlobalInitScript.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GlobalInitScript resources.
 */
export interface GlobalInitScriptState {
    contentBase64?: pulumi.Input<string>;
    /**
     * specifies if the script is enabled for execution, or not
     */
    enabled?: pulumi.Input<boolean>;
    md5?: pulumi.Input<string>;
    /**
     * - the name of the script.  It should be unique
     */
    name?: pulumi.Input<string>;
    /**
     * - the position of a global init script, where `0` represents the first global init script to run, `1` is the second global init script to run, and so on. When omitted, the script gets the last position.
     */
    position?: pulumi.Input<number>;
    /**
     * Path to script's source code on local filesystem. Conflicts with `contentBase64`
     */
    source?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GlobalInitScript resource.
 */
export interface GlobalInitScriptArgs {
    contentBase64?: pulumi.Input<string>;
    /**
     * specifies if the script is enabled for execution, or not
     */
    enabled?: pulumi.Input<boolean>;
    md5?: pulumi.Input<string>;
    /**
     * - the name of the script.  It should be unique
     */
    name?: pulumi.Input<string>;
    /**
     * - the position of a global init script, where `0` represents the first global init script to run, `1` is the second global init script to run, and so on. When omitted, the script gets the last position.
     */
    position?: pulumi.Input<number>;
    /**
     * Path to script's source code on local filesystem. Conflicts with `contentBase64`
     */
    source?: pulumi.Input<string>;
}
