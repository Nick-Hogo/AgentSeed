# FastAPI + HTML 入门示例

这个目录是一个独立的教程示例，不依赖主项目中的 `main.py` 和 `static/` 目录。

## 启动服务

在项目根目录执行：

```bash
python -m uvicorn tutorial.web_basics.main:app --reload
```

如果当前 Python 不支持带连字符的模块路径，可以先进入本目录再启动：

```bash
cd tutorial/web-basics
python -m uvicorn main:app --reload
```

然后打开浏览器访问：

```text
http://127.0.0.1:8000
```

`index.html` 保持和教程中的代码一致：点击“发送”后，页面内的 JavaScript 会直接将输入内容转换为大写并更新标题。`main.py` 中的 FastAPI 接口用于配合教程后续讲解 HTTP 请求和前后端分离。

## 目录说明

```text
web_basics/
├── README.md
├── index.html  # 前端页面：HTML、CSS 和 JavaScript
└── main.py     # 后端接口：FastAPI 和 POST /
```
