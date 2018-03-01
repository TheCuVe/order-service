from sqlalchemy.schema import CreateTable
from aiopg.sa import create_engine

from .tables import metadata


async def async_create_database(loop, conf):
    """ Need fixes:
    * correct way to retain creation order
    * remove try/except

    """
    db = await create_engine(**conf, loop=loop)
    tables = [CreateTable(table).compile(db)
              for table in (metadata.tables['companies'],
                            metadata.tables['accounts'],
                            metadata.tables['software'],
                            metadata.tables['software_orders'],
                            metadata.tables['software_order_items'])]

    async with db.acquire() as conn:
        for table_create_stmt in tables:
            await conn.execute(table_create_stmt.string)

    db.close()
    await db.wait_closed()
