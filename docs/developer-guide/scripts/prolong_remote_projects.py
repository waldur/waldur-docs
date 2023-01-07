import logging

from waldur_core.structure import models as sm
from waldur_mastermind.marketplace_remote import models as mrm
from waldur_mastermind.marketplace_remote import utils as mru
from waldur_mastermind.marketplace import models as mm
from waldur_mastermind.marketplace import callbacks as mc
from waldur_client import WaldurClientException
from waldur_core.core.utils import get_system_robot

logger = logging.getLogger(__name__)

system_robot = get_system_robot()

for customer in sm.Customer.objects.filter(archived=False):
    for project in customer.projects.all():
        update_requests = mrm.ProjectUpdateRequest.objects.filter(
            project=project, state=mrm.ProjectUpdateRequest.States.PENDING
        )
        if update_requests.count() == 0:
            continue
        prolongation_requests = [
            req
            for req in update_requests
            if req.new_end_date is not None and req.old_end_date != req.new_end_date
        ]
        if len(prolongation_requests) > 1:
            logger.warning(
                'There are more than 1 update request for %s, skipping processing',
                project,
            )
            continue

        logger.info('Approving the prolongation request for %s', project)
        request = prolongation_requests[0]
        request.approve(system_robot)

        # Processing resources
        resources = project.resource_set.filter(state=mm.Resource.States.TERMINATING)
        for resource in resources:
            logger.info('  Processing %s', resource)
            offering = resource.offering
            client = mru.get_client_for_offering(offering)
            items = mm.OrderItem.objects.filter(
                resource=resource,
                state=mm.OrderItem.States.EXECUTING,
                type=mm.OrderItem.Types.TERMINATE,
            )
            if items.count() > 1:
                logger.warning(
                    '  There are more than 1 order item for the resource, skipping modification'
                )
                continue
            if items.count() == 0:
                logger.warning(
                    '  There are no order items for the resource, skipping modification'
                )
            item = items.first()
            try:
                remote_order = client.get_order(item.backend_id)
                remote_item = remote_order['items'][0]
                remote_item_uuid = remote_item['uuid']
                logger.info('  Terminating remote order item %s', remote_item_uuid)
                client.marketplace_order_item_reject(remote_item_uuid)
            except WaldurClientException as exc:
                logger.exception(exc)
                continue

            mc.sync_order_item_state(item, mm.OrderItem.States.TERMINATED)
