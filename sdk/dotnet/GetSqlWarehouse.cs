// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    public static class GetSqlWarehouse
    {
        /// <summary>
        /// ## Related Resources
        /// 
        /// The following resources are often used in the same context:
        /// 
        /// * End to end workspace management guide.
        /// * databricks.InstanceProfile to manage AWS EC2 instance profiles that users can launch databricks.Cluster and access data, like databricks_mount.
        /// * databricks.SqlDashboard to manage Databricks SQL [Dashboards](https://docs.databricks.com/sql/user/dashboards/index.html).
        /// * databricks.SqlGlobalConfig to configure the security policy, databricks_instance_profile, and [data access properties](https://docs.databricks.com/sql/admin/data-access-configuration.html) for all databricks.getSqlWarehouse of workspace.
        /// * databricks.SqlPermissions to manage data object access control lists in Databricks workspaces for things like tables, views, databases, and [more](https://docs.databricks.com/security/access-control/table-acls/object-privileges.html).
        /// </summary>
        public static Task<GetSqlWarehouseResult> InvokeAsync(GetSqlWarehouseArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSqlWarehouseResult>("databricks:index/getSqlWarehouse:getSqlWarehouse", args ?? new GetSqlWarehouseArgs(), options.WithDefaults());

        /// <summary>
        /// ## Related Resources
        /// 
        /// The following resources are often used in the same context:
        /// 
        /// * End to end workspace management guide.
        /// * databricks.InstanceProfile to manage AWS EC2 instance profiles that users can launch databricks.Cluster and access data, like databricks_mount.
        /// * databricks.SqlDashboard to manage Databricks SQL [Dashboards](https://docs.databricks.com/sql/user/dashboards/index.html).
        /// * databricks.SqlGlobalConfig to configure the security policy, databricks_instance_profile, and [data access properties](https://docs.databricks.com/sql/admin/data-access-configuration.html) for all databricks.getSqlWarehouse of workspace.
        /// * databricks.SqlPermissions to manage data object access control lists in Databricks workspaces for things like tables, views, databases, and [more](https://docs.databricks.com/security/access-control/table-acls/object-privileges.html).
        /// </summary>
        public static Output<GetSqlWarehouseResult> Invoke(GetSqlWarehouseInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetSqlWarehouseResult>("databricks:index/getSqlWarehouse:getSqlWarehouse", args ?? new GetSqlWarehouseInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSqlWarehouseArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Time in minutes until an idle SQL warehouse terminates all clusters and stops.
        /// </summary>
        [Input("autoStopMins")]
        public int? AutoStopMins { get; set; }

        [Input("channel")]
        public Inputs.GetSqlWarehouseChannelArgs? Channel { get; set; }

        /// <summary>
        /// The size of the clusters allocated to the warehouse: "2X-Small", "X-Small", "Small", "Medium", "Large", "X-Large", "2X-Large", "3X-Large", "4X-Large".
        /// </summary>
        [Input("clusterSize")]
        public string? ClusterSize { get; set; }

        /// <summary>
        /// ID of the data source for this warehouse. This is used to bind an Databricks SQL query to an warehouse.
        /// </summary>
        [Input("dataSourceId")]
        public string? DataSourceId { get; set; }

        /// <summary>
        /// Whether to enable [Photon](https://databricks.com/product/delta-engine).
        /// </summary>
        [Input("enablePhoton")]
        public bool? EnablePhoton { get; set; }

        /// <summary>
        /// Whether this SQL warehouse is a Serverless warehouse. To use a Serverless SQL warehouse, you must enable Serverless SQL warehouses for the workspace.
        /// * `channel` block, consisting of following fields:
        /// </summary>
        [Input("enableServerlessCompute")]
        public bool? EnableServerlessCompute { get; set; }

        /// <summary>
        /// The id of the SQL warehouse
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        [Input("instanceProfileArn")]
        public string? InstanceProfileArn { get; set; }

        /// <summary>
        /// JDBC connection string.
        /// </summary>
        [Input("jdbcUrl")]
        public string? JdbcUrl { get; set; }

        /// <summary>
        /// Maximum number of clusters available when a SQL warehouse is running.
        /// </summary>
        [Input("maxNumClusters")]
        public int? MaxNumClusters { get; set; }

        /// <summary>
        /// Minimum number of clusters available when a SQL warehouse is running.
        /// </summary>
        [Input("minNumClusters")]
        public int? MinNumClusters { get; set; }

        /// <summary>
        /// Name of the Databricks SQL release channel. Possible values are: `CHANNEL_NAME_PREVIEW` and `CHANNEL_NAME_CURRENT`. Default is `CHANNEL_NAME_CURRENT`.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        [Input("numClusters")]
        public int? NumClusters { get; set; }

        /// <summary>
        /// ODBC connection params: `odbc_params.hostname`, `odbc_params.path`, `odbc_params.protocol`, and `odbc_params.port`.
        /// </summary>
        [Input("odbcParams")]
        public Inputs.GetSqlWarehouseOdbcParamsArgs? OdbcParams { get; set; }

        /// <summary>
        /// The spot policy to use for allocating instances to clusters: `COST_OPTIMIZED` or `RELIABILITY_OPTIMIZED`.
        /// </summary>
        [Input("spotInstancePolicy")]
        public string? SpotInstancePolicy { get; set; }

        [Input("state")]
        public string? State { get; set; }

        /// <summary>
        /// Databricks tags all warehouse resources with these tags.
        /// </summary>
        [Input("tags")]
        public Inputs.GetSqlWarehouseTagsArgs? Tags { get; set; }

        public GetSqlWarehouseArgs()
        {
        }
    }

    public sealed class GetSqlWarehouseInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Time in minutes until an idle SQL warehouse terminates all clusters and stops.
        /// </summary>
        [Input("autoStopMins")]
        public Input<int>? AutoStopMins { get; set; }

        [Input("channel")]
        public Input<Inputs.GetSqlWarehouseChannelInputArgs>? Channel { get; set; }

        /// <summary>
        /// The size of the clusters allocated to the warehouse: "2X-Small", "X-Small", "Small", "Medium", "Large", "X-Large", "2X-Large", "3X-Large", "4X-Large".
        /// </summary>
        [Input("clusterSize")]
        public Input<string>? ClusterSize { get; set; }

        /// <summary>
        /// ID of the data source for this warehouse. This is used to bind an Databricks SQL query to an warehouse.
        /// </summary>
        [Input("dataSourceId")]
        public Input<string>? DataSourceId { get; set; }

        /// <summary>
        /// Whether to enable [Photon](https://databricks.com/product/delta-engine).
        /// </summary>
        [Input("enablePhoton")]
        public Input<bool>? EnablePhoton { get; set; }

        /// <summary>
        /// Whether this SQL warehouse is a Serverless warehouse. To use a Serverless SQL warehouse, you must enable Serverless SQL warehouses for the workspace.
        /// * `channel` block, consisting of following fields:
        /// </summary>
        [Input("enableServerlessCompute")]
        public Input<bool>? EnableServerlessCompute { get; set; }

        /// <summary>
        /// The id of the SQL warehouse
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("instanceProfileArn")]
        public Input<string>? InstanceProfileArn { get; set; }

        /// <summary>
        /// JDBC connection string.
        /// </summary>
        [Input("jdbcUrl")]
        public Input<string>? JdbcUrl { get; set; }

        /// <summary>
        /// Maximum number of clusters available when a SQL warehouse is running.
        /// </summary>
        [Input("maxNumClusters")]
        public Input<int>? MaxNumClusters { get; set; }

        /// <summary>
        /// Minimum number of clusters available when a SQL warehouse is running.
        /// </summary>
        [Input("minNumClusters")]
        public Input<int>? MinNumClusters { get; set; }

        /// <summary>
        /// Name of the Databricks SQL release channel. Possible values are: `CHANNEL_NAME_PREVIEW` and `CHANNEL_NAME_CURRENT`. Default is `CHANNEL_NAME_CURRENT`.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("numClusters")]
        public Input<int>? NumClusters { get; set; }

        /// <summary>
        /// ODBC connection params: `odbc_params.hostname`, `odbc_params.path`, `odbc_params.protocol`, and `odbc_params.port`.
        /// </summary>
        [Input("odbcParams")]
        public Input<Inputs.GetSqlWarehouseOdbcParamsInputArgs>? OdbcParams { get; set; }

        /// <summary>
        /// The spot policy to use for allocating instances to clusters: `COST_OPTIMIZED` or `RELIABILITY_OPTIMIZED`.
        /// </summary>
        [Input("spotInstancePolicy")]
        public Input<string>? SpotInstancePolicy { get; set; }

        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// Databricks tags all warehouse resources with these tags.
        /// </summary>
        [Input("tags")]
        public Input<Inputs.GetSqlWarehouseTagsInputArgs>? Tags { get; set; }

        public GetSqlWarehouseInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetSqlWarehouseResult
    {
        /// <summary>
        /// Time in minutes until an idle SQL warehouse terminates all clusters and stops.
        /// </summary>
        public readonly int AutoStopMins;
        public readonly Outputs.GetSqlWarehouseChannelResult Channel;
        /// <summary>
        /// The size of the clusters allocated to the warehouse: "2X-Small", "X-Small", "Small", "Medium", "Large", "X-Large", "2X-Large", "3X-Large", "4X-Large".
        /// </summary>
        public readonly string ClusterSize;
        /// <summary>
        /// ID of the data source for this warehouse. This is used to bind an Databricks SQL query to an warehouse.
        /// </summary>
        public readonly string DataSourceId;
        /// <summary>
        /// Whether to enable [Photon](https://databricks.com/product/delta-engine).
        /// </summary>
        public readonly bool EnablePhoton;
        /// <summary>
        /// Whether this SQL warehouse is a Serverless warehouse. To use a Serverless SQL warehouse, you must enable Serverless SQL warehouses for the workspace.
        /// * `channel` block, consisting of following fields:
        /// </summary>
        public readonly bool EnableServerlessCompute;
        public readonly string Id;
        public readonly string InstanceProfileArn;
        /// <summary>
        /// JDBC connection string.
        /// </summary>
        public readonly string JdbcUrl;
        /// <summary>
        /// Maximum number of clusters available when a SQL warehouse is running.
        /// </summary>
        public readonly int MaxNumClusters;
        /// <summary>
        /// Minimum number of clusters available when a SQL warehouse is running.
        /// </summary>
        public readonly int MinNumClusters;
        /// <summary>
        /// Name of the Databricks SQL release channel. Possible values are: `CHANNEL_NAME_PREVIEW` and `CHANNEL_NAME_CURRENT`. Default is `CHANNEL_NAME_CURRENT`.
        /// </summary>
        public readonly string Name;
        public readonly int NumClusters;
        /// <summary>
        /// ODBC connection params: `odbc_params.hostname`, `odbc_params.path`, `odbc_params.protocol`, and `odbc_params.port`.
        /// </summary>
        public readonly Outputs.GetSqlWarehouseOdbcParamsResult OdbcParams;
        /// <summary>
        /// The spot policy to use for allocating instances to clusters: `COST_OPTIMIZED` or `RELIABILITY_OPTIMIZED`.
        /// </summary>
        public readonly string SpotInstancePolicy;
        public readonly string State;
        /// <summary>
        /// Databricks tags all warehouse resources with these tags.
        /// </summary>
        public readonly Outputs.GetSqlWarehouseTagsResult Tags;

        [OutputConstructor]
        private GetSqlWarehouseResult(
            int autoStopMins,

            Outputs.GetSqlWarehouseChannelResult channel,

            string clusterSize,

            string dataSourceId,

            bool enablePhoton,

            bool enableServerlessCompute,

            string id,

            string instanceProfileArn,

            string jdbcUrl,

            int maxNumClusters,

            int minNumClusters,

            string name,

            int numClusters,

            Outputs.GetSqlWarehouseOdbcParamsResult odbcParams,

            string spotInstancePolicy,

            string state,

            Outputs.GetSqlWarehouseTagsResult tags)
        {
            AutoStopMins = autoStopMins;
            Channel = channel;
            ClusterSize = clusterSize;
            DataSourceId = dataSourceId;
            EnablePhoton = enablePhoton;
            EnableServerlessCompute = enableServerlessCompute;
            Id = id;
            InstanceProfileArn = instanceProfileArn;
            JdbcUrl = jdbcUrl;
            MaxNumClusters = maxNumClusters;
            MinNumClusters = minNumClusters;
            Name = name;
            NumClusters = numClusters;
            OdbcParams = odbcParams;
            SpotInstancePolicy = spotInstancePolicy;
            State = state;
            Tags = tags;
        }
    }
}
