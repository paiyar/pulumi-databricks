// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class JobGitSourceArgs : Pulumi.ResourceArgs
    {
        [Input("branch")]
        public Input<string>? Branch { get; set; }

        [Input("commit")]
        public Input<string>? Commit { get; set; }

        [Input("provider")]
        public Input<string>? Provider { get; set; }

        [Input("tag")]
        public Input<string>? Tag { get; set; }

        [Input("url", required: true)]
        public Input<string> Url { get; set; } = null!;

        public JobGitSourceArgs()
        {
        }
    }
}
