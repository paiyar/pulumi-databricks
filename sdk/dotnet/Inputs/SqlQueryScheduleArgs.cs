// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class SqlQueryScheduleArgs : global::Pulumi.ResourceArgs
    {
        [Input("continuous")]
        public Input<Inputs.SqlQueryScheduleContinuousArgs>? Continuous { get; set; }

        [Input("daily")]
        public Input<Inputs.SqlQueryScheduleDailyArgs>? Daily { get; set; }

        [Input("weekly")]
        public Input<Inputs.SqlQueryScheduleWeeklyArgs>? Weekly { get; set; }

        public SqlQueryScheduleArgs()
        {
        }
        public static new SqlQueryScheduleArgs Empty => new SqlQueryScheduleArgs();
    }
}
