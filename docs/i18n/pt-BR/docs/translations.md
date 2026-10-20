<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[Original em inglês](../../../translations.md)

[Português (Brasil)](../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# Traduções de documentação

A documentação está disponível em inglês, russo, espanhol, francês, alemão e brasileiro
Português, chinês simplificado, japonês, hindi e árabe. Usar os links linguísticos
no README principal ou no [índice de línguas](../../README.md).

<a id="scope-and-source-of-truth"></a>
## O escopo e a fonte da verdade

Os documentos da fonte inglesa permanecem nos seus caminhos originais. Traduções completas em
`docs/i18n/<language>/` Reproduzir a estrutura do repositório, incluindo os guias de hardware;
Exemplos, modificações comunitárias, guias de simulação, instruções de contribuição;
e explicações de licenciamento. As ligações entre os documentos traduzidos permanecem no
linguagem. CAD, código, configuração, imagens, vídeos, PDFs originais e licença legal
Os textos são compartilhados. O texto incorporado em imagens e PDFs existentes permanece não traduzido.

A raiz `NOTICE` é autorizado para atribuição por terceiros. Traduções de
As explicações relativas às licenças são informativas; os textos originais das licenças têm prioridade.

<a id="translation-status"></a>
## Estatuto da tradução

As traduções iniciais foram geradas com um modelo local de tradução NLLB-200 e
Assistência de IA, depois verificada a estrutura do documento, valores técnicos preservados,
Identificadores de peças, blocos de código, links e âncoras. Não foram analisadas por
Línguas nativas. As verificações automatizadas não certificam a precisão da linguagem ou do hardware.
Resolver a ambigüidade em relação à fonte inglesa e comunicar os problemas com a língua,
O caminho do documento e a sentença afetada.

<a id="maintain-translations"></a>
## Manter as traduções

1. Mudança primeiro a fonte em inglês, depois atualize o documento correspondente em cada
   linguagem. Preservar todas as instruções, avisos, tabelas, valores, identificadores de peças,
   comandos e URLs externas.
2. Mantenha links de documentos traduzidos no idioma selecionado. Os activos partilhados devem ser
   utilizarem caminhos relativos para regressar aos respectivos locais de depósito existentes. Preservação explícita
   Anchor IDs em inglês para que os links de seção funcionem entre idiomas.
3. Depois de verificar uma tradução, grava a versão fonte com
   `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md`.
   Este comando registra uma versão; não traduz ou revisa o documento.
4. Correr `python .github/scripts/check_translations.py` e
   `pre-commit run --all-files`. Indicar quais línguas receberam revisão humana no PR.

Adicionar novos documentos de Markdown rastreados para `docs/i18n/manifest.json` com um
Tradução para cada língua. O verificador usa arquivos de origem rastreados, por isso local
as notas não rastreadas não se tornam requisitos de documentação. Inglês é incluído como
Uma cópia fonte para navegação consistente. As etiquetas de língua seguem o BCP 47.
<!-- /translated-content -->
