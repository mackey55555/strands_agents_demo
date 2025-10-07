from strands import Agent
from strands.models import BedrockModel
from pathlib import Path

agent = Agent(
    model=BedrockModel(
        model_id="apac.anthropic.claude-sonnet-4-20250514-v1:0",
        region_name="ap-northeast-1",
    )
)

image1_path = Path("image/test1.png")
image2_path = Path("image/test2.png")

with image1_path.open("rb") as fp:
    image1_bytes = fp.read()

with image2_path.open("rb") as fp:
    image2_bytes = fp.read()

response = agent(
    [
        {"text": "これら2つの画像を比較して、違いを説明してください"},
        {"image": {"format": "png", "source": {"bytes": image1_bytes}}},
        {"image": {"format": "png", "source": {"bytes": image2_bytes}}},
    ]
)

print(response)
