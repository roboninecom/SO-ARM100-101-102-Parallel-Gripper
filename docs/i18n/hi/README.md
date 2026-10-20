<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](README.md) · [العربية](../ar/README.md)

[अंग्रेज़ी मूल](../../../README.md)

[हिन्दी](README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm100101-parallel-gripper"></a>
# SO-ARM100/101 समानांतर ग्रिपर

<div align="center">

[![SO-ARM101 समानांतर ग्रिपर](../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

**🎥 [पकड़ कार्रवाई में देखो!](https://youtube.com/shorts/bSyXjgNGXZk)** · **🛒 [खरीदें SO-ARM102 समानांतर पकड़ के साथ किट](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

3D मुद्रित समानांतर पकड़ **[Robonine](https://robonine.com)** ओपन सोर्स के लिए SO-ARM100/101 रोबोटिक मंच।

> समानांतर पकड़ के साथ एक पूर्ण रोबोट हाथ सेट पसंद करते हैं? **[खरीदें SO-ARM102 किट](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

[![हार्डवेयरः CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt)
[![सॉफ्टवेयरः Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt)
[![दस्तावेज: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt)
[![लागत: ~$50](https://img.shields.io/badge/Cost-~%2450-green.svg)](docs/bom.md)
[![असेंबलीः 30 मिनट](https://img.shields.io/badge/Assembly-30%20min-orange.svg)](docs/assembly-guide.md)

---

**प्रश्न? हम यहाँ मदद करने के लिए हैं!**
⁇  ईमेलः [hello@robonine.com](mailto:hello@robonine.com)

</div>

---

<a id="-key-features"></a>
## ✨ प्रमुख विशेषताएं

| विशेषता | विवरण |
|---------|-------------|
| **120 एन पकड़ने की शक्ति** | विश्वसनीय समानांतर जांघ तंत्र |
| **14 mm/s गति** | चिपकने की गति |
| **84 मिमी पूर्ण स्ट्रोक** | विभिन्न वस्तुओं के लिए व्यापक उद्घाटन |
| **0.5 मिमी पुनरावृत्ति** | उच्च परिशुद्धता वाली स्थिति |
| **कैमरा संगत** | समर्थन RealSense, Orbbec, यूएसबी कैमरे |
| **3 डी प्रिंट करने योग्य** | मानक एफडीएम प्रिंटर पर सभी भागों की छपाई |
| **~$50कुल लागत** | सस्ती ओपन सोर्स समाधान |
| **आसान इकट्ठा** | बुनियादी उपकरणों के साथ 30-45 मिनट |

---

<a id="-gallery"></a>
## ⁇  गैलरी

<div align="center">

<a id="gripper-on-so-arm101"></a>
### ग्रिपर लगा है SO-ARM101

![ग्रिपर लगाया गया है SO-ARM101](../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*अनुवर्ती पकड़ के साथ एकीकृत SO-ARM101 रोबोट हाथ*

<a id="dimensions"></a>
### आयाम

![ग्रिपर के आयाम](../../../assets/images/specification/08-gripper-dimensions-3d.png)

*128 × 109 × 130.5 मिमी, पूर्ण स्ट्रोक 84 मिमी*

</div>

---

<a id="-specifications"></a>
## ⁇  विनिर्देश

<a id="gripper-parameters"></a>
### ग्रिपर के पैरामीटर

| पैरामीटर | मूल्य |
|-----------|-------|
| अधिकतम पकड़ बल | **120 N** |
| अधिकतम पकड़ की गति | **14 मिमी/सेक** |
| पूर्ण स्ट्रोक | **84 मिमी** |
| पुनरावृत्ति | **0.5 मिमी** |
| असेंबली द्रव्यमान (पीएलए, 30% भरने) | **170 g** |
| डीओएफ | **1** |

<a id="dimensions-1"></a>
### आयाम

| आयाम | मूल्य |
|-----------|-------|
| चौड़ाई | 128 मिमी |
| गहराई | 130.5 मिमी |
| ऊंचाई | 109 मिमी |

<a id="servo-parameters-feetech-sts3215"></a>
### सर्वो पैरामीटर (Feetech STS3215)

| पैरामीटर | मूल्य |
|-----------|-------|
| ऑपरेटिंग वोल्टेज | 12V |
| स्टॉल टॉर्क | 30 किलोग्राम |
| गति (लोड नहीं) | 45 आरपीएम |
| एन्कोडर | पूर्ण चुंबकीय 12-बिट |
| प्रोटोकॉल | RS485/TTL 1 एमबीपीएस तक |
| परिचालन तापमान | -20°C ~ 60°C |

---

<a id="-camera-compatibility"></a>
## ⁇  कैमरा संगतता

ग्रिपर एक आदान-प्रदान योग्य कैमरा धारक के माध्यम से कई कैमरों का समर्थन करता हैः

| कैमरा | प्रकार | उपयोग के मामले |
|--------|------|----------|
| IMX335 5MP यूएसबी | आरजीबी | मूल दृष्टि कार्य |
| GC2093 2MP यूएसबी | आरजीबी | बजट विकल्प |
| Orbbec मिथुन 2 | आरजीबी-डी | 3D धारणा |
| RealSense D405 | आरजीबी-डी | निकट दूरी की गहराई |
| RealSense D435/D435i | आरजीबी-डी | सामान्य प्रयोजन |
| RealSense D455 | आरजीबी-डी | लंबी दूरी की गहराई |

<div align="center">

![गिरिपर पर लगाए गए विभिन्न कैमरे](../../../assets/images/specification/09-camera-types.png)

*RealSense, यूएसबी कैमरा मॉड्यूल, Orbbec मिथुन 2*

</div>

---

<a id="-bill-of-materials"></a>
## ⁇  सामग्री का बिल

**कुल लागत: ~$50** ([अमेज़ॅन लिंक के साथ पूर्ण BOM](docs/bom.md))

| श्रेणी | घटक | एस्ट. लागत |
|----------|------------|-----------|
| इलेक्ट्रॉनिक्स | Feetech STS3215 सेवा | ~$29 |
| बेयरिंग | MF106ZZ (x2) | ~$2 |
| एल्यूमीनियम/कार्बन ट्यूब | D6x1×125 मिमी (x2) | ~$4 |
| 3 डी प्रिंटिंग | 8 भाग (~100-150 ग्राम पीएलए) | ~$12 |
| फास्टनर | M2/M4 शिकंजा, M2 नट्स, M3 सेट शिकंजा | ~$3 |

---

<a id="-quick-start"></a>
## ⁇  शीघ्र प्रारंभ

समानांतर पकड़ के साथ एक पूर्ण रोबोट हाथ सेट के लिए, **[खरीदें SO-ARM102 किट](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**. निर्माण के लिए SO-ARM100/101 अपने आप को पकड़ो, नीचे दिए गए चरणों का पालन करें।

<a id="1-print-the-parts-2-4-hours"></a>
### 1. भागों को छापें (2-4 घंटे)

से STL फ़ाइलें डाउनलोड करें [`models/parts/`](models/README.md). जैसे लोकप्रिय प्रिंटर के साथ संगत **बाम्बू लैब ए1 मिनी**, **Prusa MINI+**, और किसी भी प्रिंटर के साथ ≥180×180mm बिस्तर।

| भाग | Qty | सेटिंग्स |
|------|:---:|----------|
| मुख्य ढाँचा (RB9.01.062.010) | 1 | 20% भरना |
| जकड़ने वाला जबड़ा (RB9.01.062.020) | 2 | 20% भरना |
| दांतेदार रैक (RB9.01.062.030) | 2 | 100% भरना |
| गियर (RB9.01.062.040) | 1 | 100% भरना |
| कैमरा धारक (RB9.01.060.074) | 1 | 20% भरना |
| धारक (RB9.01.060.080) | 1 | 20% भरना |
| कैमरा स्पेसर (RB9.01.060.090) | 1 | 20% भरना |
| D405 धारक (RB9.01.060.110) | 1 | 20% भरना |

<a id="2-order-components-1-2-days"></a>
### 2. आदेश घटक (1-2 दिन)

देखिये [सामग्री का विवरण](docs/bom.md) सीधे अमेज़ॅन लिंक के लिए।

<a id="3-assemble-30-45-minutes"></a>
### 3. इकट्ठा करना (30-45 मिनट)

अनुसरण करें [विधानसभा गाइड](docs/assembly-guide.md) चरण-दर-चरण चित्रों के साथः

1. सर्वो डिस्क पर गियर स्थापित करें, इस असेंबली को सर्वो पर स्थापित करें
2. सर्वो केबल डालें
3. उपयोग करना Feetech सॉफ़्टवेयर सर्वो को अपनी न्यूनतम स्थिति में ले जाएं (सॉफ़्टवेयर में स्लाइडर को बाईं ओर ले जाएं)
4. दांतेदार रैक को जबड़ों से जोड़ें
5. गाइड छड़ों को दोनों जबड़ों में डालें
6. बेयरिंग को मुख्य ढाँचे में लगाएँ और स्क्रू से कसें
7. गाइड छड़ों को ढाँचे में बिठाएँ
8. जबड़ों को बाईं और दाईं अंतिम स्थितियों तक फैलाएँ
9. सर्वो डालें और इसे पेंच से ठीक करें
10. कैमरा स्पैसर और यूवीसी कैमरा संलग्न करें, 4x पेंच और नट्स M2 (वैकल्पिक) के साथ फिक्स्ड
11. माउंट टू रोबोट आर्म (वैकल्पिक)

<a id="4-software"></a>
### 4. सॉफ्टवेयर

```bash
# Configure servo motor if necessary
https://lab.robonine.com/tools/robonine/feetech-bus

# Control gripper
https://lab.robonine.com/tools/robonine/control-robot
```

---

<a id="-repository-structure"></a>
## ⁇  भंडारण संरचना

```
├── assets/
│   └── images/
│       ├── assembly/          # Assembly step images
│       └── specification/     # Technical drawings
├── docs/
│   ├── assembly-guide.md                # Step-by-step assembly
│   ├── bom.md                           # Bill of materials with links
│   ├── Parallel gripper by Robo9.pdf    # Gripper product specification
│   ├── quick-start.md                   # Getting started guide
│   ├── SO-ARM101 by Robo9.pdf           # SO-ARM101 product specification
│   └── specifications.md               # Technical specifications
├── models/
│   ├── parts/                                    # Individual STL files
│   └── Follower gripper (165x165 bed size).STL   # Complete assembly (165×165mm bed)
├── community/
│   └── histology-slide-gripper/   # Community variant (CAD, MuJoCo model)
├── simulation/
│   ├── README.md                  # Simulation overview
│   ├── gazebo/                    # Gazebo guide
│   ├── mujoco/                    # MuJoCo guide
│   ├── webots/                    # Webots guide
│   ├── coppeliasim/               # CoppeliaSim guide
│   ├── isaac_sim/                 # Isaac Sim guide
│   └── so_arm_101_description/    # ROS2 package (URDF, launch, Docker)
├── software/
│   └── python/                # Control software
├── examples/                  # Usage examples
├── HARDWARE-LICENSE.txt       # CERN-OHL-P-2.0 (CAD, geometry)
├── SOFTWARE-LICENSE.txt       # Apache-2.0 (code)
├── DOCS-LICENSE.txt           # CC BY 4.0 (docs, images)
├── LICENSING.md               # Which licence covers what
├── NOTICE                     # Third-party attribution
├── REUSE.toml                 # Machine-readable licence map
├── RELICENSING.md             # Record of the 2026 relicensing
└── CONTRIBUTING.md
```

---

<a id="-documentation"></a>
## ⁇  प्रलेखन

| दस्तावेज | विवरण |
|----------|-------------|
| [त्वरित प्रारंभ गाइड](docs/quick-start.md) | 30 मिनट में चलें |
| [विधानसभा गाइड](docs/assembly-guide.md) | चित्रों के साथ कदम-दर-चरण |
| [ग्रिपर असेंबली गाइड (पीडीएफ)](../../Assembly%20Guide%20Follower%20Gripper.pdf) | प्रिंटेबल ग्रिपर असेंबली निर्देश |
| [SO-ARM101 विधानसभा गाइड (पीडीएफ)](../../Assembly%20Guide%20SO-ARM101.pdf) | पूर्ण SO-ARM101 आर्म असेंबली निर्देश |
| [सामग्री का विवरण](docs/bom.md) | अमेज़ॅन लिंक के साथ भाग सूची |
| [विनिर्देश](docs/specifications.md) | तकनीकी विवरण |
| [3 डी मॉडल](models/README.md) | सेटिंग्स और फ़ाइलें प्रिंट करें |
| [समानांतर ग्रिपर उत्पाद विनिर्देश (पीडीएफ)](../../Parallel%20gripper%20by%20Robo9.pdf) | रोबो9 द्वारा समानांतर पकड़ उत्पाद विनिर्देश |
| [SO-ARM101 उत्पाद विनिर्देश (पीडीएफ)](../../SO-ARM101%20by%20Robo9.pdf) | SO-ARM101 Robo9 द्वारा रोबोट आर्म उत्पाद विनिर्देश |

---

<a id="-hardware-requirements"></a>
## ⁇  हार्डवेयर आवश्यकताएँ

<a id="electronics"></a>
### इलेक्ट्रॉनिक्स
- 1× Feetech STS3215 सर्वो मोटर

वर्तमान पर पकड़ कनेक्ट करें SO-ARM100/101 सर्वो बस और नियंत्रक।
रोबोट कंट्रोलर और पावर सप्लाई ग्रिपर बीओएम के बाहर हाथ सेटअप का हिस्सा हैं।

<a id="mechanical"></a>
### यांत्रिक
- 2× MF106ZZ बीयरिंग (6×10×3 मिमी)
- 2× एल्यूमीनियम/कार्बन ट्यूब D6x1×125 मिमी

<a id="fasteners"></a>
### फास्टनर
- 2 × M4 × 8 DIN 7991 पेंच
- 4x M2x8 DIN 912 पेंच
- 4 × M2 DIN 934 नट
- 4× M3×4 DIN 913 सेट शिकंजा

<a id="tools-required"></a>
### आवश्यक उपकरण
- फिलिप्स हेड स्क्रूड्राइवर (PH1)
- हेक्स कुंजी M2 (H1.5) और M4 (H2.5)

---

<a id="-simulation"></a>
## ⁇ ️ सिमुलेशन

SO-ARM101 को एक पैरामीटरयुक्त URDF वाले ROS2 विवरण पैकेज से 5 भौतिकी इंजनों में सिमुलेट किया जा सकता है। ROS2 स्थापित करने की आवश्यकता नहीं है; Docker सब संभालता है।

<div align="center">

| Gazebo (इग्निशन किले) | MuJoCo |
|:-:|:-:|
| ![SO-ARM-101 में Gazebo](../../../assets/images/simulation/gazebo/gazebo_pick_place.png) | ![SO-ARM-101 में MuJoCo](../../../assets/images/simulation/mujoco/mujoco_pick_place.png) |

</div>

| सिम्युलेटर | स्थिति | डॉकर |
|-----------|--------|--------|
| [Gazebo](simulation/gazebo/README.md) | तैयार | `docker compose run gazebo` |
| [MuJoCo](simulation/mujoco/README.md) | तैयार | `docker compose run mujoco` |
| [Webots](simulation/webots/README.md) | अस्थिर | `docker compose run webots` |
| [CoppeliaSim](simulation/coppeliasim/README.md) | परीक्षण नहीं किया | बाहरी सिम्युलेटर |
| [एनवीडीआईए Isaac हाँ](simulation/isaac_sim/README.md) | परीक्षण नहीं किया | बाहरी सिम्युलेटर |

**त्वरित प्रारंभ (डॉकर):**

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

देखो [सिमुलेशन गाइड](simulation/README.md) पूर्ण सेटअप, वास्तुकला विवरण और रोबोट कमांडिंग के लिए।

---

<a id="-community-mods"></a>
## ⁇  सामुदायिक मॉड

समुदाय द्वारा निर्मित पकड़ के संस्करण, प्रत्येक स्वयं में निहित [`community/`](../../../community):

| मोड | लेखक | विवरण |
|-----|--------|-------------|
| [हिस्टोलॉजी स्लाइड ग्रिपर](community/histology-slide-gripper/README.md) | [माइकल वियाचेस्लाव](https://github.com/histochemichael) | 75 x 25 मिमी माइक्रोस्कोप स्लाइड्स और डाइटिंग डिपर/रैक के लिए क्लैंप्स, साथ ही पकड़ की निगरानी के लिए एक कोणित Arducam धारक। |

<div align="center">

<a href="community/histology-slide-gripper/README.md"><img src="../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg" alt="Histology slide gripper mod holding a microscope slide" width="400"></a>

*हिस्टोलॉजी स्लाइड ग्रिपर मॉड  ⁇  पूर्ण विवरण, सीएडी फ़ाइलों और डेमो के लिए क्लिक करें*

</div>

---

<a id="-contributing"></a>
## ⁇  योगदान

हम योगदान का स्वागत करते हैं! कृपया इस पर विचार करने के लिए स्वतंत्र महसूस करेंः
- ⁇  बग और समस्या की रिपोर्ट करें
- ⁇  नई सुविधाओं का सुझाव दें
- ⁇  खींचने के अनुरोध प्रस्तुत करें
- ⁇  प्रलेखन में सुधार

---

<a id="-license"></a>
## ⁇  लाइसेंस

कॉपीराइट (c) 2025 Robonine. यह परियोजना बहु-लाइसेंस है  ⁇  विभिन्न प्रकार के
सामग्री में अलग-अलग लाइसेंस हैंः

| सामग्री | लाइसेंस |
|---|---|
| हार्डवेयर डिजाइन  ⁇ `models/`, सामुदायिक सीएडी, पकड़ जाल | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| सॉफ्टवेयर  ⁇ `software/`, `examples/`, `simulation/`, सिमुलेशन कोड में `community/` | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| प्रलेखन और चित्र  ⁇ `docs/`, `assets/`, सभी `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

देखिये [`LICENSING.md`](LICENSING.md) फ़ाइल-दर-फ़ाइल नक्शे के लिए सटीक और
[`REUSE.toml`](../../../REUSE.toml) मशीन-पठनीय संस्करण के लिए।

**यहाँ सब कुछ नहीं है Robonineकाम के लिए.** इनका SO-ARM101 हाथों के जाल प्राप्त होते हैं
से [TheRobotStudioअपस्ट्रीम परियोजना](https://github.com/TheRobotStudio/SO-ARM100)
और बने रहें Apache-2.0; हिस्टोलॉजी स्लाइड ग्रिपर का योगदान
[@histochemichael](https://github.com/histochemichael). देखिये [`NOTICE`](../../../NOTICE)
किसी भी जाल का पुनः उपयोग करने से पहले।

तक की रिलिज और सहित `v0.3.1` जीपीएल-3.0 के तहत प्रकाशित हुए हैं और बने रहते हैं
उन शर्तों के तहत उपलब्ध  ⁇  देखें [`RELICENSING.md`](RELICENSING.md).

---

<a id="-links"></a>
## ⁇  लिंक

- [Feetech STS3215 सेवा](https://www.feetechrc.com/525603.html)
- [STServo Python एसडीके](https://github.com/FEETECH-RC/STServo_SDK_Python)

---

<a id="-engineering-team"></a>
## ⁇  इंजीनियरिंग टीम

| नाम | भूमिका | संपर्क |
|------|------|---------|
| **बोरिस कोटोव** | सॉफ्टवेयर इंजीनियर | [टेलीग्राम](https://t.me/bkotov) |
| **एलन सुबिन** | डिजाइन इंजीनियर | [लिंक्डइन](https://www.linkedin.com/in/alan-subin/) |

---

<div align="center">

**रोबोटिक्स समुदाय के लिए बनाया गया [Robonine](https://robonine.com)** 🤖

**प्रश्न? हम यहाँ मदद करने के लिए हैं!**
⁇  ईमेलः [hello@robonine.com](mailto:hello@robonine.com)

</div>
<!-- /translated-content -->
