import logging
from typing import Any

import asyncio
import aiohttp
import click

from sqlalchemy.schema import CreateTable
from aiopg.sa import create_engine

from .app import application_factory
from .db.tables import metadata

from .config import load_config, ConfigSchema


@click.group()
@click.option('--config', default='/app/etc/config/development.yml',
              help='Path to config yaml inside container')
@click.pass_context
def cli(ctx: Any, config: str) -> None:
    """ Process generic commands
    """
    ctx.obj = {}
    ctx.obj['config'] = load_config(ConfigSchema, config)
    ctx.obj['loop'] = asyncio.get_event_loop()
    ctx.obj['app'] = application_factory(ctx.obj['config'], ctx.obj['loop'])


@cli.command(help="Run application development server")
@click.option('--host', default='0.0.0.0', help='')
@click.option('--port', default=8080, help='')
@click.pass_context
def server(ctx: Any, host: str, port: int) -> None:
    logging.basicConfig(level=logging.DEBUG)
    aiohttp.web.run_app(ctx.obj['app'], host=host, port=port)


@cli.command(help="Creates database from metadata")
@click.pass_context
def create_database(ctx: Any) -> None:
    """ Need fixes:
    * correct way to retain creation order
    * remove try/except

    """

    async def _async_create(loop, conf):
        db = await create_engine(**conf, loop=loop)
        tables = [ CreateTable(table).compile(db)
                   for table in (
                           metadata.tables['companies'],
                           metadata.tables['accounts'],
                           metadata.tables['software'],
                           metadata.tables['software_orders'],
                           metadata.tables['software_order_items'],
                   ) ]

        async with db.acquire() as conn:
            for table_create_stmt in tables:
                try:
                    await conn.execute(table_create_stmt.string)
                except:
                    pass

        db.close()
        await db.wait_closed()

    ctx.obj['loop'].run_until_complete(
        _async_create(ctx.obj['loop'],
                      ctx.obj['config']['database'])
    )


if __name__ == '__main__':
    cli()
