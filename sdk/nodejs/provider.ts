// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The provider type for the databricks package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'databricks';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Provider.__pulumiType;
    }

    public readonly accountId!: pulumi.Output<string | undefined>;
    public readonly authType!: pulumi.Output<string | undefined>;
    public readonly azureClientId!: pulumi.Output<string | undefined>;
    public readonly azureClientSecret!: pulumi.Output<string | undefined>;
    public readonly azureEnvironment!: pulumi.Output<string | undefined>;
    public readonly azureTenantId!: pulumi.Output<string | undefined>;
    public readonly azureWorkspaceResourceId!: pulumi.Output<string | undefined>;
    public readonly configFile!: pulumi.Output<string | undefined>;
    public readonly googleCredentials!: pulumi.Output<string | undefined>;
    public readonly googleServiceAccount!: pulumi.Output<string | undefined>;
    public readonly host!: pulumi.Output<string | undefined>;
    public readonly password!: pulumi.Output<string | undefined>;
    public readonly profile!: pulumi.Output<string | undefined>;
    public readonly token!: pulumi.Output<string | undefined>;
    public readonly username!: pulumi.Output<string | undefined>;

    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        {
            resourceInputs["accountId"] = (args ? args.accountId : undefined) ?? utilities.getEnv("DATABRICKS_ACCOUNT_ID");
            resourceInputs["authType"] = args ? args.authType : undefined;
            resourceInputs["azureClientId"] = args ? args.azureClientId : undefined;
            resourceInputs["azureClientSecret"] = args ? args.azureClientSecret : undefined;
            resourceInputs["azureEnvironment"] = args ? args.azureEnvironment : undefined;
            resourceInputs["azureTenantId"] = args ? args.azureTenantId : undefined;
            resourceInputs["azureUseMsi"] = pulumi.output(args ? args.azureUseMsi : undefined).apply(JSON.stringify);
            resourceInputs["azureWorkspaceResourceId"] = args ? args.azureWorkspaceResourceId : undefined;
            resourceInputs["configFile"] = (args ? args.configFile : undefined) ?? utilities.getEnv("DATABRICKS_CONFIG_FILE");
            resourceInputs["debugHeaders"] = pulumi.output((args ? args.debugHeaders : undefined) ?? utilities.getEnvBoolean("DATABRICKS_DEBUG_HEADERS")).apply(JSON.stringify);
            resourceInputs["debugTruncateBytes"] = pulumi.output((args ? args.debugTruncateBytes : undefined) ?? utilities.getEnvNumber("DATABRICKS_DEBUG_TRUNCATE_BYTES")).apply(JSON.stringify);
            resourceInputs["googleCredentials"] = args ? args.googleCredentials : undefined;
            resourceInputs["googleServiceAccount"] = args ? args.googleServiceAccount : undefined;
            resourceInputs["host"] = (args ? args.host : undefined) ?? utilities.getEnv("DATABRICKS_HOST");
            resourceInputs["httpTimeoutSeconds"] = pulumi.output(args ? args.httpTimeoutSeconds : undefined).apply(JSON.stringify);
            resourceInputs["password"] = (args ? args.password : undefined) ?? utilities.getEnv("DATABRICKS_PASSWORD");
            resourceInputs["profile"] = (args ? args.profile : undefined) ?? utilities.getEnv("DATABRICKS_PROFILE");
            resourceInputs["rateLimit"] = pulumi.output((args ? args.rateLimit : undefined) ?? utilities.getEnvNumber("DATABRICKS_RATE_LIMIT")).apply(JSON.stringify);
            resourceInputs["skipVerify"] = pulumi.output(args ? args.skipVerify : undefined).apply(JSON.stringify);
            resourceInputs["token"] = (args ? args.token : undefined) ?? utilities.getEnv("DATABRICKS_TOKEN");
            resourceInputs["username"] = (args ? args.username : undefined) ?? utilities.getEnv("DATABRICKS_USERNAME");
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Provider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    accountId?: pulumi.Input<string>;
    authType?: pulumi.Input<string>;
    azureClientId?: pulumi.Input<string>;
    azureClientSecret?: pulumi.Input<string>;
    azureEnvironment?: pulumi.Input<string>;
    azureTenantId?: pulumi.Input<string>;
    azureUseMsi?: pulumi.Input<boolean>;
    azureWorkspaceResourceId?: pulumi.Input<string>;
    configFile?: pulumi.Input<string>;
    debugHeaders?: pulumi.Input<boolean>;
    debugTruncateBytes?: pulumi.Input<number>;
    googleCredentials?: pulumi.Input<string>;
    googleServiceAccount?: pulumi.Input<string>;
    host?: pulumi.Input<string>;
    httpTimeoutSeconds?: pulumi.Input<number>;
    password?: pulumi.Input<string>;
    profile?: pulumi.Input<string>;
    rateLimit?: pulumi.Input<number>;
    skipVerify?: pulumi.Input<boolean>;
    token?: pulumi.Input<string>;
    username?: pulumi.Input<string>;
}
