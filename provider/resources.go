// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package databricks

import (
	"fmt"
	"github.com/iancoleman/strcase"
	"path/filepath"
	"strings"

	databricks "github.com/databricks/terraform-provider-databricks/provider"
	"github.com/paiyar/pulumi-databricks/provider/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "databricks"
	// modules:
	mainMod = "index" // the databricks module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

func stripDatabricksPrefix(source string) string {
	return strings.TrimPrefix(source, "databricks_")
}

func sanitizeDatabricksSourceName(source string) string {
	return strcase.ToCamel(stripDatabricksPrefix(source))
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(databricks.DatabricksProvider())

	// Ref: https://github.com/pulumi/pulumi-tf-provider-boilerplate#adding-mappings-building-the-provider-and-sdks
	resourceMap := make(map[string]*tfbridge.ResourceInfo)
	for resource := range databricks.DatabricksProvider().ResourcesMap {
		shortName := stripDatabricksPrefix(resource)
		resourceMap[resource] = &tfbridge.ResourceInfo{
			Tok: tfbridge.MakeResource(mainPkg, mainMod, sanitizeDatabricksSourceName(resource)),
			Fields: map[string]*tfbridge.SchemaInfo{
				shortName: {
					// We don't use C#, this is just to get around build errors.
					// (There is 0 thought put into prefixing names with CS)
					CSharpName: strcase.ToCamel(fmt.Sprintf("CS%s", shortName)),
				},
			},
		}
	}

	dataSourceMap := make(map[string]*tfbridge.DataSourceInfo)
	for source := range databricks.DatabricksProvider().DataSourcesMap {
		dataSourceMap[source] = &tfbridge.DataSourceInfo{
			Tok: tfbridge.MakeDataSource(
				mainPkg, mainMod,
				fmt.Sprintf("get%s", strings.Title(sanitizeDatabricksSourceName(source))),
			),
		}
	}

	// Ref: https://github.com/databricks/terraform-provider-databricks/blob/master/docs/index.md#environment-variables
	// NOTE: Intentionally elided AZURE related configurations
	configMap := make(map[string]*tfbridge.SchemaInfo)
	for _, config := range []string{
		"host",
		"token",
		"username",
		"password",
		"account_id",
		"config_file",
		"profile",
		"debug_truncate_bytes",
		"debug_headers",
		"rate_limit",
	} {
		configMap[config] = &tfbridge.SchemaInfo{
			Default: &tfbridge.DefaultInfo{
				EnvVars: []string{strings.ToUpper(fmt.Sprintf("databricks_%s", config))},
			},
		}
	}

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:    p,
		Name: "databricks",
		// DisplayName is a way to be able to change the casing of the provider
		// name when being displayed on the Pulumi registry
		DisplayName: "",
		// The default publisher for all packages is Pulumi.
		// Change this to your personal name (or a company name) that you
		// would like to be shown in the Pulumi Registry if this package is published
		// there.
		Publisher: "Pulumi",
		// LogoURL is optional but useful to help identify your package in the Pulumi Registry
		// if this package is published there.
		//
		// You may host a logo on a domain you control or add an SVG logo for your package
		// in your repository and use the raw content URL for that file as your logo URL.
		LogoURL: "",
		// PluginDownloadURL is an optional URL used to download the Provider
		// for use in Pulumi programs
		// e.g https://github.com/org/pulumi-provider-name/releases/
		PluginDownloadURL: "",
		Description:       "A Pulumi package for creating and managing databricks cloud resources.",
		// category/cloud tag helps with categorizing the package in the Pulumi Registry.
		// For all available categories, see `Keywords` in
		// https://www.pulumi.com/docs/guides/pulumi-packages/schema/#package.
		Keywords:   []string{"pulumi", "databricks", "category/cloud"},
		License:    "Apache-2.0",
		Homepage:   "https://www.pulumi.com",
		Repository: "https://github.com/paiyar/pulumi-databricks",
		// The GitHub Org for the provider - defaults to `terraform-providers`
		GitHubOrg:            "databricks",
		Config:               configMap,
		PreConfigureCallback: preConfigureCallback,
		Resources:            resourceMap,
		DataSources:          dataSourceMap,
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/paiyar/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
