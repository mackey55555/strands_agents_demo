from strands import Agent
from strands.models import BedrockModel

agent = Agent(
    model=BedrockModel(
        model_id="deepseek.v3-v1:0",
        region_name="ap-northeast-1",
    ),
    system_prompt="日本語の質問に対して英語で回答してください。"
)


print(agent("AIエージェントについて教えてください"))