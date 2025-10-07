# Strands Agents Demo Collection

Strands Agentsの様々な機能をデモンストレーションするサンプルコード集です。

## 📁 デモファイル一覧

### 基本デモ
- **`test.py`** - 基本的なエージェントの使用方法
- **`test-prompt.py`** - システムプロンプトの設定例
- **`multi-image.py`** - マルチモーダル（画像処理）のデモ

### 高度な機能デモ
- **`agent_conversation_demo.py`** - 複数エージェント間の会話シミュレーション
- **`agent_memory_demo.py`** - メモリ機能とコンテキスト管理
- **`agent_state_demo.py`** - エージェントの状態管理
- **`agent_streaming_demo.py`** - ストリーミング応答のシミュレーション
- **`agent_tools_demo.py`** - ツール統合の例

## 🚀 セットアップ

### 前提条件
- Python 3.8以上
- AWSアカウント（Bedrockアクセス権限）
- Strands Agentsライブラリ

### インストール
```bash
pip install strands
```

### AWS認証設定
```bash
aws configure
# または環境変数で設定
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=ap-northeast-1
```

## 🎯 各デモの特徴

### 1. 複数エージェント会話 (`agent_conversation_demo.py`)
- **機能**: 質問者、専門家、批判者の3つのエージェントが協働
- **LTポイント**: 役割分担による多角的な視点での問題解決
- **実行**: `python agent_conversation_demo.py`

### 2. メモリ機能 (`agent_memory_demo.py`)
- **機能**: ユーザー情報の記憶と継続的な会話
- **LTポイント**: パーソナライズされた応答とコンテキスト保持
- **実行**: `python agent_memory_demo.py`

### 3. 状態管理 (`agent_state_demo.py`)
- **機能**: エージェントの状態とセッション管理
- **LTポイント**: ユーザー設定の保存とモード切り替え
- **実行**: `python agent_state_demo.py`

### 4. ストリーミング応答 (`agent_streaming_demo.py`)
- **機能**: リアルタイムな回答表示のシミュレーション
- **LTポイント**: ユーザー体験の向上とインタラクティブ性
- **実行**: `python agent_streaming_demo.py`

### 5. ツール統合 (`agent_tools_demo.py`)
- **機能**: 外部ツールとの連携（天気、計算、事実取得）
- **LTポイント**: 動的な情報取得と機能の組み合わせ
- **実行**: `python agent_tools_demo.py`

## 📊 LT用デモ構成

### 推奨デモ順序
1. **基本機能** → 既存のチャットボットとの違い
2. **複数エージェント** → 協働の力
3. **メモリ機能** → 継続的な関係性
4. **ツール連携** → 実用的な機能
5. **ストリーミング** → ユーザー体験
6. **状態管理** → パーソナライゼーション

### 各デモの所要時間
- 基本デモ: 2-3分
- 高度な機能デモ: 5-10分
- 全体デモ: 30-45分

## 🔧 カスタマイズ

### モデル変更
```python
agent = Agent(
    model=BedrockModel(
        model_id="your-model-id",  # モデルIDを変更
        region_name="your-region",  # リージョンを変更
    )
)
```

### システムプロンプトの調整
```python
agent = Agent(
    model=model,
    system_prompt="あなたのカスタムプロンプト"
)
```

## 📝 注意事項

- 各デモは独立して実行可能です
- AWS認証が必要です
- モデルによっては応答時間が異なります
- 大量のリクエストは料金が発生する可能性があります

## 🤝 貢献

プルリクエストやイシューの報告を歓迎します！

## 📄 ライセンス

MIT License
