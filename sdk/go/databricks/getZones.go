// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetZones(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetZonesResult, error) {
	var rv GetZonesResult
	err := ctx.Invoke("databricks:index/getZones:getZones", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getZones.
type GetZonesResult struct {
	DefaultZone string `pulumi:"defaultZone"`
	// The provider-assigned unique ID for this managed resource.
	Id    string   `pulumi:"id"`
	Zones []string `pulumi:"zones"`
}
