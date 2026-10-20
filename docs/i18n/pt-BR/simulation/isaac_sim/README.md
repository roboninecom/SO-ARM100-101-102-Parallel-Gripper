<!-- translation-navigation -->
[English](../../../en/simulation/isaac_sim/README.md) · [Русский](../../../ru/simulation/isaac_sim/README.md) · [Español](../../../es/simulation/isaac_sim/README.md) · [Français](../../../fr/simulation/isaac_sim/README.md) · [Deutsch](../../../de/simulation/isaac_sim/README.md) · [Português (Brasil)](README.md) · [简体中文](../../../zh-CN/simulation/isaac_sim/README.md) · [日本語](../../../ja/simulation/isaac_sim/README.md) · [हिन्दी](../../../hi/simulation/isaac_sim/README.md) · [العربية](../../../ar/simulation/isaac_sim/README.md)

[Original em inglês](../../../../../simulation/isaac_sim/README.md)

[Português (Brasil)](../../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="nvidia-isaac-sim"></a>
# NVIDIA Isaac Sim

**Status: Não testado (simulador externo)**

Isaac Sim corre externamente e comunica com ROS2 por via `topic_based_ros2_control`. Tu corres. Isaac Sim separadamente e lançar o ROS2 lado com `sim:=isaac`.

<a id="prerequisites"></a>
## Pre-requisitos

- [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) 4.0+ (requer GPU NVIDIA RTX)
- ROS2 Humilde
- Isaac Sim ROS2 ponte habilitada
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Configuração

<a id="1-import-urdf-into-isaac-sim"></a>
### 1. Importação de URDF Isaac Sim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=isaac > /tmp/so_101_isaac.urdf
```

No Isaac Sim , sim .
1. **Isaac Utilidades > Importador URDF**
2. **Arquivo de entrada**Selecionar: `/tmp/so_101_isaac.urdf`
3. **Localização de importação**: `/World/so_101`
4. **Tipo de unidade conjunta**Posição:
5. **Fix Base Link**: verificado
6. Clique em **Importação**
7. Adicionar um avião terrestre: **Criar > Física > Avião de terra**
8. Salvo na fase USD (opcional)

<a id="2-configure-ros2-bridge-omnigraph"></a>
### 2. Configuração ROS2 Ponte (Omnigraph)

O `topic_based_ros2_control` O plugin comunica através destes tópicos:

| Tópico | Tipo | Direcção |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | Isaac Sim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> Isaac Sim |

<a id="omnigraph-setup"></a>
#### Configuração de OmniGraph

1. Abre **Janela > Visual Scripting > Grafico de Ação**
2. Criar um novo gráfico de ação
3. Adicionar estes nós:
   - **No Playback Tick** (fonte do evento)
   - **Isaac Tempo de Simulação**
   - **ROS2 Publicação do Estado comum** -- conectar-se a `/World/so_101`
   - **ROS2 Subscrever Estado Conjunto** -- para receber ordens
   - **Isaac Controlador de articulação** - aplica comandos às articulações

4. Ligue o gráfico:
   ```
   On Playback Tick -> Read Sim Time -> Publish Joint State
   On Playback Tick -> Subscribe Joint State -> Articulation Controller
   ```

5. Configuração **Publicação do Estado comum** nó:
   - `targetPrim`: `/World/so_101`
   - `topicName`: `/joint_states`

6. Configuração **Controlador de articulação** nó:
   - `targetPrim`: `/World/so_101`
   - `jointNames`: todos os 7 nomes comuns de `config/controllers.yaml`

<a id="alternative-isaac_ros2_control"></a>
#### Alternativa: isaac_ros2_control

Se `isaac_ros2_control` está disponível Isaac Sim versão:

```bash
sudo apt install ros-humble-isaac-ros2-control
```

Isso substitui a configuração de OmniGraph por uma `ros2_control` Interface de hardware.

<a id="3-launch"></a>
### 3. Lançamento

```bash
# Terminal 1: Start Isaac Sim and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
```

<a id="verify"></a>
## Verificar

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## Resolução de problemas

- **Falha na importação do URDF**: Assegure-se de que todos os caminhos de malha são absolutos. Gerar o URDF com `xacro` primeiro - não importar o `.xacro` Ficha diretamente.
- **Nenhum Estado comum**: Verifique se o OmniGraph está conectado e Isaac Sim está no modo Play.
- **Instabilidade física**: Em propriedades de cena física, definir o tipo de solvente para TGS e aumentar a contagem de iteração.
- **ROS2 ponte não encontrada**: Habilitar a extensão em **Janela > Extensões > ROS2 Ponte**.
<!-- /translated-content -->
