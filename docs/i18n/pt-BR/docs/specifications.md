<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](../../es/docs/specifications.md) · [Français](../../fr/docs/specifications.md) · [Deutsch](../../de/docs/specifications.md) · [Português (Brasil)](specifications.md) · [简体中文](../../zh-CN/docs/specifications.md) · [日本語](../../ja/docs/specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[Original em inglês](../../../specifications.md)

[Português (Brasil)](../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-100101-parallel-follower-gripper"></a>
# SO ARM 100/101 Gripper paralelo seguidor

<a id="overview"></a>
## Visão geral

Efector final de impressão 3D leve, concebido por: **Robonine** para a plataforma robótica de teletravação open-source SO ARM 100/101. O mecanismo proporciona um movimento paralelo confiável da mandíbula e força de agarre suficiente para uma ampla gama de aplicações educacionais e experimentais.

![Grifos de seguimento montados SO-ARM100](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*Grifos de seguimento montados SO-ARM100 braço robótico*

<a id="key-features"></a>
## Características fundamentais

- Desenho de código aberto
- Custo BOM por um agarrador: ~ $62
- Pode ser impressa durante um ciclo em uma impressora 3D FDM de nível consumidor
- Compatível com câmeras de vídeo populares:
  - Orbbec Gémeos 2
  - RealSense D405, D435/D435i, D455
  - GC2093 Modulo de câmera USB 2MP
  - IMX335 Câmara USB 5MP

---

<a id="dimensions"></a>
## Dimensões

<a id="3d-overview"></a>
### Visão geral em 3D

![Dimensões do agarrador  ⁇  visão isométrica](../../../../assets/images/specification/08-gripper-dimensions-3d.png)

*Visão isométrica com dimensões globais:128 × 109 × 130.5mm, revestimento completo84mm*

| Dimensão | Valor |
|-----------|-------|
| Largura | 128 mm |
| Profundidade | 130.5mm |
| Altura | 109 mm |
| Infracção total | 84 mm |

---

<a id="mounting-interface"></a>
## Interface de montagem

![Dimensões da interface de montagem](../../../../assets/images/specification/03-mounting-interface.jpg)

*Flança de montagem com padrão de buraco para fixação do braço robótico*

| Características | Dimensão |
|---------|-----------|
| Diâmetro da flange de montagem | Ø 20 mm |
| Forro central | Ø7 mm |
| Foros de montagem | 4x Ø3.2mm |

---

<a id="gripper-parameters"></a>
## Parâmetros da garra

| Parâmetro | Garra do braço seguidor |
|-----------|------------------|
| Massas de montagem (PLA, 30% de enchimento) | 170 g |
| Força máxima de agarre | 120 N |
| Velocidade máxima de agarre | 14 mm/s |
| Infracção total | 84 mm |
| Repetibilidade | 0.5mm |
| DOF | 1 |

---

<a id="technical-specifications"></a>
## Especificações técnicas

<a id="materials--construction"></a>
### Materiais e Construção

| Componente | Especificações |
|-----------|---------------|
| Materiais primários | PETG / PLA |
| Transmissão | Triturador |
| Guías | Tubos redondos de alumínio/carbono (Ø6 mm) |
| Condutor | Feetech Servo atuador STS3215 |

<a id="servo-parameters-feetech-sts3215"></a>
### Parâmetros servo (Feetech STS3215)

| Parâmetro | Valor |
|-----------|-------|
| Intervalo de voltagem operacional | 12V |
| Velocidade (sem carga) | 45 RPM |
| Corrente corrente (sem carga) | 180 mA |
| Torque de estacionamento (a bloquear) | 30 kg·cm |
| Corrente de estagnação (a bloquear) | 2.7 A |
| Corrente ociosa (em parada) | 30 mA |
| Torque nominal | 10 kg·cm |
| Corrente nominal | 900 mA |
| Resistência terminal | 1 Ω |
| Temperatura de funcionamento | -20°C ~ 60°C |
| Tipo de codificador | Magnético absoluto de 12 bits |
| Protocolo de controlo | RS485/TTL até 1 Mbps |
| Proteção electrónica | Contra alta tensão, corrente, carga e temperatura |

---

<a id="camera-compatibility"></a>
## Compatibilidade com a câmera

O agarrador Follower é compatível com várias câmeras por meio de um suportador interchangeável.

![Diferentes câmeras montadas no agarrador](../../../../assets/images/specification/09-camera-types.png)

*Diferentes câmeras montadas no agarrador (de esquerda para direita): RealSense, módulo de câmera USB, Orbbec Gémeos 2*

<a id="supported-cameras"></a>
### Câmeras com suporte

| Câmara | Tipo | Notas |
|--------|------|-------|
| IMX335 5MP USB | RGB | Compatível e de baixo custo |
| GC2093 USB de 2 MP | RGB | Opção orçamental |
| Orbbec Gémeos 2 | RGB-D | Sensores de profundidade |
| RealSense D405 | RGB-D | Profundidade de estreito alcance |
| RealSense D435/D435i | RGB-D | Propósito geral |
| RealSense D455 | RGB-D | Profundidade de longo alcance |

---

<a id="supplied-resources"></a>
## Recursos fornecidos

- Completo conjunto de arquivos STL para impressão 3D
- Guia de montagem
- Desenhos com dimensões de montagem
- Arquivo URDF para simuladores robóticos

---

<a id="integration"></a>
## Integração

O agarrador pode ser integrado de forma independente em numerosos sistemas robóticos graças à sua instalação conveniente e simples através da flange de montagem padrão.

<a id="mounting-requirements"></a>
### Requisitos crescentes

- Parafusos 4x M3 para fixação de flanges
- Compatível com: SO-ARM100/101 braço robótico
- Placas de adaptadores personalizadas disponíveis para outros braços robóticos

<a id="communication"></a>
### Comunicação

- Conexão em série através de TTL ou RS485
- Taxa de Baud: até 1 Mbps
- Protocolo: Feetech Protocolo STS

---

<a id="product-specification-documents"></a>
## Documentos de especificação do produto

- [Especificação do produto paralelo de pegamento (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf) ⁇  Especificações completas do produto para o agarrador paralelo da Robo9
- [SO-ARM101 Especificação do produto (PDF)](../../../SO-ARM101%20by%20Robo9.pdf) ⁇  Especificações completas do produto SO-ARM101 Braço robótico de Robo9

---

*Especificações sujeitas a alteração com base na implementação e nos ensaios efetivos*
<!-- /translated-content -->
