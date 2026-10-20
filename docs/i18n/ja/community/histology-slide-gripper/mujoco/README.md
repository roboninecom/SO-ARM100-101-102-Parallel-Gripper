<!-- translation-navigation -->
[English](../../../../en/community/histology-slide-gripper/mujoco/README.md) · [Русский](../../../../ru/community/histology-slide-gripper/mujoco/README.md) · [Español](../../../../es/community/histology-slide-gripper/mujoco/README.md) · [Français](../../../../fr/community/histology-slide-gripper/mujoco/README.md) · [Deutsch](../../../../de/community/histology-slide-gripper/mujoco/README.md) · [Português (Brasil)](../../../../pt-BR/community/histology-slide-gripper/mujoco/README.md) · [简体中文](../../../../zh-CN/community/histology-slide-gripper/mujoco/README.md) · [日本語](README.md) · [हिन्दी](../../../../hi/community/histology-slide-gripper/mujoco/README.md) · [العربية](../../../../ar/community/histology-slide-gripper/mujoco/README.md)

[英語原文](../../../../../../community/histology-slide-gripper/mujoco/README.md)

[日本語](../../../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="microscope-slide-gripper-in-mujoco"></a>
# 顕微鏡スライドグリッパー MuJoCo

労働組合 SO-ARM101 ヒストロジックスライド並行グリッパーを搭載し,Fusionから輸出され,スタンドのRobo9クランプに置き換えています.

試験された `mujoco` 3.4.0 `lerobot` コンドーム環境 違う ROS 2 もしくは Docker が必要なら

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py                      # full arm + slide gripper
python view.py scene_gripper.xml    # gripper alone on a testbench
python test_grasp.py                # headless grasp-and-lift check -> grasp_check.png
```

<a id="mujoco-simulation-preview"></a>
## MuJoCo シミュレーションのプレビュー

![SO-ARM101 ヒストロジースライドグリッパーが入っている MuJoCo](../../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

このシーンでは SO-ARM101 ヒストロジースライドの並行グリッパーが
腕を同じ方法で MuJoCo 以下のモデルが開始された

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python view.py
```

<a id="what-is-modelled"></a>
## モデル化されているもの

| リンク | ソース | マッサージ |
|---|---|---|
| `slide_gripper_base` | メインフレーム, STS3215,ガイドロッド,ベアリング,カメラホルダー, Arducam OV9281 | 0.20kg |
| `sg_jaw_right` / `sg_jaw_left` | RB9.01.062.020 クランプ + RB9.01.062.030 ラック (m0.8) | 単体0.035kg |
| `sg_pinion` | RB9.01.062.040 インヴォルチュートギア, 18 T,0.8 モジュール | 0.008 kg |

Fusion 組み合わさりのように構築された関節から採取された運動性
(`Slide_Jaw_Right`, `Slide_Jaw_Left`, `Drive_Pinion`),自律一致する:
18 T / 0.8 モジュールのピニオンには7.2 mm のピッチ半径があり,7.2 mm x 4.9306 rad =
**35.5mm** ⁇  CADのスライダー制限を正確に表す.

<a id="control"></a>
## 制御

単一のアクチュエーター、 `sg_grip`司令官 **マ jaws 移動のメートル**:

| `ctrl` | 爪の移動 | 刃の面間の開口 |
|---|---|---|
| `0.0` | 0 mm | **84mm** (完全に開いている) |
| `0.0295` | 29.5mm | 25 mm (顕微鏡スライド) |
| `0.0355` | 35.5mm | **13mm** (完全に閉鎖) |

両方のジョーは単一のピニオンで駆動されるため、 `sg_jaw_left_joint` そして
`sg_pinion_joint` 奴隷にされる `sg_jaw_right_joint` による `<equality>` 制限
装置は目に見えるように,爪で回転する. 司令部 *過去* 圧迫される対象:
25 mm の物体に閉じる `ctrl=0.0355` ペンダントで約4.7Nを出す.

アームの五つの関節は元の URDF 名を維持します（`base_link_to_link1` ... `link4_to_link5`).

<a id="collision-geometry"></a>
## 衝突ジオメトリ

メッシュジオームは **視覚のみ** (`contype=0`), MuJoCo ⁇ 状のボディのメッシュと
L形のマウスのボディが 握ろうとしている隙間を埋めます 連絡は
は各ジョーの二つの把持面上のボックスで表現されます（グループ 3、非表示の
レンダリング:

- `sg_pad_*` ⁇ 30mmスライドブレード,CAD x 42 ⁇ 50,z 26 ⁇ 31
- `sg_mid_*` ⁇ より広い中部,CAD x 42 ⁇ 58,z 18.5 ⁇ 38.5

TCPサイト `sg_tcp` 刃の間に座っている. `sg_camera` Arducamの光学フレームです

<a id="files"></a>
## ファイル

