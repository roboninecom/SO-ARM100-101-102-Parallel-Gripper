<!-- translation-navigation -->
[English](../../../../en/community/histology-slide-gripper/mujoco/README.md) · [Русский](../../../../ru/community/histology-slide-gripper/mujoco/README.md) · [Español](../../../../es/community/histology-slide-gripper/mujoco/README.md) · [Français](../../../../fr/community/histology-slide-gripper/mujoco/README.md) · [Deutsch](../../../../de/community/histology-slide-gripper/mujoco/README.md) · [Português (Brasil)](../../../../pt-BR/community/histology-slide-gripper/mujoco/README.md) · [简体中文](README.md) · [日本語](../../../../ja/community/histology-slide-gripper/mujoco/README.md) · [हिन्दी](../../../../hi/community/histology-slide-gripper/mujoco/README.md) · [العربية](../../../../ar/community/histology-slide-gripper/mujoco/README.md)

[英文原文](../../../../../../community/histology-slide-gripper/mujoco/README.md)

[简体中文](../../../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="microscope-slide-gripper-in-mujoco"></a>
# 显微镜幻灯片抓住器 MuJoCo

其他 SO-ARM101 配有 ⁇ 滑梯平行抓住器,出口于Fusion并安装在现货Robo9紧 ⁇ 的位置.

经过测试 `mujoco` 3.4.0 在 `lerobot` 建筑环境. 没有. ROS 2 或需要Docker.

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py                      # full arm + slide gripper
python view.py scene_gripper.xml    # gripper alone on a testbench
python test_grasp.py                # headless grasp-and-lift check -> grasp_check.png
```

<a id="mujoco-simulation-preview"></a>
## MuJoCo 模拟预览

![SO-ARM101 动脉状的滑梯抓住器 MuJoCo](../../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

这个场景显示 SO-ARM101 配备在 ⁇ 上安装的螺旋式滑梯平行抓住器
用相同的手腕 MuJoCo 由:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python view.py
```

<a id="what-is-modelled"></a>
## 什么是模型

| 链接 | 来源 | 大众 |
|---|---|---|
| `slide_gripper_base` | 主框架, STS3215,指导棒,轴承,摄像头持有器,Arducam OV9281 | 0.20公斤 |
| `sg_jaw_right` / `sg_jaw_left` | RB9.01.062.020 紧 ⁇ + RB9.01.062.030 货架 (m0.8) | 0.035每 kg |
| `sg_pinion` | RB9.01.062.040 无 ⁇ 轮,18T,0.8模块 | 0.008公斤 |

在Fusion组件中从当前构成的关节中取出的动态
(`Slide_Jaw_Right`, `Slide_Jaw_Left`, `Drive_Pinion`),它们具有一致性:
18 T / 0.8 模块螺旋 ⁇ 具有7.2 mm的射线,7.2 mm x 4.9306 rad =
**35.5毫米** 按CAD中的滑动器限制.

<a id="control"></a>
## 控制

一个执行器, `sg_grip`据报道 **⁇ 部流程的米**:

| `ctrl` | ⁇ 部旅行 | 刀片面之间的开口 |
|---|---|---|
| `0.0` | 0mm | **84毫米** (完全开放) |
| `0.0295` | 29.5毫米 | 25mm (一个显微镜幻灯片) |
| `0.0355` | 35.5毫米 | **13毫米** (完全关闭) |

两只 ⁇ 子都从单个 ⁇ 子中驱动,所以 `sg_jaw_left_joint` 和
`sg_pinion_joint` 是被奴役的 `sg_jaw_right_joint` 通过 `<equality>` 限制
仪器可见地与 ⁇ 部旋转. 司令部 *过去* 要挤压的对象:
接近25mm对象 `ctrl=0.0355` 在 ⁇ 子上,给出约4.7N.

五个手臂关节保持了 URDF名称 (`base_link_to_link1` ... `link4_to_link5`).

<a id="collision-geometry"></a>
## 碰撞几何

网格地质是 **仅可视** (`contype=0`),因为 MuJoCo ⁇ 形 ⁇ 子网和
一个L形 ⁇ 的骨架填满了你试图抓住的空隙. 联系是
在每只 ⁇ 部的两面上,被盒子携带 (组3),隐藏在
转载:

- `sg_pad_*` ⁇ 30毫米滑板刀,CAD x 42 ⁇ 50,z 26 ⁇ 31
- `sg_mid_*` ⁇ 宽的中部,CAD x 42 ⁇ 58,z 18.5 ⁇ 38.5

TCP 网站 `sg_tcp` 坐在刀片之间; `sg_camera` 是Arducam光学框架.

<a id="files"></a>
## 文件

- `so101_slide_gripper.xml` ⁇ 全机器人 (由 `build_full.py`)
- `scene_gripper.xml` ⁇ 单独的抓住器,用于测试的电梯轴
- `gripper_assets.xml` / `gripper_body.xml` / `gripper_actuation.xml` ⁇ 抓住器,
  含有可用于度和雷达单位模型
- `meshes/{base,jaw_right,jaw_left,pinion}.stl` ⁇ 从Fusion出口 **组装
  坐标**每个部分都在正确的位置 (没有每个部分的起源可以追踪)
- `meshes/arm/` ⁇ 来自Robo9的手臂网格
- `build_arm.py` ⁇ 从Xacro带 `so_101.urdf.xacro`,将股票紧 ⁇ 放下,向MJCF编译
- `build_full.py` ⁇ 将抓住器移植到 `link5`; **编辑 `MOUNT_POS`/`MOUNT_QUAT` 在这里**

<a id="how-the-gripper-was-located-on-the-wrist"></a>
## 如何在手腕上设置抓住器

`link5_1.stl` 在Robo9中,不仅仅是手腕.
抓住器 (框架,指导棒,摄像头). 所以它是幻灯片抓住器设计所取代的部分,
`build_full.py` 删除其网格并将其质量从0.556kg降至0.08 kg.

没有猜到,山面的姿势得到了解决. `base.stl` 装在
`link5_1.stl` 通过搜索所有
24个轴对齐的旋转,并得分近邻距离. 最好的适应是
**+90度左右 X** (CAD + Y -> link5 + Z,CAD + Z -> link5 - Y) 具有2.0 mm的中位数
剩余的 ⁇ 滑板紧 ⁇ 垂直挂在Robo9的尖 ⁇ 紧 ⁇ ,相匹配
聚合组件.

<a id="stability"></a>
## 稳定

模型设定为 `max|qvel| = 0` 他就在那儿. 如果你看到它震动,
首先要检查的是失踪的联系人 (`ncon` 在观众的信息面板中应该是0
随着手臂的休息. 需要三个东西:

1. **`<exclude body1="world" body2="link1_1"/>`** - - 真正的解决方案. URDF进口商
   合并 `base_link` 在 `worldbody`并且 MuJoCo 跳过父母/儿童碰撞
   *除了* 当父母是世界身体时. 所以基础网和链接1网
   在肩膀上穿透,产生永久接触,使 ⁇ 子粘着
   在其+-1.5N.m的极限下执行器. 只有这个问题才得到解决. `|qvel|` 从4.78到0.
2. `sg_pinion_joint` 钢材1e-6 -> **1e-4**. 一个被严格的平等奴役的联合
   几乎没有惯性 ⁇ 声 (它达到12rad/s的峰值).
3. 平等 `solref` 0.002 -> **0.01**. 限制时间常量等于时间步骤
   这也使得 ⁇ 杆的气温达到 -282.5°C.
   而不是-280现在,我们要去做什么?

<a id="caveats"></a>
## 洞穴

- **质量是假设的,而不是测量的.** ⁇ 合报告每一个身体都是钢 (口腔)
  每个值为 221 g;以上的值是PLA和硬件估计. 如果你
  在Fusion中分配真实材料,更新 `mass=` 在 `gripper_body.xml`.
- 动力是由 MuJoCo 而不是Fusion的 ⁇ 子.
- 双臂的关节限制, ⁇ 缩和摩擦是继承于 repo URDF 和
  没有重新调整.
- **⁇ 臂的环质量也是钢密度**, 与抓住器相同的缺陷:
  欧元基金回报总额 **2.81公斤** 对于真正的SO-101而言,大约是1kg; `link2_to_link3`
  需要1.91N.m,以抵制1.5N.m的动力极限,所以它下降了. 这确实是
  它不会引起震动 (参见以上),但会让手臂表现得更重.
  机器. 测量每一个手臂链的质量, `diaginertia` 通过 ~ 0.36 将总数达到
  1.19⁇ 度清除; STS3215 也靠近2.9N.m
  URDF的保守率为1.5.
- 2mm对齐残余是真实的:"主 frame_125 追随器"不相同
  ⁇ 成的框架 `link5_1.stl`.
- `sg_pinion_joint` 是化 ⁇ 品 - 它没有载荷,因为两个架子是连接的
  直接交往彼此. 它存在于屏幕上.

<a id="driving-it-in-the-mujoco-viewer"></a>
## 驾驶它在 MuJoCo 观众

使用 **`sg_grip` 在控制面板中的滑动器**. 滑鼠在 *关联* 面板
写作 `qpos` 直接绕过平等的限制,因此拖累那些 (特别是
在停下来时) 将 ⁇ 部与 ⁇ 部脱节. 按"运行"重新调整.

<a id="re-exporting-after-a-cad-change"></a>
## 经过CAD变更后重新出口

通过Fusion MCP连接进行出口:
在四个刚性链中,写出二进制STL在组合坐标中
(毫米) 重新出口,Fusion设计开放以刷新网格
除非你移动一个关节外, 没有什么需要改变.
<!-- /translated-content -->
