from aiohttp import web

from .views import (search_orders,
                    create_order,
                    show_order,
                    update_order,
                    order_add_software,
                    order_delete_software,
                    order_update_software)


def setup_orders_routing(app):
    order_base_url = '/api/v1.0/orders/'
    order_url = order_base_url + '{order_id:\d+}'

    app.router.add_get(order_base_url, search_orders)
    app.router.add_post(order_base_url, create_order)

    app.router.add_get(order_url, show_order)
    app.router.add_put(order_url, update_order)

    app.router.add_post(order_url + '/add',
                        order_add_software)
    app.router.add_put(order_url + '/{software_order_item_id:\d+}',
                       order_update_software)
    app.router.add_delete(order_url + '/{software_order_item_id:\d+}',
                          order_delete_software)


    return app
