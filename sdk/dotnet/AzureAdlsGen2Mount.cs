// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    [DatabricksResourceType("databricks:index/azureAdlsGen2Mount:AzureAdlsGen2Mount")]
    public partial class AzureAdlsGen2Mount : Pulumi.CustomResource
    {
        [Output("clientId")]
        public Output<string> ClientId { get; private set; } = null!;

        [Output("clientSecretKey")]
        public Output<string> ClientSecretKey { get; private set; } = null!;

        [Output("clientSecretScope")]
        public Output<string> ClientSecretScope { get; private set; } = null!;

        [Output("clusterId")]
        public Output<string?> ClusterId { get; private set; } = null!;

        [Output("containerName")]
        public Output<string> ContainerName { get; private set; } = null!;

        [Output("directory")]
        public Output<string> Directory { get; private set; } = null!;

        [Output("initializeFileSystem")]
        public Output<bool> InitializeFileSystem { get; private set; } = null!;

        [Output("mountName")]
        public Output<string> MountName { get; private set; } = null!;

        [Output("source")]
        public Output<string> Source { get; private set; } = null!;

        [Output("storageAccountName")]
        public Output<string> StorageAccountName { get; private set; } = null!;

        [Output("tenantId")]
        public Output<string> TenantId { get; private set; } = null!;


        /// <summary>
        /// Create a AzureAdlsGen2Mount resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AzureAdlsGen2Mount(string name, AzureAdlsGen2MountArgs args, CustomResourceOptions? options = null)
            : base("databricks:index/azureAdlsGen2Mount:AzureAdlsGen2Mount", name, args ?? new AzureAdlsGen2MountArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AzureAdlsGen2Mount(string name, Input<string> id, AzureAdlsGen2MountState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/azureAdlsGen2Mount:AzureAdlsGen2Mount", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AzureAdlsGen2Mount resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AzureAdlsGen2Mount Get(string name, Input<string> id, AzureAdlsGen2MountState? state = null, CustomResourceOptions? options = null)
        {
            return new AzureAdlsGen2Mount(name, id, state, options);
        }
    }

    public sealed class AzureAdlsGen2MountArgs : Pulumi.ResourceArgs
    {
        [Input("clientId", required: true)]
        public Input<string> ClientId { get; set; } = null!;

        [Input("clientSecretKey", required: true)]
        public Input<string> ClientSecretKey { get; set; } = null!;

        [Input("clientSecretScope", required: true)]
        public Input<string> ClientSecretScope { get; set; } = null!;

        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        [Input("containerName", required: true)]
        public Input<string> ContainerName { get; set; } = null!;

        [Input("directory")]
        public Input<string>? Directory { get; set; }

        [Input("initializeFileSystem", required: true)]
        public Input<bool> InitializeFileSystem { get; set; } = null!;

        [Input("mountName", required: true)]
        public Input<string> MountName { get; set; } = null!;

        [Input("storageAccountName", required: true)]
        public Input<string> StorageAccountName { get; set; } = null!;

        [Input("tenantId", required: true)]
        public Input<string> TenantId { get; set; } = null!;

        public AzureAdlsGen2MountArgs()
        {
        }
    }

    public sealed class AzureAdlsGen2MountState : Pulumi.ResourceArgs
    {
        [Input("clientId")]
        public Input<string>? ClientId { get; set; }

        [Input("clientSecretKey")]
        public Input<string>? ClientSecretKey { get; set; }

        [Input("clientSecretScope")]
        public Input<string>? ClientSecretScope { get; set; }

        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        [Input("containerName")]
        public Input<string>? ContainerName { get; set; }

        [Input("directory")]
        public Input<string>? Directory { get; set; }

        [Input("initializeFileSystem")]
        public Input<bool>? InitializeFileSystem { get; set; }

        [Input("mountName")]
        public Input<string>? MountName { get; set; }

        [Input("source")]
        public Input<string>? Source { get; set; }

        [Input("storageAccountName")]
        public Input<string>? StorageAccountName { get; set; }

        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        public AzureAdlsGen2MountState()
        {
        }
    }
}
