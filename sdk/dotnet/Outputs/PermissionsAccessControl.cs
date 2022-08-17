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
    public sealed class PermissionsAccessControl
    {
        /// <summary>
        /// name of the group. We recommend setting permissions on groups.
        /// </summary>
        public readonly string? GroupName;
        /// <summary>
        /// permission level according to specific resource. See examples above for the reference.
        /// </summary>
        public readonly string PermissionLevel;
        /// <summary>
        /// Application ID of the service_principal.
        /// </summary>
        public readonly string? ServicePrincipalName;
        /// <summary>
        /// name of the user.
        /// </summary>
        public readonly string? UserName;

        [OutputConstructor]
        private PermissionsAccessControl(
            string? groupName,

            string permissionLevel,

            string? servicePrincipalName,

            string? userName)
        {
            GroupName = groupName;
            PermissionLevel = permissionLevel;
            ServicePrincipalName = servicePrincipalName;
            UserName = userName;
        }
    }
}
