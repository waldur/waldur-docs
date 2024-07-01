from waldur_core.structure import models as sm
from waldur_openstack.openstack import models as om
from waldur_openstack.openstack.backend import OpenStackBackend
from waldur_openstack.openstack_tenant import models as otm
from waldur_openstack.openstack_tenant import executors as ote

import logging

logger = logging.getLogger(__name__)

tenant_names = []

main_tenant: om.Tenant = om.Tenant.objects.get(uuid='<main-tenant-uuid>')
backend: OpenStackBackend = main_tenant.get_backend()


def wipe_dangling_tenant_objects(tenant):
    service_settings = sm.ServiceSettings.objects.get(scope=tenant)

    try:
        backend.delete_tenant_floating_ips(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_floating_ips')

    try:
        backend.delete_tenant_routes(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_routes')

    try:
        backend.delete_tenant_ports(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_ports')

    try:
        backend.delete_tenant_routers(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_routers')

    try:
        backend.delete_tenant_networks(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_networks')

    try:
        backend.delete_tenant_security_groups(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_security_groups')

    try:
        backend.delete_tenant_snapshots(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_snapshots')
    otm.Snapshot.objects.filter(service_settings=service_settings).delete()

    backend.are_all_tenant_snapshots_deleted(tenant)

    try:
        backend.delete_tenant_instances(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_instances')
    otm.Instance.objects.filter(service_settings=service_settings).delete()

    backend.are_all_tenant_instances_deleted(tenant)

    try:
        backend.delete_tenant_volumes(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_volumes')
    otm.Volume.objects.filter(service_settings=service_settings).delete()

    backend.are_all_tenant_volumes_deleted(tenant)

    try:
        backend.delete_tenant_server_groups(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_server_groups')
    otm.ServerGroup.objects.filter(service_settings=service_settings).delete()

    try:
        backend.delete_tenant_user(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_user')

    try:
        backend.delete_tenant(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant')
    tenant.delete()


for tenant_name in tenant_names:
    tenant = om.Tenant.objects.get(name=tenant_name)
    tenant.state = om.Tenant.States.DELETING
    tenant.save(update_fields=['state'])
    ote.OpenStackTenantCleanupExecutor().execute(tenant.project, is_async=False)
    wipe_dangling_tenant_objects(tenant)
