// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Outputs
{

    [OutputType]
    public sealed class JobJobCluster
    {
        /// <summary>
        /// Identifier that can be referenced in `task` block, so that cluster is shared between tasks
        /// </summary>
        public readonly string? JobClusterKey;
        /// <summary>
        /// Same set of parameters as for databricks.Cluster resource.
        /// </summary>
        public readonly Outputs.JobJobClusterNewCluster? NewCluster;

        [OutputConstructor]
        private JobJobCluster(
            string? jobClusterKey,

            Outputs.JobJobClusterNewCluster? newCluster)
        {
            JobClusterKey = jobClusterKey;
            NewCluster = newCluster;
        }
    }
}
