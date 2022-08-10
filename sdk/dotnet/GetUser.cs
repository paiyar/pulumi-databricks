// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    public static class GetUser
    {
        public static Task<GetUserResult> InvokeAsync(GetUserArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetUserResult>("databricks:index/getUser:getUser", args ?? new GetUserArgs(), options.WithDefaults());

        public static Output<GetUserResult> Invoke(GetUserInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetUserResult>("databricks:index/getUser:getUser", args ?? new GetUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserArgs : Pulumi.InvokeArgs
    {
        [Input("userId")]
        public string? UserId { get; set; }

        [Input("userName")]
        public string? UserName { get; set; }

        public GetUserArgs()
        {
        }
    }

    public sealed class GetUserInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("userId")]
        public Input<string>? UserId { get; set; }

        [Input("userName")]
        public Input<string>? UserName { get; set; }

        public GetUserInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetUserResult
    {
        public readonly string Alphanumeric;
        public readonly string ApplicationId;
        public readonly string DisplayName;
        public readonly string ExternalId;
        public readonly string Home;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Repos;
        public readonly string? UserId;
        public readonly string? UserName;

        [OutputConstructor]
        private GetUserResult(
            string alphanumeric,

            string applicationId,

            string displayName,

            string externalId,

            string home,

            string id,

            string repos,

            string? userId,

            string? userName)
        {
            Alphanumeric = alphanumeric;
            ApplicationId = applicationId;
            DisplayName = displayName;
            ExternalId = externalId;
            Home = home;
            Id = id;
            Repos = repos;
            UserId = userId;
            UserName = userName;
        }
    }
}
