# -*- coding:utf-8 -*-
import base64
import json
import os
import uuid

import web

urls = (
    '/toPDF', 'ToPDF'
)


class ToPDF:
    _allow_params = [
        '',
    ]

    def __init__(self):
        pass

    def GET(self):
        pass

    def POST(self):
        body = json.loads(web.data())

        try:
            filename = uuid.uuid4().hex
            with open("/tmp/" + filename + ".html", "w+") as f:
                f.write(body['htmlContent'])

            # 接收前端传递的参数并通过参数生成命令
            options = body['options']
            command_option = ""
            print options
            for option in options:
                command_option = command_option + " " + option['label'] + " " + option['value']

            command = "wkhtmltopdf /tmp/" + filename + ".html " + command_option + " /tmp/" + filename + ".pdf"

            # 执行命令生成pdf文件
            os.system(command)

            # 读取生成的pdf文件,将文件内容转为base64编码
            with open("/tmp/" + filename + ".pdf", "rb") as f:
                data = base64.b64encode(f.read())

            # 删除生成的缓存文件
            os.remove("/tmp/" + filename + ".html")
            os.remove("/tmp/" + filename + ".pdf")

            return json.dumps({'code': 200, 'message': 'Success', 'data': data})
        except BaseException as e:
            return json.dumps({'code': 500, 'message': str(e)})


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
