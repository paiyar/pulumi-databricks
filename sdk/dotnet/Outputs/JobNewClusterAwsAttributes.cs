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
    public sealed class JobNewClusterAwsAttributes
    {
        public readonly string? Availability;
        public readonly int? EbsVolumeCount;
        public readonly int? EbsVolumeSize;
        public readonly string? EbsVolumeType;
        public readonly int? FirstOnDemand;
        public readonly string? InstanceProfileArn;
        public readonly int? SpotBidPricePercent;
        public readonly string? ZoneId;

        [OutputConstructor]
        private JobNewClusterAwsAttributes(
            string? availability,

            int? ebsVolumeCount,

            int? ebsVolumeSize,

            string? ebsVolumeType,

            int? firstOnDemand,

            string? instanceProfileArn,

            int? spotBidPricePercent,

            string? zoneId)
        {
            Availability = availability;
            EbsVolumeCount = ebsVolumeCount;
            EbsVolumeSize = ebsVolumeSize;
            EbsVolumeType = ebsVolumeType;
            FirstOnDemand = firstOnDemand;
            InstanceProfileArn = instanceProfileArn;
            SpotBidPricePercent = spotBidPricePercent;
            ZoneId = zoneId;
        }
    }
}
