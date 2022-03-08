// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class InstancePoolAwsAttributesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Availability type used for all nodes. Valid values are `PREEMPTIBLE_GCP`, `PREEMPTIBLE_WITH_FALLBACK_GCP` and `ON_DEMAND_GCP`, default: `ON_DEMAND_GCP`.
        /// </summary>
        [Input("availability")]
        public Input<string>? Availability { get; set; }

        /// <summary>
        /// (Integer) The max price for AWS spot instances, as a percentage of the corresponding instance type’s on-demand price. For example, if this field is set to 50, and the instance pool needs a new i3.xlarge spot instance, then the max price is half of the price of on-demand i3.xlarge instances. Similarly, if this field is set to 200, the max price is twice the price of on-demand i3.xlarge instances. If not specified, the *default value is 100*. When spot instances are requested for this instance pool, only spot instances whose max price percentage matches this field are considered. *For safety, this field cannot be greater than 10000.*
        /// </summary>
        [Input("spotBidPricePercent")]
        public Input<int>? SpotBidPricePercent { get; set; }

        /// <summary>
        /// (String) Identifier for the availability zone/datacenter in which the instance pool resides. This string is of a form like `"us-west-2a"`. The provided availability zone must be in the same region as the Databricks deployment. For example, `"us-west-2a"` is not a valid zone ID if the Databricks deployment resides in the `"us-east-1"` region. This is an optional field. If not specified, a default zone is used. You can find the list of available zones as well as the default value by using the [List Zones API](https://docs.databricks.com/dev-tools/api/latest/clusters.html#clusterclusterservicelistavailablezones).
        /// </summary>
        [Input("zoneId")]
        public Input<string>? ZoneId { get; set; }

        public InstancePoolAwsAttributesArgs()
        {
        }
    }
}
