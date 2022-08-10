// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class JobTaskArgs : Pulumi.ResourceArgs
    {
        [Input("dbtTask")]
        public Input<Inputs.JobTaskDbtTaskArgs>? DbtTask { get; set; }

        [Input("dependsOns")]
        private InputList<Inputs.JobTaskDependsOnArgs>? _dependsOns;
        public InputList<Inputs.JobTaskDependsOnArgs> DependsOns
        {
            get => _dependsOns ?? (_dependsOns = new InputList<Inputs.JobTaskDependsOnArgs>());
            set => _dependsOns = value;
        }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("emailNotifications")]
        public Input<Inputs.JobTaskEmailNotificationsArgs>? EmailNotifications { get; set; }

        [Input("existingClusterId")]
        public Input<string>? ExistingClusterId { get; set; }

        [Input("jobClusterKey")]
        public Input<string>? JobClusterKey { get; set; }

        [Input("libraries")]
        private InputList<Inputs.JobTaskLibraryArgs>? _libraries;
        public InputList<Inputs.JobTaskLibraryArgs> Libraries
        {
            get => _libraries ?? (_libraries = new InputList<Inputs.JobTaskLibraryArgs>());
            set => _libraries = value;
        }

        [Input("maxRetries")]
        public Input<int>? MaxRetries { get; set; }

        [Input("minRetryIntervalMillis")]
        public Input<int>? MinRetryIntervalMillis { get; set; }

        [Input("newCluster")]
        public Input<Inputs.JobTaskNewClusterArgs>? NewCluster { get; set; }

        [Input("notebookTask")]
        public Input<Inputs.JobTaskNotebookTaskArgs>? NotebookTask { get; set; }

        [Input("pipelineTask")]
        public Input<Inputs.JobTaskPipelineTaskArgs>? PipelineTask { get; set; }

        [Input("pythonWheelTask")]
        public Input<Inputs.JobTaskPythonWheelTaskArgs>? PythonWheelTask { get; set; }

        [Input("retryOnTimeout")]
        public Input<bool>? RetryOnTimeout { get; set; }

        [Input("sparkJarTask")]
        public Input<Inputs.JobTaskSparkJarTaskArgs>? SparkJarTask { get; set; }

        [Input("sparkPythonTask")]
        public Input<Inputs.JobTaskSparkPythonTaskArgs>? SparkPythonTask { get; set; }

        [Input("sparkSubmitTask")]
        public Input<Inputs.JobTaskSparkSubmitTaskArgs>? SparkSubmitTask { get; set; }

        [Input("sqlTask")]
        public Input<Inputs.JobTaskSqlTaskArgs>? SqlTask { get; set; }

        [Input("taskKey")]
        public Input<string>? TaskKey { get; set; }

        [Input("timeoutSeconds")]
        public Input<int>? TimeoutSeconds { get; set; }

        public JobTaskArgs()
        {
        }
    }
}
