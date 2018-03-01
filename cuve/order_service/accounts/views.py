from aiohttp import web

# from cuve.order_service.db.tables import account
# from .schemas import RegistrationSchema


async def login(request):
    return web.Response(text='OK')


async def logout(request):
    return web.Response(text='OK')


async def get_user(request):
    return web.Response(text='OK')


async def register(request):
    with request.app['db'].acquire():
        pass

    return web.Response(text='OK')
