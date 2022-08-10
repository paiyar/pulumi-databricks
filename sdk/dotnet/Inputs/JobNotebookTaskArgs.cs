// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class JobNotebookTaskArgs : Pulumi.ResourceArgs
    {
        [Input("baseParameters")]
        private InputMap<object>? _baseParameters;
        public InputMap<object> BaseParameters
        {
            get => _baseParameters ?? (_baseParameters = new InputMap<object>());
            set => _baseParameters = value;
        }

        [Input("notebookPath", required: true)]
        public Input<string> NotebookPath { get; set; } = null!;

        public JobNotebookTaskArgs()
        {
        }
    }
}
