<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[Original em inglês](../../../CONTRIBUTING.md)

[Português (Brasil)](README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing-to-open-source-parallel-gripper"></a>
# Contribuindo para o Gripper Parallel Open-Source

Obrigado pelo seu interesse em contribuir para este projecto! Acolhemos as contribuições da comunidade robótica.

<a id="ways-to-contribute"></a>
## Maneras de contribuir

<a id="-bug-reports"></a>
### ⁇  Relatórios de insetos
- Use o rastreador de problemas do GitHub
- Incluir medidas de reprodução detalhadas
- Fornecer informações sobre o sistema (OS, Python versão, modelo servo)
- Anexar registos ou mensagens de erro

<a id="-feature-requests"></a>
### ⁇  Pedidos de características
- Verifique primeiro as questões existentes
- Descrever claramente o caso de utilização
- Considere a complexidade da implementação
- Discutir com os administradores antes de grandes mudanças

<a id="-code-contributions"></a>
### ⁇  Contribuições de código
- Forque o repositório
- Criar um ramo de recursos
- Seguir as normas de codificação
- Adicionar os testes, se for caso disso
- Documentação actualizada

<a id="-documentation"></a>
### ⁇  Documentação
- Melhorar a documentação existente
- Adicionar exemplos de uso
- Criar tutoriais ou guias
- Corrigir erros de digitação ou explicações pouco claras

<a id="-hardware-improvements"></a>
### ⁇ ️ Melhorias de hardware
- Modificações ou melhorias de projeto
- Sugestões de partes alternativas
- Nova compatibilidade de servo
- Optimização mecânica

<a id="development-setup"></a>
## Configuração de desenvolvimento

1. **Clone o repositório**
   ```bash
   git clone https://github.com/your-org/parallel-gripper.git
   cd parallel-gripper
   ```

2. **Instalar dependências**
   ```bash
   pip install -r software/python/requirements.txt
   ```

3. **Instalação STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cp -r STServo_SDK_Python/STservo_sdk ./software/python/
   ```

<a id="coding-standards"></a>
## Normas de codificação

<a id="python-code"></a>
### Python Código
- Seguir o guia de estilo PEP 8
- Use indicações de tipo, quando apropriado
- Adicionar cadeias de documentos para todas as funções/classes
- Duração máxima da linha: 88 caracteres
- Usar nomes significativos de variáveis

<a id="documentation"></a>
### Documentação
- Use o formato Markdown
- Incluir exemplos de códigos
- Mantenha a linguagem clara e concisa
- Actualizar o README se necessário

<a id="3d-models"></a>
### Modelos 3D
- Fornecer arquivos STL em formato binário
- Incluir os ficheiros-fonte, se possível (STEP, Fusion 360, etc.)
- Impressão de ensaio antes do envio
- Configurações de impressão do documento

<a id="pull-request-process"></a>
## Processo de Pull Request

1. **Antes de começar**
   - Verificar as questões e relações públicas existentes
   - Discutir as principais mudanças primeiro
   - Certifique-se de poder testar as suas alterações

2. **Fazer mudanças**
   - Criar um nome de ramo descritivo
   - Faça compromissos atômicos com mensagens claras
   - Teste as suas mudanças de forma completa
   - Atualizar a documentação conforme necessário

3. **Submissão de relações públicas**
   - Preencher o modelo de PR
   - Questões relacionadas com a ligação
   - Descrever claramente as alterações
   - Incluir informações de ensaio

4. **Processo de revisão**
   - Reacções dos revisores de endereços
   - Mantenha as discussões construtivas
   - Tenha paciência com o processo de revisão

<a id="testing-guidelines"></a>
## Orientações para os testes

<a id="software-testing"></a>
### Testes de software
- Teste na configuração do hardware
- Verificar a compatibilidade entre plataformas
- Verificar o tratamento de erros
- Casos de ponta de ensaio

<a id="hardware-testing"></a>
### Testeamento de hardware
- Verifique que as impressões 3D funcionam corretamente
- Procedimentos de montagem de ensaio
- Verificar as tolerâncias mecânicas
- Validação com diferentes materiais

<a id="communication"></a>
## Comunicação

<a id="channels"></a>
### Canais
- Questões do GitHub: relatórios de bugs, solicitações de recursos
- Discussões do GitHub: perguntas gerais, ideias
- Pedidos de retirada: revisão do código, discussão técnica

<a id="guidelines"></a>
### Orientações
- Seja respeitoso e construtivo
- Pesquisa antes de publicar
- Fornecer contexto e detalhes
- Ajudar os outros quando possível

<a id="recognition"></a>
## Reconhecimento

Os contribuintes serão reconhecidos em:
- README.md secção contribuintes
- Notas de liberação
- Documentação do projecto

<a id="license"></a>
## Licença

Este projeto é licenciado em vários domínios  ⁇  ver [`LICENSING.md`](LICENSING.md) Para o mapa completo.

Ao apresentar uma contribuição, certifica que tem o direito de a submeter,
e concorda que é licenciado sob a licença aplicável à parte de
o repositório em que pousa:

| Estás a mudar . | A sua contribuição é licenciada . |
|---|---|
| Hardware / CAD | CERN-OHL-P-2.0 |
| Software | Apache-2.0 |
| Documentação e imagens | CC BY 4.0 |

Em outras palavras, entrada = saída: seja qual for a licença em que um ficheiro já está sujeito,
A sua alteração está sob a mesma licença.

**Material de terceiros.** Se a sua contribuição inclui qualquer coisa que não tenha feito
criar-se, dizer isso na solicitação de puxar para que possa ser gravado em
[`NOTICE`](../../../NOTICE). Por favor , não comete binários que você não pode licenciar
Inclui ferramentas e firmware do fornecedor.

**Novos arquivos** devem ser cobertas por: [`REUSE.toml`](../../../REUSE.toml). `reuse lint` corre em
no pre-commit e na CI, e falhará se algum arquivo não tiver informações de direitos autorais e licença
Informações.

<a id="questions"></a>
## Perguntas?

Não se sentem livres para abrir um número ou iniciar uma discussão se tiverem perguntas sobre contribuir!

---

**Obrigado por ajudar a melhorar este projeto!** 🤝
<!-- /translated-content -->
