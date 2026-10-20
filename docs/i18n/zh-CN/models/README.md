<!-- translation-navigation -->
[English](../../en/models/README.md) · [Русский](../../ru/models/README.md) · [Español](../../es/models/README.md) · [Français](../../fr/models/README.md) · [Deutsch](../../de/models/README.md) · [Português (Brasil)](../../pt-BR/models/README.md) · [简体中文](README.md) · [日本語](../../ja/models/README.md) · [हिन्दी](../../hi/models/README.md) · [العربية](../../ar/models/README.md)

[英文原文](../../../../models/README.md)

[简体中文](../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="3d-models"></a>
# 3D模型

这个文件 ⁇ 包含Follower Gripper组件的STL文件.

<a id="complete-assembly"></a>
## 完整的集会

| 文件 | 描述 | 兼容的打印机 |
|------|-------------|---------------------|
| `Follower gripper (165x165 bed size).STL` | 全套抓紧器零件 | 床尺寸 > 165×165mm的打印机 |

<a id="compatible-3d-printers"></a>
### 兼容的3D打印机

- **⁇ 木实验室A1迷你** (180×180×180毫米
- **普鲁萨 MINI / MINI+** (180×180×180毫米
- **创造力 Ender-2 Pro** 它们的尺寸为165×165×180mm.
- **任何立方科布拉尼奥** (220×220×250毫米
- **炮兵天才** (220×220×250毫米

*注:任何床尺寸≥165×165mm的打印机都可以打印完整的装配预览.*

<a id="individual-parts"></a>
## 个别部分

位于 `parts/` 文件 ⁇ :

| 部分号码 | 文件 | 排量 | 描述 |
|-------------|------|:---:|-------------|
| RB9.01.060.074 | `Camera holder.STL` | 1 | 摄像机安装支架 |
| RB9.01.060.080 | `Holder.STL` | 1 | 没有摄像头的安装支架 |
| RB9.01.060.090 | `Camera spacer.STL` | 1 | 摄像机间隔器 |
| RB9.01.060.110 | `D405 holder.STL` | 1 | D405摄像头的持有器 |
| RB9.01.062.010 | `Main frame.STL` | 1 | 主要结构框架 |
| RB9.01.062.021 (D6.0) | `Clamp.STL` | 2 | 夹持指 |
| RB9.01.062.021 (D6.1) | `Clamp.STL` | 2 | 夹持指 |
| RB9.01.062.021 (D6.2) | `Clamp.STL` | 2 | 夹持指 |
| RB9.01.062.021 (D6.3) | `Clamp.STL` | 2 | 夹持指 |
| RB9.01.062.031 | `Gear rack.STL` | 2 | 适用于线性运动的 ⁇ 轮架 |
| RB9.01.062.040 | `Gear.STL` | 1 | 驱动齿轮 |
| RB9.01.062.100 | `Nail.STL` | 2 | 钉子 |

<a id="print-settings"></a>
## 打印设置

| 参数 | 推 ⁇ 值 |
|-----------|-------------------|
| 材料 | PLA/PETG |
| 层高度 | 0.2mm (0.15mm用于 ⁇ 轮) |
| 填充 | 20% (30%用于 ⁇ 轮) |
| 支持 | 根据需要 |
| 墙壁 | 3-4周边 |

<a id="notes"></a>
## 备忘录

- 打印 ⁇ 轮,填充量更高 (100%) 以提高强度
- 主架可能需要依据方向的支 ⁇
- 后加工:轴承合适可能需要轻光 ⁇
- 任何标准FDM打印机都可以打印单个零件

<a id="better-rods-fit"></a>
## ⁇ 子更适合
![测试板](../../../../assets/images/assembly/rod-test-plate.PNG)

为了确保你购买的棒更好地适合 ⁇ ,你需要使用一个测试件. 打印它,从最大孔到最小孔,选择允许棒在测试部件中轻松和尽量宽 ⁇ 的直径. 然后打印与 stl 文件名中提到的孔径相同的 ⁇  (例如: RB9.01.062.021 (D6.1) 如果选择直径6.1mm)
<!-- /translated-content -->
