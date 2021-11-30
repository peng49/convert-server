# convert-server
PDF图片转换，支持html转pdf,html转图片,pdf转图片

[wkhtmltopdf安装包下载](https://wkhtmltopdf.org/downloads.html)

[中文乱码处理](http://gnixner.com/hallo-ninja-986.html)

API
html转pdf
```
POST /api/convert
Content-Type: application/json
{
    "method":"html2pdf",
    "options":[
    
    ],
    "htmlContent": "
    
    "
}
```

html转图片
```
POST /api/convert
Content-Type: application/json
{
    "method":"html2image",
    "options":[
    
    ],
    "htmlContent": "
    
    "
}
```

pdf转图片




