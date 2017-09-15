#!/usr/bin/python3

import sys

from charmhelpers.core.hookenv import (
    Hooks,
    DEBUG,
    UnregisteredHookError,
    log,
    relation_get,
    relation_set,
)

hooks = Hooks()

@hooks.hook('install')
def install():
    log("Entered install", DEBUG)

@hooks.hook('config-changed')
def config_changed():
    log("Entered config_changed", DEBUG)

@hooks.hook('start')
def start():
    log("Entered start", DEBUG)

@hooks.hook('update-status')
def update_status():
    log("Entered update_status", DEBUG)

@hooks.hook('api-loadbalancer-relation-changed')
def openstack_api_endpoint_changed(relation_id=None, unit=None):
    log("Entered openstack_api_endpoint_changed", DEBUG)

    log("Getting relation data:", DEBUG)
    incoming_data = relation_get()
    if incoming_data:
        for k, v in incoming_data.items():
            log("  {}: {}".format(k, v), DEBUG)

            if "service_type" in k:
                floating_ip_key = ("{}_floating_ip".format(v))
                floating_ip = "98.34.12.1"
                outgoing_data = {floating_ip_key: floating_ip}
                log("Setting relation data:", DEBUG)
                log("  {}: {}".format(floating_ip_key, floating_ip), DEBUG)
                relation_set(**outgoing_data)
    else:
        log("No incoming data", DEBUG)

    return

def main():
    try:
        hooks.execute(sys.argv)
    except UnregisteredHookError as e:
        log('Unknown hook {} - skipping.'.format(e))


if __name__ == '__main__':
    main()
