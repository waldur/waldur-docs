from waldur_openstack import models, executors
from waldur_openstack.backend import OpenStackBackend

import logging

logger = logging.getLogger(__name__)

tenant_names = []

main_tenant = models.Tenant.objects.get(uuid='<main-tenant-uuid>')
backend: OpenStackBackend = main_tenant.get_backend()


def wipe_dangling_tenant_objects(tenant):
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
    models.Snapshot.objects.filter(tenant=tenant).delete()

    backend.are_all_tenant_snapshots_deleted(tenant)

    try:
        backend.delete_tenant_instances(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_instances')
    models.Instance.objects.filter(tenant=tenant).delete()

    backend.are_all_tenant_instances_deleted(tenant)

    try:
        backend.delete_tenant_volumes(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_volumes')
    models.Volume.objects.filter(tenant=tenant).delete()

    backend.are_all_tenant_volumes_deleted(tenant)

    try:
        backend.delete_tenant_server_groups(tenant)
    except Exception as exc:
        logger.exception(exc)
        input('Continue?')
    else:
        logger.info('delete_tenant_server_groups')
    models.ServerGroup.objects.filter(tenant=tenant).delete()

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
    tenant = models.Tenant.objects.get(name=tenant_name)
    tenant.state = models.Tenant.States.DELETING
    tenant.save(update_fields=['state'])
    executors.OpenStackCleanupExecutor().execute(tenant.project, is_async=False)
    wipe_dangling_tenant_objects(tenant)
