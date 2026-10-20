<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](LICENSING.md) · [العربية](../ar/LICENSING.md)

[अंग्रेज़ी मूल](../../../LICENSING.md)

[हिन्दी](README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# लाइसेंस

कॉपीराइट (c) 2025 Robonine

इस परियोजना में अलग-अलग लाइसेंस के तहत विभिन्न प्रकार की सामग्री जारी की जाती है।
इस रिपॉजिटरी में प्रत्येक फ़ाइल को उनमें से एक द्वारा कवर किया गया है।

| सामग्री | लाइसेंस | पाठ |
|---|---|---|
| हार्डवेयर डिजाइन (CAD, विनिर्माण योग्य ज्यामिति) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| सॉफ्टवेयर (कोड, कॉन्फ़िगरेशन, आईसी, रोबोट विवरण) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| प्रलेखन, रेंडर और फ़ोटो | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

इस नक्शे के मशीन-पठनीय संस्करण है [`REUSE.toml`](../../../REUSE.toml), जो
प्रत्येक फ़ाइल को पथ द्वारा लाइसेंस सौंपता है और इसे लागू करता है `reuse lint` में
पूर्व प्रतिबद्धता और आईसी। `LICENSES/` अपने SPDX के अंतर्गत एक ही तीन ग्रंथों को रखता है
नाम, जैसा कि REUSE विनिर्देश की आवश्यकता है।

**कुछ सामग्री यहाँ नहीं है Robonine's.** देखिये [`NOTICE`](../../../NOTICE) श्रेय के लिए
और सटीक फ़ाइल सूची के लिए नीचे सेक्शन 4।

---

<a id="1-hardware--cern-ohl-p-20"></a>
## 1. हार्डवेयर CERN-OHL-P-2.0

```
models/                                             *.STEP, *.STL
models/parts/                                       *.STL
community/histology-slide-gripper/cad/              *.step, *.stl
community/histology-slide-gripper/mujoco/meshes/    base.stl, jaw_left.stl,
                                                    jaw_right.stl, pinion.stl
simulation/so_arm_101_description/meshes/visual/    clamp_1.stl, clamp_2.stl
simulation/so_arm_101_description/meshes/collision/ clamp_1.stl, clamp_2.stl
```

`README.md` इन निर्देशिकाओं के भीतर फ़ाइलें प्रलेखन हैं और अंतर्गत आते हैं
CC-BY-4.0, नहीं CERN-OHL-P-2.0.

इस हार्डवेयर का पुनः उपयोग करते समय अनुशंसित सूचनाः

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

<a id="2-software--apache-20"></a>
## 2. सॉफ्टवेयर  ⁇ Apache-2.0

```
software/python/                    examples/                 .github/workflows/
.pre-commit-config.yaml             .gitignore
simulation/so_arm_101_description/  package.xml, setup.py, setup.cfg, Dockerfile,
                                    docker-compose.yaml, .dockerignore,
                                    urdf/, config/, launch/, scripts/, test/,
                                    docker/, worlds/, so_arm_101_description/
community/histology-slide-gripper/mujoco/   *.py, *.xml, *.urdf, *.xacro,
                                            requirements.txt
```

नीचे दिए गए रोबोट विवरण `urdf/` सॉफ्टवेयर के रूप में लाइसेंस है
हार्डवेयरः यह पूरे हाथ के लिए गतिशीलता, गतिरोध और जोड़ों की सीमाओं को कोड करता है,
जिसमें से अधिकांश अपस्ट्रीम का वर्णन करता है SO-ARM101 ज्यामिति जो Robonine स्वामित्व नहीं रखता
और इसलिए नहीं रखा जा सकता CERN-OHL-P-2.0. विनिर्माण योग्य पकड़
डिजाइन स्वयं में रहता है `models/` और अनुभाग 1 में शामिल है।

<a id="3-documentation--cc-by-40"></a>
## 3. प्रलेखन  ⁇ CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, RELICENSING.md
docs/                   *.md, *.pdf
assets/images/          *.png, *.PNG, *.jpg
every other README.md in the repository
community/histology-slide-gripper/assets/   *.png, *.jpg, *.gif
```

पुनः उपयोग के लिए श्रेयः "Robonine — SO-ARM100/101 समानांतर ग्रिपर,
https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper, CC BY 4.0".

<a id="4-mixed-and-third-party-material"></a>
## 4. मिश्रित और तृतीय पक्ष सामग्री

निम्नलिखित हैं **नहीं** कवर किया गया Robonine उपरोक्त कॉपीराइट। वे हैं
ऊपर की धारा से प्राप्त SO-ARM100/SO-ARM101 परियोजना द्वारा TheRobotStudio और हैं
के तहत पुनर्वितरित Apache-2.0. देखिये [`NOTICE`](../../../NOTICE).

```
simulation/so_arm_101_description/meshes/visual/     base_link.stl, link1_1.stl,
                                                     link2_1.stl, link3_1.stl,
                                                     link4_1.stl
simulation/so_arm_101_description/meshes/collision/  convex hulls of the above,
                                                     generated by
                                                     scripts/generate_collision_meshes.py
```

`link5_1.stl` (दो में `visual/` और `collision/`) एक एकल जाल है जो फ्यूज करता है
ऊपर की धारा SO-ARM101 कलाई ज्यामिति के साथ Robonine's `RB9.01.062.010 Main frame`.
जब तक यह दो अलग-अलग जाल के रूप में फिर से निर्यात नहीं किया जाता, तब तक पूरी फाइल वितरित की जाती है
के अंतर्गत Apache-2.0: Robonine अनुदान नहीं कर सकते CERN-OHL-P-2.0 ज्यामिति पर यह नहीं है
स्वयं का है, और अपने हिस्से को लाइसेंस देने के लिए स्वतंत्र है Apache-2.0. एक ही ज्यामिति
अलग से उपलब्ध है CERN-OHL-P-2.0 जैसे
`models/parts/RB9.01.062.010 Main frame.STL`.

`community/histology-slide-gripper/mujoco/meshes/arm/*.stl` बाइट-समान हैं
की प्रतियां `simulation/so_arm_101_description/meshes/visual/*.stl` और वारिस
वहाँ से उनके लाइसेंस  ⁇  तो उन आठ फ़ाइलों में से छह अपस्ट्रीम सामग्री हैं,
नहीं Robonineकाम के लिए.

`community/histology-slide-gripper/` माइकल Viacheslavov द्वारा योगदान दिया गया था
([@histochemichael](https://github.com/histochemichael)) और लाइसेंस प्राप्त है
एक ही तीन-तरफा विभाजन; कॉपीराइट इसके लेखक के पास है।

देखिये [`simulation/so_arm_101_description/meshes/LICENSE.md`](simulation/so_arm_101_description/meshes/LICENSE.md)
उस निर्देशिका के प्रति फ़ाइल विभाजन के लिए।
<!-- /translated-content -->
