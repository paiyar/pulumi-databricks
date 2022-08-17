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
    public sealed class JobJobClusterNewClusterGcpAttributes
    {
        public readonly string? Availability;
        public readonly int? BootDiskSize;
        public readonly string? GoogleServiceAccount;
        public readonly bool? UsePreemptibleExecutors;
        public readonly string? ZoneId;

        [OutputConstructor]
        private JobJobClusterNewClusterGcpAttributes(
            string? availability,

            int? bootDiskSize,

            string? googleServiceAccount,

            bool? usePreemptibleExecutors,

            string? zoneId)
        {
            Availability = availability;
            BootDiskSize = bootDiskSize;
            GoogleServiceAccount = googleServiceAccount;
            UsePreemptibleExecutors = usePreemptibleExecutors;
            ZoneId = zoneId;
        }
    }
}
