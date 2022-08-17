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
    public sealed class SqlQueryParameterQueryMultiple
    {
        public readonly string Prefix;
        public readonly string Separator;
        public readonly string Suffix;

        [OutputConstructor]
        private SqlQueryParameterQueryMultiple(
            string prefix,

            string separator,

            string suffix)
        {
            Prefix = prefix;
            Separator = separator;
            Suffix = suffix;
        }
    }
}
