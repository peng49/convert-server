import os

import web

urls = (
    '/toPDF', 'ToPDF'
)

class ToPDF:
    def __init__(self):
        pass

    def GET(self):
        pass

    def POST(self):
        command = "wkhtmltopdf {}"
        os.system(command)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
