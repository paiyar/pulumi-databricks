// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    [DatabricksResourceType("databricks:index/globalInitScript:GlobalInitScript")]
    public partial class GlobalInitScript : Pulumi.CustomResource
    {
        [Output("contentBase64")]
        public Output<string?> ContentBase64 { get; private set; } = null!;

        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        [Output("md5")]
        public Output<string?> Md5 { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("position")]
        public Output<int> Position { get; private set; } = null!;

        [Output("source")]
        public Output<string?> Source { get; private set; } = null!;


        /// <summary>
        /// Create a GlobalInitScript resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GlobalInitScript(string name, GlobalInitScriptArgs? args = null, CustomResourceOptions? options = null)
            : base("databricks:index/globalInitScript:GlobalInitScript", name, args ?? new GlobalInitScriptArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GlobalInitScript(string name, Input<string> id, GlobalInitScriptState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/globalInitScript:GlobalInitScript", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing GlobalInitScript resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GlobalInitScript Get(string name, Input<string> id, GlobalInitScriptState? state = null, CustomResourceOptions? options = null)
        {
            return new GlobalInitScript(name, id, state, options);
        }
    }

    public sealed class GlobalInitScriptArgs : Pulumi.ResourceArgs
    {
        [Input("contentBase64")]
        public Input<string>? ContentBase64 { get; set; }

        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("md5")]
        public Input<string>? Md5 { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("position")]
        public Input<int>? Position { get; set; }

        [Input("source")]
        public Input<string>? Source { get; set; }

        public GlobalInitScriptArgs()
        {
        }
    }

    public sealed class GlobalInitScriptState : Pulumi.ResourceArgs
    {
        [Input("contentBase64")]
        public Input<string>? ContentBase64 { get; set; }

        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("md5")]
        public Input<string>? Md5 { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("position")]
        public Input<int>? Position { get; set; }

        [Input("source")]
        public Input<string>? Source { get; set; }

        public GlobalInitScriptState()
        {
        }
    }
}
