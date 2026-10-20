<!-- translation-navigation -->
[English](../../en/docs/quick-start.md) · [Русский](../../ru/docs/quick-start.md) · [Español](../../es/docs/quick-start.md) · [Français](../../fr/docs/quick-start.md) · [Deutsch](../../de/docs/quick-start.md) · [Português (Brasil)](../../pt-BR/docs/quick-start.md) · [简体中文](quick-start.md) · [日本語](../../ja/docs/quick-start.md) · [हिन्दी](../../hi/docs/quick-start.md) · [العربية](../../ar/docs/quick-start.md)

[英文原文](../../../quick-start.md)

[简体中文](../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="quick-start-guide"></a>
# 快速启动指南

给你的追随者抓住器 SO-ARM101 走上了!

[![SO-ARM101 平行夹爪](../../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

*点击图像 [看着抓住器在操作中](https://youtube.com/shorts/bSyXjgNGXZk)!*

<a id="what-youll-need"></a>
## 你需要的东西

<a id="hardware"></a>
### 硬件
- [ ] 所有3D打印部件 (见 [3D模型](../models/README.md))
- [ ] 电子组件 (见 [爆炸事件](bom.md))
- [ ] 机械部件 (轴承,棒,固定器)
- [ ] 工具:菲利普斯螺旋 ⁇  PH1,赫克斯键M2 (H1.5) 和M4 (H2.5)

<a id="software"></a>
### 软件
- [ ] Python 3.6+安装
- [ ] STServo 下载的 SDK
- [ ] 现有 SO-ARM100/101 控制器,USB连接和手臂电源

---

<a id="step-1-3d-print-the-parts-2-4-hours"></a>
## 步骤1: 3D打印零件 (2-4小时)

1. 下载STL文件 `models/parts/`
2. 使用建议设置打印:
   - 层高度:0.2mm
   - 填充量:20% ( ⁇ / ⁇ ),100% ( ⁇ 轮)
   - 材料:PLA或PETG
3. 移除支 ⁇

![测试板](../../../../assets/images/assembly/rod-test-plate.PNG)

为了确保你购买的棒更好地适合 ⁇ ,你需要使用一个测试件. 打印它,从最大孔到最小孔,选择允许棒在测试部件中轻松和尽量宽 ⁇ 的直径. 然后打印与 stl 文件名中提到的孔径相同的 ⁇  (例如: RB9.01.062.021 (D6.1) 如果选择直径6.1mm)

**兼容的3D打印机** (180×180毫米+床):
- ⁇ 木实验室A1迷你
- 普鲁萨 MINI / MINI+
- 任何立方科布拉尼奥
- 任何床位 ≥180×180mm的打印机

**打印的部件:**
- 1x 主框架 (RB9.01.062.010)
- 2x 夹爪 (RB9.01.062.020)
- 2x 齿条 (RB9.01.062.030)
- 1x 齿轮 (RB9.01.062.040)
- 1x 相机支架 (RB9.01.060.074)
- 1x 支架 (RB9.01.060.080)
- 1x 相机垫块 (RB9.01.060.090)

---

<a id="step-2-gather-components-1-2-days-shipping"></a>
## 步骤2: 集合组件 (1-2运输日)

订购零件 [材料文件](bom.md). 再利用手臂控制器和电源;这些都不符合抓住器成本:

| 组件 | 排量 | 东部. 费用 |
|-----------|:---:|-----------|
| Feetech STS3215 服务器 | 1 | ~$29 |
| MF106ZZ 轴承 (10x6x3mm) | 2 | ~$2 |
| ⁇ /碳管 D6x1x125mm | 2 | ~$4 |
| 3D打印 PLA| 8个部分 | ~$12 |
| 紧固件 (M2/M4螺丝/坚果) | 各种 | ~$3 |

**总估计成本: ~$50**

---

<a id="step-3-assembly-30-45-minutes"></a>
## 步骤3:会议 (30-45 分钟)

按照详细的说明 [会议指南](assembly-guide.md):


1. 插入伺服电缆
2. 使用 Feetech 软件将伺服器移到最小位置 (在软件中的滑动器移向左)
3. 将齿条固定到夹爪上
4. 将导杆插入两个夹爪
5. 将轴承装入主框架并用螺钉固定
6. 将导杆卡入框架
7. 将两个夹爪分别移至最左端和最右端
8. 插入伺服器并用螺丝固定它
9. 连接摄像头间隔器和UVC摄像头,用4x螺丝和M2坚果固定 (可选)
10. ⁇ 到机器人手臂 (可选)

---

<a id="step-4-software-setup-10-minutes"></a>
## 第4步:安装软件 (10 分)

1. **安装 STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cd STServo_SDK_Python
   cp -r STservo_sdk /path/to/your/project/
   ```

2. **安装 Python 依赖性**
   ```bash
   pip install pyserial
   ```

3. **配置连接**
   ```python
   DEVICENAME = 'COM7'  # Windows
   # DEVICENAME = '/dev/ttyUSB0'  # Linux
   STS_ID = 1  # Servo ID (use 6 if connected as gripper on SO-ARM101)
   ```

---

<a id="step-5-first-test-5-minutes"></a>
## 步骤5:第一次测试 (5时间:

1. **连接硬件**
   - 抓住器服务器 →服务器 No5 SO-ARM101 服务车
   - 现有的手臂控制器 →计算机 (USB)
   - 使用为安装的伺服器配置的手臂电源
   - 设置抓住器的伺服ID相匹配 `STS_ID` 在公交车上保持独特的
   - 在打开序列端口之前关闭其他机器人控制应用程序

2. **执行基本测试**
   ```bash
   cd software/python
   python gripper_control.py
   ```

3. **尝试基本命令**
   - 输入 `45` 打开夹爪
   - 输入 `-45` 闭合夹爪
   - 输入 `0` 到中心
   - 按输入以退出

---

<a id="troubleshooting"></a>
## 解决问题

<a id="connection-issues"></a>
### 联系问题
- ✅在设备管理器 (Windows) 或 `ls /dev/ttyUSB*` (Linux)
- ✅ 检查伺服电源LED开放
- ✅尝试不同的波特速率 (默认:1000000)
- ✅检查电缆连接

<a id="movement-issues"></a>
### 运动问题
- ✅验证设备与架子的接触
- ✅检查是否有机结合
- ✅确保轴承在棒上自由移动
- ✅监测伺服温度 (最高60°C)

<a id="software-issues"></a>
### 软件问题
- ✅ 安装 STServo SDK 正确
- ✅检查 Python 版本 (3.6+)
- ✅验证序列端口权限: `sudo chmod 666 /dev/ttyUSB0` (Linux)

---

<a id="next-steps"></a>
## 下一步

🎉 **恭喜你!** 你的抓住器正在工作!

现在你可以:
- 在山上 SO-ARM100/101 机器人手臂
- 与控制软件集成
- 添加相机到相机持有器
- 创建定制应用程序

<a id="need-help"></a>
## 你需要帮助吗?

- ⁇ 阅读 [规格](specifications.md)
- ⁇ 检查 [会议指南](assembly-guide.md)
- 📄 [同步抓住器产品规格 (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf)
- 📄 [SO-ARM101 产品规格 (PDF)](../../../SO-ARM101%20by%20Robo9.pdf)
- ⁇  在 GitHub 上报告问题

---

**欢迎来到平行抓住器社区!** 🤖
<!-- /translated-content -->
