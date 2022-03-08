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
    public sealed class SqlQueryScheduleContinuous
    {
        public readonly int IntervalSeconds;
        public readonly string? UntilDate;

        [OutputConstructor]
        private SqlQueryScheduleContinuous(
            int intervalSeconds,

            string? untilDate)
        {
            IntervalSeconds = intervalSeconds;
            UntilDate = untilDate;
        }
    }
}
