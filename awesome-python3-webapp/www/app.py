# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

'起始页面'

__author__ = 'SunLang'

def index(request):
    #返回响应的内容, 要指定类型和, charset
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset="utf-8")

async def init(loop):

    app = web.Application(loop=loop)
    #当主url后面跟的/时,调用index()
    app.router.add_route('GET', '/', index)
    #异步
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

#获取时间循环
loop = asyncio.get_event_loop()
#运行直到完成
loop.run_until_complete(init(loop))
#运行到永远,一直运行
loop.run_forever()