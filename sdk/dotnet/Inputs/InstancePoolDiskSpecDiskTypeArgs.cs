// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class InstancePoolDiskSpecDiskTypeArgs : Pulumi.ResourceArgs
    {
        [Input("azureDiskVolumeType")]
        public Input<string>? AzureDiskVolumeType { get; set; }

        [Input("ebsVolumeType")]
        public Input<string>? EbsVolumeType { get; set; }

        public InstancePoolDiskSpecDiskTypeArgs()
        {
        }
    }
}
