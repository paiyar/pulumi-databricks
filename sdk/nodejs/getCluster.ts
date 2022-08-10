// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

export function getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("databricks:index/getCluster:getCluster", {
        "clusterId": args.clusterId,
        "clusterInfo": args.clusterInfo,
    }, opts);
}

/**
 * A collection of arguments for invoking getCluster.
 */
export interface GetClusterArgs {
    clusterId: string;
    clusterInfo?: inputs.GetClusterClusterInfo;
}

/**
 * A collection of values returned by getCluster.
 */
export interface GetClusterResult {
    readonly clusterId: string;
    readonly clusterInfo: outputs.GetClusterClusterInfo;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}

export function getClusterOutput(args: GetClusterOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetClusterResult> {
    return pulumi.output(args).apply(a => getCluster(a, opts))
}

/**
 * A collection of arguments for invoking getCluster.
 */
export interface GetClusterOutputArgs {
    clusterId: pulumi.Input<string>;
    clusterInfo?: pulumi.Input<inputs.GetClusterClusterInfoArgs>;
}
