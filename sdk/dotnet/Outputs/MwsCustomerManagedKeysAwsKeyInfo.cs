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
    public sealed class MwsCustomerManagedKeysAwsKeyInfo
    {
        public readonly string KeyAlias;
        public readonly string KeyArn;
        public readonly string? KeyRegion;

        [OutputConstructor]
        private MwsCustomerManagedKeysAwsKeyInfo(
            string keyAlias,

            string keyArn,

            string? keyRegion)
        {
            KeyAlias = keyAlias;
            KeyArn = keyArn;
            KeyRegion = keyRegion;
        }
    }
}
