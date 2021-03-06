from aiohttp import web

from cuve.order_service.auth import auth_required
from cuve.order_service.db import tables, transaction


@auth_required
async def search_orders(request):
    pass


@auth_required
async def show_order(request):
    pass


@auth_required
async def create_order(request):
    """ Create new order for current account
    """
    async with transaction(request.app) as trans:
        order_id = await trans.connection.scalar(
            tables.software_order.insert().values(
                purchaser_id=request['auth']['account']['id']
            )
        )
        await trans.commit()
        return web.json_response({'order_id': order_id})


@auth_required
async def order_add_software(request):
    pass


@auth_required
async def order_delete_software(request):
    pass


@auth_required
async def order_update_software(request):
    pass


@auth_required
async def update_order(request):
    """ Update order with software
    """
    # request_schema = UpdateOrderSchema(strict=True)
    # payload = request_schema.load(await request.json()).data
    return web.json_response({'result': 'ok'})
