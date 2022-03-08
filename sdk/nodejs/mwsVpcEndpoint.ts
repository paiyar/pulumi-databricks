// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Import
 *
 * -> **Note** Importing this resource is not currently supported.
 */
export class MwsVpcEndpoint extends pulumi.CustomResource {
    /**
     * Get an existing MwsVpcEndpoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MwsVpcEndpointState, opts?: pulumi.CustomResourceOptions): MwsVpcEndpoint {
        return new MwsVpcEndpoint(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/mwsVpcEndpoint:MwsVpcEndpoint';

    /**
     * Returns true if the given object is an instance of MwsVpcEndpoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MwsVpcEndpoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MwsVpcEndpoint.__pulumiType;
    }

    /**
     * Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
     */
    public readonly accountId!: pulumi.Output<string | undefined>;
    public readonly awsAccountId!: pulumi.Output<string>;
    /**
     * ID of Databricks VPC endpoint service to connect to. Please contact your Databricks representative to request mapping
     */
    public readonly awsEndpointServiceId!: pulumi.Output<string>;
    public readonly awsVpcEndpointId!: pulumi.Output<string>;
    /**
     * Region of AWS VPC
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * State of VPC Endpoint
     */
    public readonly state!: pulumi.Output<string>;
    public readonly useCase!: pulumi.Output<string>;
    /**
     * Canonical unique identifier of VPC Endpoint in Databricks Account
     */
    public readonly vpcEndpointId!: pulumi.Output<string>;
    /**
     * Name of VPC Endpoint in Databricks Account
     */
    public readonly vpcEndpointName!: pulumi.Output<string>;

    /**
     * Create a MwsVpcEndpoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MwsVpcEndpointArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MwsVpcEndpointArgs | MwsVpcEndpointState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MwsVpcEndpointState | undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["awsAccountId"] = state ? state.awsAccountId : undefined;
            resourceInputs["awsEndpointServiceId"] = state ? state.awsEndpointServiceId : undefined;
            resourceInputs["awsVpcEndpointId"] = state ? state.awsVpcEndpointId : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["state"] = state ? state.state : undefined;
            resourceInputs["useCase"] = state ? state.useCase : undefined;
            resourceInputs["vpcEndpointId"] = state ? state.vpcEndpointId : undefined;
            resourceInputs["vpcEndpointName"] = state ? state.vpcEndpointName : undefined;
        } else {
            const args = argsOrState as MwsVpcEndpointArgs | undefined;
            if ((!args || args.awsVpcEndpointId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'awsVpcEndpointId'");
            }
            if ((!args || args.region === undefined) && !opts.urn) {
                throw new Error("Missing required property 'region'");
            }
            if ((!args || args.vpcEndpointName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcEndpointName'");
            }
            resourceInputs["accountId"] = args ? args.accountId : undefined;
            resourceInputs["awsAccountId"] = args ? args.awsAccountId : undefined;
            resourceInputs["awsEndpointServiceId"] = args ? args.awsEndpointServiceId : undefined;
            resourceInputs["awsVpcEndpointId"] = args ? args.awsVpcEndpointId : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["state"] = args ? args.state : undefined;
            resourceInputs["useCase"] = args ? args.useCase : undefined;
            resourceInputs["vpcEndpointId"] = args ? args.vpcEndpointId : undefined;
            resourceInputs["vpcEndpointName"] = args ? args.vpcEndpointName : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(MwsVpcEndpoint.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MwsVpcEndpoint resources.
 */
export interface MwsVpcEndpointState {
    /**
     * Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
     */
    accountId?: pulumi.Input<string>;
    awsAccountId?: pulumi.Input<string>;
    /**
     * ID of Databricks VPC endpoint service to connect to. Please contact your Databricks representative to request mapping
     */
    awsEndpointServiceId?: pulumi.Input<string>;
    awsVpcEndpointId?: pulumi.Input<string>;
    /**
     * Region of AWS VPC
     */
    region?: pulumi.Input<string>;
    /**
     * State of VPC Endpoint
     */
    state?: pulumi.Input<string>;
    useCase?: pulumi.Input<string>;
    /**
     * Canonical unique identifier of VPC Endpoint in Databricks Account
     */
    vpcEndpointId?: pulumi.Input<string>;
    /**
     * Name of VPC Endpoint in Databricks Account
     */
    vpcEndpointName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MwsVpcEndpoint resource.
 */
export interface MwsVpcEndpointArgs {
    /**
     * Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
     */
    accountId?: pulumi.Input<string>;
    awsAccountId?: pulumi.Input<string>;
    /**
     * ID of Databricks VPC endpoint service to connect to. Please contact your Databricks representative to request mapping
     */
    awsEndpointServiceId?: pulumi.Input<string>;
    awsVpcEndpointId: pulumi.Input<string>;
    /**
     * Region of AWS VPC
     */
    region: pulumi.Input<string>;
    /**
     * State of VPC Endpoint
     */
    state?: pulumi.Input<string>;
    useCase?: pulumi.Input<string>;
    /**
     * Canonical unique identifier of VPC Endpoint in Databricks Account
     */
    vpcEndpointId?: pulumi.Input<string>;
    /**
     * Name of VPC Endpoint in Databricks Account
     */
    vpcEndpointName: pulumi.Input<string>;
}
