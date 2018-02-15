from aiopg.sa import create_engine
from .tables import account, company


async def _on_app_startup(app):
    conf = app['config']['database']
    app['db'] = await create_engine(**conf, loop=app.loop)


async def _on_app_cleanup(app):
    app['db'].close()
    await app['db'].wait_closed()




def setup_db(app):
    app.on_startup.append(_on_app_startup)
    app.on_cleanup.append(_on_app_cleanup)
