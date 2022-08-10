// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    /// <summary>
    /// Installs a [library](https://docs.databricks.com/libraries/index.html) on databricks_cluster. Each different type of library has a slightly different syntax. It's possible to set only one type of library within one resource. Otherwise, the plan will fail with an error.
    /// 
    /// &gt; **Note** `databricks.Library` resource would always start the associated cluster if it's not running, so make sure to have auto-termination configured. It's not possible to atomically change the version of the same library without cluster restart. Libraries are fully removed from the cluster only after restart.
    /// 
    /// ## Java/Scala JAR
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Databricks = Pulumi.Databricks;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var appDbfsFile = new Databricks.DbfsFile("appDbfsFile", new Databricks.DbfsFileArgs
    ///         {
    ///             Source = $"{path.Module}/app-0.0.1.jar",
    ///             Path = "/FileStore/app-0.0.1.jar",
    ///         });
    ///         var appLibrary = new Databricks.Library("appLibrary", new Databricks.LibraryArgs
    ///         {
    ///             ClusterId = databricks_cluster.This.Id,
    ///             Jar = appDbfsFile.DbfsPath,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Java/Scala Maven
    /// 
    /// Installing artifacts from Maven repository. You can also optionally specify a `repo` parameter for a custom Maven-style repository, that should be accessible without any authentication. Maven libraries are resolved in Databricks Control Plane, so repo should be accessible from it. It can even be properly configured [maven s3 wagon](https://github.com/seahen/maven-s3-wagon), [AWS CodeArtifact](https://aws.amazon.com/codeartifact/) or [Azure Artifacts](https://azure.microsoft.com/en-us/services/devops/artifacts/).
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Databricks = Pulumi.Databricks;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var deequ = new Databricks.Library("deequ", new Databricks.LibraryArgs
    ///         {
    ///             ClusterId = databricks_cluster.This.Id,
    ///             Maven = new Databricks.Inputs.LibraryMavenArgs
    ///             {
    ///                 Coordinates = "com.amazon.deequ:deequ:1.0.4",
    ///                 Exclusions = 
    ///                 {
    ///                     "org.apache.avro:avro",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Python Wheel
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Databricks = Pulumi.Databricks;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var appDbfsFile = new Databricks.DbfsFile("appDbfsFile", new Databricks.DbfsFileArgs
    ///         {
    ///             Source = $"{path.Module}/baz.whl",
    ///             Path = "/FileStore/baz.whl",
    ///         });
    ///         var appLibrary = new Databricks.Library("appLibrary", new Databricks.LibraryArgs
    ///         {
    ///             ClusterId = databricks_cluster.This.Id,
    ///             Whl = appDbfsFile.DbfsPath,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Python PyPI
    /// 
    /// Installing Python PyPI artifacts. You can optionally also specify the `repo` parameter for a custom PyPI mirror, which should be accessible without any authentication for the network that cluster runs in.
    /// 
    /// &gt; **Note** `repo` host should be accessible from the Internet by Databricks control plane. If connectivity to custom PyPI repositories is required, please modify cluster-node `/etc/pip.conf` through databricks_global_init_script.
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Databricks = Pulumi.Databricks;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var fbprophet = new Databricks.Library("fbprophet", new Databricks.LibraryArgs
    ///         {
    ///             ClusterId = databricks_cluster.This.Id,
    ///             Pypi = new Databricks.Inputs.LibraryPypiArgs
    ///             {
    ///                 Package = "fbprophet==0.6",
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Python EGG
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Databricks = Pulumi.Databricks;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var appDbfsFile = new Databricks.DbfsFile("appDbfsFile", new Databricks.DbfsFileArgs
    ///         {
    ///             Source = $"{path.Module}/foo.egg",
    ///             Path = "/FileStore/foo.egg",
    ///         });
    ///         var appLibrary = new Databricks.Library("appLibrary", new Databricks.LibraryArgs
    ///         {
    ///             ClusterId = databricks_cluster.This.Id,
    ///             Egg = appDbfsFile.DbfsPath,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## R CRan
    /// 
    /// Installing artifacts from CRan. You can also optionally specify a `repo` parameter for a custom cran mirror.
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Databricks = Pulumi.Databricks;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var rkeops = new Databricks.Library("rkeops", new Databricks.LibraryArgs
    ///         {
    ///             ClusterId = databricks_cluster.This.Id,
    ///             Cran = new Databricks.Inputs.LibraryCranArgs
    ///             {
    ///                 Package = "rkeops",
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Related Resources
    /// 
    /// The following resources are often used in the same context:
    /// 
    /// * End to end workspace management guide.
    /// * databricks.getClusters data to retrieve a list of databricks.Cluster ids.
    /// * databricks.Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
    /// * databricks.ClusterPolicy to create a databricks.Cluster policy, which limits the ability to create clusters based on a set of rules.
    /// * databricks.DbfsFile data to get file content from [Databricks File System (DBFS)](https://docs.databricks.com/data/databricks-file-system.html).
    /// * databricks.getDbfsFilePaths data to get list of file names from get file content from [Databricks File System (DBFS)](https://docs.databricks.com/data/databricks-file-system.html).
    /// * databricks.DbfsFile to manage relatively small files on [Databricks File System (DBFS)](https://docs.databricks.com/data/databricks-file-system.html).
    /// * databricks.GlobalInitScript to manage [global init scripts](https://docs.databricks.com/clusters/init-scripts.html#global-init-scripts), which are run on all databricks.Cluster and databricks_job.
    /// * databricks.Job to manage [Databricks Jobs](https://docs.databricks.com/jobs.html) to run non-interactive code in a databricks_cluster.
    /// * databricks.Mount to [mount your cloud storage](https://docs.databricks.com/data/databricks-file-system.html#mount-object-storage-to-dbfs) on `dbfs:/mnt/name`.
    /// * databricks.Pipeline to deploy [Delta Live Tables](https://docs.databricks.com/data-engineering/delta-live-tables/index.html).
    /// * databricks.Repo to manage [Databricks Repos](https://docs.databricks.com/repos.html).
    /// 
    /// ## Import
    /// 
    /// -&gt; **Note** Importing this resource is not currently supported.
    /// </summary>
    [DatabricksResourceType("databricks:index/library:Library")]
    public partial class Library : Pulumi.CustomResource
    {
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        [Output("cran")]
        public Output<Outputs.LibraryCran?> Cran { get; private set; } = null!;

        [Output("egg")]
        public Output<string?> Egg { get; private set; } = null!;

        [Output("jar")]
        public Output<string?> Jar { get; private set; } = null!;

        [Output("maven")]
        public Output<Outputs.LibraryMaven?> Maven { get; private set; } = null!;

        [Output("pypi")]
        public Output<Outputs.LibraryPypi?> Pypi { get; private set; } = null!;

        [Output("whl")]
        public Output<string?> Whl { get; private set; } = null!;


        /// <summary>
        /// Create a Library resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Library(string name, LibraryArgs args, CustomResourceOptions? options = null)
            : base("databricks:index/library:Library", name, args ?? new LibraryArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Library(string name, Input<string> id, LibraryState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/library:Library", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Library resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Library Get(string name, Input<string> id, LibraryState? state = null, CustomResourceOptions? options = null)
        {
            return new Library(name, id, state, options);
        }
    }

    public sealed class LibraryArgs : Pulumi.ResourceArgs
    {
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        [Input("cran")]
        public Input<Inputs.LibraryCranArgs>? Cran { get; set; }

        [Input("egg")]
        public Input<string>? Egg { get; set; }

        [Input("jar")]
        public Input<string>? Jar { get; set; }

        [Input("maven")]
        public Input<Inputs.LibraryMavenArgs>? Maven { get; set; }

        [Input("pypi")]
        public Input<Inputs.LibraryPypiArgs>? Pypi { get; set; }

        [Input("whl")]
        public Input<string>? Whl { get; set; }

        public LibraryArgs()
        {
        }
    }

    public sealed class LibraryState : Pulumi.ResourceArgs
    {
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        [Input("cran")]
        public Input<Inputs.LibraryCranGetArgs>? Cran { get; set; }

        [Input("egg")]
        public Input<string>? Egg { get; set; }

        [Input("jar")]
        public Input<string>? Jar { get; set; }

        [Input("maven")]
        public Input<Inputs.LibraryMavenGetArgs>? Maven { get; set; }

        [Input("pypi")]
        public Input<Inputs.LibraryPypiGetArgs>? Pypi { get; set; }

        [Input("whl")]
        public Input<string>? Whl { get; set; }

        public LibraryState()
        {
        }
    }
}
