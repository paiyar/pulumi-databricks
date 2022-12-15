// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Outputs
{

    [OutputType]
    public sealed class JobSparkPythonTask
    {
        /// <summary>
        /// Parameters for the task
        /// </summary>
        public readonly ImmutableArray<string> Parameters;
        /// <summary>
        /// The URI of the Python file to be executed. databricks.DbfsFile and S3 paths are supported. This field is required.
        /// </summary>
        public readonly string PythonFile;

        [OutputConstructor]
        private JobSparkPythonTask(
            ImmutableArray<string> parameters,

            string pythonFile)
        {
            Parameters = parameters;
            PythonFile = pythonFile;
        }
    }
}
