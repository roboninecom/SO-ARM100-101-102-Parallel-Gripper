<!-- translation-navigation -->
[English](../../../en/simulation/webots/README.md) · [Русский](../../../ru/simulation/webots/README.md) · [Español](../../../es/simulation/webots/README.md) · [Français](../../../fr/simulation/webots/README.md) · [Deutsch](../../../de/simulation/webots/README.md) · [Português (Brasil)](../../../pt-BR/simulation/webots/README.md) · [简体中文](../../../zh-CN/simulation/webots/README.md) · [日本語](README.md) · [हिन्दी](../../../hi/simulation/webots/README.md) · [العربية](../../../ar/simulation/webots/README.md)

[英語原文](../../../../../simulation/webots/README.md)

[日本語](../../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="webots"></a>
# Webots

> **状態: 不安定** -- Webots インテグレーションの作業はありますが,性能とレンダリングの問題が知られています. ドーカーのみ使用は推奨されます.

Webots シミュレーション `webots_ros2_control`. 労働組合 Webots ドライバーはコントローラーマネージャーを埋め込みます

<a id="prerequisites"></a>
## 前提条件

**ドッカー (推奨):**
- ドッカーデスクトップ

**原産 ROS2:**
- ROS2 謙虚
- [Webots](https://cyberbotics.com/) R2023b+
- `ros-humble-webots-ros2`
- `urdf2webots` パッケージ

<a id="launch"></a>
## 打ち上げ

<a id="docker"></a>
### ドーカー

```bash
cd simulation/so_arm_101_description
docker compose run webots
```

> **注記**: Webots ドーカーサービスには音量計がない 世界ファイルは 作成時に画像の中に生成されます. URDFを改変する場合は: `docker compose build webots`.

<a id="native-ros2"></a>
### 原産 ROS2

```bash
pip install urdf2webots

# Generate the Webots world file
python scripts/setup_webots.py

# Generate pre-expanded URDF for the Webots driver
xacro urdf/so_101.urdf.xacro sim_backend:=webots > urdf/so_101_webots.urdf

# Launch
ros2 launch so_arm_101_description sim.launch.py sim:=webots
```

<a id="how-it-works"></a>
## 働き方

1. `scripts/setup_webots.py` URDF を A に変換する Webots ロボットノード `urdf2webots` 生産する `worlds/webots_sim.wbt`
2. 労働組合 `WebotsLauncher` 世界ファイルを開く Webots
3. `WebotsController` IPCでロボットに接続し `ros2_control` 運転手
4. 制御器 `<extern>` 世界ファイルでタグは許可する `webots_ros2_driver` 引き継ぐ
5. 前もって拡張されたURDF (`so_101_webots.urdf`) が必要である. `WebotsController` ファイルパスが必要で,インラインXMLではありません

<a id="world-settings"></a>
### 世界 の 状況

- `basicTimeStep`: 16ms (物理安定のためにデフォルトから削減)
- `maxContactJoints`: 4 (詳細なメッシュによる衝突上の負担を制限する)

<a id="known-issues"></a>
## 知られる 問題

- **X11 上にゆっくりと世界加載**レンダリングがX11で転送される時,世界には約120秒かかります. コントローラー・スポナータイムアウトは 180sに設定されています
- **Windows でワイヤフレームレンダリング**: VcXsrv は OpenGL 1.4 しか提供していないが Webots OpenGL 3.3 を必要とする. シミュレーションが実行されますが,ワイヤフレームモードでレンダリングします.
- **WSL2検出**: WSL2のドッカーがWSLカーネル名を継承し, `webots_ros2_driver` 探す `webots.exe`. ドッカーファイルのパッチ `is_wsl()` 必ず戻る `False`.
- **物理の警告**: "あなたの世界は複雑すぎる"という警告が高ポリ衝突網によって現れるかもしれません

<a id="troubleshooting"></a>
## 問題解決

- **`WEBOTS_HOME` 見つかりませんでした**: 確保する `WEBOTS_HOME=/usr/local/webots` 設定されています. ドーカー画像は自動的に設定します
- **コントローラータイムアウト**: 制御器が起動できなければ, `launch/sim.launch.py` (現在180年代)
- **ディスプレイなし**: Webots X11が必要だ Windows で,VcXsrv を `-ac -wgl` 旗を
<!-- /translated-content -->
