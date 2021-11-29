# -*- coding:utf-8 -*-
import base64
import json
import os
import uuid

import web

urls = (
    '/api/transform', 'Transform'
)


class Transform:
    _allow_params = {
        'html2pdf': [
            '--page-height',
            '--page-width',
            '--margin-top',
            '--margin-bottom',
            '--margin-left',
            '--margin-right',
        ],
        'html2image': [
            '--crop-h',
            '--crop-w'
        ]
    }

    def __init__(self):
        pass

    @staticmethod
    def __generate_command_params(options, method):
        command_option = ""
        keys = Transform._allow_params[method]
        for option in options:
            if option['label'] in keys:
                command_option = command_option + " " + option['label'] + " " + option['value']
        return command_option

    @staticmethod
    def html2pdf(body):
        filename = uuid.uuid4().hex
        suffix = 'pdf'
        with open(f"/tmp/{filename}.html", "w+") as f:
            f.write(body['htmlContent'])

        # 接收前端传递的参数并通过参数生成命令
        command_option = Transform.__generate_command_params(body['options'], 'html2pdf')

        command = f"wkhtmltopdf {command_option} /tmp/{filename}.html /tmp/{filename}.{suffix}"

        # 执行命令生成pdf文件
        res = os.system(command)
        print(res)

        # 读取生成的pdf文件,将文件内容转为base64编码
        with open(f"/tmp/{filename}.{suffix}", "rb") as f:
            data = base64.b64encode(f.read()).decode('utf-8')

        # 删除生成的缓存文件
        os.remove("/tmp/" + filename + ".html")
        os.remove("/tmp/" + filename + ".pdf")
        return data

    @staticmethod
    def html2image(body):
        filename = uuid.uuid4().hex
        suffix = 'png'
        with open("/tmp/" + filename + ".html", "w+") as f:
            f.write(body['htmlContent'])

        # 接收前端传递的参数并通过参数生成命令
        command_option = Transform.__generate_command_params(body['options'], 'html2image')

        command = f"wkhtmltoimage {command_option} /tmp/{filename}.html /tmp/{filename}.{suffix}"

        # 执行命令生成pdf文件
        res = os.system(command)
        print(res)

        # 读取生成的pdf文件,将文件内容转为base64编码
        with open(f"/tmp/{filename}.{suffix}", "rb") as f:
            data = base64.b64encode(f.read()).decode('utf-8')

        # 删除生成的缓存文件
        os.remove("/tmp/" + filename + ".html")
        os.remove("/tmp/" + filename + ".png")
        return data

    def pdf2image(self):
        # image
        pass

    def POST(self):
        body = json.loads(web.data())
        try:
            if 'method' not in body.keys():
                raise Exception('参数错误,method不能为空')

            data = ''
            if body['method'] == 'html2image':
                data = self.html2image(body)

            if body['method'] == 'html2pdf':
                data = self.html2pdf(body)

            return json.dumps({'code': 200, 'message': 'Success', 'data': data})
        except BaseException as e:
            return json.dumps({'code': 500, 'message': str(e)})


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
