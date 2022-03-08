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
    public sealed class JobNewClusterInitScriptS3
    {
        public readonly string? CannedAcl;
        public readonly string Destination;
        public readonly bool? EnableEncryption;
        public readonly string? EncryptionType;
        public readonly string? Endpoint;
        public readonly string? KmsKey;
        public readonly string? Region;

        [OutputConstructor]
        private JobNewClusterInitScriptS3(
            string? cannedAcl,

            string destination,

            bool? enableEncryption,

            string? encryptionType,

            string? endpoint,

            string? kmsKey,

            string? region)
        {
            CannedAcl = cannedAcl;
            Destination = destination;
            EnableEncryption = enableEncryption;
            EncryptionType = encryptionType;
            Endpoint = endpoint;
            KmsKey = kmsKey;
            Region = region;
        }
    }
}
