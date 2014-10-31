from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
preference = Table('preference', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('reading', Integer, default=ColumnDefault(0)),
    Column('movie', Integer, default=ColumnDefault(0)),
    Column('cycling', Integer, default=ColumnDefault(0)),
    Column('picnic', Integer, default=ColumnDefault(0)),
    Column('climbing', Integer, default=ColumnDefault(0)),
    Column('photographing', Integer, default=ColumnDefault(0)),
    Column('football', Integer, default=ColumnDefault(0)),
    Column('basketball', Integer, default=ColumnDefault(0)),
    Column('onlinegame', Integer, default=ColumnDefault(0)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['preference'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['preference'].drop()
