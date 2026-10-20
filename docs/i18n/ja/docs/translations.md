<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[英語原文](../../../translations.md)

[日本語](../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# 文書の翻訳

文書は英語,ロシア語,スペイン語,フランス語,ドイツ語,ブラジル語で提供されています
ポルトガル語 簡体字中国語 日本語 ヒンディー語 アラビア語 言語リンクを使用する
メイン README または [言語インデックス](../../README.md).

<a id="scope-and-source-of-truth"></a>
## 真理 の 範囲 と 源泉

英語の資料は原始的なままです 完全な翻訳
`docs/i18n/<language>/` ハードウェアガイドを含むリポジトリ構造を反映する
例,コミュニティの変更,シミュレーションガイド,貢献指示
ライセンス説明も 翻訳された文書のリンクは選択した文書に留まります
言語について CAD,コード,構成,画像,ビデオ,オリジナルPDFファイルおよび法的ライセンス
テキストは共有されます 既存の画像やPDFファイルに埋め込まれたテキストは翻訳されていない.

根 `NOTICE` 第三者による配属の権限がある. 翻訳
ライセンス説明は情報的なもので,オリジナルライセンスのテキストが優先される.

<a id="translation-status"></a>
## 翻訳状態

最初の翻訳は,地元の NLLB-200翻訳モデルで生成されました.
文書構造をチェックし 技術的価値が保存され
パーツ識別子,コードブロック,リンク,アンカー 審査を受けていない
母語話者 自動チェックは言語やハードウェアの精度を証明するものではありません.
英語のソースに対する曖昧さを解決し,言語に関する問題を報告する.
文書の経路と影響を受けた文

<a id="maintain-translations"></a>
## 翻訳 を 維持 する

1. まず英語のソースを変更し,それぞれに対応するドキュメントを更新します
   言語について すべての指示,警告,表,値,部品識別子を保存する
   コマンドと外部URL
2. 翻訳された文書のリンクを選択した言語内に保存します. 共有資産は
   既存のリポジトリの場所に戻る相対的な経路を使用する. 明確に保存する
   英語のアンカーIDは 言語間のセクションリンクが機能するようにします
3. 翻訳をチェックした後,そのソースバージョンを
   `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md`.
   このコマンドはバージョンを記録し,文書の翻訳やレビューを行わない.
4. 走る `python .github/scripts/check_translations.py` そして
   `pre-commit run --all-files`. 人文調査でどの言語が評価されたかを表す.

追跡された新しいマークダウン文書を追加する `docs/i18n/manifest.json` 完全な
各言語の翻訳. チェックは追跡されたソースファイルを使います
追跡されていないメモは,ドキュメントの要件になることはありません. 英語は,
一貫したナビゲーションのためのソースコピーを 言語タグは BCP47 に従います.
<!-- /translated-content -->
