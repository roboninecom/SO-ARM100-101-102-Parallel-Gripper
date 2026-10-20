<!-- translation-navigation -->
[English](../en/RELICENSING.md) · [Русский](../ru/RELICENSING.md) · [Español](../es/RELICENSING.md) · [Français](../fr/RELICENSING.md) · [Deutsch](../de/RELICENSING.md) · [Português (Brasil)](RELICENSING.md) · [简体中文](../zh-CN/RELICENSING.md) · [日本語](../ja/RELICENSING.md) · [हिन्दी](../hi/RELICENSING.md) · [العربية](../ar/RELICENSING.md)

[Original em inglês](../../../RELICENSING.md)

[Português (Brasil)](README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="relicensing-record"></a>
# Registo de relicensão

Este arquivo registra como e por que este projeto saiu da GPL-3.0, e o acordo
dos seus contribuintes. Existe para que o histórico de licença seja auditável sem
Escavava no Git.

**Estado: em progresso.** Esta alteração não deve ser combinada até que cada ac
registrado.

<a id="what-changed"></a>
## O que mudou

| Materiais | Antes | Após |
|---|---|---|
| Hardware / CAD | Apenas com GPL-3.0 | CERN-OHL-P-2.0 |
| Software | Apenas com GPL-3.0 | Apache-2.0 |
| Documentação e imagens | Apenas com GPL-3.0 | CC BY 4.0 |

Titular de direitos autorais: **Robonine**. Veja . `LICENSING.md` para o mapa de arquivo por arquivo,
`REUSE.toml` para a versão legível por máquina, e `NOTICE` para terceiros
atribuição.

<a id="why"></a>
## Porquê?

A GPL-3.0 é escrita para software. As suas definições  ⁇  "código fonte", "objeto"
código", "Fonte Correspondente"  ⁇  não mapeam limpo em um objeto físico, por isso
para a parte CAD deste projeto nunca foi claro o que realmente desencadeou
obrigações da licença. CERN-OHL-P-2.0 É escrito para hardware e diz:
O produto, a fonte coberta e o componente disponível são claramente definidos.

A escolha permisiva é deliberada. Troca proteção contra fechados
Forcas do agarrador em troca de zero atrito para integradores, e
Compatibilidade com o fluxo ascendente SO-ARM100/101 Projeto e o
LeRobot/ROS ecossistemas, que são Apache-2.0 Por todo o lado.

<a id="licence-history"></a>
## História da licença

| Compromissos | Data | O quê ? |
|---|---|---|
| `00fae7b` | 2025-06-27 | Repositório criado. `LICENSE` foi **MIT** 21 linhas). |
| `64d3f01` | 2025-07-01 | `LICENSE` Substituiu-se pela GPL-3.0 (674 linhas). |
| `d37855a` | 2025-07-06 | `README.md` Atualizado do MIT para a GPL-3.0. |
| Esta mudança | — | Divisão trilateral descrita acima. |

`CONTRIBUTING.md` e `software/python/gripper_control.py` foram **Nunca**
O MIT foi atualizado em 2025 e continuou a indicar o MIT. Foi um erro, não.
Licenciamento duplo deliberado.

A consequência é importante: todos os contribuintes externos aderiram *depois* a licença GPL,
num repositório cujo `CONTRIBUTING.md` Ainda disse-lhes *"Ao contribuir, você
Concordo que as suas contribuições serão licenciadas sob a Licença MIT".* O
A licença que realmente foram oferecidas era mais permissiva do que a GPL-3.0. Esta mudança
O repositório está em conformidade com o que foi dito aos contribuintes, e não contra
Não, não. A Comissão propõe, por um lado, que o Conselho adopte uma proposta de directiva relativa à protecção dos animais.
- Não, não.

<a id="contributor-agreement"></a>
## Contrato de contribuinte

| Contribuinte | Compromissos | Ámbito de aplicação | Ack |
|---|---|---|---|
| Robonine (Nikita Bragin  ⁇  também `brnikita`, `branikita`) | 76 | Proprietário | n/a |
| Alan Workaholic (Alan Subin) | 44 | `models/`, `models/parts/`, `assets/images/`, `docs/` | Trabalhos realizados sob contrato com atribuição de PI a Robonine; foi solicitado por cortesia |
| histochemichael (Michael Viacheslavov) | 3 + arquivos carregados em seu nome | `community/histology-slide-gripper/` | - Em espera. |
| Vladimir Osipov | 1 | `README.md` correcção de ligação morta | - Em espera. |
| Syed Azhar Hussain Quadri | 1 | `software/python/gripper_control.py` | - Em espera. |

