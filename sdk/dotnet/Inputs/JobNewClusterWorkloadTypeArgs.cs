// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class JobNewClusterWorkloadTypeArgs : Pulumi.ResourceArgs
    {
        [Input("clients", required: true)]
        public Input<Inputs.JobNewClusterWorkloadTypeClientsArgs> Clients { get; set; } = null!;

        public JobNewClusterWorkloadTypeArgs()
        {
        }
    }
}
