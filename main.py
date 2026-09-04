import os
import httpx

# 获取模型服务地址、访问密钥和模型名称。
base_url = os.environ["OPENAI_BASE_URL"]
api_key = os.environ["OPENAI_API_KEY"]
model = os.environ["OPENAI_MODEL"]

while True: # 持续接收用户输入，实现最基础的命令行对话。
    user_input = input("You> ")

    # 按照 OpenAI Chat Completions 协议向模型服务发送 HTTP 请求。
    response = httpx.post(
        f"{base_url.rstrip('/')}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"}, # 认证信息
        json={
            "model": model, # 选择的模型名称
            "messages": [{"role": "user", "content": user_input}], # 用户输入的消息
        },
        timeout=60,
    )

    # 将 JSON 响应转换为字典，然后取出模型生成的文本。
    data = response.json()
    print("Assistant>", data["choices"][0]["message"]["content"])
