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
    /// ## Import
    /// 
    /// -&gt; **Note** Importing this resource is not currently supported.
    /// </summary>
    [DatabricksResourceType("databricks:index/workspaceConf:WorkspaceConf")]
    public partial class WorkspaceConf : Pulumi.CustomResource
    {
        /// <summary>
        /// Key-value map of strings, that represent workspace configuration. Upon resource deletion, properties that start with `enable` or `enforce` will be reset to `false` value, regardless of initial default one.
        /// </summary>
        [Output("customConfig")]
        public Output<ImmutableDictionary<string, object>?> CustomConfig { get; private set; } = null!;


        /// <summary>
        /// Create a WorkspaceConf resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public WorkspaceConf(string name, WorkspaceConfArgs? args = null, CustomResourceOptions? options = null)
            : base("databricks:index/workspaceConf:WorkspaceConf", name, args ?? new WorkspaceConfArgs(), MakeResourceOptions(options, ""))
        {
        }

        private WorkspaceConf(string name, Input<string> id, WorkspaceConfState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/workspaceConf:WorkspaceConf", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing WorkspaceConf resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static WorkspaceConf Get(string name, Input<string> id, WorkspaceConfState? state = null, CustomResourceOptions? options = null)
        {
            return new WorkspaceConf(name, id, state, options);
        }
    }

    public sealed class WorkspaceConfArgs : Pulumi.ResourceArgs
    {
        [Input("customConfig")]
        private InputMap<object>? _customConfig;

        /// <summary>
        /// Key-value map of strings, that represent workspace configuration. Upon resource deletion, properties that start with `enable` or `enforce` will be reset to `false` value, regardless of initial default one.
        /// </summary>
        public InputMap<object> CustomConfig
        {
            get => _customConfig ?? (_customConfig = new InputMap<object>());
            set => _customConfig = value;
        }

        public WorkspaceConfArgs()
        {
        }
    }

    public sealed class WorkspaceConfState : Pulumi.ResourceArgs
    {
        [Input("customConfig")]
        private InputMap<object>? _customConfig;

        /// <summary>
        /// Key-value map of strings, that represent workspace configuration. Upon resource deletion, properties that start with `enable` or `enforce` will be reset to `false` value, regardless of initial default one.
        /// </summary>
        public InputMap<object> CustomConfig
        {
            get => _customConfig ?? (_customConfig = new InputMap<object>());
            set => _customConfig = value;
        }

        public WorkspaceConfState()
        {
        }
    }
}
