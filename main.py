"""AgentSeed 第三章：将命令行对话展示为一个最小的 Chat Web。"""

from pathlib import Path

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field


base_url = "https://api.example.com/v1/messages"
api_key = "sk-xxxx"
model = "claude-fable-5"
system_prompt = "请用轻松、亲切、自然的语气交流，表达简洁，有幽默感。" # 设置模型的身份和行为
messages: list[dict[str, str]] = []  # 保存本次对话的历史消息

BASE_DIR = Path(__file__).parent
MAX_TOKENS = 1024

app = FastAPI(title="AgentSeed Chat")

class MessageRequest(BaseModel):
    """描述发送消息接口接收的请求体。"""

    content: str = Field(min_length=1, max_length=2000)


@app.post("/api/messages")
def create_message(request: MessageRequest) -> dict[str, str]:
    """接收用户消息，调用模型，并保存模型回复。"""

    messages.append({"role": "user", "content": request.content})

    try:
        response = httpx.post(
            base_url,
            headers={
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
            },
            json={
                "model": model,
                "max_tokens": MAX_TOKENS,
                "system": system_prompt,
                "messages": messages,
            },
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        assistant_content = "".join(
            block["text"]
            for block in data["content"]
            if block["type"] == "text"
        )
    except (httpx.HTTPError, KeyError, IndexError, TypeError, ValueError) as exc:
        # 保留已经加入的用户消息，方便通过 GET 观察请求过程；本轮回复失败。
        raise HTTPException(status_code=502, detail="模型服务调用失败") from exc

    assistant_message = {"role": "assistant", "content": assistant_content}
    messages.append(assistant_message)
    return assistant_message

# 访问 / 时返回前端页面；API 路由定义在挂载静态目录之前。
app.mount("/", StaticFiles(directory=BASE_DIR / "static", html=True), name="static")
