<!-- translation-navigation -->
[English](../../en/docs/quick-start.md) · [Русский](../../ru/docs/quick-start.md) · [Español](../../es/docs/quick-start.md) · [Français](../../fr/docs/quick-start.md) · [Deutsch](../../de/docs/quick-start.md) · [Português (Brasil)](quick-start.md) · [简体中文](../../zh-CN/docs/quick-start.md) · [日本語](../../ja/docs/quick-start.md) · [हिन्दी](../../hi/docs/quick-start.md) · [العربية](../../ar/docs/quick-start.md)

[Original em inglês](../../../quick-start.md)

[Português (Brasil)](../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="quick-start-guide"></a>
# Guia de início rápido

Traz o teu Follower Gripper para SO-ARM101 Vão correr!

[![SO-ARM101 Garra paralela](../../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

*Clique na imagem para [Observe o agarrador em ação](https://youtube.com/shorts/bSyXjgNGXZk)!*

<a id="what-youll-need"></a>
## O que você precisará

<a id="hardware"></a>
### Ferramentas
- [ ] Todas as peças impressas em 3D (ver [Modelos 3D](../models/README.md))
- [ ] Componentes eletrônicos (ver [BOM](bom.md))
- [ ] Componentes mecânicos (aterros, barras, fixações)
- [ ] Ferramentas: parafusador Phillips PH1, teclas Hex M2 (H1.5) e M4 (H2.5)

<a id="software"></a>
### Software
- [ ] Python 3.6 + instalado
- [ ] STServo SDK baixado
- [ ] Existência SO-ARM100/101 controlador, conexão USB e alimentação do braço

---

<a id="step-1-3d-print-the-parts-2-4-hours"></a>
## Passo 1: Impressão 3D das peças (2-4 horas)

1. Descarregar arquivos STL de `models/parts/`
2. Impressão com configurações recomendadas:
   - Altura da camada:0.2mm
   - Preenchimento: 20% (quadro/presas), 100% (engrenagens)
   - Material: PLA ou PETG
3. Remover suportes

![Placa de ensaio](../../../../assets/images/assembly/rod-test-plate.PNG)

Para garantir que as hastes compradas se encaixem melhor nas sujeiras, é preciso usar uma peça de teste. Imprima-o e, trabalhando do buraco mais grande ao menor, selecione o diâmetro que permita que a vara se encaixa na parte de ensaio sem dificuldade e com um espaço mínimo. Em seguida, imprimir as sujeiras com o mesmo diâmetro de buraco que é mencionado no nome do arquivo stl (por exemplo: RB9.01.062.021 (D6.1) se escolher o diâmetro6.1mm).

**Impressoras 3D compatíveis** (180×180mm + cama):
- Bambu Lab A1 mini
- Prusa MINI / MINI+
- Anycubic Kobra Neo
- Qualquer impressora com cama ≥ 180×180 mm

**Partes para impressão:**
- 1x Estrutura principal (RB9.01.062.010)
- 2x Mordente (RB9.01.062.020)
- 2x Cremalheira (RB9.01.062.030)
- 1x Engrenagem (RB9.01.062.040)
- 1x Suporte da câmera (RB9.01.060.074)
- 1x Suporte (RB9.01.060.080)
- 1x Espaçador da câmera (RB9.01.060.090)

---

<a id="step-2-gather-components-1-2-days-shipping"></a>
## Passo 2: Recolha os componentes (1-2 dias de envio)

As peças de encomenda [Lista de Materiais](bom.md). Reutilizar o controlador de braço e a alimentação; estes estão fora do custo da sujeira:

| Componente | Qty | - Não. Custo |
|-----------|:---:|-----------|
| Feetech STS3215 servo | 1 | ~$29 |
| MF106ZZ Rolamentos (10x6x3 mm) | 2 | ~$2 |
| Tubos de alumínio/carbono D6x1x125mm | 2 | ~$4 |
| Impressão 3D PLA| 8 partes | ~$12 |
| Ferramentas de fixação (fusos/nuts M2/M4) | variados | ~$3 |

**Custo estimado total: ~$50**

---

<a id="step-3-assembly-30-45-minutes"></a>
## Passo 3: Assembléia (30-45 minutos)

Seguir os detalhes [Guia de Assembleia](assembly-guide.md):


1. Inserir cabo de servo
2. Utilização Feetech software mover servo para a sua posição mínima (mover o deslizador no software para a esquerda)
3. Prenda as cremalheiras aos mordentes
4. Insira as hastes-guia nos dois mordentes
5. Instale os rolamentos na estrutura principal e fixe-os com parafusos
6. Encaixe as hastes-guia na estrutura
7. Afaste os mordentes até as posições extremas à esquerda e à direita
8. Insira o servo e fixa com parafusos
9. Aplicar a câmera de espaçamento e a câmera UVC, fixação com parafusos 4x e frutos secos M2 (facultativo)
10. Montagem para braço robótico (opcional)

---

<a id="step-4-software-setup-10-minutes"></a>
## Passo 4: Configuração do software (10 minutos)

1. **Instalação STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cd STServo_SDK_Python
   cp -r STservo_sdk /path/to/your/project/
   ```

2. **Instalação Python dependências**
   ```bash
   pip install pyserial
   ```

3. **Configurar ligação**
   ```python
   DEVICENAME = 'COM7'  # Windows
   # DEVICENAME = '/dev/ttyUSB0'  # Linux
   STS_ID = 1  # Servo ID (use 6 if connected as gripper on SO-ARM101)
   ```

---

<a id="step-5-first-test-5-minutes"></a>
## Passo 5: Primeiro teste (5 minutos)

1. **Conectar hardware**
   - Gripper servo → servo n.o 5 no SO-ARM101 autocarro
   - Controlador de braço existente → Computador (USB)
   - Usar a fonte de alimentação do braço configurada para os servos instalados
   - Configurar a identificação servo do agarrador para corresponder `STS_ID` E mantém-no único no autocarro .
   - Fechar outras aplicações de controlo do robô antes de abrir a porta em série

2. **Realizar teste básico**
   ```bash
   cd software/python
   python gripper_control.py
   ```

3. **Tente os comandos básicos .**
   - Entrar `45` para abrir a garra
   - Entrar `-45` para fechar a garra
   - Entrar `0` para o centro
   - Pressione Entrar para sair

---

<a id="troubleshooting"></a>
## Resolução de problemas

<a id="connection-issues"></a>
### Questões de conexão
- ✅ Verifique a porta COM no Gerenciador de dispositivos (Windows) ou `ls /dev/ttyUSB*` (Linux)
- ✅ Verifique se o LED de servo está ligado
- ✅ Experimente diferentes taxas de baud (default: 1000000)
- ✅ Verifique as conexões por cabo

<a id="movement-issues"></a>
### Questões de Movimento
- ✅ Verificar o envolvimento dos equipamentos com o rack
- ✅ Verificação de ligação mecânica
- ✅ Assegurar que os rolamentos se movam livremente nas hastes
- ✅ Monitorar a temperatura do servo (max. 60°C)

<a id="software-issues"></a>
### Problemas com o software
- ✅ Instalar STServo SDK corretamente
- ✅ Cheque Python versão (3.6+)
- ✅ Verifique as permissões de portas em série: `sudo chmod 666 /dev/ttyUSB0` (Linux)

---

<a id="next-steps"></a>
## Passos seguintes

🎉 **Parabéns!** O seu agarrador está a funcionar!

Agora podes:
- Montar em SO-ARM100/101 braço robótico
- Integrar com o seu software de controle
- Adicionar uma câmera ao portador da câmera
- Criar aplicativos personalizados

<a id="need-help"></a>
## Precisas de ajuda?

- ⁇  Leia o [Especificações](specifications.md)
- ⁇  Verificar o [Guia de Assembleia](assembly-guide.md)
- 📄 [Especificações do produto de pegamento paralelo (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf)
- 📄 [SO-ARM101 Especificações do produto (PDF)](../../../SO-ARM101%20by%20Robo9.pdf)
- ⁇  Relatório de problemas no GitHub

---

**Bem-vindo à comunidade de agarradores paralelas!** 🤖
<!-- /translated-content -->
