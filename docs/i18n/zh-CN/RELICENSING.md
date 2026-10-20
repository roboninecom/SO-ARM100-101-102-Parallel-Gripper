<!-- translation-navigation -->
[English](../en/RELICENSING.md) · [Русский](../ru/RELICENSING.md) · [Español](../es/RELICENSING.md) · [Français](../fr/RELICENSING.md) · [Deutsch](../de/RELICENSING.md) · [Português (Brasil)](../pt-BR/RELICENSING.md) · [简体中文](RELICENSING.md) · [日本語](../ja/RELICENSING.md) · [हिन्दी](../hi/RELICENSING.md) · [العربية](../ar/RELICENSING.md)

[英文原文](../../../RELICENSING.md)

[简体中文](README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="relicensing-record"></a>
# 重新授权记录

这份文件记录了该项目如何和为什么从GPL-3.0移动,
投资者. 它存在,因此许可证历史可以进行审计
我在挖掘.

**状态:正在进行.** 在下面的每一个 ack
已记录.

<a id="what-changed"></a>
## 改变了什么?

| 材料 | 之前 | 之后 |
|---|---|---|
| 硬件/CAD | 仅使用GPL-3.0 | CERN-OHL-P-2.0 |
| 软件 | 仅使用GPL-3.0 | Apache-2.0 |
| 文件和图像 | 仅使用GPL-3.0 | CC BY 4.0 |

版权所有者: **Robonine**. 看看 `LICENSING.md` 对于文件按文件的地图,
`REUSE.toml` 在机器可读的版本中, `NOTICE` 对于第三方
归因.

<a id="why"></a>
## 为什么?

GPL-3.0 专为软件. 它的定义  ⁇ "源代码","对象
⁇ 不清楚地映射到物理对象上,所以
对于CAD部分,从来没有清楚什么是真正引发
许可证的义务. CERN-OHL-P-2.0 写为硬件,并说
产品,所覆盖的来源和可用组件是什么.

允许的选择是故意的. 它将保护与关闭的
接 ⁇ 的叉子,以换取集成器零摩擦;
与上游的兼容性 SO-ARM100/101 项目和更广泛的
LeRobot/ROS生态系统, Apache-2.0 在整个.

<a id="licence-history"></a>
## 许可证历史

| 承诺 | 日期 | 什么? |
|---|---|---|
| `00fae7b` | 2025-06-27 | 建立了一个库. `LICENSE` 是 **麻省理工学院** (第21行) |
| `64d3f01` | 2025-07-01 | `LICENSE` 被GPL-3.0 (674条) 替换成. |
| `d37855a` | 2025-07-06 | `README.md` 在MIT上更新到GPL-3.0. |
| 这种变化 | — | 上述的三方分离. |

`CONTRIBUTING.md` 和 `software/python/gripper_control.py` 是 **永远不会**
在2025年更新,并继续声明MIT. 这是一个错误,不是
双重许可.

后果是重要的:每个外部贡献者加入了 *之后* 在GPL翻转,
在一个存储库中, `CONTRIBUTING.md` 我还是告诉他们 *"通过做出贡献,
同意您的贡献将根据MIT许可证获得许可".* 其他
他们实际上提供的许可证比GPL-3.0更允许. 这种变化
让存储库符合贡献者被告知的内容,而不是反对
没有什么. 我们仍然要求每一个人明确,而不是依靠
这就是.

<a id="contributor-agreement"></a>
## 贡献者协议

| 贡献者 | 承诺 | 范围 | ⁇ 子 |
|---|---|---|---|
| Robonine (Nikita Bragin  ⁇ 也 `brnikita`, `branikita`) | 76 | 拥有者 | n/a |
| 艾伦·沃尔卡霍里克 (Alan Subin) | 44 | `models/`, `models/parts/`, `assets/images/`, `docs/` | 在合同下完成的工作与IP分配到 Robonine作为礼貌的要求 |
| 他 (Michael Viacheslavov) | 他代表上传的3+文件 | `community/histology-slide-gripper/` | 在等待 |
| 弗拉基米尔·奥西波夫 | 1 | `README.md` 关闭链接修复 | 在等待 |
| 萨伊德·阿扎尔·胡塞安四方 | 1 | `software/python/gripper_control.py` | 在等待 |

重新授权问题:

<a id="authorship-notes"></a>
### 作者说明

- 作者: `Codex <codex@openai.com>` 尼基塔·布拉金在
  代表 Robonine. 它们不是第三方的贡献.
- 社区变体的CAD和图像
  (`community/histology-slide-gripper/cad/*`, `assets/*`) 是 **由
  Robonine 代表迈克尔·维亚切斯拉夫** ⁇ 承诺 `537f347` 和 `b4698e7`
  编写为 `Codex`. 这些文件的作者属于迈克尔;
  这就是为什么它被写下来.

<a id="decisions-on-the-record"></a>
## 记录中的决定

**`link5_1.stl` 是一个合并的网格.** 它结合上游 SO-ARM101 手腕
Robonine's `RB9.01.062.010 Main frame` 在一个身体中. 部件不是
在文件中可分开,因此整个文件被分配到 Apache-2.0:
Robonine 无法授予 CERN-OHL-P-2.0 它没有几何,而且是自由的.
授权自己的部分 Apache-2.0. 作为两个网格将重出口
让每个部分都拥有其适当的许可证,

**关于二进制文件的通知.** CERN-OHL-P-2.0 预计许可证的通知
在源头中留下来. 二进制 STL 和 STEP 文件不能携带它们,并且
`.pre-commit-config.yaml` 故意将这些格式排除在文本 ⁇ 中.
`REUSE.toml` 这项项目如何履行这一义务:它分配
每个文件的版权和许可证, `reuse lint` 强制
没有什么被揭露.

只有在这些情况下,目录级公告被故意限制至最低.
根地图没有. 两个幸存下来:
`simulation/so_arm_101_description/meshes/LICENSE.md`因为这个目录
混合物 Robonine 并且有些人需要复制一个网格
这; `simulation/so_arm_101_description/LICENSE.md`因为这个ROS
包装单独分发,必须自定义.

**许可证的文本存在两个地方.** `LICENSES/` 在REUSE的位置
规格要求它们; `HARDWARE-LICENSE.txt`, `SOFTWARE-LICENSE.txt` 和
`DOCS-LICENSE.txt` 根源是GitHub的许可检测所读的,所以
存储库显示了三个许可证,而不是没有.

**`software/FD.exe` 已经被删除了.** 这就是 Feetech专利的FT SCServo 调试"
投资工具 `7783073` 没有授予许可证,并被
项目总体GPL-3.0要求是错误的. `docs/assembly-guide.md`
现在指出 Feetech通过自己的下载和开源替代品.

**基特历史没有被重写.** `FD.exe` 在历史和来源中留下
发行文件的档案 `v0.1.0` 通过 `v0.3.1`. 改写将使所有
从开放的上游拉动请求中引用的SHA,即
对于一个工具来说,这并不值得. Feetech 免费发行.

**`ament_copyright` 被放下了** 在 `package.xml`. 它被宣布,但从来没有
连接或运行. 它检查源文件中的许可证标题,
与本项目的申报许可的方法相冲突 `REUSE.toml` —
由于大多数文件都是二进制的, `reuse lint` 覆盖
不仅仅是几十个文件. Python 在ROS内部的文件
包装.

<a id="releases"></a>
## 释放

这不会以后效果改变发布 `v0.1.0` 通过 `v0.3.1`,其中
仅在GPL-3.0下可使用.

---

由项目维护人员准备. 这是一份关于决定的记录,而不是法律.
建议.
<!-- /translated-content -->
