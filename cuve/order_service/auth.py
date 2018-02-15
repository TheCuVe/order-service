from collections import namedtuple
from functools import wraps

from sqlalchemy import sql

from aiohttp.web import middleware, HTTPUnauthorized

from .db.tables import company, account

@middleware
async def auth_middleware(request, handler):
    db = request.app['db']

    credentials_select = (
        sql.select([account, company.c.id], use_labels=True)
        .select_from(account.join(company))
        .where(account.c.id == 1)
    )

    async with db.acquire() as conn:
        result = await conn.execute(credentials_select)
        credentials = await result.fetchone()

        # FIXME: Fake credentials creation for development purpose
        if credentials is None:
            await conn.execute(
                company.insert().values(name='Fake LLC',
                                        phone='+7 (000) 000 0000',
                                        description='')
            )
            await conn.execute(
                account.insert().values(company_id=1,
                                        email='fake@email.test',
                                        first_name='Fake',
                                        last_name='Person',
                                        password='CrAzzyP$wrD')
            )

            result = await conn.execute(credentials_select)
            credentials = await result.fetchone()

        if credentials is not None:
            request['auth'] = {
                'company': credentials.companies_id,
                'account': {
                    'id': credentials.accounts_id,
                    'email': credentials.accounts_email,
                }
            }

    return await handler(request)


def auth_required(f):
    """ Decorator for aiohttp web handlers with primitive auth check
    """

    @wraps(f)
    async def _wrapper(request):
        if 'auth' not in request:
            raise HTTPUnauthorized()
        return await f(request)

    return _wrapper