- `so101_slide_gripper.xml` ⁇  ロボット全体 ( `build_full.py`)
- `scene_gripper.xml` ⁇  試験用のリフト軸を搭載したグリッパーのみ
- `gripper_assets.xml` / `gripper_body.xml` / `gripper_actuation.xml` ⁇ グリッパー
  度単位とラディアン単位の両方のモデルから使用可能なものを含む
- `meshes/{base,jaw_right,jaw_left,pinion}.stl` ⁇ **組み立て
  座標**部分の起源は確認できない
- `meshes/arm/` ローボ9 レポの腕メッシュ
- `build_arm.py` ⁇  Xacro のストライプ `so_101.urdf.xacro`, ストッククラップを落とし,MJCFにまとめます
- `build_full.py` ⁇ グリッパーを挿入する `link5`; **編集する `MOUNT_POS`/`MOUNT_QUAT` ここに**

<a id="how-the-gripper-was-located-on-the-wrist"></a>
## 手首に握り付けが置かれた方法

`link5_1.stl` ロボ9のリポでは手首だけではありません  ⁇  全ストックが含まれています
グレーパー (フレーム,ガイド棒,カメラ) スライドグリッパーのデザインが置き換えられる部分です
`build_full.py` 網を削除し,質量を0.556kgから0.08 kgに低下させる.

山の姿勢は解決した 予想しなかった `base.stl` 装置は
`link5_1.stl` 共有する幾何学 (メインフレーム +ガイド棒) をすべて検索することで
24つの軸に沿った回転と近隣距離のスコア 最適な方法は
**+90°C 約X** (CAD + Y -> リンク)5+Z,CAD +Z ->リンク5-Y) と2.0ミリメートル中位
余剰  ⁇  スライドクラップは,Robo9の尖ったクラップに垂直に吊っている.
融合装置

<a id="stability"></a>
## 安定性

モデルは `max|qvel| = 0` そしてそこに残る. 震えるのを 見たら
まず見逃した連絡先をチェックする (`ncon` 視聴者の情報パネルは0でなければならない
腕が休んでいる. 三つの事項が必要でした：

1. **`<exclude body1="world" body2="link1_1"/>`** - 本当のことだ URDF輸入業者
   合併 `base_link` 中へ `worldbody`そして MuJoCo 親と子供との衝突を回避する
   *ほか* 両親が世界体であるとき リンク1のメッシュとベースメッシュです
   肩に貫通し, ⁇ を固定した永久接触を生成する
   アクチュエーターは +-1.5 N.m の限界で このことだけで 解決が必要だった `|qvel|` 4.78 から 0 に
2. `sg_pinion_joint` armature 1e-6 -> **1e-4**. 結束は,
   慣性チャッターもほとんどありませんでした (ピークは12rad/sでした).
3. 平等 `solref` 0.002 -> **0.01**. 制限時間定数がタイムステップに等しい
   ピンニオンも -282.5°Cに落ちた
   代わりに-280デグ

<a id="caveats"></a>
## 洞窟

- **質量は推定される 測定されない** フュージョンは全ての身体を鋼として報告します
  各221gで出ている);上記の値は,PLAとハードウェアの推定値である. もし
  Fusion の実際の材料を割り当て, `mass=` の属性 `gripper_body.xml`.
- イネルシアは MuJoCo Fusionのテンソールではなく,
- 腕の関節制限,抑制と摩擦は repo の URDF から継承され
  調整されていない.
- **腕のリンク質量も鋼密度です**,グリッパーと同じ欠陥:
  repo URDF総額 **2.81 kg** 実際のSO-101に対して約1kg;および `link2_to_link3`
  1.5Nmのアクチュエーター制限に 抵抗するために 1.91N.mが必要なので, これは
  振動を起こすのではなく,腕がより重いように振る舞うのです.
  機械だ 各腕のリンク質量をスケールして `diaginertia` ~0.36で合計を
  1.19 kg で飽和度を清算する STS3215 また,N.m 2.9 より近いスタンド
  URDFの保守的な1.5.
- 2 mm の調整残りは実用である. "メインフレーム_125 フォロワー"は同一ではない
  焼いた枠に `link5_1.stl`.
- `sg_pinion_joint` 化粧品です - 荷物も持ちません,なぜなら両架は結合しているからです
  直接相互に 画面に右の方向を回すように

<a id="driving-it-in-the-mujoco-viewer"></a>
## 運転する MuJoCo 視聴者

活用する **`sg_grip` スライダー 制御パネル**. スライダーが *結合* パネル
書く `qpos` 平等の制約を回避し,
停滞している間) は,ピニオンから口腔を同期化しない. ランを押すと再収縮します

<a id="re-exporting-after-a-cad-change"></a>
## CAD変更後再輸出

輸出はFusion MCP接続を通じて行われました
のボディを四つの剛体リンクにまとめ、アセンブリ座標系のバイナリ STL を書き出します
(mm) 再び輸出し,Fusion設計がオープンしてメッシュをリフレッシュする
場所  ⁇  動かない限り何も変わらない.
<!-- /translated-content -->
