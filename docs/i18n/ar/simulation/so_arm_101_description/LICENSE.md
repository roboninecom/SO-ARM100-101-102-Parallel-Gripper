<!-- translation-navigation -->
[English](../../../en/simulation/so_arm_101_description/LICENSE.md) · [Русский](../../../ru/simulation/so_arm_101_description/LICENSE.md) · [Español](../../../es/simulation/so_arm_101_description/LICENSE.md) · [Français](../../../fr/simulation/so_arm_101_description/LICENSE.md) · [Deutsch](../../../de/simulation/so_arm_101_description/LICENSE.md) · [Português (Brasil)](../../../pt-BR/simulation/so_arm_101_description/LICENSE.md) · [简体中文](../../../zh-CN/simulation/so_arm_101_description/LICENSE.md) · [日本語](../../../ja/simulation/so_arm_101_description/LICENSE.md) · [हिन्दी](../../../hi/simulation/so_arm_101_description/LICENSE.md) · [العربية](LICENSE.md)

[الأصل الإنجليزي](../../../../../simulation/so_arm_101_description/LICENSE.md)

[العربية](../../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-this-package"></a>
# ترخيص هذه الحزمة

`so_arm_101_description` يتم توزيعها كجزء من
[SO-ARM100/101 قابض متوازٍ](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)
المشروع، الذي يمتلك مرخصات متعددة هذا الملف يصف الحزمة لذلك هو
التفسير الذاتي عند تثبيتها أو إعادة توزيعها بمفردها.

| المحتوى | الترخيص | حقوق الطبع والنشر |
|---|---|---|
| `urdf/`, `config/`, `launch/`, `scripts/`, `test/`, `worlds/`, `docker/`, `so_arm_101_description/`, `setup.py`, `package.xml` | Apache-2.0 | Robonine |
| `meshes/` | **مختلطة** ⁇  انظر [`meshes/LICENSE.md`](meshes/LICENSE.md) | مختلطة |

<a id="meshes--read-before-reusing"></a>
## الشباك  ⁇  قراءة قبل إعادة استخدامها

`meshes/` ليس لديه ترخيص موحد:

- `clamp_1.stl`, `clamp_2.stl` هي Robonineهندسة المقبضات **CERN-OHL-P-2.0**.
- `base_link.stl`, `link1_1.stl` … `link4_1.stl` هل هي SO-ARM101 **الذراع**, مشتق
  من التيار الصاعد [SO-ARM100/101 المشروع
  TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) ومرخصة
  **Apache-2.0**. إنهم ليسوا كذلك Robonineالعمل.
- `link5_1.stl` الاندماج على مسافة المعصم Robonineالإطار الرئيسي في
  جسم واحد و هو **Apache-2.0** في الكامل

وصف الروبوت أدناه `urdf/` تم ترخيصها كبرمجيات بدلاً من
الأجهزة: هو يرمز السيناميات والمعايير الهبطية للذراع بأكملها، الكثير
من بينها تصف الهندسة فوق النهر التي Robonine لا يملك

النصوص الكاملة للترخيص موجودة في جذور المخزن `HARDWARE-LICENSE.txt`,
`SOFTWARE-LICENSE.txt` و `DOCS-LICENSE.txt` (ومرة أخرى تحت أسمائهم
في `LICENSES/`، كما يتطلب تصنيف REUSE). انظر أيضاً `LICENSING.md`
للخريطة الكاملة، `NOTICE` للتخصيص من طرف ثالث، و `REUSE.toml` لـ
نسخة قابلة للقراءة الآلية.
<!-- /translated-content -->
