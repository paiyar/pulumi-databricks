// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class JobTaskSqlTaskGetArgs : Pulumi.ResourceArgs
    {
        [Input("alert")]
        public Input<Inputs.JobTaskSqlTaskAlertGetArgs>? Alert { get; set; }

        [Input("dashboard")]
        public Input<Inputs.JobTaskSqlTaskDashboardGetArgs>? Dashboard { get; set; }

        [Input("parameters")]
        private InputMap<object>? _parameters;

        /// <summary>
        /// Parameters for the task
        /// </summary>
        public InputMap<object> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<object>());
            set => _parameters = value;
        }

        [Input("query")]
        public Input<Inputs.JobTaskSqlTaskQueryGetArgs>? Query { get; set; }

        [Input("warehouseId")]
        public Input<string>? WarehouseId { get; set; }

        public JobTaskSqlTaskGetArgs()
        {
        }
    }
}
