<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[英語原文](../../../README.md)

[日本語](README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm100101-parallel-gripper"></a>
# SO-ARM100/101 平行グリッパー

<div align="center">

[![SO-ARM101 平行グリッパー](../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

**🎥 [握手機を動かす!](https://youtube.com/shorts/bSyXjgNGXZk)** · **🛒 [購入する SO-ARM102 パラレルグリッパー付きのキット](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

3Dプリントの軽量平行グリッパー **[Robonine](https://robonine.com)** オープンソースの SO-ARM100/101 ロボットプラットフォーム

> パラレルグリッパー付きの ロボット腕セットを 気に入った? **[購入する SO-ARM102 キット](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

[![ハードウェア: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt)
[![ソフトウェア: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt)
[![ドクター: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt)
[![費用: ~$50](https://img.shields.io/badge/Cost-~%2450-green.svg)](docs/bom.md)
[![組み立て時間: 30分](https://img.shields.io/badge/Assembly-30%20min-orange.svg)](docs/assembly-guide.md)

---

**質問? 助けてくれ!**
⁇ メール: [hello@robonine.com](mailto:hello@robonine.com)

</div>

---

<a id="-key-features"></a>
## ✨ 主要な特徴

| 特徴 | 記述 |
|---------|-------------|
| **120N 握手力** | 信頼性の高い並行マハメカニズム |
| **14 mm/s 速度** | グリッパー操作速度 |
| **84mm フルストロー** | 様々な物体への広い開口 |
| **0.5mm 繰り返し性** | 高精度な位置付け |
| **カメラ対応** | サポート RealSense, Orbbec,USBカメラ |
| **3Dプリント可能** | 標準FDMプリンターですべての部品を印刷する |
| **~ $50 総費用** | 安価なオープンソースソリューション |
| **簡単に組み立て** | 30-45基本ツールによる分 |

---

<a id="-gallery"></a>
## ギャラリー

<div align="center">

<a id="gripper-on-so-arm101"></a>
### グリッパーの搭載先： SO-ARM101

![グリッパーの搭載先： SO-ARM101](../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*フォロワーグリッパーが SO-ARM101 ロボット腕*

<a id="dimensions"></a>
### 寸法

![グリッパーの寸法](../../../assets/images/specification/08-gripper-dimensions-3d.png)

*128 × 109 × 130.5 mm,フルストロー 84 mm*

</div>

---

<a id="-specifications"></a>
## ⁇ 仕様

<a id="gripper-parameters"></a>
### グリッパーの仕様

| パラメーター | 価値 |
|-----------|-------|
| 最大の握力 | **120 N** |
| 握りの最大速度 | **14 mm/s** |
| 完全な脳卒中 | **84mm** |
| 繰り返し性 | **0.5mm** |
| 組み立て量 (PLA,30%充填) | **170 g** |
| DOF | **1** |

<a id="dimensions-1"></a>
### 寸法

| 寸法 | 価値 |
|-----------|-------|
| 幅 | 128mm |
| 深さ | 130.5 mm |
| 高さ | 109mm |

<a id="servo-parameters-feetech-sts3215"></a>
### セルボパラメータ (Feetech STS3215)

| パラメーター | 価値 |
|-----------|-------|
| 動作電圧 | 12V |
| ストールトルク | 30kg·cm |
| スピード (負荷なし) | 45 RPM |
| 暗号化 | 絶対磁気12ビット |
| 議定書 | RS485/TTL 最大1 Mbps |
| 動作温度 | -20°C ~ 60°C |

---

<a id="-camera-compatibility"></a>
## ⁇  カメラ互換性

接着器は,交換可能なカメラホルダーを通じて複数のカメラをサポートします.

| カメラ | タイプ | 使用例 |
|--------|------|----------|
| IMX335 5MP USB | RGB | 基本視力課題 |
| GC2093 2MP USB | RGB | 予算オプション |
| Orbbec 双子座 2 | RGB-D | 3D認識 |
| RealSense D405 | RGB-D | 接近深度 |
| RealSense D435/D435i | RGB-D | 一般的な目的 |
| RealSense D455 | RGB-D | 長距離深さ |

<div align="center">

![グリッパーに搭載された異なるカメラ](../../../assets/images/specification/09-camera-types.png)

*RealSense,USBカメラモジュール, Orbbec 双子座 2*

</div>

---

<a id="-bill-of-materials"></a>
## ⁇  資料簿

**総費用: ~$50** ([アマゾンリンクのフルBOM](docs/bom.md))

| カテゴリー | 構成要素 | - エスト 費用 |
|----------|------------|-----------|
| 電子機器 | Feetech STS3215 セルボ | ~$29 |
| ベアリング | MF106ZZ (x2) | ~$2 |
| アルミニウム/炭素管 | D6x1×125mm (x2) | ~$4 |
| 3Dプリント | 8部 (~100-150g PLA) | ~$12 |
| 締結部品 | M2/M4螺旋 ⁇ ,M2ナッツ,M3セット螺旋 ⁇ | ~$3 |

---

<a id="-quick-start"></a>
## ⁇  迅速なスタート

パラレルグリッパー付きのロボットアームキット **[購入する SO-ARM102 キット](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**. 建設のために SO-ARM100/101 手を握って 下の手順に従ってください

<a id="1-print-the-parts-2-4-hours"></a>
### 1. パーツ を 印刷 する (2-4 時間)

STLファイルをダウンロードする [`models/parts/`](models/README.md). 人気プリンターのような互換性 **バンボラボ A1 ミニ**, **プロサ・ミニ+**,および180×180mm以上のベッドを持つ任意のプリンタ.

| 部分 | Qty | 設定 |
|------|:---:|----------|
| メインフレーム (RB9.01.062.010) | 1 | 20% 充填する |
| ジョー (RB9.01.062.020) | 2 | 20% 充填する |
| ラックギア (RB9.01.062.030) | 2 | 100% 充填する |
| 歯車 (RB9.01.062.040) | 1 | 100% 充填する |
| カメラホルダー (RB9.01.060.074) | 1 | 20% 充填する |
| ホルダー (RB9.01.060.080) | 1 | 20% 充填する |
| カメラスペーサー (RB9.01.060.090) | 1 | 20% 充填する |
| D405 保持者 (RB9.01.060.110) | 1 | 20% 充填する |

<a id="2-order-components-1-2-days"></a>
### 2. オーダー構成要素 (1-2日)

見てください [資料の表](docs/bom.md) アマゾンからの直接リンク

<a id="3-assemble-30-45-minutes"></a>
### 3. 組み立て (30-45 分)

フォローする [集会ガイド](docs/assembly-guide.md) ステップ・バイ・ステップ画像:

1. サーボディスクにギアを設置し,このセットをサーボ上にインストールする
2. セルボケーブルを挿入する
3. 使用する Feetech ソフトウェアは,セルボを最小の位置に移動する (ソフトウェア内のスライダーを左へ移動する)
4. ラックギアをジョーに取り付けます
5. ガイドロッドを両方のジョーに通します
6. ベアリングをメインフレームに取り付け、ねじで固定します
7. ガイドロッドをフレームにはめ込みます
8. ジョーを左右の端まで広げます
9. セルボを挿入し,螺栓で固定する
10. カメラ スパッサーとUVCカメラを固定し, 4x螺栓とナッツ M2 (オプション) を用いて固定する
11. ロボット腕へのマウント (オプション)

<a id="4-software"></a>
### 4. ソフトウェア

```bash
# Configure servo motor if necessary
https://lab.robonine.com/tools/robonine/feetech-bus

# Control gripper
https://lab.robonine.com/tools/robonine/control-robot
```

---

<a id="-repository-structure"></a>
## ⁇  リポジトリ構造

```
├── assets/
│   └── images/
│       ├── assembly/          # Assembly step images
│       └── specification/     # Technical drawings
├── docs/
│   ├── assembly-guide.md                # Step-by-step assembly
│   ├── bom.md                           # Bill of materials with links
│   ├── Parallel gripper by Robo9.pdf    # Gripper product specification
│   ├── quick-start.md                   # Getting started guide
│   ├── SO-ARM101 by Robo9.pdf           # SO-ARM101 product specification
│   └── specifications.md               # Technical specifications
├── models/
│   ├── parts/                                    # Individual STL files
│   └── Follower gripper (165x165 bed size).STL   # Complete assembly (165×165mm bed)
├── community/
│   └── histology-slide-gripper/   # Community variant (CAD, MuJoCo model)
├── simulation/
│   ├── README.md                  # Simulation overview
│   ├── gazebo/                    # Gazebo guide
│   ├── mujoco/                    # MuJoCo guide
│   ├── webots/                    # Webots guide
│   ├── coppeliasim/               # CoppeliaSim guide
│   ├── isaac_sim/                 # Isaac Sim guide
│   └── so_arm_101_description/    # ROS2 package (URDF, launch, Docker)
├── software/
│   └── python/                # Control software
├── examples/                  # Usage examples
├── HARDWARE-LICENSE.txt       # CERN-OHL-P-2.0 (CAD, geometry)
├── SOFTWARE-LICENSE.txt       # Apache-2.0 (code)
├── DOCS-LICENSE.txt           # CC BY 4.0 (docs, images)
├── LICENSING.md               # Which licence covers what
├── NOTICE                     # Third-party attribution
├── REUSE.toml                 # Machine-readable licence map
├── RELICENSING.md             # Record of the 2026 relicensing
└── CONTRIBUTING.md
```

---

<a id="-documentation"></a>
## ⁇  文書

| 文書 | 記述 |
|----------|-------------|
| [スピード・スタートガイド](docs/quick-start.md) | 30分以内に走る |
| [集会ガイド](docs/assembly-guide.md) | ステップバイ・ステップ画像 |
| [グリッパー・アセンブリガイド (PDF)](../../Assembly%20Guide%20Follower%20Gripper.pdf) | プリント可能なグリッパー組み立ての指示 |
| [SO-ARM101 集会ガイド (PDF)](../../Assembly%20Guide%20SO-ARM101.pdf) | 満員 SO-ARM101 腕組み立ての指示 |
| [資料の表](docs/bom.md) | アマゾンリンクを含む部品リスト |
| [仕様](docs/specifications.md) | 技術的な詳細 |
| [3Dモデル](models/README.md) | プリント設定とファイル |
| [パラレルグリッパー製品の仕様 (PDF)](../../Parallel%20gripper%20by%20Robo9.pdf) | ロボ9による平行グリッパー製品の仕様 |
| [SO-ARM101 製品仕様 (PDF)](../../SO-ARM101%20by%20Robo9.pdf) | SO-ARM101 ロボ9によるロボット腕製品仕様 |

---

<a id="-hardware-requirements"></a>
## ⁇  ハードウェア要件

<a id="electronics"></a>
### 電子機器
- 1× Feetech STS3215 セルボモーター

握手を既存のものに接続する SO-ARM100/101 セルボバスとコントローラー
ロボットコントローラと電源は,グリッパーBOMの外の腕セットアップの一部です.

<a id="mechanical"></a>
### メカニカル
- 2× MF106ZZ ベアリング (6×10×3mm)
- 2×アルミニウム/炭素チューブ D6x1×125mm

<a id="fasteners"></a>
### 締結部品
- 2×M4×8 DIN 7991 スイッチ
- 4x M2x8 DIN 912 スイッチ
- 4×M2 DIN 934ナッツ
- 4×M3×4 DIN 913セット スイッチ

<a id="tools-required"></a>
### 必要 な 道具
- フリップスヘッドスクリュードライバー (PH1)
- ヘックスキー M2 (H1.5) と M4 (H2.5)

---

<a id="-simulation"></a>
## ⁇ ️シミュレーション

SO-ARM101 は、ROS2 記述パッケージと単一のパラメータ化された URDF により、5 種類の物理エンジンでシミュレーションできます。ROS2 のインストールは不要で、Docker がすべてを処理します。

<div align="center">

| Gazebo (イグニッション砦) | MuJoCo |
|:-:|:-:|
| ![SO-ARM-101 中 Gazebo](../../../assets/images/simulation/gazebo/gazebo_pick_place.png) | ![SO-ARM-101 中 MuJoCo](../../../assets/images/simulation/mujoco/mujoco_pick_place.png) |

</div>

| シミュレーター | 状態 | ドーカー |
|-----------|--------|--------|
| [Gazebo](simulation/gazebo/README.md) | 準備する | `docker compose run gazebo` |
| [MuJoCo](simulation/mujoco/README.md) | 準備する | `docker compose run mujoco` |
| [Webots](simulation/webots/README.md) | 不安定 | `docker compose run webots` |
| [CoppeliaSim](simulation/coppeliasim/README.md) | 試験されていない | 外部シミュレーター |
| [NVIDIA Isaac はい](simulation/isaac_sim/README.md) | 試験されていない | 外部シミュレーター |

**スピードスタート (Docker):**

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

見てください [シミュレーションガイド](simulation/README.md) 完全なセットアップ,建築の詳細と ロボットコマンド

---

<a id="-community-mods"></a>
## ⁇  コミュニティ・モッド

コミュニティによって構築されたグリッパーのバリエーションが,それぞれ自立して [`community/`](../../../community):

| モッド | 作者 | 記述 |
|-----|--------|-------------|
| [ヒストロジー スライドグリッパー](community/histology-slide-gripper/README.md) | [マイケル・ヴィアチェスラフ](https://github.com/histochemichael) | 75 x 25 mm 顕微鏡スライドとステーニングディッパー/ラック用のブタ,そして握手を監視するための角のアルドゥキャムホルダー. |

<div align="center">

<a href="community/histology-slide-gripper/README.md"><img src="../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg" alt="Histology slide gripper mod holding a microscope slide" width="400"></a>

*ヒストロジースライドグリッパーモッド 詳細説明,CADファイル,デモをクリック*

</div>

---

<a id="-contributing"></a>
## ⁇ 貢献

寄付は歓迎する! どうかご自由に:
- ⁇  バグと問題を報告する
- ⁇  新しい機能を提案する
- ⁇  引き寄せ要請を提出する
- 文献の改善

---

<a id="-license"></a>
## ライセンス

著作権 (c) 2025 Robonine. このプロジェクトには複数のライセンスがあります
材料には異なるライセンスがあります.

| 材料 | ライセンス |
|---|---|
| ハードウェアデザイン  ⁇ `models/`,コミュニティ CAD,グリッパーマッシュ | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| ソフトウェア `software/`, `examples/`, `simulation/`, シミュレーションコード `community/` | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| 文書と画像 `docs/`, `assets/`全員 `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

見てください [`LICENSING.md`](LICENSING.md) ファイルごとに正確な地図と
[`REUSE.toml`](../../../REUSE.toml) 機械で読み取れるバージョンについて

**ここには全てない Robonine仕事だ** 労働組合 SO-ARM101 腕のメッシュが取られる
から [TheRobotStudio上流プロジェクトです](https://github.com/TheRobotStudio/SO-ARM100)
そして残る Apache-2.0; ヒストロジックスライドグリッパーは
[@histochemichael](https://github.com/histochemichael). 見てください [`NOTICE`](../../../NOTICE)
網を再利用する前に

リリースまで及び含 `v0.3.1` GPL-3.0で公開され,
これらの条件で利用可能  ⁇ 参照 [`RELICENSING.md`](RELICENSING.md).

---

<a id="-links"></a>
## ⁇ リンク

- [Feetech STS3215 セルボ](https://www.feetechrc.com/525603.html)
- [STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python)

---

<a id="-engineering-team"></a>
## ⁇  エンジニアリングチーム

| 名前 | 役割 | 連絡先 |
|------|------|---------|
| **ボリス・コトフ** | ソフトウェアエンジニア | [テレグラム](https://t.me/bkotov) |
| **アラン・サビン** | 設計技術者 | [リンクイン](https://www.linkedin.com/in/alan-subin/) |

---

<a id="-star-history"></a>
## ⭐ スター履歴

[![スター履歴](https://api.star-history.com/svg?repos=roboninecom/so-arm100-101-parallel-gripper&type=Date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm100-101-parallel-gripper&type=date&legend=top-left)

---

<div align="center">

**ロボットコミュニティのために作られた [Robonine](https://robonine.com)** 🤖

**質問? 助けてくれ!**
⁇ メール: [hello@robonine.com](mailto:hello@robonine.com)

</div>
<!-- /translated-content -->
