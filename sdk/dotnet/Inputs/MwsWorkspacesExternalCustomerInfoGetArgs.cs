// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class MwsWorkspacesExternalCustomerInfoGetArgs : Pulumi.ResourceArgs
    {
        [Input("authoritativeUserEmail", required: true)]
        public Input<string> AuthoritativeUserEmail { get; set; } = null!;

        [Input("authoritativeUserFullName", required: true)]
        public Input<string> AuthoritativeUserFullName { get; set; } = null!;

        [Input("customerName", required: true)]
        public Input<string> CustomerName { get; set; } = null!;

        public MwsWorkspacesExternalCustomerInfoGetArgs()
        {
        }
    }
}
