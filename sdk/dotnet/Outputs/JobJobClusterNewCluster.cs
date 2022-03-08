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
    public sealed class JobJobClusterNewCluster
    {
        public readonly Outputs.JobJobClusterNewClusterAutoscale? Autoscale;
        public readonly int? AutoterminationMinutes;
        public readonly Outputs.JobJobClusterNewClusterAwsAttributes? AwsAttributes;
        public readonly Outputs.JobJobClusterNewClusterAzureAttributes? AzureAttributes;
        public readonly string? ClusterId;
        public readonly Outputs.JobJobClusterNewClusterClusterLogConf? ClusterLogConf;
        public readonly string? ClusterName;
        public readonly ImmutableDictionary<string, object>? CustomTags;
        public readonly string? DataSecurityMode;
        public readonly Outputs.JobJobClusterNewClusterDockerImage? DockerImage;
        public readonly string? DriverInstancePoolId;
        public readonly string? DriverNodeTypeId;
        public readonly bool? EnableElasticDisk;
        public readonly bool? EnableLocalDiskEncryption;
        public readonly Outputs.JobJobClusterNewClusterGcpAttributes? GcpAttributes;
        public readonly string? IdempotencyToken;
        public readonly ImmutableArray<Outputs.JobJobClusterNewClusterInitScript> InitScripts;
        public readonly string? InstancePoolId;
        public readonly string? NodeTypeId;
        public readonly int NumWorkers;
        public readonly string? PolicyId;
        public readonly string? SingleUserName;
        public readonly ImmutableDictionary<string, object>? SparkConf;
        public readonly ImmutableDictionary<string, object>? SparkEnvVars;
        public readonly string SparkVersion;
        public readonly ImmutableArray<string> SshPublicKeys;

        [OutputConstructor]
        private JobJobClusterNewCluster(
            Outputs.JobJobClusterNewClusterAutoscale? autoscale,

            int? autoterminationMinutes,

            Outputs.JobJobClusterNewClusterAwsAttributes? awsAttributes,

            Outputs.JobJobClusterNewClusterAzureAttributes? azureAttributes,

            string? clusterId,

            Outputs.JobJobClusterNewClusterClusterLogConf? clusterLogConf,

            string? clusterName,

            ImmutableDictionary<string, object>? customTags,

            string? dataSecurityMode,

            Outputs.JobJobClusterNewClusterDockerImage? dockerImage,

            string? driverInstancePoolId,

            string? driverNodeTypeId,

            bool? enableElasticDisk,

            bool? enableLocalDiskEncryption,

            Outputs.JobJobClusterNewClusterGcpAttributes? gcpAttributes,

            string? idempotencyToken,

            ImmutableArray<Outputs.JobJobClusterNewClusterInitScript> initScripts,

            string? instancePoolId,

            string? nodeTypeId,

            int numWorkers,

            string? policyId,

            string? singleUserName,

            ImmutableDictionary<string, object>? sparkConf,

            ImmutableDictionary<string, object>? sparkEnvVars,

            string sparkVersion,

            ImmutableArray<string> sshPublicKeys)
        {
            Autoscale = autoscale;
            AutoterminationMinutes = autoterminationMinutes;
            AwsAttributes = awsAttributes;
            AzureAttributes = azureAttributes;
            ClusterId = clusterId;
            ClusterLogConf = clusterLogConf;
            ClusterName = clusterName;
            CustomTags = customTags;
            DataSecurityMode = dataSecurityMode;
            DockerImage = dockerImage;
            DriverInstancePoolId = driverInstancePoolId;
            DriverNodeTypeId = driverNodeTypeId;
            EnableElasticDisk = enableElasticDisk;
            EnableLocalDiskEncryption = enableLocalDiskEncryption;
            GcpAttributes = gcpAttributes;
            IdempotencyToken = idempotencyToken;
            InitScripts = initScripts;
            InstancePoolId = instancePoolId;
            NodeTypeId = nodeTypeId;
            NumWorkers = numWorkers;
            PolicyId = policyId;
            SingleUserName = singleUserName;
            SparkConf = sparkConf;
            SparkEnvVars = sparkEnvVars;
            SparkVersion = sparkVersion;
            SshPublicKeys = sshPublicKeys;
        }
    }
}
