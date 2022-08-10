// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    [DatabricksResourceType("databricks:index/job:Job")]
    public partial class Job : Pulumi.CustomResource
    {
        [Output("alwaysRunning")]
        public Output<bool?> AlwaysRunning { get; private set; } = null!;

        [Output("emailNotifications")]
        public Output<Outputs.JobEmailNotifications?> EmailNotifications { get; private set; } = null!;

        [Output("existingClusterId")]
        public Output<string?> ExistingClusterId { get; private set; } = null!;

        [Output("format")]
        public Output<string> Format { get; private set; } = null!;

        [Output("gitSource")]
        public Output<Outputs.JobGitSource?> GitSource { get; private set; } = null!;

        [Output("jobClusters")]
        public Output<ImmutableArray<Outputs.JobJobCluster>> JobClusters { get; private set; } = null!;

        [Output("libraries")]
        public Output<ImmutableArray<Outputs.JobLibrary>> Libraries { get; private set; } = null!;

        [Output("maxConcurrentRuns")]
        public Output<int?> MaxConcurrentRuns { get; private set; } = null!;

        [Output("maxRetries")]
        public Output<int?> MaxRetries { get; private set; } = null!;

        [Output("minRetryIntervalMillis")]
        public Output<int?> MinRetryIntervalMillis { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("newCluster")]
        public Output<Outputs.JobNewCluster?> NewCluster { get; private set; } = null!;

        [Output("notebookTask")]
        public Output<Outputs.JobNotebookTask?> NotebookTask { get; private set; } = null!;

        [Output("pipelineTask")]
        public Output<Outputs.JobPipelineTask?> PipelineTask { get; private set; } = null!;

        [Output("pythonWheelTask")]
        public Output<Outputs.JobPythonWheelTask?> PythonWheelTask { get; private set; } = null!;

        [Output("retryOnTimeout")]
        public Output<bool?> RetryOnTimeout { get; private set; } = null!;

        [Output("schedule")]
        public Output<Outputs.JobSchedule?> Schedule { get; private set; } = null!;

        [Output("sparkJarTask")]
        public Output<Outputs.JobSparkJarTask?> SparkJarTask { get; private set; } = null!;

        [Output("sparkPythonTask")]
        public Output<Outputs.JobSparkPythonTask?> SparkPythonTask { get; private set; } = null!;

        [Output("sparkSubmitTask")]
        public Output<Outputs.JobSparkSubmitTask?> SparkSubmitTask { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        [Output("tasks")]
        public Output<ImmutableArray<Outputs.JobTask>> Tasks { get; private set; } = null!;

        [Output("timeoutSeconds")]
        public Output<int?> TimeoutSeconds { get; private set; } = null!;

        [Output("url")]
        public Output<string> Url { get; private set; } = null!;


        /// <summary>
        /// Create a Job resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Job(string name, JobArgs? args = null, CustomResourceOptions? options = null)
            : base("databricks:index/job:Job", name, args ?? new JobArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Job(string name, Input<string> id, JobState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/job:Job", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Job resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Job Get(string name, Input<string> id, JobState? state = null, CustomResourceOptions? options = null)
        {
            return new Job(name, id, state, options);
        }
    }

    public sealed class JobArgs : Pulumi.ResourceArgs
    {
        [Input("alwaysRunning")]
        public Input<bool>? AlwaysRunning { get; set; }

        [Input("emailNotifications")]
        public Input<Inputs.JobEmailNotificationsArgs>? EmailNotifications { get; set; }

        [Input("existingClusterId")]
        public Input<string>? ExistingClusterId { get; set; }

        [Input("format")]
        public Input<string>? Format { get; set; }

        [Input("gitSource")]
        public Input<Inputs.JobGitSourceArgs>? GitSource { get; set; }

        [Input("jobClusters")]
        private InputList<Inputs.JobJobClusterArgs>? _jobClusters;
        public InputList<Inputs.JobJobClusterArgs> JobClusters
        {
            get => _jobClusters ?? (_jobClusters = new InputList<Inputs.JobJobClusterArgs>());
            set => _jobClusters = value;
        }

        [Input("libraries")]
        private InputList<Inputs.JobLibraryArgs>? _libraries;
        public InputList<Inputs.JobLibraryArgs> Libraries
        {
            get => _libraries ?? (_libraries = new InputList<Inputs.JobLibraryArgs>());
            set => _libraries = value;
        }

        [Input("maxConcurrentRuns")]
        public Input<int>? MaxConcurrentRuns { get; set; }

        [Input("maxRetries")]
        public Input<int>? MaxRetries { get; set; }

        [Input("minRetryIntervalMillis")]
        public Input<int>? MinRetryIntervalMillis { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("newCluster")]
        public Input<Inputs.JobNewClusterArgs>? NewCluster { get; set; }

        [Input("notebookTask")]
        public Input<Inputs.JobNotebookTaskArgs>? NotebookTask { get; set; }

        [Input("pipelineTask")]
        public Input<Inputs.JobPipelineTaskArgs>? PipelineTask { get; set; }

        [Input("pythonWheelTask")]
        public Input<Inputs.JobPythonWheelTaskArgs>? PythonWheelTask { get; set; }

        [Input("retryOnTimeout")]
        public Input<bool>? RetryOnTimeout { get; set; }

        [Input("schedule")]
        public Input<Inputs.JobScheduleArgs>? Schedule { get; set; }

        [Input("sparkJarTask")]
        public Input<Inputs.JobSparkJarTaskArgs>? SparkJarTask { get; set; }

        [Input("sparkPythonTask")]
        public Input<Inputs.JobSparkPythonTaskArgs>? SparkPythonTask { get; set; }

        [Input("sparkSubmitTask")]
        public Input<Inputs.JobSparkSubmitTaskArgs>? SparkSubmitTask { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        [Input("tasks")]
        private InputList<Inputs.JobTaskArgs>? _tasks;
        public InputList<Inputs.JobTaskArgs> Tasks
        {
            get => _tasks ?? (_tasks = new InputList<Inputs.JobTaskArgs>());
            set => _tasks = value;
        }

        [Input("timeoutSeconds")]
        public Input<int>? TimeoutSeconds { get; set; }

        public JobArgs()
        {
        }
    }

    public sealed class JobState : Pulumi.ResourceArgs
    {
        [Input("alwaysRunning")]
        public Input<bool>? AlwaysRunning { get; set; }

        [Input("emailNotifications")]
        public Input<Inputs.JobEmailNotificationsGetArgs>? EmailNotifications { get; set; }

        [Input("existingClusterId")]
        public Input<string>? ExistingClusterId { get; set; }

        [Input("format")]
        public Input<string>? Format { get; set; }

        [Input("gitSource")]
        public Input<Inputs.JobGitSourceGetArgs>? GitSource { get; set; }

        [Input("jobClusters")]
        private InputList<Inputs.JobJobClusterGetArgs>? _jobClusters;
        public InputList<Inputs.JobJobClusterGetArgs> JobClusters
        {
            get => _jobClusters ?? (_jobClusters = new InputList<Inputs.JobJobClusterGetArgs>());
            set => _jobClusters = value;
        }

        [Input("libraries")]
        private InputList<Inputs.JobLibraryGetArgs>? _libraries;
        public InputList<Inputs.JobLibraryGetArgs> Libraries
        {
            get => _libraries ?? (_libraries = new InputList<Inputs.JobLibraryGetArgs>());
            set => _libraries = value;
        }

        [Input("maxConcurrentRuns")]
        public Input<int>? MaxConcurrentRuns { get; set; }

        [Input("maxRetries")]
        public Input<int>? MaxRetries { get; set; }

        [Input("minRetryIntervalMillis")]
        public Input<int>? MinRetryIntervalMillis { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("newCluster")]
        public Input<Inputs.JobNewClusterGetArgs>? NewCluster { get; set; }

        [Input("notebookTask")]
        public Input<Inputs.JobNotebookTaskGetArgs>? NotebookTask { get; set; }

        [Input("pipelineTask")]
        public Input<Inputs.JobPipelineTaskGetArgs>? PipelineTask { get; set; }

        [Input("pythonWheelTask")]
        public Input<Inputs.JobPythonWheelTaskGetArgs>? PythonWheelTask { get; set; }

        [Input("retryOnTimeout")]
        public Input<bool>? RetryOnTimeout { get; set; }

        [Input("schedule")]
        public Input<Inputs.JobScheduleGetArgs>? Schedule { get; set; }

        [Input("sparkJarTask")]
        public Input<Inputs.JobSparkJarTaskGetArgs>? SparkJarTask { get; set; }

        [Input("sparkPythonTask")]
        public Input<Inputs.JobSparkPythonTaskGetArgs>? SparkPythonTask { get; set; }

        [Input("sparkSubmitTask")]
        public Input<Inputs.JobSparkSubmitTaskGetArgs>? SparkSubmitTask { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        [Input("tasks")]
        private InputList<Inputs.JobTaskGetArgs>? _tasks;
        public InputList<Inputs.JobTaskGetArgs> Tasks
        {
            get => _tasks ?? (_tasks = new InputList<Inputs.JobTaskGetArgs>());
            set => _tasks = value;
        }

        [Input("timeoutSeconds")]
        public Input<int>? TimeoutSeconds { get; set; }

        [Input("url")]
        public Input<string>? Url { get; set; }

        public JobState()
        {
        }
    }
}
