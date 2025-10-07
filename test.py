from strands import Agent
from strands.models import BedrockModel

agent = Agent(
    model=BedrockModel(
        model_id="deepseek.v3-v1:0",
        region_name="ap-northeast-1",
    )
)

print(agent("AIエージェントについて教えてください"))
