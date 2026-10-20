<!-- translation-navigation -->
[English](../../en/docs/quick-start.md) · [Русский](../../ru/docs/quick-start.md) · [Español](../../es/docs/quick-start.md) · [Français](../../fr/docs/quick-start.md) · [Deutsch](../../de/docs/quick-start.md) · [Português (Brasil)](../../pt-BR/docs/quick-start.md) · [简体中文](../../zh-CN/docs/quick-start.md) · [日本語](quick-start.md) · [हिन्दी](../../hi/docs/quick-start.md) · [العربية](../../ar/docs/quick-start.md)

[英語原文](../../../quick-start.md)

[日本語](../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="quick-start-guide"></a>
# スピード・スタートガイド

フォロワーグリッパーを SO-ARM101 立ち上がって走る!

[![SO-ARM101 平行グリッパー](../../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

*画像をクリックして [動作するグリッパーを観察](https://youtube.com/shorts/bSyXjgNGXZk)!*

<a id="what-youll-need"></a>
## 必要なもの

<a id="hardware"></a>
### ハードウェア
- [ ] 3Dプリント部品 (参照) [3Dモデル](../models/README.md))
- [ ] 電子部品 (参照) [BOM](bom.md))
- [ ] メカニカルコンポーネント (ローヤ,棒,固定装置)
- [ ] ツール:フィリップス スクリュードライバー PH1,ヘックスキー M2 (H1.5) と M4 (H2.5)

<a id="software"></a>
### ソフトウェア
- [ ] Python 3.6+ インストール
- [ ] STServo SDKがダウンロードされました
- [ ] 現存する SO-ARM100/101 制御器,USB接続,腕電源

---

<a id="step-1-3d-print-the-parts-2-4-hours"></a>
## ステップ1: 3Dプリントパーツ (2-4時間)

1. STLファイルをダウンロードする `models/parts/`
2. 推奨設定で印刷する:
   - 層の高さ: 0.2mm
   - 充填:20% (フレーム/クラップ),100% (ギア)
   - 材料: PLA または PETG
3. 支柱を削除する

![テストプレート](../../../../assets/images/assembly/rod-test-plate.PNG)

クランプによりよく収まるために 試用品を使わなければなりません 印刷して,最大から最小まで作業して,棒がテスト部品に簡単に収まるようにする直径を選択します. その後, stlファイル名 (例えば, RB9.01.062.021 (D6.1) もし直径 6.1 mm を選択した場合.

**互換性のある3Dプリンター** (180×180mm+ ベッド):
- バンボラボ A1 ミニ
- プロサ・ミニ / ミニ+
- アニキュビック・コブラ・ネオ
- 床が ≥180×180mm のプリンター

**印刷する部品:**
- 1x メインフレーム (RB9.01.062.010)
- 2x ジョー (RB9.01.062.020)
- 2x ラックギア (RB9.01.062.030)
- 1x 歯車 (RB9.01.062.040)
- 1x カメラホルダー (RB9.01.060.074)
- 1x ホルダー (RB9.01.060.080)
- 1x カメラスペーサー (RB9.01.060.090)

---

<a id="step-2-gather-components-1-2-days-shipping"></a>
## ステップ2: コンポーネントを集める (1-2運送日)

オーダーパーツ [資料の表](bom.md). 腕制御器と電源を再利用する.これはグリッパーコストの外にある:

| 構成要素 | Qty | - エスト 費用 |
|-----------|:---:|-----------|
| Feetech STS3215 セルボ | 1 | ~$29 |
| MF106ZZ ベアリング (10x6x3mm) | 2 | ~$2 |
| アルミニウム/炭素チューブ D6x1x125mm | 2 | ~$4 |
| 3Dプリント PLA| 8部 | ~$12 |
| 固定装置 (M2/M4螺旋/ナッツ) | 種類 | ~$3 |

**総額推定費用: ~$50**

---

<a id="step-3-assembly-30-45-minutes"></a>
## 3 ステップ:集会 (30-45 分)

詳細は [集会ガイド](assembly-guide.md):


1. セルボケーブルを挿入する
2. 使用する Feetech ソフトウェアは,セルボを最小の位置に移動する (ソフトウェア内のスライダーを左へ移動する)
3. ラックギアをジョーに取り付けます
4. ガイドロッドを両方のジョーに通します
5. ベアリングをメインフレームに取り付け、ねじで固定します
6. ガイドロッドをフレームにはめ込みます
7. ジョーを左右の端まで広げます
8. セルボを挿入し,螺栓で固定する
9. カメラ スパッサーとUVCカメラを固定し, 4x螺栓とナッツ M2 (オプション) を用いて固定する
10. ロボット腕へのマウント (オプション)

---

<a id="step-4-software-setup-10-minutes"></a>
## 4 ステップ:ソフトウェアを設置する (10 分)

1. **インストール STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cd STServo_SDK_Python
   cp -r STservo_sdk /path/to/your/project/
   ```

2. **インストール Python 依存性**
   ```bash
   pip install pyserial
   ```

3. **接続を設定する**
   ```python
   DEVICENAME = 'COM7'  # Windows
   # DEVICENAME = '/dev/ttyUSB0'  # Linux
   STS_ID = 1  # Servo ID (use 6 if connected as gripper on SO-ARM101)
   ```

---

<a id="step-5-first-test-5-minutes"></a>
## 5 ステップ: 最初のテスト (5 分)

1. **ハードウェアを接続する**
   - グリッパーセルボ → セルボ No5 SO-ARM101 サーボバス
   - 既存の腕制御器 → コンピュータ (USB)
   - 設置されたセルボに設定した腕電源を使用する
   - グレープのセルボIDを一致させる `STS_ID` バスで独創的に
   - シリアルポートを開く前に他のロボット制御アプリケーションを閉じる

2. **基本テストを実行する**
   ```bash
   cd software/python
   python gripper_control.py
   ```

3. **基本的なコマンドを試してみてください**
   - 入力する `45` グリッパーを開く
   - 入力する `-45` グリッパーを閉じる
   - 入力する `0` 中央へ
   - 入力を押して終了する

---

<a id="troubleshooting"></a>
## 問題解決

<a id="connection-issues"></a>
### 接続問題
- ✅デバイスマネージャー (Windows) または `ls /dev/ttyUSB*` (Linux)
- ✅セルボ電源LEDがオンであることを確認する
- ✅ 異なるバードレートを試してみてください (デフォルト: 1000000)
- ✅ケーブル接続を確認する

<a id="movement-issues"></a>
### 移動問題
- ✅ ラックと装備の接触を確認する
- ✅機械的な結合をチェック
- ✅ ロイヤリングが棒で自由に移動することを確保する
- ✅サーボ温度をモニターする (最大60°C)

<a id="software-issues"></a>
### ソフトウェア 問題
- ✅インストール STServo SDKが正しく
- ✅チェック Python バージョン (3.6+)
- ✅シリアルポートの許可を確認する `sudo chmod 666 /dev/ttyUSB0` (Linux)

---

<a id="next-steps"></a>
## 次 の ステップ

🎉 **あけましておめでとうございます** あなたのグリッパーが動作しています!

今度は
- マウンテン SO-ARM100/101 ロボット腕
- 制御ソフトウェアに統合する
- カメラホルダーにカメラを追加する
- カスタムアプリケーションを作成する

<a id="need-help"></a>
## 助けが必要か?

- ⁇  読書 [仕様](specifications.md)
- ⁇  チェック [集会ガイド](assembly-guide.md)
- 📄 [パラレルグリッパー製品の仕様 (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf)
- 📄 [SO-ARM101 製品仕様 (PDF)](../../../SO-ARM101%20by%20Robo9.pdf)
- ⁇  GitHubで問題報告

---

**パラレルグリッパーコミュニティへようこそ!** 🤖
<!-- /translated-content -->
