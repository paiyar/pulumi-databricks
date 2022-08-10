// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class JobScheduleArgs : Pulumi.ResourceArgs
    {
        [Input("pauseStatus")]
        public Input<string>? PauseStatus { get; set; }

        [Input("quartzCronExpression", required: true)]
        public Input<string> QuartzCronExpression { get; set; } = null!;

        [Input("timezoneId", required: true)]
        public Input<string> TimezoneId { get; set; } = null!;

        public JobScheduleArgs()
        {
        }
    }
}
