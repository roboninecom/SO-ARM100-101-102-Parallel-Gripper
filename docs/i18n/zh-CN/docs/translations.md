<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[英文原文](../../../translations.md)

[简体中文](../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# 文件翻译

文件可用英语,俄语,西班牙语,法语,德语,巴西
葡萄牙语,简体中文,日语,印度语和阿拉伯语. 使用语言链接
在主要README或 [语言指数](../../README.md).

<a id="scope-and-source-of-truth"></a>
## 真理的范围和来源

英文来源文件保持原始的路径. 完整的翻译
`docs/i18n/<language>/` 反映存储库结构,包括硬件指南,
实例,社区修改,模拟指南,贡献说明
许可证的解释. 翻译文档之间的链接仍然存在
语言. CAD,代码,配置,图像,视频,原始PDF文件和法律许可证
通过电子邮件来分享. 目前已有图像和PDF文件中嵌入的文本仍未翻译.

根源 `NOTICE` 是权威于第三方归因. 翻译
许可证的解释是信息性的,优先考虑原始许可文本.

<a id="translation-status"></a>
## 翻译状态

首次翻译使用本地NLLB-200翻译模型和
后检查文件结构,保存技术价值,
部分标识符,代码区块,链接和 ⁇ . 它们尚未被审查
语言母语 自动检查不证实语言或硬件的准确性.
解决对英语来源的模糊性,并报告语言问题;
文件路径和受影响的句子.

<a id="maintain-translations"></a>
## 维护翻译

1. 首先更改英语源,然后在每个文件中更新相应的文档
   语言. 保存所有指令,警告,表格,值,零件标识符
   其他命令和外部URL.
2. 在选择的语言中保存翻译文档链接. 股权必须
   使用相对的返回存储场所的路径. 保持明确
   英语 ⁇ 标识,所以部分链接可以跨语言运行.
3. 在检查翻译后,记录其源版本
   `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md`.
   这个命令记录了版本;它不翻译或审查文档.
4. 跑步 `python .github/scripts/check_translations.py` 和
   `pre-commit run --all-files`. 说明在公关中接受了人类审查的语言.

添加新的追踪的标记文件到 `docs/i18n/manifest.json` 有一个完整的
每种语言的翻译. 检查器使用追踪源文件,所以本地
没有追踪的笔记不会成为文件要求. 英语包括:
一份源副本,可用于一致的导航. 语言标签遵循BCP 47.
<!-- /translated-content -->
