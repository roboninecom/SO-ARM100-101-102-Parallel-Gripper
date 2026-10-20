<!-- translation-navigation -->
[English](../../en/docs/assembly-guide.md) · [Русский](../../ru/docs/assembly-guide.md) · [Español](../../es/docs/assembly-guide.md) · [Français](../../fr/docs/assembly-guide.md) · [Deutsch](../../de/docs/assembly-guide.md) · [Português (Brasil)](../../pt-BR/docs/assembly-guide.md) · [简体中文](../../zh-CN/docs/assembly-guide.md) · [日本語](assembly-guide.md) · [हिन्दी](../../hi/docs/assembly-guide.md) · [العربية](../../ar/docs/assembly-guide.md)

[英語原文](../../../assembly-guide.md)

[日本語](../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="assembly-guide-for-follower-gripper-so-arm101"></a>
# フォロワーグリッパー の 集会ガイド SO-ARM101

このガイドは,並行グリッパーを組み立てるためのステップバイ・ステップ指示を提供します. この手順を注意深く実行して,適切な動作を確保してください.

<a id="required-tools"></a>
## 必要 な 道具

- フィルプスヘッド スクリュードライバー PH1
- ヘックスキー M2 (H1.5) と M4 (H2.5)

---

<a id="step-1-install-gear-on-servo"></a>
## ステップ1: サーボにギアを設置する

![装置のセット付きのセルボ](../../../../assets/images/assembly/02-servo-with-gear-assembly.png)

**必要な構成要素:**
- 1x Feetech STS3215 セルボ
- 1x 歯車  (RB9.01.062.040)
- 1x セルボディスク (セルボキットから)
- 1x セルボマウントスクリュー M3x6 (セルボキットから)
- 4xセット スクロール DIN 913 M3x4

**指示:**
1. Servo ディスクにグリッパー用のギアを置いて,Servo ディスクからギアまでの方向に 4xセットスクロール M3x4を絞る. スイッチを締めるときには,ディスクとギアの間に隙間が表示されないようにしてください.
2. サーボ出力軸にギアセットを設置する.
3. セルボキットに搭載されたM3x6螺旋で固定する.

---

<a id="step-2-servo-positioning-and-torque-limit"></a>
## ステップ2:セルボポジショニングとトーク制限

![セルボ定位](../../../../assets/images/assembly/Feetech-Servo-Window.png)

**必要な構成要素:**
- 現存する SO-ARM100/101 コントローラー,セルボケーブル,腕電源

**Windows ユーザの指示:**
1. セルボバスを介して,既存の腕制御器に接続し,USBでコントローラをPCに接続する. 腕の電源を使う チェーンにグリッパーを追加する前にユニークなセルボIDを設定し,COMポートを開く前に他のロボット制御アプリケーションを閉じる.
2. Servo を設定する Feetech's **FD** (SCServo デバッグツール 封鎖ソースです
   Windows のソフトウェア Feetech そして **はい** このリポジトリに再配布された:
   - 公式ダウンロード: <https://www.feetechrc.com/software.html> ⁇ FDを探して
     SCServo ファイルデバッグ パスワードで保護されている.
     パスワード Feetech.
   - オープンソースクロスプラットフォーム代替:
     <https://github.com/Kotakku/FT_SCServo_Debug_Qt>

   下のステップは,FDインターフェースを記述します.
   類似の名前によるパラメータ
3. COM ポートを選択し,BaudRate 1 000 000 を選択して"開く"ボタンを押して"検索"をクリックします.
4. 下のリストからあなたのセルボを選択してください.
5. サーボでトークを有効にするかチェックする
6. スライダーを左に移動する.

![最大トルク制限](../../../../assets/images/assembly/max-torque-window.png)

7. 窓を"プログラミング"タブに切り替える.
8. "最大トーク制限"を選択して,500 ans に設定し",保存"を押します.

---

<a id="step-3-clamps"></a>
## 3 ステップ: クランプ

![ジョー](../../../../assets/images/assembly/clamp+rack+nail.PNG)

**必要な構成要素:**
- 2x ジョー (RB9.01.062.021)
- 2x ラックギア (RB9.01.062.031)
- 2x ネイル (RB9.01.062.100)

**指示:**
1. ラックギアをジョーに横から差し込みます。
2. 続いて背面から釘を差し込みます。

---

<a id="step-4-rods"></a>
## 4 ステップ:棒

![ガイドロッド](../../../../assets/images/assembly/rods+clamps.PNG)

**必要な構成要素:**
- 2x ロッド D6x125mm

**指示:**
1. 両方のクランプに棒を挿入する. 125 mm以上の棒/チューブを注文した場合は,この長さまで切断する必要があります.

---

<a id="step-5-install-bearings-on-main-frame"></a>
## 5 ステップ: メインフレームにベアリングを設置する

![メインフレームに設置されたベアリング](../../../../assets/images/assembly/frame+bearings.png)

**必要な構成要素:**
- 2x MF106ZZ ベアリング (10x6x3 mm)
- 2x M4x8 DIN 7991 スクリュー

**指示:**
1. 2x を挿入する MF106ZZ 軸承は,主要フレームに指定された位置に配置されます. ローリングフラングは上向きで
2. 各ベアリングを M4x8 ねじで固定します。

---

<a id="step-6-connection-of-rods-and-frame"></a>
## ステップ6:棒とフレームの接続

![棒とメインフレームの接続](../../../../assets/images/assembly/frame-with-clamps.png)

**指示:**
1. ガイドロッドをフレームにはめ込みます.
2. ジョーを左右の端まで広げます.

---

<a id="step-7-mount-servo-on-main-frame"></a>
## ステップ 7: メインフレームのセルボ山

![メインフレームに設置されたセルボ](../../../../assets/images/assembly/servo-on-frame.png)

**必要な構成要素:**
- 3x 自動タッピングスイッチ (セルボキットから)

**指示:**
1. セルボをメインフレームに配置し,マウントホールを並べます.
2. サーボ付属のタッピングねじを 3x 使用して固定します。

---

<a id="step-8-gripper-holder-attachment"></a>
## ステップ8 グリッパーホルダー付属

![グリップホルダー付属](../../../../assets/images/assembly/09-gripper-holder-attachment.png)

**必要な構成要素:**
- 1x カメラホルダー (RB9.01.060.074) または保有者 (RB9.01.060.080)
- 1x SO-ARM101
- 4x M3x6 スクリュー (セルボキットから)
- 4x 自動タップスウィッチ (セルボキットから)

**指示:**
1. カメラ付きのGripperを使用する場合は,カメラホルダーを固定してください. SO-ARM101 4x M3x6 スイッチで固定する
2. カメラホルダーまたはホルダーに並行グリッパーを固定して 4x 自律タッピングスクリューで固定する
3. パラレルグリッパーからセルボにケーブルを接続する5について SO-ARM101

---

<a id="step-9-camera-attachment-optional"></a>
## ステップ 9: カメラの添付 (オプション)

![カメラの固定装置](../../../../assets/images/assembly/camera-attachment.png)

**必要な構成要素:**
- 1x UVC カメラ,マウントホールは 28x28 mm
- 1x カメラスペーサー (RB9.01.060.090)
- 4x M2x8 スクロール
- 4x M2ナッツ

**指示:**
1. カメラホルダーの背面から 4x M2 ナットを入れます。
2. 前面からカメラスペーサーとカメラを取り付け、4x M2x8 ねじで固定します。

---
<a id="assembly-complete"></a>
## 集会 が 完了 し た!

![組み立て SO-ARM101 Follower Gripper とする](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

あけましておめでとうございます あなたの SO-ARM101 現在組み立てられ,使用準備ができています.

<a id="next-steps"></a>
### 次 の ステップ
- 使用前にグリッパー操作をテストする
<!-- /translated-content -->
