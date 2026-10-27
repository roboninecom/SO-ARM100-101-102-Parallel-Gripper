<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[英文原文](../../../README.md)

[简体中文](README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm100101-parallel-gripper"></a>
# SO-ARM100/101 平行夹爪

<div align="center">

[![SO-ARM101 平行夹爪](../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

**🎥 [看着抓住器在行动!](https://youtube.com/shorts/bSyXjgNGXZk)** · **🛒 [购买 SO-ARM102 有平行抓住器的套件](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

设计的轻量级3D打印平行抓住器 **[Robonine](https://robonine.com)** 对于开源 SO-ARM100/101 机器人平台.

> 你更喜欢一套完整的机器人手臂套件? **[购买 SO-ARM102 套件](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

[![硬件: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt)
[![软件: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt)
[![文件: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt)
[![价格: ~$50](https://img.shields.io/badge/Cost-~%2450-green.svg)](docs/bom.md)
[![组装时间:30分钟](https://img.shields.io/badge/Assembly-30%20min-orange.svg)](docs/assembly-guide.md)

---

**有什么问题? 我们来这里是为了帮助!**
⁇ 电子邮件: [您的好@robonine.com](mailto:hello@robonine.com)

</div>

---

<a id="-key-features"></a>
## ✨ 主要特征

| 功能 | 描述 |
|---------|-------------|
| **120N 抓取力** | 可靠的平行 ⁇  jaws机制 |
| **14mm/s 速度** | 抓住器运行速度 |
| **84毫米全力冲击** | 对各种物体的宽 ⁇ 开放 |
| **0.5mm 可重复性** | 高精度定位 |
| **相机兼容** | 支持 RealSense, Orbbec,USB摄像头 |
| **3D打印式** | 所有零件均用标准FDM打印机打印 |
| **~$50总成本** | 经济适用的开源解决方案 |
| **容易组装** | 30-45分钟使用基本工具 |

---

<a id="-gallery"></a>
## ⁇ 画廊

<div align="center">

<a id="gripper-on-so-arm101"></a>
### 夹爪安装于 SO-ARM101

![夹爪安装于 SO-ARM101](../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*附着的跟随器抓住器 SO-ARM101 机器人手臂*

<a id="dimensions"></a>
### 尺寸

![夹爪尺寸](../../../assets/images/specification/08-gripper-dimensions-3d.png)

*128 × 109 × 130.5 mm,全程 84 mm*

</div>

---

<a id="-specifications"></a>
## ⁇ 规格

<a id="gripper-parameters"></a>
### 夹爪参数

| 参数 | 价值 |
|-----------|-------|
| 极限抓住力 | **120 N** |
| 抓取速度最高 | **14毫米/秒** |
| 全球冲击 | **84毫米** |
| 复制性 | **0.5毫米** |
| 装配质量 (PLA,充满30%) | **170 g** |
| 美国 | **1** |

<a id="dimensions-1"></a>
### 尺寸

| 尺寸 | 价值 |
|-----------|-------|
| 宽度 | 128毫米 |
| 深度 | 130.5毫米 |
| 高度 | 109毫米 |

<a id="servo-parameters-feetech-sts3215"></a>
### 服务器参数 (Feetech STS3215)

| 参数 | 价值 |
|-----------|-------|
| 运行电压 | 12V |
| 堵转扭矩 | 30公斤·厘米 |
| 速度 (没有负载) | 45 RPM |
| 编码器 | 绝对磁性12位 |
| 议定书 | RS485/TTL最大1 Mbps |
| 操作温度 | -20°C ~ 60°C |

---

<a id="-camera-compatibility"></a>
## ⁇ 相机兼容性

通过可替换的相机持有器,抓住器支持多部摄像头:

| 摄像头 | 类型 | 使用案例 |
|--------|------|----------|
| IMX335 5MP USB | RGB | 基本视觉任务 |
| GC2093 2MP USB | RGB | 预算选择 |
| Orbbec 双胞胎2 | RGB-D | 3D感知 |
| RealSense D405 | RGB-D | 接近深度 |
| RealSense D435/D435i | RGB-D | 一般目的 |
| RealSense D455 | RGB-D | 长距离深度 |

<div align="center">

![在抓住器上安装的不同摄像头](../../../assets/images/specification/09-camera-types.png)

*RealSense,USB摄像头模块, Orbbec 双胞胎2*

</div>

---

<a id="-bill-of-materials"></a>
## ⁇ 材料文件

**总成本: ~$50** ([全BOM与亚马逊链接](docs/bom.md))

| 类别 | 组件 | 东部. 费用 |
|----------|------------|-----------|
| 电子 | Feetech STS3215 服务器 | ~$29 |
| 轴承 | MF106ZZ (x2) | ~$2 |
| ⁇ /碳管 | D6x1×125毫米 (x)2) | ~$4 |
| 3D打印 | 8个部件 (~100-150g PLA) | ~$12 |
| 紧固件 | 螺丝 M2/M4,M2核子,M3设置螺丝 | ~$3 |

---

<a id="-quick-start"></a>
## ⁇ 快速开始

对于一套完整的机器人手臂套件, **[购买 SO-ARM102 套件](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**. 为了建立 SO-ARM100/101 抓住自己,跟随下面的步骤.

<a id="1-print-the-parts-2-4-hours"></a>
### 1. 打印部件 (2-4小时)

下载STL文件 [`models/parts/`](models/README.md). 适合像 **⁇ 木实验室A1迷你**, **普鲁萨 MINI+**,以及任何床位≥180×180mm的打印机.

| 部分 | 排量 | 设置 |
|------|:---:|----------|
| 主框架 (RB9.01.062.010) | 1 | 充满20% |
| 夹爪 (RB9.01.062.020) | 2 | 充满20% |
| 齿条 (RB9.01.062.030) | 2 | 100%填充 |
| 齿轮 (RB9.01.062.040) | 1 | 100%填充 |
| 相机支架 (RB9.01.060.074) | 1 | 充满20% |
| 支架 (RB9.01.060.080) | 1 | 充满20% |
| 相机垫块 (RB9.01.060.090) | 1 | 充满20% |
| D405 持有者 (RB9.01.060.110) | 1 | 充满20% |

<a id="2-order-components-1-2-days"></a>
### 2. 订单组件 (1-2天)

看看 [材料文件](docs/bom.md) 在亚马逊的直接链接上.

<a id="3-assemble-30-45-minutes"></a>
### 3. 组装 (30-45 分钟)

按照 [会议指南](docs/assembly-guide.md) 用步骤图像:

1. 在伺服器盘上安装设备.
2. 插入伺服电缆
3. 使用 Feetech 软件将伺服器移到最小位置 (在软件中的滑动器移向左)
4. 将齿条固定到夹爪上
5. 将导杆插入两个夹爪
6. 将轴承装入主框架并用螺钉固定
7. 将导杆卡入框架
8. 将两个夹爪分别移至最左端和最右端
9. 插入伺服器并用螺丝固定它
10. 连接摄像头间隔器和UVC摄像头,用4x螺丝和M2坚果固定 (可选)
11. ⁇ 到机器人手臂 (可选)

<a id="4-software"></a>
### 4. 软件

```bash
# Configure servo motor if necessary
https://lab.robonine.com/tools/robonine/feetech-bus

# Control gripper
https://lab.robonine.com/tools/robonine/control-robot
```

---

<a id="-repository-structure"></a>
## ⁇ 存储库结构

```
├── assets/
│   └── images/
│       ├── assembly/          # Assembly step images
│       └── specification/     # Technical drawings
├── docs/
│   ├── assembly-guide.md                # Step-by-step assembly
│   ├── bom.md                           # Bill of materials with links
│   ├── Parallel gripper by Robo9.pdf    # Gripper product specification
│   ├── quick-start.md                   # Getting started guide
│   ├── SO-ARM101 by Robo9.pdf           # SO-ARM101 product specification
│   └── specifications.md               # Technical specifications
├── models/
│   ├── parts/                                    # Individual STL files
│   └── Follower gripper (165x165 bed size).STL   # Complete assembly (165×165mm bed)
├── community/
│   └── histology-slide-gripper/   # Community variant (CAD, MuJoCo model)
├── simulation/
│   ├── README.md                  # Simulation overview
│   ├── gazebo/                    # Gazebo guide
│   ├── mujoco/                    # MuJoCo guide
│   ├── webots/                    # Webots guide
│   ├── coppeliasim/               # CoppeliaSim guide
│   ├── isaac_sim/                 # Isaac Sim guide
│   └── so_arm_101_description/    # ROS2 package (URDF, launch, Docker)
├── software/
│   └── python/                # Control software
├── examples/                  # Usage examples
├── HARDWARE-LICENSE.txt       # CERN-OHL-P-2.0 (CAD, geometry)
├── SOFTWARE-LICENSE.txt       # Apache-2.0 (code)
├── DOCS-LICENSE.txt           # CC BY 4.0 (docs, images)
├── LICENSING.md               # Which licence covers what
├── NOTICE                     # Third-party attribution
├── REUSE.toml                 # Machine-readable licence map
├── RELICENSING.md             # Record of the 2026 relicensing
└── CONTRIBUTING.md
```

---

<a id="-documentation"></a>
## ⁇ 文件

| 文件 | 描述 |
|----------|-------------|
| [快速启动指南](docs/quick-start.md) | 在30分钟内开始跑步 |
| [会议指南](docs/assembly-guide.md) | 一步一步的图像 |
| [抓住器组装指南 (PDF)](../../Assembly%20Guide%20Follower%20Gripper.pdf) | 打印式抓住器组装说明 |
| [SO-ARM101 会议指南 (PDF)](../../Assembly%20Guide%20SO-ARM101.pdf) | 全面 SO-ARM101 手臂组装说明 |
| [材料文件](docs/bom.md) | 亚马逊链接的零件列表 |
| [规格](docs/specifications.md) | 技术细节 |
| [3D模型](models/README.md) | 打印设置和文件 |
| [同步抓住器产品规格 (PDF)](../../Parallel%20gripper%20by%20Robo9.pdf) | 机器人9的平行抓住器产品规格 |
| [SO-ARM101 产品规格 (PDF)](../../SO-ARM101%20by%20Robo9.pdf) | SO-ARM101 机器人手臂产品规格由Robo9 |

---

<a id="-hardware-requirements"></a>
## ⁇ 硬件要求

<a id="electronics"></a>
### 电子
- 1× Feetech STS3215 伺服电机

连接抓紧器到现有的 SO-ARM100/101 服务器和控制器.
机器人控制器和电源是臂部设置的一部分,

<a id="mechanical"></a>
### 机械
- 2× MF106ZZ 轴承 (6×10×3mm)
- 2× ⁇ /碳管 D6x1×125mm

<a id="fasteners"></a>
### 紧固件
- 2×M4×8 DIN 7991螺丝
- 4x M2x8 DIN 912螺丝
- 4×M2 DIN 934坚果
- 4×M3×4 DIN 913设置螺丝

<a id="tools-required"></a>
### 需要的工具
- ⁇ 螺旋转机 (PH1)
- 六重键M2 (H1.5) 和M4 (H2.5)

---

<a id="-simulation"></a>
## ⁇ ️模拟

SO-ARM101 可通过 ROS2 描述包和统一的参数化 URDF 在 5 种物理引擎中仿真。无需安装 ROS2，全部由 Docker 处理。

<div align="center">

| Gazebo (火焰堡垒) | MuJoCo |
|:-:|:-:|
| ![SO-ARM-101 在 Gazebo](../../../assets/images/simulation/gazebo/gazebo_pick_place.png) | ![SO-ARM-101 在 MuJoCo](../../../assets/images/simulation/mujoco/mujoco_pick_place.png) |

</div>

| 模拟器 | 状态 | 码头 |
|-----------|--------|--------|
| [Gazebo](simulation/gazebo/README.md) | 准备好 | `docker compose run gazebo` |
| [MuJoCo](simulation/mujoco/README.md) | 准备好 | `docker compose run mujoco` |
| [Webots](simulation/webots/README.md) | 不稳定 | `docker compose run webots` |
| [CoppeliaSim](simulation/coppeliasim/README.md) | 未经测试 | 外部模拟器 |
| [印度 Isaac 是的](simulation/isaac_sim/README.md) | 未经测试 | 外部模拟器 |

**快速启动 (Docker):**

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

看看 [模拟指南](simulation/README.md) 对于完整的设置,建筑细节和机器人指挥.

---

<a id="-community-mods"></a>
## ⁇ 社区模式

社区构建的 ⁇ 接器的变体,每种自主 [`community/`](../../../community):

| 调整器 | 作者 | 描述 |
|-----|--------|-------------|
| [历史学幻灯片抓住器](community/histology-slide-gripper/README.md) | [迈克尔·维亚切斯拉夫](https://github.com/histochemichael) | 75 x 25 mm显微镜滑梯和涂料 ⁇ 布/架,加上一个角式的Arducam持有器来监控抓. |

<div align="center">

<a href="community/histology-slide-gripper/README.md"><img src="../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg" alt="Histology slide gripper mod holding a microscope slide" width="400"></a>

*历史学Slide Gripper mod  ⁇  点击查看完整的描述,CAD文件和演示*

</div>

---

<a id="-contributing"></a>
## ⁇ 贡献

我们欢迎捐款! 您可以:
- ⁇ 报告错误和问题
- ⁇ 建议新的功能
- ⁇ 提交拉动请求
- ⁇ 改善文档

---

<a id="-license"></a>
## ⁇ 许可证

版权 (c) 2025 Robonine. 这项项目拥有多种许可证
材料具有不同的许可证:

| 材料 | 许可证 |
|---|---|
| 硬件设计 `models/`,社区CAD,抓住网 | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| 软件 `software/`, `examples/`, `simulation/`,模拟代码在 `community/` | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| 文件和图像 `docs/`, `assets/`所有的 `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

看看 [`LICENSING.md`](LICENSING.md) 具体的文件按文件地图和
[`REUSE.toml`](../../../REUSE.toml) 在机器可读的版本中.

**这里的一切都不是 Robonine是工作.** 其他 SO-ARM101 手臂网格是从中获得的
在 [TheRobotStudio在上游的项目](https://github.com/TheRobotStudio/SO-ARM100)
并且保持 Apache-2.0; 史蒂斯科幻灯片抓住器由
[没有任何问题.](https://github.com/histochemichael). 看看 [`NOTICE`](../../../NOTICE)
在重新使用任何网格之前.

释放至包括 `v0.3.1` 在GPL-3.0下发布,并且仍然存在
在这些条款下可使用 ⁇ 见 [`RELICENSING.md`](RELICENSING.md).

---

<a id="-links"></a>
## ⁇ 链接

- [Feetech STS3215 服务器](https://www.feetechrc.com/525603.html)
- [STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python)

---

<a id="-engineering-team"></a>
## ⁇ 工程团队

| 名称 | 角色 | 联系人 |
|------|------|---------|
| **博里斯·科托夫** | 软件工程师 | [电报](https://t.me/bkotov) |
| **艾伦·苏宾** | 设计工程师 | [链接](https://www.linkedin.com/in/alan-subin/) |

---

<a id="-star-history"></a>
## ⭐ 星标历史

[![星标历史](https://api.star-history.com/svg?repos=roboninecom/so-arm100-101-parallel-gripper&type=Date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm100-101-parallel-gripper&type=date&legend=top-left)

---

<div align="center">

**为了机器人社区 [Robonine](https://robonine.com)** 🤖

**有什么问题? 我们来这里是为了帮助!**
⁇ 电子邮件: [您的好@robonine.com](mailto:hello@robonine.com)

</div>
<!-- /translated-content -->
