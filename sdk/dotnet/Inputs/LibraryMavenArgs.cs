// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class LibraryMavenArgs : global::Pulumi.ResourceArgs
    {
        [Input("coordinates", required: true)]
        public Input<string> Coordinates { get; set; } = null!;

        [Input("exclusions")]
        private InputList<string>? _exclusions;
        public InputList<string> Exclusions
        {
            get => _exclusions ?? (_exclusions = new InputList<string>());
            set => _exclusions = value;
        }

        [Input("repo")]
        public Input<string>? Repo { get; set; }

        public LibraryMavenArgs()
        {
        }
        public static new LibraryMavenArgs Empty => new LibraryMavenArgs();
    }
}
