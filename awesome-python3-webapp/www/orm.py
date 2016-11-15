# -*- coding: utf-8 -*-

__author__ = 'SunLang'

'数据库操作'

import asyncio, logging
import aiomysql

logging.basicConfig(level=logging.INFO)

def log(sql, args=()):
    logging.info('SQL: %s' % sql)

#创建连接池
async def creat_pool(loop, **kw):
    logging.info('creat database connection pool...')
    global __pool

    #创建连接池
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf-8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

#查询数据, 默认大小为None
async def select(sql, args, size=None):
    log(sql)
    global __pool
    with (await __pool) as conn:
        try:
            cur = await conn.cursor()

