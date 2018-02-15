from aiohttp import web

from .views import (create_order, update_order,
                    show_order, search_orders)


def setup_orders_routing(app):
    app.router.add_get('/api/v1.0/orders/', search_orders)
    app.router.add_post('/api/v1.0/orders/', create_order)

    app.router.add_get('/api/v1.0/orders/{id:\d+}', show_order)
    app.router.add_post('/api/v1.0/orders/{id:\d+}', update_order)

    return app
