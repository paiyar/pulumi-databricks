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
    public sealed class SqlPermissionsPrivilegeAssignment
    {
        /// <summary>
        /// `display_name` of databricks.Group or databricks_user.
        /// </summary>
        public readonly string Principal;
        /// <summary>
        /// set of available privilege names in upper case.
        /// </summary>
        public readonly ImmutableArray<string> Privileges;

        [OutputConstructor]
        private SqlPermissionsPrivilegeAssignment(
            string principal,

            ImmutableArray<string> privileges)
        {
            Principal = principal;
            Privileges = privileges;
        }
    }
}
