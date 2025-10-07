from strands import Agent
from strands.models import BedrockModel

# 複数のエージェントを作成
# 1. 質問者エージェント
questioner = Agent(
    model=BedrockModel(
        model_id="deepseek.v3-v1:0",
        region_name="ap-northeast-1",
    ),
    system_prompt="あなたは好奇心旺盛な質問者です。技術的なトピックについて深く掘り下げた質問をします。"
)

# 2. 専門家エージェント
expert = Agent(
    model=BedrockModel(
        model_id="deepseek.v3-v1:0",
        region_name="ap-northeast-1",
    ),
    system_prompt="あなたはAI技術の専門家です。複雑な技術概念を分かりやすく説明し、実例を交えて回答します。"
)

# 3. 批判者エージェント
critic = Agent(
    model=BedrockModel(
        model_id="deepseek.v3-v1:0",
        region_name="ap-northeast-1",
    ),
    system_prompt="あなたは批判的思考を持つレビュアーです。提示された内容の限界や課題点を指摘し、より良いアプローチを提案します。"
)

print("=== Strands Agents 複数エージェント会話デモ ===\n")

# エージェント間の会話をシミュレート
topic = "大規模言語モデルの限界について"

print(f"【トピック】: {topic}\n")

# 1. 質問者からの質問
question = questioner(f"「{topic}」について、現在の技術的課題と将来の展望を教えてください。")
print(f"🤔 質問者: {question}\n")

# 2. 専門家の回答
expert_response = expert(f"質問: {question}\n\nこの質問に専門家として詳しく回答してください。")
print(f"👨‍💻 専門家: {expert_response}\n")

# 3. 批判者の視点
critic_response = critic(f"専門家の回答: {expert_response}\n\nこの回答について批判的な視点から検討し、改善点や見落とされた点があれば指摘してください。")
print(f"🔍 批判者: {critic_response}\n")

# 4. 専門家の再回答（批判を受けて）
final_response = expert(f"批判者の指摘: {critic_response}\n\nこの批判を踏まえて、よりバランスの取れた回答をしてください。")
print(f"👨‍💻 専門家（再回答）: {final_response}\n")

print("=== デモ終了 ===")
