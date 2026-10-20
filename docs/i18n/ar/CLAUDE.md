<!-- translation-navigation -->
[English](../en/CLAUDE.md) · [Русский](../ru/CLAUDE.md) · [Español](../es/CLAUDE.md) · [Français](../fr/CLAUDE.md) · [Deutsch](../de/CLAUDE.md) · [Português (Brasil)](../pt-BR/CLAUDE.md) · [简体中文](../zh-CN/CLAUDE.md) · [日本語](../ja/CLAUDE.md) · [हिन्दी](../hi/CLAUDE.md) · [العربية](CLAUDE.md)

[الأصل الإنجليزي](../../../CLAUDE.md)

[العربية](README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="claudemd"></a>
# CLAUDE.md

يقدم هذا الملف توجيهات لـ (Claude.ai/code) عند العمل مع الشفرة في هذا المستودع.

<a id="what-this-repository-is"></a>
## ما هو هذا المستودع

مشروع أجهزة مفتوحة المصدر: مقبض متوازي مطبوع 3D لل SO-ARM100/101 الذراع الروبوتية Robonine). مرخصات متعددة: CERN-OHL-P-2.0 للجهاز / CAD ، Apache-2.0 للبرمجيات، CC BY 4.0 للدقائق  ⁇  الخريطة موجودة في `LICENSING.md`، النسخة القراءة الآلية في `REUSE.toml`، إصدار طرف ثالث في `NOTICE`. يجب تغطية الملفات الجديدة `REUSE.toml`; `reuse lint` يُجري في مرحلة ما قبل الالتزام. معظم النماذج الاحتياطية هي نماذج CAD (`models/`(), الوثائق (`docs/`) و الصور (`assets/`). الكود يعيش في مكانين:

- `software/python/gripper_control.py` ⁇  النص الخادم التحكم المستقل لل Feetech STS3215 (يعتمد على STServo SDK، الذي يتم استنساخه يدويا  ⁇  انظر `software/python/requirements.txt`؛ لا يوجد في PyPI). `examples/basic_usage.py` الواردات من هناك عن طريق `sys.path` هالك.
- `simulation/so_arm_101_description/` — a ROS2 حزمة تصفية (تواضع) التي تمثيل الذراع + المقبض في 5 محركات الفيزياء. هذا هو المكان الذي يعيش فيه جميع الاختبارات ومعظم المعلومات.

<a id="commands"></a>
## الأوامر

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

المعلوماتية (`.github/workflows/ci.yaml`) التشغيل: التزاماً مسبقاً، تصحيح XML/YAML `xacro ... sim_backend:=<backend> | check_urdf` للجميع5الخلفيات داخل `ros:humble` الحاوية، والفندق يجب أن يظل تغيير URDF صالحاً **جميعها** الخلفيات، ليس فقط تلك التي تستهدفها.

<a id="simulation-architecture"></a>
## معمارة المحاكاة

وصف روبوت معدل واحد يقود كل محاكاة:

- `urdf/so_101.urdf.xacro` هو المصدر الوحيد للحقيقة الـ " أكرو ارغ " `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` يختار `ros2_control` إضافة (via `urdf/so_101.ros2_control.xacro`) في وقت التوسع.
- `config/controllers.yaml` يحدد المفاصل/المراقبين المتطابقين لجميع الخلفيات؛ `launch/sim.launch.py` مع `sim:=<backend>` هي نقطة دخول واحدة.
- الروبوت: ذراع 5-DOF + مقبض مع 2 مفصلات ضغط بريزمية، حيث تعكس الضغط اليسرى على اليمين عبر `<mimic>`.
- يتم تقسيم الشباك: `meshes/visual/` (مرتفعة) بمقابل `meshes/collision/` (الهياكل الملتوية، تم تجديدها مع `scripts/generate_collision_meshes.py`).

تغيير المفاصل أو الروابط أو أسماء المحكمات عادة ما يحتاج إلى تعديلات منسقة عبر ملفات xacro، `controllers.yaml`، والاختبارات في `test/`.

<a id="cad-models-and-part-numbering"></a>
## نماذج CAD ورقم الأجزاء

أجزاء في `models/parts/` استخدام Robonine أرقام الأجزاء (مثل: `RB9.01.062.010 Main frame.STL`). هذه الأرقام مرجعية في جميع `README.md` (جداول طباعة) `docs/bom.md`و `docs/assembly-guide.md` ⁇  إضافة أو تغيير اسم جزء يعني تحديث هذه الوثائق أيضا. الـ STLات ثنائية، وتقوم المتغيرات بتشفير معاناة التكيف في اسم الملف (مثل `RB9.01.062.021 (D6.1) Clamp.STL` لقطرات مختلفة). المكعبات السابقة للالتزام (المساحة البيضاء، EOF، نهاية الخط) تستبعد عمدا `.stl/.STL/.STEP` الملفات، والملفات التي تزيد عن 1 MB يتم رفضها من قبل `check-added-large-files`.

<a id="conventions"></a>
## الحفلات

- Python: flake8 مع `--max-line-length=100`، يتم ترتيبها مع ملف أسود (يتم تطبيقه بواسطة التزاماً مسبقاً) `software/` و `examples/` يتم استبعادها من الفاكهة8).
- يتم نسخ الوثائق حسب التصميم (مختصرات README) bom.md, specifications.md, assembly-guide.md)  ⁇  الحفاظ على استمرارها عند تغيير المواصفات أو الأجزاء أو الأسعار.
- لا تضيف `Co-Authored-By: Claude` خط لالتزامات
<!-- /translated-content -->
