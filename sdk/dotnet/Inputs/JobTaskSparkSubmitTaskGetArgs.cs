// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class JobTaskSparkSubmitTaskGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("parameters")]
        private InputList<string>? _parameters;

        /// <summary>
        /// Parameters for the task
        /// </summary>
        public InputList<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputList<string>());
            set => _parameters = value;
        }

        public JobTaskSparkSubmitTaskGetArgs()
        {
        }
        public static new JobTaskSparkSubmitTaskGetArgs Empty => new JobTaskSparkSubmitTaskGetArgs();
    }
}
