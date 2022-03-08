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
    /// With this resource you can insert a secret under the provided scope with the given name. If a secret already exists with the same name, this command overwrites the existing secret’s value. The server encrypts the secret using the secret scope’s encryption settings before storing it. You must have WRITE or MANAGE permission on the secret scope. The secret key must consist of alphanumeric characters, dashes, underscores, and periods, and cannot exceed 128 characters. The maximum allowed secret value size is 128 KB. The maximum number of secrets in a given scope is 1000. You can read a secret value only from within a command on a cluster (for example, through a notebook); there is no API to read a secret value outside of a cluster. The permission applied is based on who is invoking the command and you must have at least READ permission. Please consult [Secrets User Guide](https://docs.databricks.com/security/secrets/index.html#secrets-user-guide) for more details.
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
    ///         var app = new Databricks.SecretScope("app", new Databricks.SecretScopeArgs
    ///         {
    ///         });
    ///         var publishingApi = new Databricks.Secret("publishingApi", new Databricks.SecretArgs
    ///         {
    ///             Key = "publishing_api",
    ///             StringValue = data.Azurerm_key_vault_secret.Example.Value,
    ///             Scope = app.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ## Related Resources
    /// 
    /// The following resources are often used in the same context:
    /// 
    /// * End to end workspace management guide.
    /// * databricks.Notebook to manage [Databricks Notebooks](https://docs.databricks.com/notebooks/index.html).
    /// * databricks.Pipeline to deploy [Delta Live Tables](https://docs.databricks.com/data-engineering/delta-live-tables/index.html).
    /// * databricks.Repo to manage [Databricks Repos](https://docs.databricks.com/repos.html).
    /// * databricks.SecretAcl to manage access to [secrets](https://docs.databricks.com/security/secrets/index.html#secrets-user-guide) in Databricks workspace.
    /// * databricks.SecretScope to create [secret scopes](https://docs.databricks.com/security/secrets/index.html#secrets-user-guide) in Databricks workspace.
    /// 
    /// ## Import
    /// 
    /// The resource secret can be imported using `scopeName|||secretKey` combination. **This may change in future versions.** bash
    /// 
    /// ```sh
    ///  $ pulumi import databricks:index/secret:Secret app `scopeName|||secretKey`
    /// ```
    /// </summary>
    [DatabricksResourceType("databricks:index/secret:Secret")]
    public partial class Secret : Pulumi.CustomResource
    {
        /// <summary>
        /// (String) key within secret scope. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
        /// </summary>
        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        /// <summary>
        /// (Integer) time secret was updated
        /// </summary>
        [Output("lastUpdatedTimestamp")]
        public Output<int> LastUpdatedTimestamp { get; private set; } = null!;

        /// <summary>
        /// (String) name of databricks secret scope. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
        /// </summary>
        [Output("scope")]
        public Output<string> Scope { get; private set; } = null!;

        /// <summary>
        /// (String) super secret sensitive value.
        /// </summary>
        [Output("stringValue")]
        public Output<string> StringValue { get; private set; } = null!;


        /// <summary>
        /// Create a Secret resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Secret(string name, SecretArgs args, CustomResourceOptions? options = null)
            : base("databricks:index/secret:Secret", name, args ?? new SecretArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Secret(string name, Input<string> id, SecretState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/secret:Secret", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Secret resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Secret Get(string name, Input<string> id, SecretState? state = null, CustomResourceOptions? options = null)
        {
            return new Secret(name, id, state, options);
        }
    }

    public sealed class SecretArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// (String) key within secret scope. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// (String) name of databricks secret scope. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
        /// </summary>
        [Input("scope", required: true)]
        public Input<string> Scope { get; set; } = null!;

        /// <summary>
        /// (String) super secret sensitive value.
        /// </summary>
        [Input("stringValue", required: true)]
        public Input<string> StringValue { get; set; } = null!;

        public SecretArgs()
        {
        }
    }

    public sealed class SecretState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// (String) key within secret scope. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// (Integer) time secret was updated
        /// </summary>
        [Input("lastUpdatedTimestamp")]
        public Input<int>? LastUpdatedTimestamp { get; set; }

        /// <summary>
        /// (String) name of databricks secret scope. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
        /// </summary>
        [Input("scope")]
        public Input<string>? Scope { get; set; }

        /// <summary>
        /// (String) super secret sensitive value.
        /// </summary>
        [Input("stringValue")]
        public Input<string>? StringValue { get; set; }

        public SecretState()
        {
        }
    }
}
