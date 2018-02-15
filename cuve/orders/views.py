from aiohttp import web
from cuve.auth import auth_required

from cuve.db.tables import software_order, software_order_item, software

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
async def update_order(request):
    pass


@auth_required
async def show_order(request):
    pass


@auth_required
async def search_orders(request):
    pass
