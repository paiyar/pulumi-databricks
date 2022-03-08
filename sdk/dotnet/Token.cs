// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    /// <summary>
    /// This resource creates [Personal Access Tokens](https://docs.databricks.com/sql/user/security/personal-access-tokens.html) for the same user, that is authenticated with the provider. Most likely you should use databricks.OboToken to create [On-Behalf-Of tokens](https://docs.databricks.com/administration-guide/users-groups/service-principals.html#manage-personal-access-tokens-for-a-service-principal) for a databricks.ServicePrincipal in Databricks workspaces on AWS. Databricks workspaces on other clouds use their own native OAuth token flows.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Databricks = Pulumi.Databricks;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         // initialize provider in normal mode
    ///         var createdWorkspace = new Databricks.Provider("createdWorkspace", new Databricks.ProviderArgs
    ///         {
    ///             Host = databricks_mws_workspaces.This.Workspace_url,
    ///         });
    ///         // create PAT token to provision entities within workspace
    ///         var pat = new Databricks.Token("pat", new Databricks.TokenArgs
    ///         {
    ///             Comment = "Terraform Provisioning",
    ///             LifetimeSeconds = 8640000,
    ///         }, new CustomResourceOptions
    ///         {
    ///             Provider = databricks.Created_workspace,
    ///         });
    ///         this.DatabricksToken = pat.TokenValue;
    ///     }
    /// 
    ///     [Output("databricksToken")]
    ///     public Output&lt;string&gt; DatabricksToken { get; set; }
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// -&gt; **Note** Importing this resource is not currently supported.
    /// </summary>
    [DatabricksResourceType("databricks:index/token:Token")]
    public partial class Token : Pulumi.CustomResource
    {
        /// <summary>
        /// (String) Comment that will appear on the user’s settings page for this token.
        /// </summary>
        [Output("comment")]
        public Output<string?> Comment { get; private set; } = null!;

        [Output("creationTime")]
        public Output<int> CreationTime { get; private set; } = null!;

        [Output("expiryTime")]
        public Output<int> ExpiryTime { get; private set; } = null!;

        /// <summary>
        /// (Integer) The lifetime of the token, in seconds. If no lifetime is specified, the token remains valid indefinitely.
        /// </summary>
        [Output("lifetimeSeconds")]
        public Output<int?> LifetimeSeconds { get; private set; } = null!;

        [Output("tokenId")]
        public Output<string> TokenId { get; private set; } = null!;

        /// <summary>
        /// **Sensitive** value of the newly-created token.
        /// </summary>
        [Output("tokenValue")]
        public Output<string> TokenValue { get; private set; } = null!;


        /// <summary>
        /// Create a Token resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Token(string name, TokenArgs? args = null, CustomResourceOptions? options = null)
            : base("databricks:index/token:Token", name, args ?? new TokenArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Token(string name, Input<string> id, TokenState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/token:Token", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Token resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Token Get(string name, Input<string> id, TokenState? state = null, CustomResourceOptions? options = null)
        {
            return new Token(name, id, state, options);
        }
    }

    public sealed class TokenArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// (String) Comment that will appear on the user’s settings page for this token.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        [Input("creationTime")]
        public Input<int>? CreationTime { get; set; }

        [Input("expiryTime")]
        public Input<int>? ExpiryTime { get; set; }

        /// <summary>
        /// (Integer) The lifetime of the token, in seconds. If no lifetime is specified, the token remains valid indefinitely.
        /// </summary>
        [Input("lifetimeSeconds")]
        public Input<int>? LifetimeSeconds { get; set; }

        [Input("tokenId")]
        public Input<string>? TokenId { get; set; }

        public TokenArgs()
        {
        }
    }

    public sealed class TokenState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// (String) Comment that will appear on the user’s settings page for this token.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        [Input("creationTime")]
        public Input<int>? CreationTime { get; set; }

        [Input("expiryTime")]
        public Input<int>? ExpiryTime { get; set; }

        /// <summary>
        /// (Integer) The lifetime of the token, in seconds. If no lifetime is specified, the token remains valid indefinitely.
        /// </summary>
        [Input("lifetimeSeconds")]
        public Input<int>? LifetimeSeconds { get; set; }

        [Input("tokenId")]
        public Input<string>? TokenId { get; set; }

        /// <summary>
        /// **Sensitive** value of the newly-created token.
        /// </summary>
        [Input("tokenValue")]
        public Input<string>? TokenValue { get; set; }

        public TokenState()
        {
        }
    }
}
