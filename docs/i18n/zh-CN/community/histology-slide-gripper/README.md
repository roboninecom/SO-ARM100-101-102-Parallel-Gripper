<!-- translation-navigation -->
[English](../../../en/community/histology-slide-gripper/README.md) · [Русский](../../../ru/community/histology-slide-gripper/README.md) · [Español](../../../es/community/histology-slide-gripper/README.md) · [Français](../../../fr/community/histology-slide-gripper/README.md) · [Deutsch](../../../de/community/histology-slide-gripper/README.md) · [Português (Brasil)](../../../pt-BR/community/histology-slide-gripper/README.md) · [简体中文](README.md) · [日本語](../../../ja/community/histology-slide-gripper/README.md) · [हिन्दी](../../../hi/community/histology-slide-gripper/README.md) · [العربية](../../../ar/community/histology-slide-gripper/README.md)

[英文原文](../../../../../community/histology-slide-gripper/README.md)

[简体中文](../../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="histology-slide-gripper-community-mod"></a>
# 历史学幻灯片抓住器 (社区模特)

一种社区的变体 SO-ARM100/101 通过平行抓住器 [迈克尔·维亚切斯拉夫](https://github.com/histochemichael)适用于历史学和史托技术自动化:轻松采集标准75 x 25mm显微镜幻灯片,幻灯片染色 ⁇ /架子以及近距离的摄像头视图.

<div align="center">

![历史学幻灯片抓住器演示](../../../../../community/histology-slide-gripper/assets/histology-slide-gripper-demo.gif)

*SO-ARM100/101 使用定制的紧 ⁇ 来处理显微镜滑梯和涂料 ⁇ /架.*

</div>

<a id="what-changed-vs-the-base-gripper"></a>
## 什么变化与基层抓住器

| 补充 | 描述 |
|----------|-------------|
| 显微镜滑梯 ⁇ | 长,平坦的 ⁇ 门几何可直接接收标准75 x 25mm显微镜幻灯片. |
| 滑板架/ ⁇ 水处理 | 紧 ⁇ 间隔和尖端将如下链接的Medicus Health滑梯染色 ⁇ 布/架子进行调动. |
| ⁇ 角的Arducam持有器 | 一个可打印的持有器将Arducam全球关闭USB相机定向于抓住器口腔,以便近距离监控滑梯和架子接收. |
| 完整组装CAD | 一个完全可打印的STL和可编辑的 STEP集装在 [`cad/`](../../../../../community/histology-slide-gripper/cad). |

<a id="gallery"></a>
## 画廊

<div align="center">

| 单个幻灯片接收器 | 涂料 ⁇ /货架接车 | 视频: |
|:-:|:-:|:-:|
| ![持有显微镜幻灯片的 ⁇](../../../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg) | ![与滑梯染色 ⁇ 布相对齐的紧 ⁇](../../../../../community/histology-slide-gripper/assets/slide-gripper-staining-dipper.jpg) | ![在抓住器的 ⁇ 上,](../../../../../community/histology-slide-gripper/assets/arducam-holder-front.jpg) |

| 前面视图 | ⁇ 子几何 | 离子体组件 |
|:-:|:-:|:-:|
| <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-front.png" alt="Front CAD view of the microscope slide gripper mod" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-side.png" alt="Angled CAD view showing the microscope slide jaw geometry" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-isometric.png" alt="Isometric CAD view of the full microscope slide gripper assembly" width="250"> |

</div>

<a id="cad-files"></a>
## CAD 文件

| 文件 | 格式 | 使用 |
|------|--------|-----|
| [`cad/the-parallel-microscope-slide-gripper.stl`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.stl) | 其他技术 | 显微镜滑梯抓住器模块的可打印全组件. |
| [`cad/the-parallel-microscope-slide-gripper.step`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.step) | 步骤 | 可编辑的CAD源,用于完整的组装. |

<a id="add-on-bill-of-materials"></a>
## 附加材料文件

这些物件是滑梯/货架工作流程的特点,不属于底部抓紧器的一部分 [爆炸事件](../../docs/bom.md).

| 组件 | 排量 | 备忘录 | 链接 |
|-----------|:---:|-------|------|
| ⁇ 片 100fps 单光全球遮蔽USB相机,OV9281 | 1 | 摄像头用角式持有器观看滑梯和货架在 ⁇ 口附近的接收. | [亚马逊英国](https://www.amazon.co.uk/Arducam-Shutter-Distortion-Computer-Raspberry/dp/B0FXWWF55X) |
| 带手柄的滑动涂料塑料 ⁇ | 1+ | 参考染色 ⁇ /架目标;为标准75 x 25mm的幻灯片设计. | [医生健康](https://www.medicus-health.com/slide-staining-dipper.html) |
| 平行显微镜滑梯抓住器组件 | 1 | 打印 `the-parallel-microscope-slide-gripper.stl`; STEP文件包含编辑. | [`cad/`](../../../../../community/histology-slide-gripper/cad) |

<a id="mujoco-simulation"></a>
## MuJoCo 模拟

<div align="center">

![SO-ARM101 动脉状的滑梯抓住器 MuJoCo](../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

*SO-ARM101 配有 ⁇ 滑板紧持器,并运行在 MuJoCo.*

</div>

一个自主的人 MuJoCo 3.4.0模型可在 [`mujoco/`](mujoco/README.md). 包括全部 SO-ARM101 模型,抓住器网格,一个独立的抓住器试验台,构建脚本和无头式抓起检查.

从存储库的根:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py
```

使用 `sg_grip` 控制 MuJoCo 观众可以打开和关闭口腔. 看看 [模拟 README](mujoco/README.md) 模型细节,控制,验证和重建指令.

<a id="notes"></a>
## 备忘录

- 抓住手指是用于标准75 x 25mm显微镜滑梯和滑梯染色 ⁇ /货架.
- 装置将摄像头视图转向抓住器 ⁇ 部,以便摄像机可以观察滑梯和架子接收.
- 首先使用非关键幻灯片进行测试,并调整打印材料,填料和抓紧力来适应工作流程.

<a id="links"></a>
## 链接

- 🎥 [演示:滑梯和涂料架 (LinkedIn)](https://www.linkedin.com/posts/michael-viacheslavov_histology-histotechnology-robotics-ugcPost-7482570199859240960-Gqpw/)
<!-- /translated-content -->
