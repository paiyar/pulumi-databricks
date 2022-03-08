// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use `Pipeline` to deploy [Delta Live Tables](https://docs.databricks.com/data-engineering/delta-live-tables/index.html).
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/paiyar/pulumi-databricks/sdk/go/databricks"
// 	"github.com/pulumi/pulumi-databricks/sdk/go/databricks"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		dltDemo, err := databricks.NewNotebook(ctx, "dltDemo", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = databricks.NewPipeline(ctx, "this", &databricks.PipelineArgs{
// 			Storage: pulumi.String("/test/first-pipeline"),
// 			Configuration: pulumi.AnyMap{
// 				"key1": pulumi.Any("value1"),
// 				"key2": pulumi.Any("value2"),
// 			},
// 			Clusters: PipelineClusterArray{
// 				&PipelineClusterArgs{
// 					Label:      pulumi.String("default"),
// 					NumWorkers: pulumi.Int(2),
// 					CustomTags: pulumi.AnyMap{
// 						"cluster_type": pulumi.Any("default"),
// 					},
// 				},
// 				&PipelineClusterArgs{
// 					Label:      pulumi.String("maintenance"),
// 					NumWorkers: pulumi.Int(1),
// 					CustomTags: pulumi.AnyMap{
// 						"cluster_type": pulumi.Any("maintenance"),
// 					},
// 				},
// 			},
// 			Libraries: PipelineLibraryArray{
// 				&PipelineLibraryArgs{
// 					Notebook: &PipelineLibraryNotebookArgs{
// 						Path: dltDemo.ID(),
// 					},
// 				},
// 			},
// 			Filters: &PipelineFiltersArgs{
// 				Includes: pulumi.StringArray{
// 					pulumi.String("com.databricks.include"),
// 				},
// 				Excludes: pulumi.StringArray{
// 					pulumi.String("com.databricks.exclude"),
// 				},
// 			},
// 			Continuous: pulumi.Bool(false),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ## Related Resources
//
// The following resources are often used in the same context:
//
// * End to end workspace management guide.
// * Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
// * Job to manage [Databricks Jobs](https://docs.databricks.com/jobs.html) to run non-interactive code in a databricks_cluster.
// * Notebook to manage [Databricks Notebooks](https://docs.databricks.com/notebooks/index.html).
//
// ## Import
//
// The resource job can be imported using the id of the pipeline bash
//
// ```sh
//  $ pulumi import databricks:index/pipeline:Pipeline this <pipeline-id>
// ```
type Pipeline struct {
	pulumi.CustomResourceState

	AllowDuplicateNames pulumi.BoolPtrOutput `pulumi:"allowDuplicateNames"`
	// blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
	Clusters PipelineClusterArrayOutput `pulumi:"clusters"`
	// An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
	Configuration pulumi.MapOutput `pulumi:"configuration"`
	// A flag indicating whether to run the pipeline continuously. The default value is `false`.
	Continuous pulumi.BoolPtrOutput  `pulumi:"continuous"`
	Filters    PipelineFiltersOutput `pulumi:"filters"`
	Id         pulumi.StringOutput   `pulumi:"id"`
	// blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
	Libraries PipelineLibraryArrayOutput `pulumi:"libraries"`
	// A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
	Name pulumi.StringOutput `pulumi:"name"`
	// A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
	Storage pulumi.StringPtrOutput `pulumi:"storage"`
	// The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
	Target pulumi.StringPtrOutput `pulumi:"target"`
	Url    pulumi.StringOutput    `pulumi:"url"`
}

// NewPipeline registers a new resource with the given unique name, arguments, and options.
func NewPipeline(ctx *pulumi.Context,
	name string, args *PipelineArgs, opts ...pulumi.ResourceOption) (*Pipeline, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Filters == nil {
		return nil, errors.New("invalid value for required argument 'Filters'")
	}
	var resource Pipeline
	err := ctx.RegisterResource("databricks:index/pipeline:Pipeline", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPipeline gets an existing Pipeline resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPipeline(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PipelineState, opts ...pulumi.ResourceOption) (*Pipeline, error) {
	var resource Pipeline
	err := ctx.ReadResource("databricks:index/pipeline:Pipeline", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Pipeline resources.
type pipelineState struct {
	AllowDuplicateNames *bool `pulumi:"allowDuplicateNames"`
	// blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
	Clusters []PipelineCluster `pulumi:"clusters"`
	// An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
	Configuration map[string]interface{} `pulumi:"configuration"`
	// A flag indicating whether to run the pipeline continuously. The default value is `false`.
	Continuous *bool            `pulumi:"continuous"`
	Filters    *PipelineFilters `pulumi:"filters"`
	Id         *string          `pulumi:"id"`
	// blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
	Libraries []PipelineLibrary `pulumi:"libraries"`
	// A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
	Name *string `pulumi:"name"`
	// A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
	Storage *string `pulumi:"storage"`
	// The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
	Target *string `pulumi:"target"`
	Url    *string `pulumi:"url"`
}

type PipelineState struct {
	AllowDuplicateNames pulumi.BoolPtrInput
	// blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
	Clusters PipelineClusterArrayInput
	// An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
	Configuration pulumi.MapInput
	// A flag indicating whether to run the pipeline continuously. The default value is `false`.
	Continuous pulumi.BoolPtrInput
	Filters    PipelineFiltersPtrInput
	Id         pulumi.StringPtrInput
	// blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
	Libraries PipelineLibraryArrayInput
	// A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
	Name pulumi.StringPtrInput
	// A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
	Storage pulumi.StringPtrInput
	// The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
	Target pulumi.StringPtrInput
	Url    pulumi.StringPtrInput
}

func (PipelineState) ElementType() reflect.Type {
	return reflect.TypeOf((*pipelineState)(nil)).Elem()
}

type pipelineArgs struct {
	AllowDuplicateNames *bool `pulumi:"allowDuplicateNames"`
	// blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
	Clusters []PipelineCluster `pulumi:"clusters"`
	// An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
	Configuration map[string]interface{} `pulumi:"configuration"`
	// A flag indicating whether to run the pipeline continuously. The default value is `false`.
	Continuous *bool           `pulumi:"continuous"`
	Filters    PipelineFilters `pulumi:"filters"`
	Id         *string         `pulumi:"id"`
	// blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
	Libraries []PipelineLibrary `pulumi:"libraries"`
	// A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
	Name *string `pulumi:"name"`
	// A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
	Storage *string `pulumi:"storage"`
	// The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
	Target *string `pulumi:"target"`
}

// The set of arguments for constructing a Pipeline resource.
type PipelineArgs struct {
	AllowDuplicateNames pulumi.BoolPtrInput
	// blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
	Clusters PipelineClusterArrayInput
	// An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
	Configuration pulumi.MapInput
	// A flag indicating whether to run the pipeline continuously. The default value is `false`.
	Continuous pulumi.BoolPtrInput
	Filters    PipelineFiltersInput
	Id         pulumi.StringPtrInput
	// blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
	Libraries PipelineLibraryArrayInput
	// A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
	Name pulumi.StringPtrInput
	// A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
	Storage pulumi.StringPtrInput
	// The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
	Target pulumi.StringPtrInput
}

func (PipelineArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*pipelineArgs)(nil)).Elem()
}

type PipelineInput interface {
	pulumi.Input

	ToPipelineOutput() PipelineOutput
	ToPipelineOutputWithContext(ctx context.Context) PipelineOutput
}

func (*Pipeline) ElementType() reflect.Type {
	return reflect.TypeOf((**Pipeline)(nil)).Elem()
}

func (i *Pipeline) ToPipelineOutput() PipelineOutput {
	return i.ToPipelineOutputWithContext(context.Background())
}

func (i *Pipeline) ToPipelineOutputWithContext(ctx context.Context) PipelineOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineOutput)
}

