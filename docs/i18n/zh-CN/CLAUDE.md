<!-- translation-navigation -->
[English](../en/CLAUDE.md) · [Русский](../ru/CLAUDE.md) · [Español](../es/CLAUDE.md) · [Français](../fr/CLAUDE.md) · [Deutsch](../de/CLAUDE.md) · [Português (Brasil)](../pt-BR/CLAUDE.md) · [简体中文](CLAUDE.md) · [日本語](../ja/CLAUDE.md) · [हिन्दी](../hi/CLAUDE.md) · [العربية](../ar/CLAUDE.md)

[英文原文](../../../CLAUDE.md)

[简体中文](README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="claudemd"></a>
# CLAUDE.md

本文件提供了对此库中的代码工作的指导.

<a id="what-this-repository-is"></a>
## 这个库是什么?

一个开源硬件项目:为3D打印的平行抓头 SO-ARM100/101 机器人手臂 (由 Robonine). 多种许可证: CERN-OHL-P-2.0 对于硬件/CAD, Apache-2.0 对于软件, CC BY 4.0 对于 doc  ⁇  地图是 `LICENSING.md`机器可读的版本 `REUSE.toml`,第三方属性 `NOTICE`. 新文件必须由: `REUSE.toml`; `reuse lint` 在预订之前. 大多数回复是CAD模型 (`models/`),文件 (`docs/`),以及图像 (`assets/`). 代码生活在两个地方:

- `software/python/gripper_control.py` ⁇ 独立的伺服控制脚本 Feetech STS3215 (取决于 STServo SDK,是手动克隆的 `software/python/requirements.txt`没有在PyPI上). `examples/basic_usage.py` 通过 `sys.path` 打破了.
- `simulation/so_arm_101_description/` — a ROS2 在5个物理发动机中模拟了手臂+抓住器的描述包. 这里是所有测试和大多数CI居住的地方.

<a id="commands"></a>
## 命令

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

产品 (`.github/workflows/ci.yaml`) 运行:预约,XML/YAML验证, `xacro ... sim_backend:=<backend> | check_urdf` 对于所有5个后端 `ros:humble` 容器和最 ⁇ 的套房. 一个 URDF 变更必须保持有效性 **所有的** 不仅仅是你 ⁇ 准的那个.

<a id="simulation-architecture"></a>
## 模拟架构

一个参数化的机器人描述驱动每个模拟器:

- `urdf/so_101.urdf.xacro` 这是真理的唯一来源. 亚克罗阿格 `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` 选择了 `ros2_control` 通过插件 `urdf/so_101.ros2_control.xacro`) 在扩张时.
- `config/controllers.yaml` 为所有后端定义相同的关节/控制器; `launch/sim.launch.py` 在 `sim:=<backend>` 是唯一的入口点.
- 机器人:5DOF臂+ ⁇ ,有2个 ⁇ 门关节,左 ⁇ 门通过右镜反射 `<mimic>`.
- ⁇ 子分开: `meshes/visual/` (高波利) vs `meshes/collision/` ( ⁇ 形的船体, `scripts/generate_collision_meshes.py`).

关节,链接或控制器名称的更改通常需要对xacro文件进行协调编辑. `controllers.yaml`并且在 `test/`.

<a id="cad-models-and-part-numbering"></a>
## CAD模型和零部件编号

零部件 `models/parts/` 使用 Robonine 部分号码 (例如: `RB9.01.062.010 Main frame.STL`). 这些数字在整个 `README.md` (打印表), `docs/bom.md`并且 `docs/assembly-guide.md` ⁇ 添加或更名部分也意味着更新这些文件. STL是二进制的;变体在文件名中编码适应宽容 (例如: `RB9.01.062.021 (D6.1) Clamp.STL` 对于不同棒直径). 预约 ⁇ 子 (白色空间,EOF,线结) 故意排除 `.stl/.STL/.STEP` 文件和超过1MB的文件被拒绝 `check-added-large-files`.

<a id="conventions"></a>
## 大会

- Python⁇ 子8在 `--max-line-length=100`,以黑色形状进行分类 (由预约执行; `software/` 和 `examples/` 已被排除在 ⁇ 子中8.
- 文件的设计是复制性的 (README总结 bom.md, specifications.md, assembly-guide.md)  ⁇ 在变化规格,零件或价格时保持一致性.
- 不要添加一个 `Co-Authored-By: Claude` 交付的行程.
<!-- /translated-content -->
