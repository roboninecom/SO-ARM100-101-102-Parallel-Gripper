<!-- translation-navigation -->
[English](../../en/examples/README.md) · [Русский](../../ru/examples/README.md) · [Español](../../es/examples/README.md) · [Français](../../fr/examples/README.md) · [Deutsch](../../de/examples/README.md) · [Português (Brasil)](../../pt-BR/examples/README.md) · [简体中文](../../zh-CN/examples/README.md) · [日本語](README.md) · [हिन्दी](../../hi/examples/README.md) · [العربية](../../ar/examples/README.md)

[英語原文](../../../../examples/README.md)

[日本語](../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="examples---parallel-gripper"></a>
# 例 - 平行グリッパー

このディレクトリには,さまざまなシナリオで並行グリッパーを使用する方法を示す例コードが含まれています.

<a id="available-examples"></a>
## 入手可能な例

<a id="basic_usagepy"></a>
### `basic_usage.py`
基本的なグリッパー操作を示します.
- グレープに接続する
- 特定のポジションに移行
- 読み込み状況情報
- 基本エラー処理

**使用:**
```bash
cd examples
python basic_usage.py
```

<a id="configuration"></a>
## 構成

既存のグリッパーを接続する SO-ARM100/101 セルボバスとコントローラー
制御器のUSBシリアルポートを設定する `STS_ID` グレーパーセルボID (通常6点) SO-ARM101),
そのポートを使って他のアプリケーションを閉じる.

実行例の前に,設定パラメータを調整する必要があります.

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

<a id="common-issues"></a>
## 一般 的 な 問題

<a id="connection-problems"></a>
### 接続 問題
- **窓**: デバイスマネージャーを正しくCOMポートをチェック
- **Linux**: ユーザがシリアルポートにアクセスできるようにする (`sudo usermod -a -G dialout $USER`)
- **macOS**使用: `/dev/cu.usbserial-*` または `/dev/tty.usbserial-*`

<a id="permission-errors"></a>
### 許可の誤り
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

<a id="stservo-sdk-issues"></a>
### STServo SDKの問題
確認してください STServo SDKが正しくインストールされている:
1. クローン [Feetech STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python).
2. 複製 `STservo_sdk` フォルダ (フォルダーそのものを含む) に `software/python/` ディレクトリ

<a id="creating-your-own-examples"></a>
## 自分 の 模範 を 作る

新しい例を作成する際:

1. **握手モジュールを輸入する**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **間違いを優雅に処理する**
   ```python
   try:
       gripper = ParallelGripper()
       if not gripper.connect():
           print("Connection failed!")
           return
       # Your code here
   finally:
       gripper.disconnect()
   ```

3. **適切な文書を記載する**
   - 模範 の 意味 を 明瞭 に 説明 する
   - 必要なハードウェア設定
   - 予想される行動

<a id="safety-notes"></a>
## 安全記号

⚠️ **重要 な 安全 の 考慮:**
- 常に温度と電流を監視する
- 誤差処理を適切に実施する
- まず低力テスト
- 適切な機械の設置を確保する
- 動いている部分から指を遠ざけてください

<a id="contributing-examples"></a>
## 貢献する例

新しい例を歓迎します! 頼む
- 既存のコードスタイルに従います
- 詳細なコメントを記載する
- 提出する前に徹底的に検査する
- この README にエントリを追加する

---

**楽しいコード化!** 🤖
<!-- /translated-content -->
