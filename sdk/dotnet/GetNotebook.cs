// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    public static class GetNotebook
    {
        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Databricks = Pulumi.Databricks;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var features = Databricks.GetNotebook.Invoke(new()
        ///     {
        ///         Format = "SOURCE",
        ///         Path = "/Production/Features",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetNotebookResult> InvokeAsync(GetNotebookArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNotebookResult>("databricks:index/getNotebook:getNotebook", args ?? new GetNotebookArgs(), options.WithDefaults());

        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Databricks = Pulumi.Databricks;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var features = Databricks.GetNotebook.Invoke(new()
        ///     {
        ///         Format = "SOURCE",
        ///         Path = "/Production/Features",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetNotebookResult> Invoke(GetNotebookInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetNotebookResult>("databricks:index/getNotebook:getNotebook", args ?? new GetNotebookInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNotebookArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Notebook format to export. Either `SOURCE`, `HTML`, `JUPYTER`, or `DBC`.
        /// </summary>
        [Input("format", required: true)]
        public string Format { get; set; } = null!;

        /// <summary>
        /// notebook language
        /// </summary>
        [Input("language")]
        public string? Language { get; set; }

        /// <summary>
        /// notebook object ID
        /// </summary>
        [Input("objectId")]
        public int? ObjectId { get; set; }

        /// <summary>
        /// notebook object type
        /// </summary>
        [Input("objectType")]
        public string? ObjectType { get; set; }

        /// <summary>
        /// Notebook path on the workspace
        /// </summary>
        [Input("path", required: true)]
        public string Path { get; set; } = null!;

        public GetNotebookArgs()
        {
        }
        public static new GetNotebookArgs Empty => new GetNotebookArgs();
    }

    public sealed class GetNotebookInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Notebook format to export. Either `SOURCE`, `HTML`, `JUPYTER`, or `DBC`.
        /// </summary>
        [Input("format", required: true)]
        public Input<string> Format { get; set; } = null!;

        /// <summary>
        /// notebook language
        /// </summary>
        [Input("language")]
        public Input<string>? Language { get; set; }

        /// <summary>
        /// notebook object ID
        /// </summary>
        [Input("objectId")]
        public Input<int>? ObjectId { get; set; }

        /// <summary>
        /// notebook object type
        /// </summary>
        [Input("objectType")]
        public Input<string>? ObjectType { get; set; }

        /// <summary>
        /// Notebook path on the workspace
        /// </summary>
        [Input("path", required: true)]
        public Input<string> Path { get; set; } = null!;

        public GetNotebookInvokeArgs()
        {
        }
        public static new GetNotebookInvokeArgs Empty => new GetNotebookInvokeArgs();
    }


    [OutputType]
    public sealed class GetNotebookResult
    {
        /// <summary>
        /// notebook content in selected format
        /// </summary>
        public readonly string Content;
        public readonly string Format;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// notebook language
        /// </summary>
        public readonly string Language;
        /// <summary>
        /// notebook object ID
        /// </summary>
        public readonly int ObjectId;
        /// <summary>
        /// notebook object type
        /// </summary>
        public readonly string ObjectType;
        public readonly string Path;

        [OutputConstructor]
        private GetNotebookResult(
            string content,

            string format,

            string id,

            string language,

            int objectId,

            string objectType,

            string path)
        {
            Content = content;
            Format = format;
            Id = id;
            Language = language;
            ObjectId = objectId;
            ObjectType = objectType;
            Path = path;
        }
    }
}
