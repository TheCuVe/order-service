from aiohttp import web
from aiopg.sa import create_engine


class transaction:
    """ Context manager wrapping postgresql transaction
    """

    def __init__(self, app: web.Application) -> None:
        assert 'db' in app, 'Using transaction without database in app context'
        self.db = app['db']

    async def __aenter__(self):
        self.connection = await self.db._acquire()
        self.transaction = await self.connection.begin()
        return self.transaction

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.transaction.close()
        await self.connection.close()


async def _on_app_startup(app: web.Application) -> None:
    """ Initialize connection aiopg pool
    """
    conf = app['config']['database']
    app['db'] = await create_engine(**conf, loop=app.loop)


async def _on_app_cleanup(app: web.Application) -> None:
    """ Close aiopg connection pool
    """
    app['db'].close()
    await app['db'].wait_closed()


def setup_db(app: web.Application) -> None:
    """ Hook aiopg pool creation and cleanup to aiohttp.web.Application
    startup/cleanup signals
    """
    app.on_startup.append(_on_app_startup)
    app.on_cleanup.append(_on_app_cleanup)
