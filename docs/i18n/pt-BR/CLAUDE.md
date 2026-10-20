<!-- translation-navigation -->
[English](../en/CLAUDE.md) · [Русский](../ru/CLAUDE.md) · [Español](../es/CLAUDE.md) · [Français](../fr/CLAUDE.md) · [Deutsch](../de/CLAUDE.md) · [Português (Brasil)](CLAUDE.md) · [简体中文](../zh-CN/CLAUDE.md) · [日本語](../ja/CLAUDE.md) · [हिन्दी](../hi/CLAUDE.md) · [العربية](../ar/CLAUDE.md)

[Original em inglês](../../../CLAUDE.md)

[Português (Brasil)](README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="claudemd"></a>
# CLAUDE.md

Este arquivo fornece orientações ao código Claude (claude.ai/code) para trabalhar com o código neste repositório.

<a id="what-this-repository-is"></a>
## O que é este repositório

Um projeto de hardware open-source: um agarrador paralelo impresso em 3D para o SO-ARM100/101 braço robótico (por Robonine). Licença múltipla: CERN-OHL-P-2.0 para hardware/CAD, Apache-2.0 para software, CC BY 4.0 para doc  ⁇  o mapa está em `LICENSING.md`, a versão legível por máquina em `REUSE.toml`, atribuição de terceiros em `NOTICE`. Os novos ficheiros devem ser cobertos por: `REUSE.toml`; `reuse lint` - É um pré-comitamento. A maior parte do repo é de modelos CAD (`models/`), documentação (`docs/`), e imagens (`assets/`). O código vive em dois lugares:

- `software/python/gripper_control.py` ⁇  Escrito de comando servo independente para o Feetech STS3215 (depende da STServo SDK, que é clonado manualmente  ⁇  ver `software/python/requirements.txt`; não está no PyPI). `examples/basic_usage.py` importações provenientes de `sys.path` Hackear.
- `simulation/so_arm_101_description/` — a ROS2 Pacote de descrição que simula o braço + agarrador em 5 motores físicos. É aqui que vivem todos os testes e a maior parte das informações.

<a id="commands"></a>
## Comandações

```bash
# Lint (what CI runs; hooks exclude STL/STEP files)
pre-commit run --all-files

# Offline tests (65 pytest tests; deps: pytest trimesh numpy mujoco pyyaml)
cd simulation/so_arm_101_description
python -m pytest test/ -v

# Single test file / single test
python -m pytest test/test_urdf_structure.py -v
python -m pytest test/test_config.py -k <name> -v

# Validate xacro/URDF XML without ROS2
python simulation/so_arm_101_description/scripts/validate_xml.py simulation/so_arm_101_description/urdf/*.xacro

# Docker (from simulation/so_arm_101_description/; no ROS2 install needed)
docker compose run test          # run pytest suite
docker compose run validate      # xacro + check_urdf for all 5 backends
docker compose run check-launch  # verify launch files parse
docker compose run gazebo        # or: mujoco, webots, rviz (need X11)
```

CI (`.github/workflows/ci.yaml`) executadas: pré-comitamento, validação XML/YAML; `xacro ... sim_backend:=<backend> | check_urdf` para todos os 5 backends dentro de um `ros:humble` Container, e a suite Pitest. Uma alteração do URDF deve permanecer válida para **todos** As costas, não apenas a que estás a apontar.

<a id="simulation-architecture"></a>
## Arquitetura de simulação

Uma descrição do robô parametrizada impulsiona todos os simuladores:

- `urdf/so_101.urdf.xacro` É a única fonte da verdade. O xacro arg `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` seleciona o `ros2_control` Plug-in (via `urdf/so_101.ros2_control.xacro`) no momento da expansão.
- `config/controllers.yaml` define conjuntos/controladores idênticos para todos os backends; `launch/sim.launch.py` com `sim:=<backend>` é o único ponto de entrada.
- Robô: braço 5 DOF + aderente com 2 articulações de sujeira prismática, onde a sujeira esquerda reflete a direita através `<mimic>`.
- As malhas são divididas: `meshes/visual/` (High-poly) vs `meshes/collision/` (cascos convexos, regenerados com `scripts/generate_collision_meshes.py`).

Uma mudança em conjuntos, links ou nomes de controladores geralmente requer edições coordenadas nos arquivos xacro. `controllers.yaml`, e os testes em `test/`.

<a id="cad-models-and-part-numbering"></a>
## Modelos CAD e numeração de peças

Partes `models/parts/` Utilização Robonine Números de peças (por exemplo: `RB9.01.062.010 Main frame.STL`). Estes números são referenciados em toda a `README.md` (tabela impressa), `docs/bom.md`, e `docs/assembly-guide.md` ⁇  adicionar ou renomear uma parte significa atualizar também esses documentos. Os STL são binários; as variantes codificam tolerâncias de ajuste no nome do arquivo (por exemplo: `RB9.01.062.021 (D6.1) Clamp.STL` para diferentes diâmetros de barras). Os ganchos pré-comitados (espaço branco, EOF, terminações de linha) excluem deliberadamente `.stl/.STL/.STEP` Os arquivos e os arquivos superiores a 1 MB são rejeitados por `check-added-large-files`.

<a id="conventions"></a>
## Convenções

- Python: flake8 com `--max-line-length=100`, isort com perfil preto (imposto por pré-comitamento; `software/` e `examples/` são excluídas da flaque8).
- Os documentos são duplicados por design (README resume bom.md, specifications.md, assembly-guide.md)  ⁇  mantê-las consistentes ao alterar especificações, peças ou preços.
- Não adicionar um `Co-Authored-By: Claude` linha para compromissos.
<!-- /translated-content -->
