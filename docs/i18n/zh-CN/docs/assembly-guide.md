<!-- translation-navigation -->
[English](../../en/docs/assembly-guide.md) · [Русский](../../ru/docs/assembly-guide.md) · [Español](../../es/docs/assembly-guide.md) · [Français](../../fr/docs/assembly-guide.md) · [Deutsch](../../de/docs/assembly-guide.md) · [Português (Brasil)](../../pt-BR/docs/assembly-guide.md) · [简体中文](assembly-guide.md) · [日本語](../../ja/docs/assembly-guide.md) · [हिन्दी](../../hi/docs/assembly-guide.md) · [العربية](../../ar/docs/assembly-guide.md)

[英文原文](../../../assembly-guide.md)

[简体中文](../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="assembly-guide-for-follower-gripper-so-arm101"></a>
# 追随者抓住器的集会指南 SO-ARM101

本指南提供了对平行 ⁇ 接器组装的步骤说明. 仔细遵循这些步骤,以确保正常运行.

<a id="required-tools"></a>
## 需要的工具

- 飞利普斯头螺旋 ⁇  PH1
- 六重键M2 (H1.5) 和M4 (H2.5)

---

<a id="step-1-install-gear-on-servo"></a>
## 步骤1:安装机器在伺服器上

![配备设备的伺服器](../../../../assets/images/assembly/02-servo-with-gear-assembly.png)

**需要的组件:**
- 1x Feetech STS3215 服务器
- 1x 齿轮  (RB9.01.062.040)
- 1x 伺服磁盘 (从伺服器套件中)
- 1x 伺服装安装螺丝M3x6 (来自伺服装组件)
- 4x 设置螺丝 DIN 913 M3x4

**指示:**
1. 放Gripper Gear在Servo盘上,并将4x Set Screw M3x4拉紧从Servo盘到Gear的方向. 当紧 ⁇ 时,确保磁盘和仪器之间没有出现差距.
2. 装配仪器在伺服输出轴上.
3. 用在伺服组装中提供的M3x6螺丝来固定.

---

<a id="step-2-servo-positioning-and-torque-limit"></a>
## 步骤2: 伺服定位和扭矩限制

![伺服定位](../../../../assets/images/assembly/Feetech-Servo-Window.png)

**需要的组件:**
- 现有 SO-ARM100/101 控制器,伺服电缆和手臂电源

**对于Windows用户的说明:**
1. 通过伺服器巴士将伺服器连接到现有的手臂控制器,并通过USB将控制器连接到PC. 用手臂电源. 在将抓住器添加到链上之前,设置独特的伺服ID;在打开COM端口前关闭其他机器人控制应用.
2. 设置服务器 Feetech's **FD** (SCServo 调试工具. 它是封闭源的
   在Windows软件中 Feetech 并且是 **没有** 在本存储库中重新分配:
   - 官方下载: <https://www.feetechrc.com/software.html> ⁇ 寻找FD
     SCServo 调试档案. 一些下载是密码保护的;
     来自 Feetech.
   - 开源跨平台替代方案:
     <https://github.com/Kotakku/FT_SCServo_Debug_Qt>

   下面的步骤描述了FD接口;替代方案揭示了相同的
   具有类似名称的参数.
3. 选择您的COM端口,选择BaudRate 1 000 000,按 ⁇ "开放",然后按 ⁇ "搜索".
4. 在列表下面,选择您的伺服器.
5. 检查该框,以启动伺服器的扭矩.
6. 移动滑鼠到左边.

![最大扭矩限制](../../../../assets/images/assembly/max-torque-window.png)

7. 转换窗口到"编程"选项.
8. 选择参数"最大扭矩限制",设置为500 ans,按"保存".

---

<a id="step-3-clamps"></a>
## 步骤3:紧 ⁇

![夹爪](../../../../assets/images/assembly/clamp+rack+nail.PNG)

**需要的组件:**
- 2x 夹爪 (RB9.01.062.021)
- 2x 齿条 (RB9.01.062.031)
- 2x 钉子 (RB9.01.062.100)

**指示:**
1. 从侧面将齿条插入夹爪。
2. 然后从背面插入钉子。

---

<a id="step-4-rods"></a>
## 步骤4: 棒子

![导杆](../../../../assets/images/assembly/rods+clamps.PNG)

**需要的组件:**
- 2x 棒 D6x125mm

**指示:**
1. 插入两条 ⁇ 子中的杆子. 如果您订购长于125毫米的棒/管,则需要将它们切割到此长度.

---

<a id="step-5-install-bearings-on-main-frame"></a>
## 步骤5:安装轴承在主框架上

![在主 ⁇ 上安装的轴承](../../../../assets/images/assembly/frame+bearings.png)

**需要的组件:**
- 2x MF106ZZ 轴承 (10x6x3mm)
- 2x M4x8 DIN 7991螺丝

**指示:**
1. 插入2x MF106ZZ 轴承在主 ⁇ 上的指定位置. 轴承 ⁇ 应面向上.
2. 用 M4x8 螺钉固定每个轴承。

---

<a id="step-6-connection-of-rods-and-frame"></a>
## 第6步:棒和框架的连接

![棒和主 ⁇ 的连接](../../../../assets/images/assembly/frame-with-clamps.png)

**指示:**
1. 将导杆卡入框架.
2. 将两个夹爪分别移至最左端和最右端.

---

<a id="step-7-mount-servo-on-main-frame"></a>
## 第7步:在主 ⁇ 上的塞尔沃山

![在主 ⁇ 上安装的伺服器](../../../../assets/images/assembly/servo-on-frame.png)

**需要的组件:**
- 3x 自动 ⁇ 螺丝 (来自伺服器套件)

**指示:**
1. 设置伺服器在主 ⁇ 上,并对齐安装孔.
2. 使用伺服套件中的 3x 自攻螺钉固定伺服电机。

---

<a id="step-8-gripper-holder-attachment"></a>
## 第8步:抓住器持有器附带

![抓住器持有器的连接](../../../../assets/images/assembly/09-gripper-holder-attachment.png)

**需要的组件:**
- 1x 相机支架 (RB9.01.060.074) 或持有者 (RB9.01.060.080)
- 1x SO-ARM101
- 4x M3x6螺丝 (来自伺服组件)
- 4x 自动 ⁇ 螺丝 (来自伺服器套件)

**指示:**
1. 如果您计划使用Gripper与相机,请将相机持有器连接起来. SO-ARM101 用4xM3x6螺丝来固定
2. 连接平行抓住器到摄像头持有器或持有器,并用4倍自动 ⁇ 螺丝固定
3. 连接从平行抓住器到服务器No5的电缆 SO-ARM101

---

<a id="step-9-camera-attachment-optional"></a>
## 第9步:摄像头连接 (可选)

![摄像头连接器](../../../../assets/images/assembly/camera-attachment.png)

**需要的组件:**
- 1x UVC 摄像头,装备孔为28x28mm
- 1x 相机垫块 (RB9.01.060.090)
- 4x M2x8螺丝
- 4x M2 坚果

**指示:**
1. 从相机支架背面装入 4x M2 螺母。
2. 从正面安装相机垫块和相机，并用 4x M2x8 螺钉固定。

---
<a id="assembly-complete"></a>
## 大会完成!

![组装 SO-ARM101 与Follower Gripper](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

恭喜你! 你的 SO-ARM101 现在已经组装,准备好使用.

<a id="next-steps"></a>
### 下一步
- 在使用前测试抓住器操作
<!-- /translated-content -->
