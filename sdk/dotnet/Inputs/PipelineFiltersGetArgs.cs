// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class PipelineFiltersGetArgs : Pulumi.ResourceArgs
    {
        [Input("excludes")]
        private InputList<string>? _excludes;
        public InputList<string> Excludes
        {
            get => _excludes ?? (_excludes = new InputList<string>());
            set => _excludes = value;
        }

        [Input("includes")]
        private InputList<string>? _includes;
        public InputList<string> Includes
        {
            get => _includes ?? (_includes = new InputList<string>());
            set => _includes = value;
        }

        public PipelineFiltersGetArgs()
        {
        }
    }
}
