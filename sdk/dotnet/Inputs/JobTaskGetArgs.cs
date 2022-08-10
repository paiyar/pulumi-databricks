// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class JobTaskGetArgs : Pulumi.ResourceArgs
    {
        [Input("dbtTask")]
        public Input<Inputs.JobTaskDbtTaskGetArgs>? DbtTask { get; set; }

        [Input("dependsOns")]
        private InputList<Inputs.JobTaskDependsOnGetArgs>? _dependsOns;
        public InputList<Inputs.JobTaskDependsOnGetArgs> DependsOns
        {
            get => _dependsOns ?? (_dependsOns = new InputList<Inputs.JobTaskDependsOnGetArgs>());
            set => _dependsOns = value;
        }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("emailNotifications")]
        public Input<Inputs.JobTaskEmailNotificationsGetArgs>? EmailNotifications { get; set; }

        [Input("existingClusterId")]
        public Input<string>? ExistingClusterId { get; set; }

        [Input("jobClusterKey")]
        public Input<string>? JobClusterKey { get; set; }

        [Input("libraries")]
        private InputList<Inputs.JobTaskLibraryGetArgs>? _libraries;
        public InputList<Inputs.JobTaskLibraryGetArgs> Libraries
        {
            get => _libraries ?? (_libraries = new InputList<Inputs.JobTaskLibraryGetArgs>());
            set => _libraries = value;
        }

        [Input("maxRetries")]
        public Input<int>? MaxRetries { get; set; }

        [Input("minRetryIntervalMillis")]
        public Input<int>? MinRetryIntervalMillis { get; set; }

        [Input("newCluster")]
        public Input<Inputs.JobTaskNewClusterGetArgs>? NewCluster { get; set; }

        [Input("notebookTask")]
        public Input<Inputs.JobTaskNotebookTaskGetArgs>? NotebookTask { get; set; }

        [Input("pipelineTask")]
        public Input<Inputs.JobTaskPipelineTaskGetArgs>? PipelineTask { get; set; }

        [Input("pythonWheelTask")]
        public Input<Inputs.JobTaskPythonWheelTaskGetArgs>? PythonWheelTask { get; set; }

        [Input("retryOnTimeout")]
        public Input<bool>? RetryOnTimeout { get; set; }

        [Input("sparkJarTask")]
        public Input<Inputs.JobTaskSparkJarTaskGetArgs>? SparkJarTask { get; set; }

        [Input("sparkPythonTask")]
        public Input<Inputs.JobTaskSparkPythonTaskGetArgs>? SparkPythonTask { get; set; }

        [Input("sparkSubmitTask")]
        public Input<Inputs.JobTaskSparkSubmitTaskGetArgs>? SparkSubmitTask { get; set; }

        [Input("sqlTask")]
        public Input<Inputs.JobTaskSqlTaskGetArgs>? SqlTask { get; set; }

        [Input("taskKey")]
        public Input<string>? TaskKey { get; set; }

        [Input("timeoutSeconds")]
        public Input<int>? TimeoutSeconds { get; set; }

        public JobTaskGetArgs()
        {
        }
    }
}
