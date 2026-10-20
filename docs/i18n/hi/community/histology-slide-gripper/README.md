<!-- translation-navigation -->
[English](../../../en/community/histology-slide-gripper/README.md) · [Русский](../../../ru/community/histology-slide-gripper/README.md) · [Español](../../../es/community/histology-slide-gripper/README.md) · [Français](../../../fr/community/histology-slide-gripper/README.md) · [Deutsch](../../../de/community/histology-slide-gripper/README.md) · [Português (Brasil)](../../../pt-BR/community/histology-slide-gripper/README.md) · [简体中文](../../../zh-CN/community/histology-slide-gripper/README.md) · [日本語](../../../ja/community/histology-slide-gripper/README.md) · [हिन्दी](README.md) · [العربية](../../../ar/community/histology-slide-gripper/README.md)

[अंग्रेज़ी मूल](../../../../../community/histology-slide-gripper/README.md)

[हिन्दी](../../README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="histology-slide-gripper-community-mod"></a>
# हिस्टोलॉजी स्लाइड ग्रिपर (सामुदायिक मोड)

एक सामुदायिक संस्करण SO-ARM100/101 समानांतर ग्रिपर द्वारा [माइकल वियाचेस्लाव](https://github.com/histochemichael), हिस्टोलॉजी और हिस्टोटैक्नोलोजी स्वचालन के लिए अनुकूलितः मानक 75 x 25 मिमी माइक्रोस्कोप स्लाइड्स का हल्का पिकअप, स्लाइड डाईनिंग डिपर/रैक, और पकड़ को कैमरे द्वारा करीब से देखा जा सकता है।

<div align="center">

![हिस्टोलॉजी स्लाइड पकड़ डेमो](../../../../../community/histology-slide-gripper/assets/histology-slide-gripper-demo.gif)

*SO-ARM100/101 माइक्रोस्कोप स्लाइड्स और एक रंग डिपर/रैक को संभालने के लिए कस्टम क्लैंप का उपयोग करके समानांतर पकड़।*

</div>

<a id="what-changed-vs-the-base-gripper"></a>
## बेस ग्रिपर के मुकाबले क्या बदल गया

| अतिरिक्त | विवरण |
|----------|-------------|
| माइक्रोस्कोप स्लाइड क्लैंप | लंबी, सपाट क्लैंप ज्यामिति मानक 75 x 25 मिमी माइक्रोस्कोप स्लाइड्स के प्रत्यक्ष पिकअप का समर्थन करती है। |
| स्लाइड रैक/डिपर हैंडलिंग | क्लैंप की दूरी और टिप्स स्लाइड डाईनिंग डिपर / रैक जैसे कि नीचे जुड़ा हुआ मेडिसस हेल्थ स्लाइड डाईनिंग डिपर शामिल करते हैं। |
| कोणयुक्त अर्डकैम धारक | एक प्रिंटेबल होल्डर स्लाइड और रैक पिकअप की नज़दीकी निगरानी के लिए ग्रिपर जांघों पर एक अर्डुकैम ग्लोबल-शटर यूएसबी कैमरा लक्षित करता है। |
| पूर्ण विधानसभा सीएडी | एक पूर्ण मुद्रित STL और संपादन योग्य STEP विधानसभा में हैं [`cad/`](../../../../../community/histology-slide-gripper/cad). |

<a id="gallery"></a>
## गैलरी

<div align="center">

| एकल स्लाइड पिकअप | डाईपर/रैक पिकअप | Arducam धारक दृश्य |
|:-:|:-:|:-:|
| ![माइक्रोस्कोप स्लाइड को पकड़ने वाला क्लैंप](../../../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg) | ![स्लाइड डाईनिंग डिपर के साथ संरेखित क्लैंप](../../../../../community/histology-slide-gripper/assets/slide-gripper-staining-dipper.jpg) | ![पकाने वाले jaws के ऊपर Arducam धारक](../../../../../community/histology-slide-gripper/assets/arducam-holder-front.jpg) |

| सामने का दृश्य | जावा ज्यामिति | आइसोमेट्रिक संयोजन |
|:-:|:-:|:-:|
| <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-front.png" alt="Front CAD view of the microscope slide gripper mod" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-side.png" alt="Angled CAD view showing the microscope slide jaw geometry" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-isometric.png" alt="Isometric CAD view of the full microscope slide gripper assembly" width="250"> |

</div>

<a id="cad-files"></a>
## सीएडी फ़ाइलें

| फ़ाइल | प्रारूप | उपयोग |
|------|--------|-----|
| [`cad/the-parallel-microscope-slide-gripper.stl`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.stl) | एसटीएल | माइक्रोस्कोप स्लाइड पकड़ मॉड के लिए प्रिंटेबल पूर्ण विधानसभा। |
| [`cad/the-parallel-microscope-slide-gripper.step`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.step) | चरण | पूर्ण असेंबली के लिए संपादन योग्य CAD स्रोत। |

<a id="add-on-bill-of-materials"></a>
## सामग्री का अतिरिक्त विवरण

ये आइटम स्लाइड/रैक वर्कफ़्लो के लिए विशिष्ट हैं और आधार पकड़ का हिस्सा नहीं हैं [बीओएम](../../docs/bom.md).

| घटक | Qty | नोट्स | लिंक |
|-----------|:---:|-------|------|
| Arducam 100fps मोनो ग्लोबल शटर यूएसबी कैमरा, OV9281 | 1 | स्लाइड और रैक पिकअप को चकनाचूर के पास देखने के लिए कोण धारक के साथ इस्तेमाल किया गया कैमरा। | [अमेज़ॅन यूके](https://www.amazon.co.uk/Arducam-Shutter-Distortion-Computer-Raspberry/dp/B0FXWWF55X) |
| हैंडल के साथ स्लाइड डाइटिंग प्लास्टिक डिपर | 1+ | संदर्भ रंग डिपर/रैक लक्ष्य; मानक 75 x 25 मिमी स्लाइड के लिए डिज़ाइन किया गया। | [मेडिकस स्वास्थ्य](https://www.medicus-health.com/slide-staining-dipper.html) |
| समानांतर सूक्ष्मदर्शी स्लाइड पकड़ की स्थापना | 1 | मुद्रण `the-parallel-microscope-slide-gripper.stl`; संपादन के लिए STEP फ़ाइल शामिल है। | [`cad/`](../../../../../community/histology-slide-gripper/cad) |

<a id="mujoco-simulation"></a>
## MuJoCo सिमुलेशन

<div align="center">

![SO-ARM101 हिस्टॉलॉजी स्लाइड ग्रिपर चल रहा है MuJoCo](../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

*SO-ARM101 हिस्टॉलॉजी स्लाइड पकाने के साथ जोड़ा गया है और अंदर चलाया जाता है MuJoCo.*

</div>

एक आत्मनिर्भर MuJoCo 3.4.0 मॉडल उपलब्ध है [`mujoco/`](mujoco/README.md). इसमें पूर्ण SO-ARM101 मॉडल, ग्रिपर जाल, एक स्टैंडअलोन ग्रिपर परीक्षण बेंच, निर्माण स्क्रिप्ट, और एक सिर के बिना पकड़-और-लिफ्ट जांच.

रिपॉजिटरी रूट सेः

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py
```

उपयोग करें `sg_grip` नियंत्रण में MuJoCo दर्शकों को खोलने और बंद करने के लिए jaws. देखो [सिमुलेशन README](mujoco/README.md) मॉडल विवरण, नियंत्रण, सत्यापन और पुनर्निर्माण निर्देशों के लिए।

<a id="notes"></a>
## नोट्स

- ग्रिपर की उंगलियों को मानक 75 x 25 मिमी माइक्रोस्कोप स्लाइड और स्लाइड रंग डिपर/रैक के लिए डिज़ाइन किया गया है।
- असेंबली कैमरे के दृश्य को पकड़ने वाले जांघों की ओर लक्षित रखती है ताकि कैमरा स्लाइड और रैक पिकअप का अवलोकन कर सके।
- सबसे पहले गैर-महत्वपूर्ण स्लाइड्स के साथ परीक्षण करें और अपने वर्कफ़्लो के लिए प्रिंट सामग्री, भरने और पकड़ बल को समायोजित करें।

<a id="links"></a>
## लिंक

- 🎥 [डेमोः स्लाइड और रंगाई रैक पिकअप (लिंक्डइन)](https://www.linkedin.com/posts/michael-viacheslavov_histology-histotechnology-robotics-ugcPost-7482570199859240960-Gqpw/)
<!-- /translated-content -->
