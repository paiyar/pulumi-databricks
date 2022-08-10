// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Import
 *
 * The resource cluster can be imported using ID of Git credential that could be obtained via REST APIbash
 *
 * ```sh
 *  $ pulumi import databricks:index/gitCredential:GitCredential this <git-credential-id>
 * ```
 */
export class GitCredential extends pulumi.CustomResource {
    /**
     * Get an existing GitCredential resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GitCredentialState, opts?: pulumi.CustomResourceOptions): GitCredential {
        return new GitCredential(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/gitCredential:GitCredential';

    /**
     * Returns true if the given object is an instance of GitCredential.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GitCredential {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GitCredential.__pulumiType;
    }

    /**
     * specify if settings need to be enforced - right now, Databricks allows only single Git credential, so if it's already configured, the apply operation will fail.
     */
    public readonly force!: pulumi.Output<boolean | undefined>;
    /**
     * case insensitive name of the Git provider.  Following values are supported right now (could be a subject for a change, consult [Git Credentials API documentation](https://docs.databricks.com/dev-tools/api/latest/gitcredentials.html)): `gitHub`, `gitHubEnterprise`, `bitbucketCloud`, `bitbucketServer`, `azureDevOpsServices`, `gitLab`, `gitLabEnterpriseEdition`, `awsCodeCommit`.
     */
    public readonly gitProvider!: pulumi.Output<string>;
    /**
     * user name at Git provider.
     */
    public readonly gitUsername!: pulumi.Output<string>;
    public readonly personalAccessToken!: pulumi.Output<string>;

    /**
     * Create a GitCredential resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GitCredentialArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GitCredentialArgs | GitCredentialState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GitCredentialState | undefined;
            resourceInputs["force"] = state ? state.force : undefined;
            resourceInputs["gitProvider"] = state ? state.gitProvider : undefined;
            resourceInputs["gitUsername"] = state ? state.gitUsername : undefined;
            resourceInputs["personalAccessToken"] = state ? state.personalAccessToken : undefined;
        } else {
            const args = argsOrState as GitCredentialArgs | undefined;
            if ((!args || args.gitProvider === undefined) && !opts.urn) {
                throw new Error("Missing required property 'gitProvider'");
            }
            if ((!args || args.gitUsername === undefined) && !opts.urn) {
                throw new Error("Missing required property 'gitUsername'");
            }
            if ((!args || args.personalAccessToken === undefined) && !opts.urn) {
                throw new Error("Missing required property 'personalAccessToken'");
            }
            resourceInputs["force"] = args ? args.force : undefined;
            resourceInputs["gitProvider"] = args ? args.gitProvider : undefined;
            resourceInputs["gitUsername"] = args ? args.gitUsername : undefined;
            resourceInputs["personalAccessToken"] = args ? args.personalAccessToken : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(GitCredential.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GitCredential resources.
 */
export interface GitCredentialState {
    /**
     * specify if settings need to be enforced - right now, Databricks allows only single Git credential, so if it's already configured, the apply operation will fail.
     */
    force?: pulumi.Input<boolean>;
    /**
     * case insensitive name of the Git provider.  Following values are supported right now (could be a subject for a change, consult [Git Credentials API documentation](https://docs.databricks.com/dev-tools/api/latest/gitcredentials.html)): `gitHub`, `gitHubEnterprise`, `bitbucketCloud`, `bitbucketServer`, `azureDevOpsServices`, `gitLab`, `gitLabEnterpriseEdition`, `awsCodeCommit`.
     */
    gitProvider?: pulumi.Input<string>;
    /**
     * user name at Git provider.
     */
    gitUsername?: pulumi.Input<string>;
    personalAccessToken?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GitCredential resource.
 */
export interface GitCredentialArgs {
    /**
     * specify if settings need to be enforced - right now, Databricks allows only single Git credential, so if it's already configured, the apply operation will fail.
     */
    force?: pulumi.Input<boolean>;
    /**
     * case insensitive name of the Git provider.  Following values are supported right now (could be a subject for a change, consult [Git Credentials API documentation](https://docs.databricks.com/dev-tools/api/latest/gitcredentials.html)): `gitHub`, `gitHubEnterprise`, `bitbucketCloud`, `bitbucketServer`, `azureDevOpsServices`, `gitLab`, `gitLabEnterpriseEdition`, `awsCodeCommit`.
     */
    gitProvider: pulumi.Input<string>;
    /**
     * user name at Git provider.
     */
    gitUsername: pulumi.Input<string>;
    personalAccessToken: pulumi.Input<string>;
}
