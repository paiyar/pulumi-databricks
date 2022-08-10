// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class GetClusterClusterInfoArgs : Pulumi.InvokeArgs
    {
        [Input("autoscale")]
        public Inputs.GetClusterClusterInfoAutoscaleArgs? Autoscale { get; set; }

        [Input("autoterminationMinutes")]
        public int? AutoterminationMinutes { get; set; }

        [Input("awsAttributes")]
        public Inputs.GetClusterClusterInfoAwsAttributesArgs? AwsAttributes { get; set; }

        [Input("azureAttributes")]
        public Inputs.GetClusterClusterInfoAzureAttributesArgs? AzureAttributes { get; set; }

        [Input("clusterCores")]
        public double? ClusterCores { get; set; }

        [Input("clusterId")]
        public string? ClusterId { get; set; }

        [Input("clusterLogConf")]
        public Inputs.GetClusterClusterInfoClusterLogConfArgs? ClusterLogConf { get; set; }

        [Input("clusterLogStatus")]
        public Inputs.GetClusterClusterInfoClusterLogStatusArgs? ClusterLogStatus { get; set; }

        [Input("clusterMemoryMb")]
        public int? ClusterMemoryMb { get; set; }

        [Input("clusterName")]
        public string? ClusterName { get; set; }

        [Input("clusterSource")]
        public string? ClusterSource { get; set; }

        [Input("creatorUserName")]
        public string? CreatorUserName { get; set; }

        [Input("customTags")]
        private Dictionary<string, object>? _customTags;
        public Dictionary<string, object> CustomTags
        {
            get => _customTags ?? (_customTags = new Dictionary<string, object>());
            set => _customTags = value;
        }

        [Input("dataSecurityMode")]
        public string? DataSecurityMode { get; set; }

        [Input("defaultTags", required: true)]
        private Dictionary<string, object>? _defaultTags;
        public Dictionary<string, object> DefaultTags
        {
            get => _defaultTags ?? (_defaultTags = new Dictionary<string, object>());
            set => _defaultTags = value;
        }

        [Input("dockerImage")]
        public Inputs.GetClusterClusterInfoDockerImageArgs? DockerImage { get; set; }

        [Input("driver")]
        public Inputs.GetClusterClusterInfoDriverArgs? Driver { get; set; }

        [Input("driverInstancePoolId", required: true)]
        public string DriverInstancePoolId { get; set; } = null!;

        [Input("driverNodeTypeId")]
        public string? DriverNodeTypeId { get; set; }

        [Input("enableElasticDisk")]
        public bool? EnableElasticDisk { get; set; }

        [Input("enableLocalDiskEncryption")]
        public bool? EnableLocalDiskEncryption { get; set; }

        [Input("executors")]
        private List<Inputs.GetClusterClusterInfoExecutorArgs>? _executors;
        public List<Inputs.GetClusterClusterInfoExecutorArgs> Executors
        {
            get => _executors ?? (_executors = new List<Inputs.GetClusterClusterInfoExecutorArgs>());
            set => _executors = value;
        }

        [Input("gcpAttributes")]
        public Inputs.GetClusterClusterInfoGcpAttributesArgs? GcpAttributes { get; set; }

        [Input("initScripts")]
        private List<Inputs.GetClusterClusterInfoInitScriptArgs>? _initScripts;
        public List<Inputs.GetClusterClusterInfoInitScriptArgs> InitScripts
        {
            get => _initScripts ?? (_initScripts = new List<Inputs.GetClusterClusterInfoInitScriptArgs>());
            set => _initScripts = value;
        }

        [Input("instancePoolId")]
        public string? InstancePoolId { get; set; }

        [Input("jdbcPort")]
        public int? JdbcPort { get; set; }

        [Input("lastActivityTime")]
        public int? LastActivityTime { get; set; }

        [Input("lastStateLossTime")]
        public int? LastStateLossTime { get; set; }

        [Input("nodeTypeId")]
        public string? NodeTypeId { get; set; }

        [Input("numWorkers")]
        public int? NumWorkers { get; set; }

        [Input("policyId")]
        public string? PolicyId { get; set; }

        [Input("singleUserName")]
        public string? SingleUserName { get; set; }

        [Input("sparkConf")]
        private Dictionary<string, object>? _sparkConf;
        public Dictionary<string, object> SparkConf
        {
            get => _sparkConf ?? (_sparkConf = new Dictionary<string, object>());
            set => _sparkConf = value;
        }

        [Input("sparkContextId")]
        public int? SparkContextId { get; set; }

        [Input("sparkEnvVars")]
        private Dictionary<string, object>? _sparkEnvVars;
        public Dictionary<string, object> SparkEnvVars
        {
            get => _sparkEnvVars ?? (_sparkEnvVars = new Dictionary<string, object>());
            set => _sparkEnvVars = value;
        }

        [Input("sparkVersion", required: true)]
        public string SparkVersion { get; set; } = null!;

        [Input("sshPublicKeys")]
        private List<string>? _sshPublicKeys;
        public List<string> SshPublicKeys
        {
            get => _sshPublicKeys ?? (_sshPublicKeys = new List<string>());
            set => _sshPublicKeys = value;
        }

        [Input("startTime")]
        public int? StartTime { get; set; }

        [Input("state", required: true)]
        public string State { get; set; } = null!;

        [Input("stateMessage")]
        public string? StateMessage { get; set; }

        [Input("terminateTime")]
        public int? TerminateTime { get; set; }

        [Input("terminationReason")]
        public Inputs.GetClusterClusterInfoTerminationReasonArgs? TerminationReason { get; set; }

        public GetClusterClusterInfoArgs()
        {
        }
    }
}
