<!-- translation-navigation -->
[English](../en/RELICENSING.md) · [Русский](../ru/RELICENSING.md) · [Español](../es/RELICENSING.md) · [Français](../fr/RELICENSING.md) · [Deutsch](../de/RELICENSING.md) · [Português (Brasil)](../pt-BR/RELICENSING.md) · [简体中文](../zh-CN/RELICENSING.md) · [日本語](RELICENSING.md) · [हिन्दी](../hi/RELICENSING.md) · [العربية](../ar/RELICENSING.md)

[英語原文](../../../RELICENSING.md)

[日本語](README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="relicensing-record"></a>
# ライセンス取得記録

このファイルは,このプロジェクトが GPLからどのように,そしてなぜ移ったかを記録します-3.0合意
その貢献者の ライセンス履歴は
ゲートを掘る

**状態:進行中** この変更は,下にあるすべての ack が
記録された

<a id="what-changed"></a>
## 何が変わったのか

| 材料 | 前のこと | 後に |
|---|---|---|
| ハードウェア / CAD | GPL-3.0のみ | CERN-OHL-P-2.0 |
| ソフトウェア | GPL-3.0のみ | Apache-2.0 |
| 文書と画像 | GPL-3.0のみ | CC BY 4.0 |

著作権保有者: **Robonine**. 見てください `LICENSING.md` ファイル別マップについては,
`REUSE.toml` 機械で読み取れるバージョン,および `NOTICE` 第三者向け
属性

<a id="why"></a>
## なぜ?

GPL-3.0はソフトウェア向けに書かれています. 定義は"ソースコード", "オブジェクト"
"対応する源"  ⁇ は物理的な物体にきれいに映し出されないので,
このプロジェクトのCAD部分では 何が実際に引き起こすのか 明らかになることはありませんでした
免許証の義務 CERN-OHL-P-2.0 ハードウェアのために書かれていて
製品,カバーされたソースと利用可能な成分について明確に説明します.

許容的な選択は故意です 封鎖された保護を交換する
組み合わす装置の割引は,零摩擦と交換され,
上流と互換性 SO-ARM100/101 プロジェクトとより広範な
LeRobot/ROS生態系 Apache-2.0 全域で

<a id="licence-history"></a>
## ライセンス履歴

| 約束する | 日付 | 何だ |
|---|---|---|
| `00fae7b` | 2025-06-27 | リポジトリが作成されました `LICENSE` だった **MIT** (第21行) |
| `64d3f01` | 2025-07-01 | `LICENSE` GPL-3.0 (674行) と置き換える. |
| `d37855a` | 2025-07-06 | `README.md` MITからGPLに更新された-3.0. |
| この変化 | — | 上記に示した三角形分割. |

`CONTRIBUTING.md` そして `software/python/gripper_control.py` だった **決して**
2025年に更新され,MITを継続した. 誤ったことだった
意図的な二重ライセンス

影響は重要だ: すべての外部貢献者が参加 *後に* GPLのリップ,
その保管庫に `CONTRIBUTING.md` まだ話してた *"貢献することで
MITのライセンスの下であなたの貢献が許可されることに同意します"* 労働組合
実際のライセンスがGPLよりも許容的でした-3.0. この変化
資料庫を,貢献者に伝えられたことと一致させるのではなく
やってくれ しかし,我々はそれぞれに 頼るのではなく,明示的に求めています.
そのこと

<a id="contributor-agreement"></a>
## 貢献者契約

| 貢献者 | コミットメント | 適用範囲 | アック |
|---|---|---|---|
| Robonine (ニキタ・ブラギン  ⁇ `brnikita`, `branikita`) | 76 | オーナー | n/a |
| アラン・ワーカホリック (アラン・サビン) | 44 | `models/`, `models/parts/`, `assets/images/`, `docs/` | 契約上の作業とIPの割り当て Robonine丁寧に要請した |
| ヒトオケミカエル (マイケル・ヴィアチェスラヴォフ) | 3 + ファイルが彼の名でアップロードされた | `community/histology-slide-gripper/` | 待機する |
| ウラジミール・オシポフ | 1 | `README.md` デッドリンクの修正 | 待機する |
| サイド・アザール・フセイン・クワドリ | 1 | `software/python/gripper_control.py` | 待機する |

ライセンス変更問題: _ 填写する_

<a id="authorship-notes"></a>
### 筆者記

- 責任は, `Codex <codex@openai.com>` ニキタ・ブラギンによって作られました
  代表 Robonine. 第三者からの貢献ではありません.
- コミュニティの変数CADと画像
  (`community/histology-slide-gripper/cad/*`, `assets/*`) であった. **責任者
  Robonine マイケル・ヴィアチェスラボフの名において** ⁇ コミットする `537f347` そして `b4698e7`
  本文は, `Codex`. ファイルの作者とはマイケル
  メタデータには反映されていません だからここに書いてあります

<a id="decisions-on-the-record"></a>
## 記録上の決定

**`link5_1.stl` 溶けたマッシュです** 上流を組み合わせる SO-ARM101 手首
Robonine's `RB9.01.062.010 Main frame` 一つの体で 部品は
ファイル内には分離できるので,ファイル全体が Apache-2.0:
Robonine 譲渡できない CERN-OHL-P-2.0 ゲオメトリーに勝ったものではなく,自由です
ライセンスを取得する Apache-2.0. 二つのメッシュとして再出力すると、
各部には適切な許可が与えられれば,それは将来の仕事として残ります.

**バイナリーファイルに関する通知** CERN-OHL-P-2.0 免許証の通知を期待する
泉の中に留められている. バイナリ STL と STEP ファイルはそれらを運べることはできません.
`.pre-commit-config.yaml` 意図的にこれらのフォーマットをテキストハックから除外する.
`REUSE.toml` このプロジェクトがこの義務をどのように果たすのか
経路による各ファイルに対する著作権とライセンス,および `reuse lint` 執行する
隠されたものはありません

ディレクトリレベルでの通知は意図的に最小限に保持された場合のみ
ルーツマップには情報はありません. 二つが残っています：
`simulation/so_arm_101_description/meshes/LICENSE.md`, そのディレクトリから
混合物 Robonine そして,上流幾何学と 網をコピーする誰かが見なければならない
そのこと; `simulation/so_arm_101_description/LICENSE.md`, そのROSから
パッケージは単独で配布され,自定義しなければならない.

**ライセンス本文は二か所にあります。** `LICENSES/` REUSEが
仕様では要求される. `HARDWARE-LICENSE.txt`, `SOFTWARE-LICENSE.txt` そして
`DOCS-LICENSE.txt` GitHubのライセンスの検出が読んでいるので,
リポジトリにはライセンスが未表示になるのではなく、三つすべてが表示されます。

**`software/FD.exe` 削除されました.** それは Feetech特許のFT SCServo "デバッグ"
ツール, `7783073` ライセンス授予なし,
プロジェクトの一般的なGPL-3.0の主張は誤っていた. `docs/assembly-guide.md`
現在 Feetechオープンソースの代替案に

**Gitの履歴は書き換えられませんでした.** `FD.exe` 歴史と起源に留まっています
公開のアーカイブ `v0.1.0` 経由 `v0.3.1`. 書き換えれば
クローン,フォークおよびコンビート SHAは,開いている上流引き込み要求から参照され,
道具には価値がない Feetech 無料で配布する

**`ament_copyright` 落ちた** から `package.xml`. 宣言されましたが 決して
ケーブルを接続するか実行する ソースファイル内のライセンスヘッダをチェックします
このプロジェクトにおけるライセンス申告方法と矛盾する `REUSE.toml` —
バイナリーファイルが多いので `reuse lint` カバー
資料庫内の全てのファイルだけでなく Python ROS内のファイル
パッケージ

<a id="releases"></a>
## リリース

これはリクエストを後期的に変更しない. `v0.1.0` 経由 `v0.3.1`,
GPL-3.0のみで利用できます.

---

プロジェクト管理者によって準備された これは法律上の決定の記録ではなく
助言する
<!-- /translated-content -->
