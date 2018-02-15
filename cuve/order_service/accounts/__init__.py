from aiohttp import web

from .views import login, logout, get_user, register

def accounts_subapp_factory():
    app = web.Application()

    app.router.add_get('/me', get_user)
    app.router.add_post('/register', register)

    app.router.add_post('/login', login)
    app.router.add_post('/logout', logout)

    return app
