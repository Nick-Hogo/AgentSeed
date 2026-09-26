from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


BASE_DIR = Path(__file__).parent
app = FastAPI()


# 请求体：定义客户端提交的数据结构
class InputData(BaseModel):
    value: str


@app.get("/")
def get_page() -> FileResponse:
    """返回前端页面。"""
    return FileResponse(BASE_DIR / "index.html")


@app.post("/")
def process_data(request: InputData) -> dict[str, str]:
    """将输入全部大写，然后返回给客户端。"""
    result = request.value.strip().upper()

    # 返回结果：将处理后的数据封装成字典，也称为响应体。
    return {
        "result": result,
    }
