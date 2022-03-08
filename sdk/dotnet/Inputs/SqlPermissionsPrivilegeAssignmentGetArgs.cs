// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Inputs
{

    public sealed class SqlPermissionsPrivilegeAssignmentGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// `display_name` of databricks.Group or databricks_user.
        /// </summary>
        [Input("principal", required: true)]
        public Input<string> Principal { get; set; } = null!;

        [Input("privileges", required: true)]
        private InputList<string>? _privileges;

        /// <summary>
        /// set of available privilege names in upper case.
        /// </summary>
        public InputList<string> Privileges
        {
            get => _privileges ?? (_privileges = new InputList<string>());
            set => _privileges = value;
        }

        public SqlPermissionsPrivilegeAssignmentGetArgs()
        {
        }
    }
}
