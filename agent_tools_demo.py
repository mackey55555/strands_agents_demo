from strands import Agent
from strands.models import BedrockModel
from strands.tools import Tool
import json
import datetime
import random

# カスタムツールを定義
def get_weather(city: str) -> str:
    """指定された都市の天気を取得します"""
    # 実際のAPIの代わりにサンプルデータを返す
    weather_data = {
        "東京": {"temperature": "22°C", "condition": "晴れ", "humidity": "65%"},
        "大阪": {"temperature": "25°C", "condition": "曇り", "humidity": "70%"},
        "名古屋": {"temperature": "23°C", "condition": "雨", "humidity": "80%"},
        "福岡": {"temperature": "26°C", "condition": "晴れ", "humidity": "60%"}
    }
    
    if city in weather_data:
        data = weather_data[city]
        return f"{city}の天気: {data['condition']}, 気温: {data['temperature']}, 湿度: {data['humidity']}"
    else:
        return f"申し訳ありませんが、{city}の天気情報が見つかりませんでした。"

def calculate_math(expression: str) -> str:
    """数学的な計算式を評価します"""
    try:
        # 安全な計算のため、基本的な演算子のみ許可
        allowed_chars = set('0123456789+-*/.() ')
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            return f"{expression} = {result}"
        else:
            return "無効な文字が含まれています。数字と基本的な演算子（+, -, *, /, (, )）のみ使用してください。"
    except Exception as e:
        return f"計算エラー: {str(e)}"

def get_random_fact() -> str:
    """ランダムな興味深い事実を返します"""
    facts = [
        "ハチミツは永遠に腐りません。",
        "人間の脳は約75%が水でできています。",
        "地球の大気の約21%は酸素です。",
        "光の速度は秒速約30万キロメートルです。",
        "アマゾン川は世界で最も長い川です。"
    ]
    return random.choice(facts)

# ツールを定義
weather_tool = Tool(
    name="get_weather",
    description="指定された都市の天気情報を取得します",
    function=get_weather
)

math_tool = Tool(
    name="calculate_math",
    description="数学的な計算式を評価します",
    function=calculate_math
)

fact_tool = Tool(
    name="get_random_fact",
    description="ランダムな興味深い事実を返します",
    function=get_random_fact
)

# ツールを持つエージェントを作成
tool_agent = Agent(
    model=BedrockModel(
        model_id="deepseek.v3-v1:0",
        region_name="ap-northeast-1",
    ),
    system_prompt="あなたは様々なツールを使って質問に答えるアシスタントです。必要に応じて適切なツールを使用してください。",
    tools=[weather_tool, math_tool, fact_tool]
)

print("=== Strands Agents ツール呼び出しデモ ===\n")

# デモ1: 天気情報の取得
print("【デモ1: 天気情報の取得】")
response1 = tool_agent("東京の天気を教えてください。")
print(f"エージェント: {response1}\n")

# デモ2: 数学計算
print("【デモ2: 数学計算】")
response2 = tool_agent("(15 + 25) * 3 - 10 を計算してください。")
print(f"エージェント: {response2}\n")

# デモ3: ランダムな事実
print("【デモ3: ランダムな事実】")
response3 = tool_agent("面白い事実を教えてください。")
print(f"エージェント: {response3}\n")

# デモ4: 複合的な質問
print("【デモ4: 複合的な質問】")
response4 = tool_agent("大阪の天気を教えて、それから今日の日付を教えてください。")
print(f"エージェント: {response4}\n")

# デモ5: ツールの組み合わせ
print("【デモ5: ツールの組み合わせ】")
response5 = tool_agent("数学の問題を解いて、それから興味深い事実も教えてください。問題は 100 / 4 + 15 です。")
print(f"エージェント: {response5}\n")

print("=== デモ終了 ===")
