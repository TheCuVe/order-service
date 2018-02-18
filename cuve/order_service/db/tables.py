from functools import partial
import sqlalchemy as sa

RequiredColumn = partial(sa.Column, nullable=False)
metadata = sa.MetaData()

COMPANY_ROLES = 'owner', 'accountant', 'manager'

company = sa.Table(
    'companies', metadata,
    sa.Column('id', sa.types.Integer, primary_key=True),
    RequiredColumn('name', sa.types.String),
    RequiredColumn('phone', sa.types.String),
    sa.Column('description', sa.types.String),
    # Allthroug it is possible to provide separate contact
    # email for company, i thing it would be more legitimate
    # to contant person who created buy order for company
    # RequiredColumn('email', sa.types.String),
)

account = sa.Table(
    'accounts', metadata,
    sa.Column('id', sa.types.Integer, primary_key=True),
    RequiredColumn('company_id', sa.types.Integer,
                   sa.schema.ForeignKey('companies.id')),
    RequiredColumn('email', sa.types.String, unique=True),
    RequiredColumn('first_name', sa.types.String),
    RequiredColumn('last_name', sa.types.String),
    RequiredColumn('password', sa.types.String),
)


software = sa.Table(
    'software', metadata,
    sa.Column('id', sa.types.Integer, primary_key=True),
    RequiredColumn('version', sa.types.Integer),
    RequiredColumn('distributor_id', sa.types.Integer,
                   sa.schema.ForeignKey('companies.id')),
    RequiredColumn('name', sa.types.String),
    RequiredColumn('description', sa.types.String),
    sa.Column('icon', sa.types.Binary),

    sa.schema.UniqueConstraint('id', 'version')
)

software_order = sa.Table(
    'software_orders', metadata,
    sa.Column('id', sa.types.Integer, primary_key=True),
    sa.Column('purchaser_id', sa.types.Integer,
              sa.schema.ForeignKey('accounts.id')),
)

software_order_item = sa.Table(
    'software_order_items', metadata,
    sa.Column('id', sa.types.Integer, primary_key=True),

    RequiredColumn('order_id', sa.types.Integer,
                   sa.schema.ForeignKey('software_orders.id')),
    RequiredColumn('software_id', sa.types.Integer),
    RequiredColumn('software_version', sa.types.Integer),
    RequiredColumn('amount', sa.types.Integer,
                   sa.schema.CheckConstraint('amount>0'), default=1),
    RequiredColumn('price', sa.types.Numeric,
                   sa.schema.CheckConstraint('price>=0')),

    sa.schema.ForeignKeyConstraint(('software_id', 'software_version'),
                                   ('software.id', 'software.version'))
)
