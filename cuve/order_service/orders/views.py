from aiohttp import web

from cuve.order_service.auth import auth_required
from cuve.order_service.db.tables import (
    software_order, software_order_item, software
)

from .schemas import UpdateOrderSchema

@auth_required
async def create_order(request):
    """ Create new order for current account
    """
    db = request.app['db']

    async with db.acquire() as conn:
        result = await conn.execute(
            software_order.insert().values(
                purchaser_id=request['auth']['account']['id']
            )
        )
        return web.json_response({
            'order_id': (await result.fetchone())[0]
        })


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
    request_schema = UpdateOrderSchema(strict=True)
    payload = request_schema.load(await request.json()).data



    return web.json_response(payload)



@auth_required
async def show_order(request):
    pass


@auth_required
async def search_orders(request):
    pass
