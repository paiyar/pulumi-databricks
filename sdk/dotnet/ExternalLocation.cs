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
    /// &gt; **Public Preview** This feature is in [Public Preview](https://docs.databricks.com/release-notes/release-types.html). Contact your Databricks representative to request access.
    /// 
    /// To work with external tables, Unity Catalog introduces two new objects to access and work with external cloud storage:
    /// - databricks.StorageCredential represent authentication methods to access cloud storage (e.g. an IAM role for Amazon S3 or a service principal for Azure Storage). Storage credentials are access-controlled to determine which users can use the credential.
    /// - `databricks.ExternalLocation` are objects that combine a cloud storage path with a Storage Credential that can be used to access the location.
    /// 
    /// ## Import
    /// 
    /// This resource can be imported by namebash
    /// 
    /// ```sh
    ///  $ pulumi import databricks:index/externalLocation:ExternalLocation this &lt;name&gt;
    /// ```
    /// </summary>
    [DatabricksResourceType("databricks:index/externalLocation:ExternalLocation")]
    public partial class ExternalLocation : Pulumi.CustomResource
    {
        /// <summary>
        /// User-supplied free-form text.
        /// </summary>
        [Output("comment")]
        public Output<string?> Comment { get; private set; } = null!;

        /// <summary>
        /// Name of the databricks.StorageCredential to use with this External Location.
        /// </summary>
        [Output("credentialName")]
        public Output<string> CredentialName { get; private set; } = null!;

        [Output("metastoreId")]
        public Output<string> MetastoreId { get; private set; } = null!;

        /// <summary>
        /// Name of External Location, which must be unique within the databricks_metastore. Change forces creation of a new resource.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Username/groupname/sp application_id External Location owner.
        /// </summary>
        [Output("owner")]
        public Output<string> Owner { get; private set; } = null!;

        /// <summary>
        /// Suppress validation errors if any &amp; force save the external location
        /// </summary>
        [Output("skipValidation")]
        public Output<bool?> SkipValidation { get; private set; } = null!;

        /// <summary>
        /// Path URL in cloud storage, of the form: `s3://[bucket-host]/[bucket-dir]` (AWS), `abfss://[user]@[host]/[path]` (Azure).
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;


        /// <summary>
        /// Create a ExternalLocation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ExternalLocation(string name, ExternalLocationArgs args, CustomResourceOptions? options = null)
            : base("databricks:index/externalLocation:ExternalLocation", name, args ?? new ExternalLocationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ExternalLocation(string name, Input<string> id, ExternalLocationState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/externalLocation:ExternalLocation", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ExternalLocation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ExternalLocation Get(string name, Input<string> id, ExternalLocationState? state = null, CustomResourceOptions? options = null)
        {
            return new ExternalLocation(name, id, state, options);
        }
    }

    public sealed class ExternalLocationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// User-supplied free-form text.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Name of the databricks.StorageCredential to use with this External Location.
        /// </summary>
        [Input("credentialName", required: true)]
        public Input<string> CredentialName { get; set; } = null!;

        [Input("metastoreId")]
        public Input<string>? MetastoreId { get; set; }

        /// <summary>
        /// Name of External Location, which must be unique within the databricks_metastore. Change forces creation of a new resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Username/groupname/sp application_id External Location owner.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        /// <summary>
        /// Suppress validation errors if any &amp; force save the external location
        /// </summary>
        [Input("skipValidation")]
        public Input<bool>? SkipValidation { get; set; }

        /// <summary>
        /// Path URL in cloud storage, of the form: `s3://[bucket-host]/[bucket-dir]` (AWS), `abfss://[user]@[host]/[path]` (Azure).
        /// </summary>
        [Input("url", required: true)]
        public Input<string> Url { get; set; } = null!;

        public ExternalLocationArgs()
        {
        }
    }

    public sealed class ExternalLocationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// User-supplied free-form text.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Name of the databricks.StorageCredential to use with this External Location.
        /// </summary>
        [Input("credentialName")]
        public Input<string>? CredentialName { get; set; }

        [Input("metastoreId")]
        public Input<string>? MetastoreId { get; set; }

        /// <summary>
        /// Name of External Location, which must be unique within the databricks_metastore. Change forces creation of a new resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Username/groupname/sp application_id External Location owner.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        /// <summary>
        /// Suppress validation errors if any &amp; force save the external location
        /// </summary>
        [Input("skipValidation")]
        public Input<bool>? SkipValidation { get; set; }

        /// <summary>
        /// Path URL in cloud storage, of the form: `s3://[bucket-host]/[bucket-dir]` (AWS), `abfss://[user]@[host]/[path]` (Azure).
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        public ExternalLocationState()
        {
        }
    }
}
