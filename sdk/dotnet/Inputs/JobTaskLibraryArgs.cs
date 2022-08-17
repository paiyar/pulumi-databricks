// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class JobTaskLibraryArgs : global::Pulumi.ResourceArgs
    {
        [Input("cran")]
        public Input<Inputs.JobTaskLibraryCranArgs>? Cran { get; set; }

        [Input("egg")]
        public Input<string>? Egg { get; set; }

        [Input("jar")]
        public Input<string>? Jar { get; set; }

        [Input("maven")]
        public Input<Inputs.JobTaskLibraryMavenArgs>? Maven { get; set; }

        [Input("pypi")]
        public Input<Inputs.JobTaskLibraryPypiArgs>? Pypi { get; set; }

        [Input("whl")]
        public Input<string>? Whl { get; set; }

        public JobTaskLibraryArgs()
        {
        }
        public static new JobTaskLibraryArgs Empty => new JobTaskLibraryArgs();
    }
}
