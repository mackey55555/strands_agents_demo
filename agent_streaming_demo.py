from strands import Agent
from strands.models import BedrockModel
import time

# ストリーミング対応のエージェントを作成
streaming_agent = Agent(
    model=BedrockModel(
        model_id="deepseek.v3-v1:0",
        region_name="ap-northeast-1",
    ),
    system_prompt="あなたは詳細で包括的な回答をするアシスタントです。長い回答をする際は、段階的に説明してください。"
)

print("=== Strands Agents ストリーミング応答デモ ===\n")

# デモ1: 通常の応答（一括取得）
print("【デモ1: 通常の応答】")
print("質問: 人工知能の歴史について詳しく教えてください。")
print("回答:")
response1 = streaming_agent("人工知能の歴史について詳しく教えてください。")
print(response1)
print("\n" + "="*50 + "\n")

# デモ2: ストリーミング応答のシミュレーション
print("【デモ2: ストリーミング応答のシミュレーション】")
print("質問: 機械学習の種類とそれぞれの特徴について説明してください。")
print("回答（ストリーミング風）:")

# 長い回答を段階的に表示するシミュレーション
long_response = streaming_agent("機械学習の種類とそれぞれの特徴について説明してください。")

# 回答を文単位で分割して段階的に表示
long_response_text = str(long_response)
sentences = long_response_text.split('。')
for i, sentence in enumerate(sentences):
    if sentence.strip():
        print(f"[{i+1:02d}] {sentence.strip()}。")
        time.sleep(0.5)  # ストリーミングの効果をシミュレート

print("\n" + "="*50 + "\n")

# デモ3: リアルタイム対話のシミュレーション
print("【デモ3: リアルタイム対話のシミュレーション】")
print("質問: プログラミング言語の選び方について教えてください。")
print("回答（リアルタイム風）:")

response3 = streaming_agent("プログラミング言語の選び方について教えてください。")

# 単語単位で段階的に表示
response3_text = str(response3)
words = response3_text.split()
for i, word in enumerate(words):
    print(word, end=" ", flush=True)
    time.sleep(0.1)  # より速いストリーミング効果

print("\n\n" + "="*50 + "\n")

# デモ4: 段階的な説明
print("【デモ4: 段階的な説明】")
print("質問: データベース設計の基本原則を段階的に教えてください。")
print("回答:")

response4 = streaming_agent("データベース設計の基本原則を段階的に教えてください。")

# 段落ごとに段階的に表示
response4_text = str(response4)
paragraphs = response4_text.split('\n\n')
for i, paragraph in enumerate(paragraphs):
    if paragraph.strip():
        print(f"\n【ステップ {i+1}】")
        print(paragraph.strip())
        time.sleep(1)  # 各ステップの間で一時停止

print("\n=== デモ終了 ===")