// PipelineArrayInput is an input type that accepts PipelineArray and PipelineArrayOutput values.
// You can construct a concrete instance of `PipelineArrayInput` via:
//
//          PipelineArray{ PipelineArgs{...} }
type PipelineArrayInput interface {
	pulumi.Input

	ToPipelineArrayOutput() PipelineArrayOutput
	ToPipelineArrayOutputWithContext(context.Context) PipelineArrayOutput
}

type PipelineArray []PipelineInput

func (PipelineArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Pipeline)(nil)).Elem()
}

func (i PipelineArray) ToPipelineArrayOutput() PipelineArrayOutput {
	return i.ToPipelineArrayOutputWithContext(context.Background())
}

func (i PipelineArray) ToPipelineArrayOutputWithContext(ctx context.Context) PipelineArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineArrayOutput)
}

// PipelineMapInput is an input type that accepts PipelineMap and PipelineMapOutput values.
// You can construct a concrete instance of `PipelineMapInput` via:
//
//          PipelineMap{ "key": PipelineArgs{...} }
type PipelineMapInput interface {
	pulumi.Input

	ToPipelineMapOutput() PipelineMapOutput
	ToPipelineMapOutputWithContext(context.Context) PipelineMapOutput
}

type PipelineMap map[string]PipelineInput

func (PipelineMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Pipeline)(nil)).Elem()
}

func (i PipelineMap) ToPipelineMapOutput() PipelineMapOutput {
	return i.ToPipelineMapOutputWithContext(context.Background())
}

func (i PipelineMap) ToPipelineMapOutputWithContext(ctx context.Context) PipelineMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineMapOutput)
}

type PipelineOutput struct{ *pulumi.OutputState }

func (PipelineOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Pipeline)(nil)).Elem()
}

func (o PipelineOutput) ToPipelineOutput() PipelineOutput {
	return o
}

func (o PipelineOutput) ToPipelineOutputWithContext(ctx context.Context) PipelineOutput {
	return o
}

type PipelineArrayOutput struct{ *pulumi.OutputState }

func (PipelineArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Pipeline)(nil)).Elem()
}

func (o PipelineArrayOutput) ToPipelineArrayOutput() PipelineArrayOutput {
	return o
}

func (o PipelineArrayOutput) ToPipelineArrayOutputWithContext(ctx context.Context) PipelineArrayOutput {
	return o
}

func (o PipelineArrayOutput) Index(i pulumi.IntInput) PipelineOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Pipeline {
		return vs[0].([]*Pipeline)[vs[1].(int)]
	}).(PipelineOutput)
}

type PipelineMapOutput struct{ *pulumi.OutputState }

func (PipelineMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Pipeline)(nil)).Elem()
}

func (o PipelineMapOutput) ToPipelineMapOutput() PipelineMapOutput {
	return o
}

func (o PipelineMapOutput) ToPipelineMapOutputWithContext(ctx context.Context) PipelineMapOutput {
	return o
}

func (o PipelineMapOutput) MapIndex(k pulumi.StringInput) PipelineOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Pipeline {
		return vs[0].(map[string]*Pipeline)[vs[1].(string)]
	}).(PipelineOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineInput)(nil)).Elem(), &Pipeline{})
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineArrayInput)(nil)).Elem(), PipelineArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineMapInput)(nil)).Elem(), PipelineMap{})
	pulumi.RegisterOutputType(PipelineOutput{})
	pulumi.RegisterOutputType(PipelineArrayOutput{})
	pulumi.RegisterOutputType(PipelineMapOutput{})
}
