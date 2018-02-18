from aiohttp import web
from typing import Dict

from .db import setup_db
from .auth import auth_middleware

from .orders import setup_orders_routing


API_URL_PREFIX = '/api/v1.0'


def application_factory(config: Dict, loop) -> web.Application:
    """ Creates and setups aiohttp web application instance
    """

    app = web.Application(loop=loop, middlewares=[
        auth_middleware
    ])
    app['config'] = config

    setup_db(app)

    setup_orders_routing(app)

    return app
