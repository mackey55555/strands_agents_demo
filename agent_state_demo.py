from strands import Agent
from strands.models import BedrockModel
import json

# 状態管理機能を持つエージェントを作成
state_agent = Agent(
    model=BedrockModel(
        model_id="deepseek.v3-v1:0",
        region_name="ap-northeast-1",
    ),
    system_prompt="あなたは状態を管理できるアシスタントです。ユーザーの設定や好みを記憶し、それに基づいて行動してください。"
)

print("=== Strands Agents 状態管理デモ ===\n")

# エージェントの状態を管理する辞書
agent_state = {
    "user_preferences": {},
    "conversation_context": {},
    "session_data": {},
    "current_mode": "normal"
}

def update_state(key, value):
    """エージェントの状態を更新"""
    agent_state[key] = value
    print(f"🔄 状態更新: {key} = {value}")

def get_state(key):
    """エージェントの状態を取得"""
    return agent_state.get(key, None)

def display_state():
    """現在の状態を表示"""
    print("\n📊 現在のエージェント状態:")
    for key, value in agent_state.items():
        print(f"  {key}: {value}")
    print()

# デモ1: ユーザー設定の保存と適用
print("【デモ1: ユーザー設定の保存と適用】")
update_state("user_preferences", {
    "language": "日本語",
    "response_style": "詳細",
    "technical_level": "中級",
    "favorite_topics": ["プログラミング", "AI", "データサイエンス"]
})

response1 = state_agent("私の設定に基づいて、Pythonの基本について教えてください。")
print(f"エージェント: {response1}\n")

# デモ2: 会話コンテキストの管理
print("【デモ2: 会話コンテキストの管理】")
update_state("conversation_context", {
    "current_topic": "Pythonプログラミング",
    "discussion_level": "基本概念",
    "last_question": "Pythonの基本について"
})

response2 = state_agent("前の質問に関連して、Pythonの変数について詳しく教えてください。")
print(f"エージェント: {response2}\n")

# デモ3: セッションデータの蓄積
print("【デモ3: セッションデータの蓄積】")
update_state("session_data", {
    "questions_asked": 2,
    "topics_covered": ["Python基本", "Python変数"],
    "user_satisfaction": "高"
})

response3 = state_agent("これまでの会話を振り返って、次に何を学ぶべきか提案してください。")
print(f"エージェント: {response3}\n")

# デモ4: モード切り替え
print("【デモ4: モード切り替え】")
update_state("current_mode", "expert")
print("モードを「専門家」に切り替えました。")

response4 = state_agent("専門家モードで、Pythonの高度な機能について教えてください。")
print(f"エージェント: {response4}\n")

# デモ5: 状態の確認とリセット
print("【デモ5: 状態の確認とリセット】")
display_state()

print("状態をリセットします...")
agent_state = {
    "user_preferences": {},
    "conversation_context": {},
    "session_data": {},
    "current_mode": "normal"
}

response5 = state_agent("状態がリセットされました。新しい会話を始めましょう。")
print(f"エージェント: {response5}\n")

# デモ6: 状態に基づくパーソナライゼーション
print("【デモ6: 状態に基づくパーソナライゼーション】")
update_state("user_preferences", {
    "name": "田中さん",
    "experience_level": "初心者",
    "learning_goal": "Web開発",
    "available_time": "週末のみ"
})

response6 = state_agent("私の学習状況に合わせて、効率的な学習プランを提案してください。")
print(f"エージェント: {response6}\n")

display_state()

print("=== デモ終了 ===")
