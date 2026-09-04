import httpx    

base_url = "https://api.example.com/v1/messages"
api_key = "sk-xxxx"
model = "claude-fable-5"

while True: # 持续接收用户输入，实现最基础的命令行对话。
    user_input = input("You> ")

    # 按照 Anthropic Messages API 协议向模型服务发送 HTTP 请求。
    response = httpx.post(
        base_url,
        headers={
            "x-api-key": api_key, # Anthropic 格式的认证信息
            "anthropic-version": "2023-06-01", # Anthropic API 版本
        },
        json={
            "model": model, # 选择的模型名称
            "messages": [
                {"role": "user", "content": user_input}, # 用户输入的消息
            ],
        },
        timeout=60,
    )

    # 将 JSON 响应转换为字典，然后取出模型生成的文本。
    data = response.json()
    print("Assistant>", end=" ")
    for block in data["content"]: # 循环解析LLM返回信息
        if block["type"] == "text":
            print(block["text"], end="")
    print()