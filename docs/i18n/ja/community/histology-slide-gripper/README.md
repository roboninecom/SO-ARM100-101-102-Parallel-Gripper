<!-- translation-navigation -->
[English](../../../en/community/histology-slide-gripper/README.md) · [Русский](../../../ru/community/histology-slide-gripper/README.md) · [Español](../../../es/community/histology-slide-gripper/README.md) · [Français](../../../fr/community/histology-slide-gripper/README.md) · [Deutsch](../../../de/community/histology-slide-gripper/README.md) · [Português (Brasil)](../../../pt-BR/community/histology-slide-gripper/README.md) · [简体中文](../../../zh-CN/community/histology-slide-gripper/README.md) · [日本語](README.md) · [हिन्दी](../../../hi/community/histology-slide-gripper/README.md) · [العربية](../../../ar/community/histology-slide-gripper/README.md)

[英語原文](../../../../../community/histology-slide-gripper/README.md)

[日本語](../../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="histology-slide-gripper-community-mod"></a>
# ヒストロジースライドグリッパー (コミュニティモッド)

コミュニティー・バリエーション SO-ARM100/101 パラレルグリッパー [マイケル・ヴィアチェスラフ](https://github.com/histochemichael),ヒストロジーとヒストテクノリティの自動化に適応:標準75×25mm顕微鏡スライドを軽くピックアップし,スライド染色するディッパー/ラックとキャップをカメラから近くで見ることができます.

<div align="center">

![ヒストロジースライドグリッパー デモ](../../../../../community/histology-slide-gripper/assets/histology-slide-gripper-demo.gif)

*SO-ARM100/101 顕微鏡スライドと染色するディッパー/ラックを扱うためのカスタマイズされたクランプを使用した平行グリッパー.*

</div>

<a id="what-changed-vs-the-base-gripper"></a>
## ベースグリッパーと何が変わったか

| 追加 | 記述 |
|----------|-------------|
| 顕微鏡スライドクラップ | 長いフラットクランプの幾何学は標準75×25mm顕微鏡スライドの直接ピックアップをサポートします. |
| スライドラック/ディッパー操作 | クランプの間隔とピップは,下にあるMedicus Healthのようなスライド染色ジッパー/ラックに触れます. |
| アングル付きのアードゥキャムホルダー | プリント可能なホルダーは,スライドとラックピックアップを近似モニタリングするためにグリッパー jawsに Arducam 全球シャッターUSBカメラを狙っています. |
| コンプリート・アセンブリ CAD | プリント可能な STLと編集可能な STEP アセンブリが搭載されています. [`cad/`](../../../../../community/histology-slide-gripper/cad). |

<a id="gallery"></a>
## ギャラリー

<div align="center">

| シングルスライドピックアップ | 染色するジッパー/ラックピックアップ | アードキャムホルダービュー |
|:-:|:-:|:-:|
| ![顕微鏡スライドを保持するクランプ](../../../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg) | ![スライドの染色するディッパーと並べられたクランプ](../../../../../community/histology-slide-gripper/assets/slide-gripper-staining-dipper.jpg) | ![アルダカムホルダー](../../../../../community/histology-slide-gripper/assets/arducam-holder-front.jpg) |

| 前面表示 | 爪の幾何学 | 離子測定組 |
|:-:|:-:|:-:|
| <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-front.png" alt="Front CAD view of the microscope slide gripper mod" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-side.png" alt="Angled CAD view showing the microscope slide jaw geometry" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-isometric.png" alt="Isometric CAD view of the full microscope slide gripper assembly" width="250"> |

</div>

<a id="cad-files"></a>
## CADファイル

| ファイル | フォーマット | 使用 |
|------|--------|-----|
| [`cad/the-parallel-microscope-slide-gripper.stl`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.stl) | STL | 顕微鏡スライドグリッパーモッドのプリント可能な完全な組み立て |
| [`cad/the-parallel-microscope-slide-gripper.step`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.step) | ステップ | 編集可能なCADソースは,完全な組み立てのために. |

<a id="add-on-bill-of-materials"></a>
## 材料の追加ファイル

これらのアイテムはスライド/ラックワークフローに特有のもので,ベースグリッパーの一部ではありません. [BOM](../../docs/bom.md).

| 構成要素 | Qty | 注記 | リンク |
|-----------|:---:|-------|------|
| アードキャム 100fps モノグローバルシャッター USBカメラ,OV9281 | 1 | スライドとラックピックアップを監視するために 角度付きのホルダーで使用されたカメラ | [アマゾン イギリス](https://www.amazon.co.uk/Arducam-Shutter-Distortion-Computer-Raspberry/dp/B0FXWWF55X) |
| スライド 染色 プラスチックの ディッパー 手柄 | 1+ | 基準染色器/ラックターゲット;標準75 x 25 mmスライドに設計されています. | [メディキュスの健康](https://www.medicus-health.com/slide-staining-dipper.html) |
| パラレル顕微鏡スライドグリッパー組 | 1 | プリント `the-parallel-microscope-slide-gripper.stl`; STEPファイルは編集のために含まれています. | [`cad/`](../../../../../community/histology-slide-gripper/cad) |

<a id="mujoco-simulation"></a>
## MuJoCo シミュレーション

<div align="center">

![SO-ARM101 ヒストロジースライドグリッパーが入っている MuJoCo](../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

*SO-ARM101 ヒストロジックスライドグリッパーが設置され, MuJoCo.*

</div>

独占者 MuJoCo 3.4.0モデルは [`mujoco/`](mujoco/README.md). 全面を含む SO-ARM101 モデル,グリッパーメッシュ,スタンドアロンのグリッパーテストベンチ,ビルドスクリプト,そしてヘッドレスハプとリフトチェック.

リポジトリのルーツから:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py
```

活用する `sg_grip` コントロール MuJoCo 観客が口を開いて閉める 見てください [シミュレーション README](mujoco/README.md) モデル詳細,制御,検証,再構築指示について

<a id="notes"></a>
## 注記

- 握手指は,標準75 x 25 mmの顕微鏡スライドとスライド染色ディッパー/ラックに設計されています.
- 組み立てはカメラの視線をグリッパーの口頭に向けますので カメラはスライドとラックピックアップを観察できます
- まず非重要なスライドでテストし,印刷材料,充填料,グリッパー力をワークフローに調整します.

<a id="links"></a>
## リンク

- 🎥 [デモ:スライドとステーニングラックピックアップ (LinkedIn)](https://www.linkedin.com/posts/michael-viacheslavov_histology-histotechnology-robotics-ugcPost-7482570199859240960-Gqpw/)
<!-- /translated-content -->
