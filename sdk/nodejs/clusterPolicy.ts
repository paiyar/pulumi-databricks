// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * This resource creates a cluster policy, which limits the ability to create clusters based on a set of rules. The policy rules limit the attributes or attribute values available for cluster creation. cluster policies have ACLs that limit their use to specific users and groups. Only admin users can create, edit, and delete policies. Admin users also have access to all policies.
 *
 * Cluster policies let you:
 *
 * * Limit users to create clusters with prescribed settings.
 * * Simplify the user interface and enable more users to create their own clusters (by fixing and hiding some values).
 * * Control cost by limiting per cluster maximum cost (by setting limits on attributes whose values contribute to hourly price).
 *
 * Cluster policy permissions limit which policies a user can select in the Policy drop-down when the user creates a cluster:
 *
 * * If no policies have been created in the workspace, the Policy drop-down does not display.
 * * A user who has cluster create permission can select the `Free form` policy and create fully-configurable clusters.
 * * A user who has both cluster create permission and access to cluster policies can select the Free form policy and policies they have access to.
 * * A user that has access to only cluster policies, can select the policies they have access to.
 *
 * ## Related Resources
 *
 * The following resources are often used in the same context:
 *
 * * Dynamic Passthrough Clusters for a Group guide
 * * End to end workspace management guide
 * * databricks.getClusters data to retrieve a list of databricks.Cluster ids.
 * * databricks.Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
 * * databricks.getCurrentUser data to retrieve information about databricks.User or databricks_service_principal, that is calling Databricks REST API.
 * * databricks.GlobalInitScript to manage [global init scripts](https://docs.databricks.com/clusters/init-scripts.html#global-init-scripts), which are run on all databricks.Cluster and databricks_job.
 * * databricks.InstancePool to manage [instance pools](https://docs.databricks.com/clusters/instance-pools/index.html) to reduce cluster start and auto-scaling times by maintaining a set of idle, ready-to-use instances.
 * * databricks.InstanceProfile to manage AWS EC2 instance profiles that users can launch databricks.Cluster and access data, like databricks_mount.
 * * databricks.IpAccessList to allow access from [predefined IP ranges](https://docs.databricks.com/security/network/ip-access-list.html).
 * * databricks.Library to install a [library](https://docs.databricks.com/libraries/index.html) on databricks_cluster.
 * * databricks.getNodeType data to get the smallest node type for databricks.Cluster that fits search criteria, like amount of RAM or number of cores.
 * * databricks.Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
 * * databricks.getSparkVersion data to get [Databricks Runtime (DBR)](https://docs.databricks.com/runtime/dbr.html) version that could be used for `sparkVersion` parameter in databricks.Cluster and other resources.
 * * databricks.UserInstanceProfile to attach databricks.InstanceProfile (AWS) to databricks_user.
 * * databricks.WorkspaceConf to manage workspace configuration for expert usage.
 *
 * ## Import
 *
 * The resource cluster policy can be imported using the policy idbash
 *
 * ```sh
 *  $ pulumi import databricks:index/clusterPolicy:ClusterPolicy this <cluster-policy-id>
 * ```
 */
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
     * Policy definition JSON document expressed in [Databricks Policy Definition Language](https://docs.databricks.com/administration-guide/clusters/policies.html#cluster-policy-definition).
     */
    public readonly definition!: pulumi.Output<string | undefined>;
    /**
     * Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Canonical unique identifier for the cluster policy.
     */
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
     * Policy definition JSON document expressed in [Databricks Policy Definition Language](https://docs.databricks.com/administration-guide/clusters/policies.html#cluster-policy-definition).
     */
    definition?: pulumi.Input<string>;
    /**
     * Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
     */
    name?: pulumi.Input<string>;
    /**
     * Canonical unique identifier for the cluster policy.
     */
    policyId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ClusterPolicy resource.
 */
export interface ClusterPolicyArgs {
    /**
     * Policy definition JSON document expressed in [Databricks Policy Definition Language](https://docs.databricks.com/administration-guide/clusters/policies.html#cluster-policy-definition).
     */
    definition?: pulumi.Input<string>;
    /**
     * Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
     */
    name?: pulumi.Input<string>;
}
