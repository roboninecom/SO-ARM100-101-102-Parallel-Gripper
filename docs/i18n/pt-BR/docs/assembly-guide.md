<!-- translation-navigation -->
[English](../../en/docs/assembly-guide.md) · [Русский](../../ru/docs/assembly-guide.md) · [Español](../../es/docs/assembly-guide.md) · [Français](../../fr/docs/assembly-guide.md) · [Deutsch](../../de/docs/assembly-guide.md) · [Português (Brasil)](assembly-guide.md) · [简体中文](../../zh-CN/docs/assembly-guide.md) · [日本語](../../ja/docs/assembly-guide.md) · [हिन्दी](../../hi/docs/assembly-guide.md) · [العربية](../../ar/docs/assembly-guide.md)

[Original em inglês](../../../assembly-guide.md)

[Português (Brasil)](../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="assembly-guide-for-follower-gripper-so-arm101"></a>
# Guia de Assembléia para Gripper SO-ARM101

Este guia fornece instruções passo-a-passo para a montagem do agarrador paralelo. Siga estes passos cuidadosamente para assegurar um bom funcionamento.

<a id="required-tools"></a>
## Ferramentas necessárias

- Fibra de cabeça Phillips PH1
- Chaves de hexagonal M2 (H1.5) e M4 (H2.5)

---

<a id="step-1-install-gear-on-servo"></a>
## Passo 1: Instale Engrenagem no Servo

![Servo com montagem de engrenagem](../../../../assets/images/assembly/02-servo-with-gear-assembly.png)

**Componentes necessários:**
- 1x Feetech STS3215 Servo
- 1x Engrenagem  (RB9.01.062.040)
- 1x Servo Disco (do servo kit)
- 1x parafusos de montagem servo M3x6 (do kit servo)
- 4x Set Screw DIN 913 M3x4

**Instruções:**
1. Colocar o engrenagem para a Gripper no disco servo e apertar os parafusos 4x Set M3x4 na direcção do disco servo para o engrenagem. Certifique-se de que não apareça qualquer diferença entre o Disco e a Engranagem ao apertar os parafusos.
2. Montar o conjunto de engrenagens no eixo de saída do servo.
3. Segure-se com o parafuso M3x6 fornecido no servo kit.

---

<a id="step-2-servo-positioning-and-torque-limit"></a>
## Passo 2: Posicionamento do servo e limite de torque

![Posicionamento por servo](../../../../assets/images/assembly/Feetech-Servo-Window.png)

**Componentes necessários:**
- Existência SO-ARM100/101 controlador, cabo servo e alimentação do braço

**Instruções para usuários do Windows:**
1. Conectar o servo ao controlador de braço existente através do servo-bus e conectar o controlador ao PC por USB. Usa a fonte de alimentação do braço. Configurar uma identificação servo única antes de adicionar o agarrador à cadeia; fechar outras aplicações de controlo robótico antes de abrir a porta COM.
2. Configurar o servo com Feetech's **FD** (SCServo Ferramenta de depuração. É de código fechado .
   Software Windows de Feetech e é **Não** redistribuídos neste repositório:
   - Download oficial: <https://www.feetechrc.com/software.html> ⁇  procurar o FD /
     SCServo Debug arquivo. Alguns downloads estão protegidos por senha; solicite o
     senha de Feetech.
   - Alternativa multi-plataforma de código aberto:
     <https://github.com/Kotakku/FT_SCServo_Debug_Qt>

   Os passos abaixo descrevem a interface FD; a alternativa expõe o mesmo
   Parâmetros com nomes similares.
3. Escolha a sua porta COM, selecione BaudRate 1 000 000, pressione os botões "Abrir" e depois de "Buscar".
4. Abaixo da lista, selecione o seu servo.
5. Verifique a caixa para ativar o torque no servo.
6. Mova o deslizador para a esquerda.

![Limite máximo de torque](../../../../assets/images/assembly/max-torque-window.png)

7. Passe a janela para uma guia "Programação".
8. Escolha o parâmetro "Max Torque Limit", defina-o para 500 ans pressionando "Save".

---

<a id="step-3-clamps"></a>
## Passo 3: Clemas

![Mordentes](../../../../assets/images/assembly/clamp+rack+nail.PNG)

**Componentes necessários:**
- 2x Mordentes (RB9.01.062.021)
- 2x Cremalheiras (RB9.01.062.031)
- 2x Nails (RB9.01.062.100)

**Instruções:**
1. Insira as cremalheiras nos mordentes pela lateral.
2. Em seguida, insira os pregos pela parte traseira.

---

<a id="step-4-rods"></a>
## Passo 4: Barras

![Hastes-guia](../../../../assets/images/assembly/rods+clamps.PNG)

**Componentes necessários:**
- 2x Bastos D6x125mm

**Instruções:**
1. Inserir as hastes em ambas as pinças. Se tiver encomendado barras/tubos com mais de 125 mm, é necessário cortá-los a este comprimento.

---

<a id="step-5-install-bearings-on-main-frame"></a>
## Passo 5: Instale os rolamentos no quadro principal

![Os rolamentos instalados no quadro principal](../../../../assets/images/assembly/frame+bearings.png)

**Componentes necessários:**
- 2x MF106ZZ Os rolamentos (10x6x3 mm)
- 2x M4x8 parafusos DIN 7991

**Instruções:**
1. Insira o 2x MF106ZZ Os rolamentos em suas posições designadas no quadro principal. A flange de rolamento deve virar para cima.
2. Fixe cada rolamento com um parafuso M4x8.

---

<a id="step-6-connection-of-rods-and-frame"></a>
## Passo 6: Conexão das hastes e do quadro

![Conexão das hastes e do quadro principal](../../../../assets/images/assembly/frame-with-clamps.png)

**Instruções:**
1. Encaixe as hastes-guia na estrutura.
2. Afaste os mordentes até as posições extremas à esquerda e à direita.

---

<a id="step-7-mount-servo-on-main-frame"></a>
## Passo 7: Monte Servo no quadro principal

![Servo montado no quadro principal](../../../../assets/images/assembly/servo-on-frame.png)

**Componentes necessários:**
- 3x parafusos de auto-toque (do kit servo)

**Instruções:**
1. Colocar o servo no quadro principal e alinhar os buracos de montagem.
2. Fixe o servo com 3x parafusos autoatarraxantes do kit do servo.

---

<a id="step-8-gripper-holder-attachment"></a>
## Passo 8: Agregação do segurador de adesivos

![Fixação do retalhador de pegada](../../../../assets/images/assembly/09-gripper-holder-attachment.png)

**Componentes necessários:**
- 1x Suporte da câmera (RB9.01.060.074) ou Titular (RB9.01.060.080)
- 1x SO-ARM101
- Parafusos 4x M3x6 (do kit servo)
- 4x parafusos de auto-toque (do servo kit)

**Instruções:**
1. Se pretende usar o Gripper com câmera, então anexe o segurador da câmera. SO-ARM101 e fixa com parafusos 4x M3x6
2. Ligue a Gripper paralela ao portador da câmera e fixa-a com parafusos automáticos de 4x
3. Conectar o cabo do Gripper paralelo ao servo n.o 5 da SO-ARM101

---

<a id="step-9-camera-attachment-optional"></a>
## Passo 9: Anexo de câmera (opcional)

![Instalação de câmera](../../../../assets/images/assembly/camera-attachment.png)

**Componentes necessários:**
- 1x Câmara UVC com buracos de montagem a 28x28 mm
- 1x Espaçador da câmera (RB9.01.060.090)
- 4x M2x8 parafusos
- 4x M2 Nozes

**Instruções:**
1. Insira 4x porcas M2 pela parte traseira do suporte da câmera.
2. Coloque o espaçador e a câmera pela frente e fixe com 4x parafusos M2x8.

---
<a id="assembly-complete"></a>
## Assembléia completa!

![Reunião SO-ARM101 com Follower Gripper](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

Parabéns! O teu SO-ARM101 - está agora montada e pronta para utilização.

<a id="next-steps"></a>
### Passos seguintes
- Funcionamento do agarrador de ensaio antes da utilização
<!-- /translated-content -->
