<!-- translation-navigation -->
[English](../../en/models/README.md) · [Русский](../../ru/models/README.md) · [Español](../../es/models/README.md) · [Français](../../fr/models/README.md) · [Deutsch](../../de/models/README.md) · [Português (Brasil)](README.md) · [简体中文](../../zh-CN/models/README.md) · [日本語](../../ja/models/README.md) · [हिन्दी](../../hi/models/README.md) · [العربية](../../ar/models/README.md)

[Original em inglês](../../../../models/README.md)

[Português (Brasil)](../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="3d-models"></a>
# Modelos 3D

Esta pasta contém arquivos STL para o conjunto Follower Gripper.

<a id="complete-assembly"></a>
## Assembléia completa

| Arquivo | Descrição | Impressoras compatíveis |
|------|-------------|---------------------|
| `Follower gripper (165x165 bed size).STL` | Kit completo de peças de sujeira | Impressoras com tamanho de cama > 165×165 mm |

<a id="compatible-3d-printers"></a>
### Impressoras 3D compatíveis

- **Bambu Lab A1 mini** (180×180×180mm)
- **Prusa MINI / MINI+** (180×180×180mm)
- **Criatividade Ender-2 Pro** (165×165×180mm)
- **Anycubic Kobra Neo** (220×220×250mm)
- **Gênio de artilharia** (220×220×250mm)

*Nota: Qualquer impressora com tamanho de cama ≥ 165×165 mm pode imprimir a prévia completa da montagem.*

<a id="individual-parts"></a>
## Partes individuais

Localizado no `parts/` Cartão:

| Número da parte | Arquivo | Qty | Descrição |
|-------------|------|:---:|-------------|
| RB9.01.060.074 | `Camera holder.STL` | 1 | Capa de montagem da câmera |
| RB9.01.060.080 | `Holder.STL` | 1 | Prateleiras de montagem sem câmera |
| RB9.01.060.090 | `Camera spacer.STL` | 1 | Espaçador para câmera |
| RB9.01.060.110 | `D405 holder.STL` | 1 | Retalhador para câmera D405 |
| RB9.01.062.010 | `Main frame.STL` | 1 | Quadro estrutural principal |
| RB9.01.062.021 (D6.0) | `Clamp.STL` | 2 | Mordentes da garra |
| RB9.01.062.021 (D6.1) | `Clamp.STL` | 2 | Mordentes da garra |
| RB9.01.062.021 (D6.2) | `Clamp.STL` | 2 | Mordentes da garra |
| RB9.01.062.021 (D6.3) | `Clamp.STL` | 2 | Mordentes da garra |
| RB9.01.062.031 | `Gear rack.STL` | 2 | Estacas de engrenagem para movimento linear |
| RB9.01.062.040 | `Gear.STL` | 1 | Engrenagem motriz |
| RB9.01.062.100 | `Nail.STL` | 2 | Anéis |

<a id="print-settings"></a>
## Configurações de Impressão

| Parâmetro | Valor recomendado |
|-----------|-------------------|
| Materiais | PLA / PETG |
| Altura da camada | 0.2mm (0.15mm para engrenagens) |
| Enchimento | 20% (30% para engrenagens) |
| Suporte | De acordo com a necessidade |
| Paredes | 3-4perímetros |

<a id="notes"></a>
## Notas

- Engrenagens de impressão com maior preenchimento (100%) para melhor resistência
- O quadro principal pode exigir suportes dependendo da orientação
- Pós-processamento: pode ser necessária ponta leve para encaixes de rolamentos
- As peças individuais podem ser impressas em qualquer impressora FDM padrão

<a id="better-rods-fit"></a>
## Melhores barras para caber
![Placa de ensaio](../../../../assets/images/assembly/rod-test-plate.PNG)

Para garantir que as hastes compradas se encaixem melhor nas sujeiras, é preciso usar uma peça de teste. Imprima-o e, trabalhando do buraco mais grande ao menor, selecione o diâmetro que permita que a vara se encaixa na parte de ensaio sem dificuldade e com um espaço mínimo. Em seguida, imprimir as sujeiras com o mesmo diâmetro de buraco que é mencionado no nome do arquivo stl (por exemplo: RB9.01.062.021 (D6.1) se escolher o diâmetro6.1mm).
<!-- /translated-content -->
