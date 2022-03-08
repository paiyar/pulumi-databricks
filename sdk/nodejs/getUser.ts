// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getUser(args?: GetUserArgs, opts?: pulumi.InvokeOptions): Promise<GetUserResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("databricks:index/getUser:getUser", {
        "userId": args.userId,
        "userName": args.userName,
    }, opts);
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserArgs {
    /**
     * ID of the user.
     */
    userId?: string;
    /**
     * User name of the user. The user must exist before this resource can be planned.
     */
    userName?: string;
}

/**
 * A collection of values returned by getUser.
 */
export interface GetUserResult {
    /**
     * Alphanumeric representation of user local name. e.g. `mrFoo`.
     */
    readonly alphanumeric: string;
    /**
     * Display name of the user, e.g. `Mr Foo`.
     */
    readonly displayName: string;
    /**
     * ID of the user in an external identity provider.
     */
    readonly externalId: string;
    /**
     * Home folder of the user, e.g. `/Users/mr.foo@example.com`.
     */
    readonly home: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Personal Repos location of the user, e.g. `/Repos/mr.foo@example.com`.
     */
    readonly repos: string;
    readonly userId?: string;
    /**
     * Name of the user, e.g. `mr.foo@example.com`.
     */
    readonly userName?: string;
}

export function getUserOutput(args?: GetUserOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetUserResult> {
    return pulumi.output(args).apply(a => getUser(a, opts))
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserOutputArgs {
    /**
     * ID of the user.
     */
    userId?: pulumi.Input<string>;
    /**
     * User name of the user. The user must exist before this resource can be planned.
     */
    userName?: pulumi.Input<string>;
}
