// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class SqlQueryParameterEnumMultipleArgs : Pulumi.ResourceArgs
    {
        [Input("prefix", required: true)]
        public Input<string> Prefix { get; set; } = null!;

        [Input("separator", required: true)]
        public Input<string> Separator { get; set; } = null!;

        [Input("suffix", required: true)]
        public Input<string> Suffix { get; set; } = null!;

        public SqlQueryParameterEnumMultipleArgs()
        {
        }
    }
}
