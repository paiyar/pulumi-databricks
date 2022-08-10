// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    public static class GetCatalogs
    {
        public static Task<GetCatalogsResult> InvokeAsync(GetCatalogsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetCatalogsResult>("databricks:index/getCatalogs:getCatalogs", args ?? new GetCatalogsArgs(), options.WithDefaults());

        public static Output<GetCatalogsResult> Invoke(GetCatalogsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetCatalogsResult>("databricks:index/getCatalogs:getCatalogs", args ?? new GetCatalogsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCatalogsArgs : Pulumi.InvokeArgs
    {
        [Input("ids")]
        private List<string>? _ids;
        public List<string> Ids
        {
            get => _ids ?? (_ids = new List<string>());
            set => _ids = value;
        }

        public GetCatalogsArgs()
        {
        }
    }

    public sealed class GetCatalogsInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("ids")]
        private InputList<string>? _ids;
        public InputList<string> Ids
        {
            get => _ids ?? (_ids = new InputList<string>());
            set => _ids = value;
        }

        public GetCatalogsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetCatalogsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<string> Ids;

        [OutputConstructor]
        private GetCatalogsResult(
            string id,

            ImmutableArray<string> ids)
        {
            Id = id;
            Ids = ids;
        }
    }
}
