from strands import Agent
from strands.models import BedrockModel

# メモリ機能を持つエージェントを作成
memory_agent = Agent(
    model=BedrockModel(
        model_id="deepseek.v3-v1:0",
        region_name="ap-northeast-1",
    ),
    system_prompt="あなたは個人情報を記憶し、継続的な会話ができるアシスタントです。過去の会話内容を参照して、よりパーソナライズされた回答をしてください。"
)

print("=== Strands Agents メモリ機能デモ ===\n")

# セッション1: ユーザー情報の登録
print("【セッション1: ユーザー情報の登録】")
response1 = memory_agent("こんにちは！私は田中太郎です。プログラマーとして働いていて、PythonとJavaScriptを主に使っています。趣味は読書と映画鑑賞です。")
print(f"エージェント: {response1}\n")

# セッション2: 過去の情報を参照した質問
print("【セッション2: 過去の情報を参照】")
response2 = memory_agent("私の趣味について、おすすめの本や映画はありますか？")
print(f"エージェント: {response2}\n")

# セッション3: 技術的な質問（職業情報を参照）
print("【セッション3: 技術的な質問】")
response3 = memory_agent("最近、新しいフレームワークを学びたいと思っているのですが、私のスキルレベルに合ったものを教えてください。")
print(f"エージェント: {response3}\n")

# セッション4: 複合的な質問（複数の過去情報を参照）
print("【セッション4: 複合的な質問】")
response4 = memory_agent("仕事で疲れた時、どのようにリフレッシュすればいいでしょうか？私の趣味も考慮に入れて教えてください。")
print(f"エージェント: {response4}\n")

# セッション5: 情報の確認
print("【セッション5: 情報の確認】")
response5 = memory_agent("私について覚えていることを教えてください。")
print(f"エージェント: {response5}\n")

print("=== デモ終了 ===")