Issue de relicensing: _to be filled in_

<a id="authorship-notes"></a>
### Notas de autor

- Compromissos `Codex <codex@openai.com>` foram feitas por Nikita Bragin em
  em nome do Robonine. Não são contribuições de terceiros.
- CAD e imagens da variante comunitária
  (`community/histology-slide-gripper/cad/*`, `assets/*`) foram **Cometido por
  Robonine em nome de Michael Viacheslavov** ⁇  compromissos `537f347` e `b4698e7`
  são compostas por: `Codex`. A autoria desses ficheiros pertence a Michael;
  Os metadados não refletem isso, e é por isso que estão aqui escritos.

<a id="decisions-on-the-record"></a>
## Decisões no registo

**`link5_1.stl` é uma malha fundida.** Combina a corrente ascendente SO-ARM101 pulso com
Robonine's `RB9.01.062.010 Main frame` num só corpo. As peças não são
separáveis dentro do arquivo, de modo que todo o arquivo é distribuído Apache-2.0:
Robonine não pode conceder CERN-OHL-P-2.0 sobre a geometria que não possui, e é livre
Licenciar a sua própria porção no âmbito do Apache-2.0. Reexportá-lo como duas malhas
O que é necessário para o desenvolvimento de um mercado único?

**Notificações para arquivos binários.** CERN-OHL-P-2.0 espera que os avisos de licença sejam
conservados na Fonte. Os arquivos binários STL e STEP não podem transportá-los, e
`.pre-commit-config.yaml` exclui deliberadamente esses formatos dos ganchos de texto.
`REUSE.toml` O projeto é o que faz com essa obrigação: atribui
direitos autorais e licenças para cada arquivo por caminho, e `reuse lint` aplica que
Nada fica descoberto.

As notificações de nível de diretório foram deliberadamente mantidas a um mínimo  ⁇  somente quando
O mapa raiz não possui informações. Dois sobreviveram:
`simulation/so_arm_101_description/meshes/LICENSE.md`, porque esse diretório
misturas Robonine E a geometria upstream e alguém copiando uma malha fora precisa ver
que; e `simulation/so_arm_101_description/LICENSE.md`, porque essa ROS
O pacote é distribuído de forma independente e deve ser auto-descrito.

**Os textos de licença existem em dois lugares.** `LICENSES/` é onde o REUSE
As especificações exigem-nas; `HARDWARE-LICENSE.txt`, `SOFTWARE-LICENSE.txt` e
`DOCS-LICENSE.txt` na raiz são o que a detecção de licenças do GitHub diz, então o
O repositório apresenta as três licenças, em vez de nenhuma.

**`software/FD.exe` Foi removido.** - É verdade. Feetech"FT" é proprietário SCServo Debug"
Instrumentos, cometidos em `7783073` Não foi concedida licença, e foi coberta pela
a reivindicação geral da GPL-3.0 do projeto  ⁇  que foi incorreta. `docs/assembly-guide.md`
agora aponta FeetechO download próprio e uma alternativa de código aberto.

**O histórico do Git não foi reescrito.** `FD.exe` permanece na história e na fonte
Arquivos de libertações `v0.1.0` através `v0.3.1`. A reescritura invalidaria todos os
clone, fork e commit SHA referenciados a partir de solicitações abertas upstream pull, que é
Não vale a pena para uma ferramenta . Feetech distribui-se gratuitamente.

**`ament_copyright` Foi deixado cair.** de `package.xml`. Foi declarado , mas nunca
acoplado ou executado. Verifica os cabeçalhos das licenças dentro dos ficheiros-fonte, que
Conflito com a abordagem do projeto de declaração de licenças em `REUSE.toml` —
Forçados pelo facto de a maioria dos arquivos aqui serem binários. `reuse lint` coberturas
Todos os arquivos no repositório, não apenas a dúzia Python arquivos dentro do ROS
Pacote.

<a id="releases"></a>
## Liberações

Isto não altera retroativamente as libertações `v0.1.0` através `v0.3.1`, que
permanecem disponíveis apenas sob a GPL-3.0.

---

Preparada pelos responsáveis pelo projecto. Este é um registro de decisões, não legal.
É um conselho.
<!-- /translated-content -->
