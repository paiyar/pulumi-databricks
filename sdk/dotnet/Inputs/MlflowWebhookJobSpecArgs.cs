// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class MlflowWebhookJobSpecArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The personal access token used to authorize webhook's job runs.
        /// </summary>
        [Input("accessToken", required: true)]
        public Input<string> AccessToken { get; set; } = null!;

        /// <summary>
        /// ID of the Databricks job that the webhook runs.
        /// </summary>
        [Input("jobId", required: true)]
        public Input<string> JobId { get; set; } = null!;

        /// <summary>
        /// URL of the workspace containing the job that this webhook runs. If not specified, the job’s workspace URL is assumed to be the same as the workspace where the webhook is created.
        /// </summary>
        [Input("workspaceUrl")]
        public Input<string>? WorkspaceUrl { get; set; }

        public MlflowWebhookJobSpecArgs()
        {
        }
        public static new MlflowWebhookJobSpecArgs Empty => new MlflowWebhookJobSpecArgs();
    }
}
