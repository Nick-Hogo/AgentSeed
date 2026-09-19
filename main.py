import httpx    

base_url = "https://api.example.com/v1/messages"
api_key = "sk-xxxx"
model = "claude-fable-5"
system_prompt = "你是一只可爱活泼元气猫娘~ 说话末尾带喵～" # 设置模型的身份和行为
messages = [] # 保存本次对话的历史消息

while True: 
    user_input = input("You> ")

    messages.append({"role": "user", "content": user_input}) # 添加用户输入的消息到历史消息列表中

    response = httpx.post(
        base_url,
        headers={
            "x-api-key": api_key, 
            "anthropic-version": "2023-06-01", 
        },
        json={
            "model": model, 
            "max_tokens": 20, # 设置模型最多生成的 Token 数量
            "system": system_prompt, # 设置模型的身份和行为
            "messages": messages, # 历史消息列表
        },
        timeout=60,
    )

    data = response.json()
    assistant_message = "" # 初始化助手回复的消息
    print("Assistant>", end=" ")
    for block in data["content"]: 
        if block["type"] == "text":
            assistant_message += block["text"] # 拼接助手回复的消息
            print(block["text"], end="")
    print()
    messages.append({"role": "assistant", "content": assistant_message}) # 添加助手回复的消息到历史消息列表中