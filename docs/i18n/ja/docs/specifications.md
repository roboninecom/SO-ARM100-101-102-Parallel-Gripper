<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](../../es/docs/specifications.md) · [Français](../../fr/docs/specifications.md) · [Deutsch](../../de/docs/specifications.md) · [Português (Brasil)](../../pt-BR/docs/specifications.md) · [简体中文](../../zh-CN/docs/specifications.md) · [日本語](specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[英語原文](../../../specifications.md)

[日本語](../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-100101-parallel-follower-gripper"></a>
# SO ARM 100/101 平行フォロワーグリッパー

<a id="overview"></a>
## 概要

設計された軽量3Dプリントエンドエフェクター **Robonine** オープンソースの遠隔操作ロボットプラットフォーム SO ARM 100/101 このメカニズムは,教育および実験的な幅広い用途のために信頼性の高い平行な jaws動きと十分な握力を提供します.

![フォロワーグリッパーを設置する SO-ARM100](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*フォロワーグリッパーを設置する SO-ARM100 ロボット腕*

<a id="key-features"></a>
## 主要 な 特徴

- オープンソースデザイン
- グリッパー一台の部品費用：~$62
- 一般向け FDM 3D プリンターで一回の印刷で作製できます
- 人気ビデオカメラと互換性:
  - Orbbec 双子座 2
  - RealSense D405, D435/D435i, D455
  - GC2093 2MPのUSBカメラモジュール
  - IMX335 5MPのUSBカメラ

---

<a id="dimensions"></a>
## 寸法

<a id="3d-overview"></a>
### 3D概要

![グリッパー寸法  ⁇ 同位数表示](../../../../assets/images/specification/08-gripper-dimensions-3d.png)

*総尺寸を示す同位数表示: 128 × 109 × 130.5 mm,フルストロー 84 mm*

| 寸法 | 価値 |
|-----------|-------|
| 幅 | 128mm |
| 深さ | 130.5 mm |
| 高さ | 109mm |
| 完全な脳卒中 | 84mm |

---

<a id="mounting-interface"></a>
## マウントインターフェイス

![設置インターフェースの尺寸](../../../../assets/images/specification/03-mounting-interface.jpg)

*ロボット腕の固定用の穴パターン付きのフロンジを設置する*

| 特徴 | 寸法 |
|---------|-----------|
| マンションフロング直径 | Ø20mm |
| 中央穴 | Ø7mm |
| 設置穴 | 4x Ø3.2mm |

---

<a id="gripper-parameters"></a>
## グリッパーの仕様

| パラメーター | フォロワーアームのグリッパー |
|-----------|------------------|
| 組み立て量 (PLA,30%充填) | 170 g |
| 最大の握力 | 120 N |
| 握りの最大速度 | 14 mm/s |
| 完全な脳卒中 | 84mm |
| 繰り返し性 | 0.5mm |
| DOF | 1 |

---

<a id="technical-specifications"></a>
## 技術仕様

<a id="materials--construction"></a>
### 材料 & 建設

| 構成要素 | 仕様 |
|-----------|---------------|
| 原材料 | PETG / PLA |
| 送信 | ラックとピニオン |
| ガイド | 丸いアルミニウム/炭素管 (Ø6 mm) |
| 運転手 | Feetech サーボアクチュエーター STS3215 |

<a id="servo-parameters-feetech-sts3215"></a>
### セルボパラメータ (Feetech STS3215)

| パラメーター | 価値 |
|-----------|-------|
| 動作電圧範囲 | 12V |
| スピード (負荷なし) | 45 RPM |
| 走動電流 (負荷なし) | 180mA |
| ストールトーク (ロック) | 30kg·cm |
| 停電電 (ロック) | 2.7 A |
| 静止電流 (停止) | 30mA |
| 定格トルク | 10kg·cm |
| 定位電流 | 900mA |
| ターミナル抵抗 | 1 Ω |
| 動作温度 | -20°C ~ 60°C |
| エンコードタイプ | 絶対磁気12ビット |
| 制御プロトコル | RS485/TTL 最大1 Mbps |
| 電子保護 | 高電圧,電流,負荷,温度に対して |

---

<a id="camera-compatibility"></a>
## カメラ互換性

フォローワーグリッパは,交換可能なカメラホルダーを通じて様々なカメラと互換性がある.

![グリッパーに搭載された異なるカメラ](../../../../assets/images/specification/09-camera-types.png)

*グリッパーに搭載された異なるカメラ (左から右へ): RealSense,USBカメラモジュール, Orbbec 双子座 2*

<a id="supported-cameras"></a>
### 支援カメラ

| カメラ | タイプ | 注記 |
|--------|------|-------|
| IMX335 5MP USB | RGB | コンパクトで安価 |
| GC2093 2MP USB | RGB | 予算オプション |
| Orbbec 双子座 2 | RGB-D | 深度感知 |
| RealSense D405 | RGB-D | 接近深度 |
| RealSense D435/D435i | RGB-D | 一般的な目的 |
| RealSense D455 | RGB-D | 長距離深さ |

---

<a id="supplied-resources"></a>
## 供給された資源

- 3Dプリントのための STLファイルの完全なセット
- 組み立てガイド
- 組み立ての尺寸を持つ図
- ロボットシミュレーターのための URDFファイル

---

<a id="integration"></a>
## 統合

このグリッパは,標準のマウントングフラージュを通じて便利でシンプルな設置のおかげで,無数のロボットシステムに独立して統合できます.

<a id="mounting-requirements"></a>
### 増える 必要

- 4x M3 スイッチ
- 互換性 SO-ARM100/101 ロボット腕
- 他のロボット腕に利用可能なカスタマイズされたアダプタープレート

<a id="communication"></a>
### コミュニケーション

- TTLまたはRS485による連続接続
- バード速度は:最大1 Mbps
- プロトコル: Feetech STSプロトコル

---

<a id="product-specification-documents"></a>
## 製品仕様文書

- [パラレルグリッパー製品の仕様 (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf) ⁇  ロボ9による平行グリッパーに関する完全な製品仕様
- [SO-ARM101 製品仕様 (PDF)](../../../SO-ARM101%20by%20Robo9.pdf) ⁇  完全製品規格 SO-ARM101 ロボ9によるロボット腕

---

*実際の実施と試験に基づく変更の対象となる仕様*
<!-- /translated-content -->
