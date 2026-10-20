<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](../../es/docs/specifications.md) · [Français](../../fr/docs/specifications.md) · [Deutsch](../../de/docs/specifications.md) · [Português (Brasil)](../../pt-BR/docs/specifications.md) · [简体中文](specifications.md) · [日本語](../../ja/docs/specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[英文原文](../../../specifications.md)

[简体中文](../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-100101-parallel-follower-gripper"></a>
# SO ARM 100/101 平行追随者抓住器

<a id="overview"></a>
## 概述

设计的轻量级3D打印终端效应器 **Robonine** 对于开源远程操作机器人平台SO ARM 100/101 该机制为可靠的平行 ⁇ 部运动提供了足够的抓住力,用于广泛的教育和实验应用.

![接着的抓住器安装 SO-ARM100](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*接着的抓住器安装 SO-ARM100 机器人手臂*

<a id="key-features"></a>
## 主要特征

- 开源设计
- 一个抓住器的BOM成本: ~$62
- 可在一个周期内在消费级FDM3D打印机上打印
- 适合流行的视频摄像头:
  - Orbbec 双胞胎2
  - RealSense D405, D435/D435i, D455
  - GC2093 2MP USB摄像机模块
  - IMX335 5MP USB 摄像头

---

<a id="dimensions"></a>
## 尺寸

<a id="3d-overview"></a>
### 3D概况

![抓住器尺寸  ⁇ 同位数视图](../../../../assets/images/specification/08-gripper-dimensions-3d.png)

*显示整体尺寸的同位数视图:128 × 109 × 130.5mm,全拍84mm*

| 尺寸 | 价值 |
|-----------|-------|
| 宽度 | 128毫米 |
| 深度 | 130.5毫米 |
| 高度 | 109毫米 |
| 全球冲击 | 84毫米 |

---

<a id="mounting-interface"></a>
## 装机接口

![装备接口尺寸](../../../../assets/images/specification/03-mounting-interface.jpg)

*机器人手臂 ⁇ 接的孔格式安装 ⁇*

| 功能 | 尺寸 |
|---------|-----------|
| 装 ⁇ 直径 | Ø20毫米 |
| 中部钻孔 | Ø7毫米 |
| 装机孔 | 4x Ø3.2毫米 |

---

<a id="gripper-parameters"></a>
## 夹爪参数

| 参数 | 从动臂夹爪 |
|-----------|------------------|
| 装配质量 (PLA,充满30%) | 170 g |
| 极限抓住力 | 120 N |
| 抓取速度最高 | 14毫米/秒 |
| 全球冲击 | 84毫米 |
| 复制性 | 0.5毫米 |
| 美国 | 1 |

---

<a id="technical-specifications"></a>
## 技术规格

<a id="materials--construction"></a>
### 材料和建筑

| 组件 | 规格 |
|-----------|---------------|
| 基本材料 | PETG/PLA |
| 传输 | 货架和 ⁇ 子 |
| 导游 | 圆 ⁇ /碳管 (Ø6mm) |
| 司机 | Feetech 伺服执行器 STS3215 |

<a id="servo-parameters-feetech-sts3215"></a>
### 服务器参数 (Feetech STS3215)

| 参数 | 价值 |
|-----------|-------|
| 运行电压范围 | 12V |
| 速度 (没有负载) | 45 RPM |
| 运行电流 (没有负载) | 180 mA |
| 停机扭矩 (锁定时) | 30公斤·厘米 |
| 停电 (锁定) | 2.7 A |
| ⁇ 置电流 (停止) | 30mA |
| 额定扭矩 | 10公斤·厘米 |
| 额定电流 | 900mA |
| 终端阻力 | 1 Ω |
| 操作温度 | -20°C ~ 60°C |
| 编码器类型 | 绝对磁性12位 |
| 控制协议 | RS485/TTL最大1 Mbps |
| 电子保护 | 抗高电压,电流,负载和温度 |

---

<a id="camera-compatibility"></a>
## 摄像头兼容性

通过可替换的相机持有器,Follower抓住器与各种摄像头兼容.

![在抓住器上安装的不同摄像头](../../../../assets/images/specification/09-camera-types.png)

*在抓住器上安装的不同摄像头 (左到右): RealSense,USB摄像头模块, Orbbec 双胞胎2*

<a id="supported-cameras"></a>
### 支持摄像头

| 摄像头 | 类型 | 备忘录 |
|--------|------|-------|
| IMX335 5MP USB | RGB | 紧 ⁇ ,低成本 |
| GC2093 2MP USB | RGB | 预算选择 |
| Orbbec 双胞胎2 | RGB-D | 深度传感 |
| RealSense D405 | RGB-D | 接近深度 |
| RealSense D435/D435i | RGB-D | 一般目的 |
| RealSense D455 | RGB-D | 长距离深度 |

---

<a id="supplied-resources"></a>
## 提供资源

- 3D打印的STL文件的完整套件
- 装配指南
- 装配尺寸的图纸
- 机器人模拟器的URDF文件

---

<a id="integration"></a>
## 整合

由于通过标准的安装 ⁇ 带,可方便且简单地安装该抓紧器,可以独立集成到众多机器人系统中.

<a id="mounting-requirements"></a>
### 增加的要求

- 4x M3螺丝用于 ⁇ 门接头
- 兼容于 SO-ARM100/101 机器人手臂
- 其他机器人手臂可用的定制适应器板

<a id="communication"></a>
### 沟通

- 通过TTL或RS485连接
- 低速:高达1 Mbps
- 协议: Feetech STS协议

---

<a id="product-specification-documents"></a>
## 产品规格文件

- [同步抓住器产品规范 (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf) ⁇  Robo9对平行抓住器的完整产品规格
- [SO-ARM101 产品规格 (PDF)](../../../SO-ARM101%20by%20Robo9.pdf) ⁇  全产品规格 SO-ARM101 机器人手臂由Robo9

---

*根据实际实施和测试的变化可能的规格*
<!-- /translated-content -->
