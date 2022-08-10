// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    [DatabricksResourceType("databricks:index/mwsCredentials:MwsCredentials")]
    public partial class MwsCredentials : Pulumi.CustomResource
    {
        [Output("accountId")]
        public Output<string> AccountId { get; private set; } = null!;

        [Output("creationTime")]
        public Output<int> CreationTime { get; private set; } = null!;

        [Output("credentialsId")]
        public Output<string> CredentialsId { get; private set; } = null!;

        [Output("credentialsName")]
        public Output<string> CredentialsName { get; private set; } = null!;

        [Output("externalId")]
        public Output<string> ExternalId { get; private set; } = null!;

        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;


        /// <summary>
        /// Create a MwsCredentials resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MwsCredentials(string name, MwsCredentialsArgs args, CustomResourceOptions? options = null)
            : base("databricks:index/mwsCredentials:MwsCredentials", name, args ?? new MwsCredentialsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private MwsCredentials(string name, Input<string> id, MwsCredentialsState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/mwsCredentials:MwsCredentials", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing MwsCredentials resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MwsCredentials Get(string name, Input<string> id, MwsCredentialsState? state = null, CustomResourceOptions? options = null)
        {
            return new MwsCredentials(name, id, state, options);
        }
    }

    public sealed class MwsCredentialsArgs : Pulumi.ResourceArgs
    {
        [Input("accountId", required: true)]
        public Input<string> AccountId { get; set; } = null!;

        [Input("credentialsName", required: true)]
        public Input<string> CredentialsName { get; set; } = null!;

        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        public MwsCredentialsArgs()
        {
        }
    }

    public sealed class MwsCredentialsState : Pulumi.ResourceArgs
    {
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        [Input("creationTime")]
        public Input<int>? CreationTime { get; set; }

        [Input("credentialsId")]
        public Input<string>? CredentialsId { get; set; }

        [Input("credentialsName")]
        public Input<string>? CredentialsName { get; set; }

        [Input("externalId")]
        public Input<string>? ExternalId { get; set; }

        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        public MwsCredentialsState()
        {
        }
    }
}
