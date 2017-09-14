#!/usr/bin/python3

import sys

from charmhelpers.core.hookenv import (
    Hooks,
    DEBUG,
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

@hooks.hook('update-status')
def update_status():
    log("Entered update_status", DEBUG)

@hooks.hook('openstack-api-endpoint-relation-changed')
def openstack_api_endpoint_changed(relation_id=None, unit=None):
    log("Entered openstack_api_endpoint_changed", DEBUG)

    log("Getting relation data:", DEBUG)
    incoming_data = relation_get()
    for k, v in incoming_data.iteritems():
        log("  {}: {}".format(k, v), DEBUG)

    log("Setting relation data:", DEBUG)
    outgoing_data = {"floating_ip": "98.34.12.1"}
    relation_set(relation_id=rel_id, **outgoing_data)

    return

def main():
    try:
        hooks.execute(sys.argv)
    except UnregisteredHookError as e:
        log('Unknown hook {} - skipping.'.format(e))


if __name__ == '__main__':
    main()
