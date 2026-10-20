<!-- translation-navigation -->
[English](../../../en/simulation/so_arm_101_description/LICENSE.md) · [Русский](../../../ru/simulation/so_arm_101_description/LICENSE.md) · [Español](../../../es/simulation/so_arm_101_description/LICENSE.md) · [Français](../../../fr/simulation/so_arm_101_description/LICENSE.md) · [Deutsch](../../../de/simulation/so_arm_101_description/LICENSE.md) · [Português (Brasil)](../../../pt-BR/simulation/so_arm_101_description/LICENSE.md) · [简体中文](../../../zh-CN/simulation/so_arm_101_description/LICENSE.md) · [日本語](../../../ja/simulation/so_arm_101_description/LICENSE.md) · [हिन्दी](LICENSE.md) · [العربية](../../../ar/simulation/so_arm_101_description/LICENSE.md)

[अंग्रेज़ी मूल](../../../../../simulation/so_arm_101_description/LICENSE.md)

[हिन्दी](../../README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-this-package"></a>
# इस पैकेज का लाइसेंस

`so_arm_101_description` इस योजना के अंतर्गत
[SO-ARM100/101 समानांतर ग्रिपर](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)
परियोजना, जो बहु-लाइसेंस है। इस फ़ाइल पैकेज का वर्णन करता है तो यह है
स्व-व्याख्यात्मक जब इसे स्वयं स्थापित या पुनः वितरित किया जाता है।

| सामग्री | लाइसेंस | कॉपीराइट |
|---|---|---|
| `urdf/`, `config/`, `launch/`, `scripts/`, `test/`, `worlds/`, `docker/`, `so_arm_101_description/`, `setup.py`, `package.xml` | Apache-2.0 | Robonine |
| `meshes/` | **मिश्रित** ⁇  देखें [`meshes/LICENSE.md`](meshes/LICENSE.md) | मिश्रित |

<a id="meshes--read-before-reusing"></a>
## पुनः उपयोग से पहले मेष  ⁇  पढ़ें

`meshes/` एक समान लाइसेंस नहीं हैः

- `clamp_1.stl`, `clamp_2.stl` हैं Robonineपकाने की ज्यामिति, **CERN-OHL-P-2.0**.
- `base_link.stl`, `link1_1.stl` … `link4_1.stl` क्या वे SO-ARM101 **हाथ**, व्युत्पन्न
  ऊपर की धारा से [SO-ARM100/101 परियोजना द्वारा
  TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) और लाइसेंस प्राप्त
  **Apache-2.0**. वे नहीं हैं Robonineकाम के लिए.
- `link5_1.stl` विलय ऊपर धारा में कलाई ज्यामिति के साथ Robonineएक में मुख्य फ्रेम
  एकल शरीर और है **Apache-2.0** पूरी तरह से।

नीचे दिए गए रोबोट विवरण `urdf/` सॉफ्टवेयर के रूप में लाइसेंस है
हार्डवेयरः यह पूरे हाथ के लिए kinematics और गतिरोध पैरामीटर को कोड करता है, बहुत
जिसमें से अपस्ट्रीम ज्यामिति का वर्णन करता है जो Robonine स्वामित्व नहीं है।

पूर्ण लाइसेंस ग्रंथों को रिपॉजिटरी रूट में लाइव किया गया है `HARDWARE-LICENSE.txt`,
`SOFTWARE-LICENSE.txt` और `DOCS-LICENSE.txt` (और फिर से अपने एसपीडीएक्स नामों के तहत
में `LICENSES/`, जैसा कि REUSE स्पेसिफिकेशन की आवश्यकता है) । यह भी देखें `LICENSING.md`
पूरा नक्शा के लिए, `NOTICE` तीसरे पक्ष के लिए श्रेय, तथा `REUSE.toml` के लिए
मशीन-पठनीय संस्करण।
<!-- /translated-content -->
