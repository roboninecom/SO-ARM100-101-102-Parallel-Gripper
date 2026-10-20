<!-- translation-navigation -->
[English](../../../../en/simulation/so_arm_101_description/meshes/LICENSE.md) · [Русский](../../../../ru/simulation/so_arm_101_description/meshes/LICENSE.md) · [Español](../../../../es/simulation/so_arm_101_description/meshes/LICENSE.md) · [Français](../../../../fr/simulation/so_arm_101_description/meshes/LICENSE.md) · [Deutsch](../../../../de/simulation/so_arm_101_description/meshes/LICENSE.md) · [Português (Brasil)](../../../../pt-BR/simulation/so_arm_101_description/meshes/LICENSE.md) · [简体中文](../../../../zh-CN/simulation/so_arm_101_description/meshes/LICENSE.md) · [日本語](../../../../ja/simulation/so_arm_101_description/meshes/LICENSE.md) · [हिन्दी](../../../../hi/simulation/so_arm_101_description/meshes/LICENSE.md) · [العربية](LICENSE.md)

[الأصل الإنجليزي](../../../../../../simulation/so_arm_101_description/meshes/LICENSE.md)

[العربية](../../../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-the-meshes-in-this-directory"></a>
# ترخيص الشبكات في هذا الإرشاد

**هذا الإداري مختلط** ليس كل شبكة هنا مملوكة Robonine، لذلك
يتم تعيين الترخيص لكل ملف وليس كل دليل.

`collision/` يحتوي على هيكل مغمور تم إنتاجه من `visual/` بواسطة
`../scripts/generate_collision_meshes.py`. كل هيكل يحمل نفس رخصة
الشبكة البصرية التي تم إنشاؤها منها.

| الملف (في كلا `visual/` و `collision/`) | الترخيص | حقوق الطبع والنشر |
|---|---|---|
| `clamp_1.stl`, `clamp_2.stl` | CERN-OHL-P-2.0 | Robonine |
| `base_link.stl` | Apache-2.0 | TheRobotStudio |
| `link1_1.stl`, `link2_1.stl`, `link3_1.stl`, `link4_1.stl` | Apache-2.0 | TheRobotStudio |
| `link5_1.stl` | Apache-2.0 | مختلطة  ⁇  انظر أدناه |

<a id="upstream-geometry"></a>
## الهندسة فوق النهر

`base_link.stl` و `link1_1.stl` … `link4_1.stl` هل هي SO-ARM101 **الذراع**,
المستمدة من التيار الصاعد [SO-ARM100/101 المشروع
TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) وإعادة توزيعها
تحت Apache-2.0. هذا المشروع لم يصمم هذه الهندسة انظر مخزن
`NOTICE`.

<a id="link5_1stl--fused-mesh"></a>
## `link5_1.stl` ⁇  الشبكة المدمجة

`link5_1.stl` هو شبكة واحدة التي تجمع في النهر الصاعد SO-ARM101 معصم مع
Robonine's `RB9.01.062.010 Main frame`. يتم توزيع الملف بأكمله تحت
**Apache-2.0**: Robonine لا يمكن منحها CERN-OHL-P-2.0 على الهندسة لا
و هو حر في ترخيص حصته الخاصة تحت Apache-2.0.

إعادة تصدير هذا كشبيتين منفصلين سيسمح لكل جزء تحمل
رخصة. حتى ذلك الحين، تعامل الملف ك Apache-2.0 في الكامل

<a id="robonine-geometry"></a>
## Robonine الهندسة

`clamp_1.stl` و `clamp_2.stl` هي Robonineتصميمه الخاص
`RB9.01.062.021 Clamp` تم دمجها مع `RB9.01.062.031 Gear rack`. إنها مفتوحة
الأجهزة تحت CERN-OHL-P-2.0:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

انظروا `LICENSING.md` في جذور مخزن للحصول على خريطة الترخيص الكاملة
<!-- /translated-content -->
