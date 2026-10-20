<!-- translation-navigation -->
[English](../../en/examples/README.md) · [Русский](../../ru/examples/README.md) · [Español](../../es/examples/README.md) · [Français](../../fr/examples/README.md) · [Deutsch](../../de/examples/README.md) · [Português (Brasil)](README.md) · [简体中文](../../zh-CN/examples/README.md) · [日本語](../../ja/examples/README.md) · [हिन्दी](../../hi/examples/README.md) · [العربية](../../ar/examples/README.md)

[Original em inglês](../../../../examples/README.md)

[Português (Brasil)](../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="examples---parallel-gripper"></a>
# Exemplos - Gripper paralelo

Este diretório contém exemplos de código que demonstram a utilização do agarrador paralelo em vários cenários.

<a id="available-examples"></a>
## Exemplos disponíveis

<a id="basic_usagepy"></a>
### `basic_usage.py`
Demonstra as funções fundamentais do agarrador:
- Conexão ao agarrador
- Movimento para posições específicas
- Informações sobre o estado de leitura
- Manutenção de erros básicos

**Utilização:**
```bash
cd examples
python basic_usage.py
```

<a id="configuration"></a>
## Configuração

Antes de executar exemplos, pode ser necessário ajustar os parâmetros de configuração:

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

<a id="common-issues"></a>
## Questões comuns

<a id="connection-problems"></a>
### Problemas de conexão
- **Janela**: Verifique o gerenciador de dispositivos para a correcção do porto COM
- **Linux**: Assegurar que o utilizador tenha acesso a portas em série (`sudo usermod -a -G dialout $USER`)
- **macOS**Utilização: `/dev/cu.usbserial-*` ou `/dev/tty.usbserial-*`

<a id="permission-errors"></a>
### Erros de autorização
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

<a id="stservo-sdk-issues"></a>
### STServo Questões do SDK
Certifique-se de que STServo O SDK está corretamente instalado:
1. Descarga em: [STServo Python SDK](https://files.waveshare.com/wiki/Bus-Servo-Adapter-(A)/STServo_Python.zip)
2. Extrair o arquivo ZIP baixado e copiar `STservo_sdk` pasta (com a própria pasta) para `software/python/` diretório

<a id="creating-your-own-examples"></a>
## Criando seus próprios exemplos

Ao criar novos exemplos:

1. **Importar o módulo de agarre**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **Tratar os erros com graça**
   ```python
   try:
       gripper = ParallelGripper()
       if not gripper.connect():
           print("Connection failed!")
           return
       # Your code here
   finally:
       gripper.disconnect()
   ```

3. **Incluir documentação adequada**
   - Descrição clara do que o exemplo faz
   - Instalação de hardware necessária
   - Comportamento esperado

<a id="safety-notes"></a>
## Notas de segurança

⚠️ **Importantes considerações de segurança:**
- Monitorar sempre a temperatura e o fluxo de corrente
- Implementar o tratamento adequado de erros
- Teste com forças baixas primeiro
- Assegurar a instalação mecânica adequada
- Mantenha os dedos longe das partes em movimento

<a id="contributing-examples"></a>
## Exemplos de contribuição

Acolhemos novos exemplos! Por favor, não me esqueça.
- Siga o estilo de código existente
- Incluir observações abrangentes
- Teste minuciosamente antes da submissão
- Adicionar entrada a este README

---

**Feliz codificação!** 🤖
<!-- /translated-content -->
