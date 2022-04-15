import typing

import asyncpg

from config import Config

class DB:
    """
    <<<--------------------------------------------------->>>
    table = user_model
        id: Integer Primary Key
        username: String(256) NOT NULL UNIQUE = TRUE
        password: String(256) NOT NULL
        email: String(256) NOT NULL UNIQUE = TRUE
        is_admin: Bool NOT NULL DEFAULT 0
    <<<--------------------------------------------------->>>
    """

    @staticmethod
    async def __select_method(sql, is_all: bool = False):
        connection: asyncpg.Connection = None
        try:
            connection: asyncpg.Connection = await asyncpg.connect(Config)
            if is_all:
                return await connection.fetchrow(sql)
            else:
                return await connection.fetch(sql)
        except Exception as error:
            raise error
        finally:
            if connection is not None:
                await connection.close()

    @staticmethod
    async def __insert_method(sql):
        connection: asyncpg.Connection = None
        try:
            connection: asyncpg.Connection = await asyncpg.connect(Config.DATABASE_URL)
            await connection.execute(sql)
            return True
        except Exception as error:
            raise error
        finally:
            if connection is not None:
                await connection.close()

    @staticmethod
    async def get_users_id() -> typing.List:
        return [i[0] for i in await DB.__select_method("SELECT id FROM user_model WHERE is_admin=0", is_all=True)]

    @staticmethod
    async def get_users() -> typing.Dict:
        return dict(await DB.__select_method("SELECT id, username FROM user_model WHERE is_admin=0"))


db = DB