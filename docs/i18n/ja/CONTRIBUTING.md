<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[英語原文](../../../CONTRIBUTING.md)

[日本語](README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing-to-open-source-parallel-gripper"></a>
# オープンソースのパラレルグリッパーへの貢献

このプロジェクトにご協力いただきありがとうございました! ロボット界からの貢献を歓迎します

<a id="ways-to-contribute"></a>
## 寄付 する 方法

<a id="-bug-reports"></a>
### ⁇  バグ報告
- GitHub の問題追跡器を使用する
- 詳細な繁殖手順を含みます
- システム情報 (OS, Python バージョン,セルボモデル)
- ログやエラーメッセージを添付する

<a id="-feature-requests"></a>
### ⁇  特色要求
- 既存の問題を最初に確認する
- 使用事例を明確に記述する
- 実施の複雑さを考慮する
- 大規模な変更前に メンテナンス担当者達と話し合う

<a id="-code-contributions"></a>
### ⁇  コード貢献
- 貯蔵庫をフォークする
- 機能ブランチを作成する
- コード付け基準に従う
- 必要に応じてテストを追加する
- 更新ドキュメント

<a id="-documentation"></a>
### ⁇  文書
- 既存のドキュメントの改善
- 使用例を追加する
- チュートリアルやガイドを作成する
- 字体誤りや不明の説明を修正する

<a id="-hardware-improvements"></a>
### ⁇ ️ ハードウェア改良
- デザインの変更や改善
- 代替部品の提案
- 新しいセルボ互換性
- メカニカル最適化

<a id="development-setup"></a>
## 開発設定

1. **リポジトリをクローンする**
   ```bash
   git clone https://github.com/your-org/parallel-gripper.git
   cd parallel-gripper
   ```

2. **依存をインストールする**
   ```bash
   pip install -r software/python/requirements.txt
   ```

3. **インストール STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cp -r STServo_SDK_Python/STservo_sdk ./software/python/
   ```

<a id="coding-standards"></a>
## プログラミング基準

<a id="python-code"></a>
### Python コード
- PEP 8 のスタイルガイドに従ってください
- 適切な場合,タイプヒントを使用する
- すべての関数/クラスに docstrings を追加する
- 最大線長さ: 88文字
- 意味のある変数名を使用する

<a id="documentation"></a>
### 文書化
- マークダウン形式を使用する
- コードの例を含める
- 言語 を 明瞭 に し て,簡潔 に する
- 必要に応じて README を更新する

<a id="3d-models"></a>
### 3Dモデル
- バイナリ形式でSTLファイルを提供する
- 可能な限りソースファイル (STEP,Fusion 360,など) を含む.
- 送信前にテストプリント
- 文書印刷設定

<a id="pull-request-process"></a>
## 引き出願プロセス

1. **始める前に**
   - 既存の問題とPRをチェック
   - 重要な 変化 を 話し合う
   - 変化をテストできるようにしてください

2. **変化 を する**
   - 記述式のブランチ名を作成
   - 明確なメッセージで原子的な約束をする
   - 変化 を よく 試す
   - 必要に応じてドキュメントを更新する

3. **PRを提出する**
   - PR テンプレートを記入する
   - リンク関連問題
   - 変更の明確な説明を提供する
   - 試験情報を含める

4. **審査プロセス**
   - アドレス審査員からのフィードバック
   - 建設 的 な 議論 を する
   - 審査過程で忍耐強く

<a id="testing-guidelines"></a>
## 試験ガイドライン

<a id="software-testing"></a>
### ソフトウェアテスト
- ハードウェアの設定をテストする
- プラットフォーム間互換性を確認する
- エラー処理をチェック
- 試験縁ケース

<a id="hardware-testing"></a>
### ハードウェアテスト
- 3Dプリントが正しく動作していることを確認する
- 試験組成手順
- 機械的許容量を確認する
- 異なる材料で検証する

<a id="communication"></a>
## コミュニケーション

<a id="channels"></a>
### チャンネル
- GitHubの問題:バグ報告,機能要求
- GitHub 議論: 一般的な質問,アイデア
- 撤回要請:コードレビュー,技術論議

<a id="guidelines"></a>
### ガイドライン
- 尊敬 し,建設 的 な もの を する
- 投稿する前に検索
- 文脈と詳細を記載する
- 可能な限り 他 人 を 助け

<a id="recognition"></a>
## 認識

貢献者は以下の項目で認められる:
- README.md 貢献者セクション
- リリースノート
- プロジェクトドキュメント

<a id="license"></a>
## ライセンス

このプロジェクトには複数のライセンスがあります  ⁇ 参照 [`LICENSING.md`](LICENSING.md) 完全な地図です

寄付を提出することで,その権利があることを証明します.
そして,そのライセンスが適用される
貯蔵庫は:

| 変わってる | あなたの貢献は許可されています |
|---|---|
| ハードウェア / CAD | CERN-OHL-P-2.0 |
| ソフトウェア | Apache-2.0 |
| 文書と画像 | CC BY 4.0 |

つまり,入行 =出行:ファイルが既に保有されているライセンスに関係なく
変更は同じライセンスでします

**第三者の資料** 寄付金には,あなたがしていないものが含まれている場合
引き出しの要求に書いてください
[`NOTICE`](../../../NOTICE). バイナリーを許可できないので
販売業者ツールとファームウェアを含む.

**新しいファイル** 対象となるのは [`REUSE.toml`](../../../REUSE.toml). `reuse lint` 走る
著作権とライセンスが欠けている場合は失敗します.
情報

<a id="questions"></a>
## 質問?

寄付 に つい て の 質問 が ある と いう 場合,本 を 開くか 会話 を 始める の は 無料 です.

---

**このプロジェクトを良くするためにお手伝いありがとうございました!** 🤝
<!-- /translated-content -->
