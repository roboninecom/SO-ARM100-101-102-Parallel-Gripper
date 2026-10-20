<!-- translation-navigation -->
[English](../../../../en/simulation/so_arm_101_description/meshes/LICENSE.md) · [Русский](../../../../ru/simulation/so_arm_101_description/meshes/LICENSE.md) · [Español](../../../../es/simulation/so_arm_101_description/meshes/LICENSE.md) · [Français](../../../../fr/simulation/so_arm_101_description/meshes/LICENSE.md) · [Deutsch](../../../../de/simulation/so_arm_101_description/meshes/LICENSE.md) · [Português (Brasil)](../../../../pt-BR/simulation/so_arm_101_description/meshes/LICENSE.md) · [简体中文](../../../../zh-CN/simulation/so_arm_101_description/meshes/LICENSE.md) · [日本語](../../../../ja/simulation/so_arm_101_description/meshes/LICENSE.md) · [हिन्दी](LICENSE.md) · [العربية](../../../../ar/simulation/so_arm_101_description/meshes/LICENSE.md)

[अंग्रेज़ी मूल](../../../../../../simulation/so_arm_101_description/meshes/LICENSE.md)

[हिन्दी](../../../README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-the-meshes-in-this-directory"></a>
# इस निर्देशिका में जाल का लाइसेंस

**यह निर्देशिका मिश्रित है।** यहाँ हर जाल के स्वामित्व में नहीं Robonine, तो
लाइसेंस प्रति निर्देशिका के बजाय प्रति फ़ाइल आवंटित किया जाता है।

`collision/` इसमें कंवेक्स शेल होते हैं जो `visual/` द्वारा
`../scripts/generate_collision_meshes.py`. प्रत्येक पतवार में समान लाइसेंस है
दृश्य जाल से यह उत्पन्न किया गया था।

| फ़ाइल (दोनों में `visual/` और `collision/`) | लाइसेंस | कॉपीराइट |
|---|---|---|
| `clamp_1.stl`, `clamp_2.stl` | CERN-OHL-P-2.0 | Robonine |
| `base_link.stl` | Apache-2.0 | TheRobotStudio |
| `link1_1.stl`, `link2_1.stl`, `link3_1.stl`, `link4_1.stl` | Apache-2.0 | TheRobotStudio |
| `link5_1.stl` | Apache-2.0 | मिश्रित  ⁇  नीचे देखें |

<a id="upstream-geometry"></a>
## अपस्ट्रीम ज्यामिति

`base_link.stl` और `link1_1.stl` … `link4_1.stl` क्या वे SO-ARM101 **हाथ**,
ऊपर की धारा से प्राप्त [SO-ARM100/101 परियोजना द्वारा
TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) और पुनर्वितरित
के अंतर्गत Apache-2.0. इस परियोजना ने उस ज्यामिति को डिजाइन नहीं किया। भंडार को देखें
`NOTICE`.

<a id="link5_1stl--fused-mesh"></a>
## `link5_1.stl` ⁇  फ्यूज मेष

`link5_1.stl` एक एकल जाल है जो अपस्ट्रीम को मिलाता है SO-ARM101 कलाई के साथ
Robonine's `RB9.01.062.010 Main frame`. पूरी फ़ाइल के तहत वितरित किया गया है
**Apache-2.0**: Robonine अनुदान नहीं कर सकते CERN-OHL-P-2.0 ज्यामिति पर यह नहीं है
स्वयं का है, और अपने हिस्से को लाइसेंस देने के लिए स्वतंत्र है Apache-2.0.

दो अलग-अलग जाली के रूप में इसे फिर से निर्यात करने से प्रत्येक भाग को अपना उचित
लाइसेंस। तब तक, फ़ाइल को Apache-2.0 पूरी तरह से।

<a id="robonine-geometry"></a>
## Robonine ज्यामिति

`clamp_1.stl` और `clamp_2.stl` हैं Robonineअपने डिजाइन  ⁇
`RB9.01.062.021 Clamp` के साथ विलय `RB9.01.062.031 Gear rack`. वे खुले हैं
हार्डवेयर नीचे CERN-OHL-P-2.0:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

देखिये `LICENSING.md` पूर्ण लाइसेंस मानचित्र के लिए रिपॉजिटरी रूट में।
<!-- /translated-content -->
