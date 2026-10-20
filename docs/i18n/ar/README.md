<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../README.md)

[العربية](README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm100101-parallel-gripper"></a>
# SO-ARM100/101 قابض متوازٍ

<div align="center">

[![SO-ARM101 قابض متوازٍ](../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

**🎥 [راقبوا المقبض في العمل!](https://youtube.com/shorts/bSyXjgNGXZk)**

ضغط متوازي خفيف المطبوع 3D مصمم من قبل: **[Robonine](https://robonine.com)** للمصدر المفتوح SO-ARM100/101 منصة روبوتية

[![الأجهزة: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt)
[![البرمجيات: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt)
[![الأدلة: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt)
[![التكلفة:$70](https://img.shields.io/badge/Cost-~%2470-green.svg)](docs/bom.md)
[![التجميع: 30 دقيقة](https://img.shields.io/badge/Assembly-30%20min-orange.svg)](docs/assembly-guide.md)

---

**أسئلة؟ نحن هنا لمساعدة!**
⁇  البريد الإلكتروني: [مرحباً@robonine.com](mailto:hello@robonine.com)

</div>

---

<a id="-key-features"></a>
## ✨ الميزات الرئيسية

| الميزة | وصف |
|---------|-------------|
| **قوة الالتقاط 120N** | آلية متوازية موثوقة في الفك |
| **السرعة 14 مم/س** | سرعة تشغيل المقبض |
| **84 مليمتر ضرب كامل** | فتحة واسعة لمختلف الأشياء |
| **0.5mm تكرارية** | تحديد المواقع بدقة عالية |
| **آلة التصوير متوافقة** | الدعم RealSense, Orbbec، كاميرات USB |
| **3D قابل للطباعة** | جميع الأجزاء الطباعة على طابعات FDM القياسية |
| **~$62التكلفة الإجمالية** | حل مفتوح المصدر بأسعار معقولة |
| **التجميع السهل** | 30-45 دقيقة مع الأدوات الأساسية |

---

<a id="-gallery"></a>
## ⁇  المعرض

<div align="center">

<a id="gripper-on-so-arm101"></a>
### القابض على SO-ARM101

![القابض مثبت على SO-ARM101](../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*مقبض التابع مدمج مع SO-ARM101 ذراع الروبوت*

<a id="dimensions"></a>
### الأبعاد

![أبعاد القابض](../../../assets/images/specification/08-gripper-dimensions-3d.png)

*128 × 109 × 130.5 مليمتر، ضربة كاملة 84 مليمتر*

</div>

---

<a id="-specifications"></a>
## ⁇  المواصفات

<a id="gripper-parameters"></a>
### مواصفات القابض

| المعيار | القيمة |
|-----------|-------|
| أقصى قوة الالتقاط | **120 N** |
| الحد الأقصى لسرعة الالتقاط | **14 مم/س** |
| ضربة كاملة | **84 ملم** |
| التكرار | **0.5 ملم** |
| كتلة التجميع (PLA، 30٪ ملء) | **170 g** |
| الدولية | **1** |

<a id="dimensions-1"></a>
### الأبعاد

| الأبعاد | القيمة |
|-----------|-------|
| عرض | 128 مم |
| العمق | 130.5 ملم |
| الارتفاع | 109 مم |

<a id="servo-parameters-feetech-sts3215"></a>
### ملامح الخدمة (Feetech STS3215)

| المعيار | القيمة |
|-----------|-------|
| الجهد التشغيلي | 12V |
| عزم التوقف | 30 كجم |
| السرعة (لا حمولة) | 45 ر/م |
| كودر | مغناطيسية مطلقة 12 بت |
| البروتوكول | RS485/TTL إلى 1 ميغابتس |
| درجة حرارة العمل | -20°C ~ 60°C |

---

<a id="-camera-compatibility"></a>
## ⁇  متوافقة مع الكاميرا

يدعم المقبض العديد من الكاميرات عن طريق حامل الكاميرا القابلة للتبادل:

| الكاميرا | النوع | حالة الاستخدام |
|--------|------|----------|
| IMX335 5MP USB | الـ RGB | مهام الرؤية الأساسية |
| GC2093 USB 2MP | الـ RGB | خيار الميزانية |
| Orbbec التوأم 2 | RGB-D | 3D الإدراك |
| RealSense D405 | RGB-D | عمق على نطاق قريب |
| RealSense D435/D435i | RGB-D | الغرض العام |
| RealSense D455 | RGB-D | عمق طويل المدى |

<div align="center">

![كاميرات مختلفة مثبتة على المقبض](../../../assets/images/specification/09-camera-types.png)

*RealSense، وحدات الكاميرا USB Orbbec التوأم 2*

</div>

---

<a id="-bill-of-materials"></a>
## ⁇  مخطط المواد

**التكلفة الإجمالية$62** ([BOM كاملة مع روابط أمازون](docs/bom.md))

| الفئة | المكونات | -إست التكلفة |
|----------|------------|-----------|
| الإلكترونيات | Feetech STS3215 مُعدّل الحافلة الخادم + الخادم | ~$40 |
| محامل | MF106ZZ (x2) | ~$2 |
| الألومنيوم/كربون | D6x1x125mm (x2) | ~$4 |
| 3D الطباعة | 8 أجزاء (~100-150 غرام من PLA) | ~$12 |
| أدوات التثبيت | مسامير M2/M4، مكسرات M2، مسامير مجموعة M3 | ~$3 |

---

<a id="-quick-start"></a>
## ⁇  بدء سريع

<a id="1-print-the-parts-2-4-hours"></a>
### 1. طباعة الأجزاء (2-4 ساعات)

تحميل ملفات STL من [`models/parts/`](models/README.md). متوافق مع الطابعات الشعبية مثل **المختبر البامبو A1 ميني**, **بروسا ميني+**، وأي طابعة ذات سرير ≥180 × 180mm.

| الجزء | القيادة | الإعدادات |
|------|:---:|----------|
| الهيكل الرئيسي (RB9.01.062.010) | 1 | 20 في المئة |
| فك التثبيت (RB9.01.062.020) | 2 | 20 في المئة |
| جريدة مسننة (RB9.01.062.030) | 2 | 100% ملء |
| ترس (RB9.01.062.040) | 1 | 100% ملء |
| حامل الكاميرا (RB9.01.060.074) | 1 | 20 في المئة |
| حامل (RB9.01.060.080) | 1 | 20 في المئة |
| مباعد الكاميرا (RB9.01.060.090) | 1 | 20 في المئة |
| D405 حامل (RB9.01.060.110) | 1 | 20 في المئة |

<a id="2-order-components-1-2-days"></a>
### 2. مكونات الطلب (1-2 أيام)

انظروا [وثيقة المواد](docs/bom.md) للاتصالات المباشرة على أمازون.

<a id="3-assemble-30-45-minutes"></a>
### 3. التجميع (30-45 دقيقة)

اتبعوا [دليل الجمعية](docs/assembly-guide.md) مع صور خطوة بخطوة:

1. قم بتثبيت المعدات على قرص الخدمة، قم بتثبيت هذه الجمعية على جهاز الخدمة
2. إدراج كابل الخدمة
3. استخدام Feetech البرنامج تحريك الخادم إلى موقعها الحد الأدنى (تحرك المنزلق في البرنامج إلى اليسار)
4. ثبّت الجرائد المسننة في فكوك التثبيت
5. أدخل قضبان التوجيه في كلا الفكين
6. ركّب المحامل في الهيكل الرئيسي وثبّتها بالبراغي
7. ثبّت قضبان التوجيه في الهيكل بالضغط
8. حرّك الفكين إلى أقصى اليسار وأقصى اليمين
9. ادخل الخادم واصليها بالشواشف
10. ربط الكاميرا spacer وكاميرا UVC ، معالجة مع المسامير 4x والمكسرات M2 (اختياري)
11. الجمع إلى ذراع الروبوت (اختياري)

<a id="4-software"></a>
### 4. البرمجيات

```bash
# Configure servo motor if necessary
https://lab.robonine.com/tools/robonine/feetech-bus

# Control gripper
https://lab.robonine.com/tools/robonine/control-robot
```

---

<a id="-repository-structure"></a>
## ⁇  هيكل المستودع

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
## ⁇  الوثائق

| الوثيقة | وصف |
|----------|-------------|
| [دليل البدء السريع](docs/quick-start.md) | إبدأ بالركض خلال 30 دقيقة |
| [دليل الجمعية](docs/assembly-guide.md) | خطوة بخطوة مع الصور |
| [دليل تجميع اللاصقة (PDF)](../../Assembly%20Guide%20Follower%20Gripper.pdf) | تعليمات تجميع الجهاز المقبض للطباعة |
| [SO-ARM101 دليل التجميع (PDF)](../../Assembly%20Guide%20SO-ARM101.pdf) | كاملة SO-ARM101 تعليمات تجميع الذراع |
| [وثيقة المواد](docs/bom.md) | قائمة الأجزاء مع روابط Amazon |
| [المواصفات](docs/specifications.md) | التفاصيل الفنية |
| [3D النماذج](models/README.md) | طباعة الإعدادات والملفات |
| [تحديد المنتج المتوازي للمقبضات (PDF)](../../Parallel%20gripper%20by%20Robo9.pdf) | مواصفات المنتج المتوازية للقبض بواسطة Robo9 |
| [SO-ARM101 تحديد المنتج (PDF)](../../SO-ARM101%20by%20Robo9.pdf) | SO-ARM101 مواصفات منتج الذراع الروبوتية بواسطة Robo9 |

---

<a id="-hardware-requirements"></a>
## ⁇  متطلبات الأجهزة

<a id="electronics"></a>
### الإلكترونيات
- 1× Feetech STS3215 محرك الخدمة
- 1× لوحة تعديل الحافلة (Waveshare)

<a id="mechanical"></a>
### الميكانيكية
- 2× MF106ZZ حاويات (6 × 10 × 3 مم)
- 2 × ألومنيوم/كربون أنابيب D6x1×125 مم

<a id="fasteners"></a>
### أدوات التثبيت
- 2 × M4 × 8 دين 7991 المسامير
- 4x M2x8 DIN 912 المسامير
- 4× M2 DIN 934 نطاقات
- 4× M3×4 DIN 913 معقب مجموعة

<a id="tools-required"></a>
### الأدوات المطلوبة
- محرك المفات فيليبس الرأس (PH1)
- المفاتيح الماسحة M2 (H1.5) وM4 (H2.5)

---

<a id="-simulation"></a>
## ⁇ ️ محاكاة

يمكن محاكاة SO-ARM101 في 5 محركات فيزيائية باستخدام حزمة وصف ROS2 وملف URDF موحد ذي معاملات. لا يلزم تثبيت ROS2؛ يتولى Docker كل شيء.

<div align="center">

| Gazebo (حصن الإضاءة) | MuJoCo |
|:-:|:-:|
| ![SO-ARM-101 في Gazebo](../../../assets/images/simulation/gazebo/gazebo_pick_place.png) | ![SO-ARM-101 في MuJoCo](../../../assets/images/simulation/mujoco/mujoco_pick_place.png) |

</div>

| محاكاة | الحالة | (دوكر) |
|-----------|--------|--------|
| [Gazebo](simulation/gazebo/README.md) | جاهز | `docker compose run gazebo` |
| [MuJoCo](simulation/mujoco/README.md) | جاهز | `docker compose run mujoco` |
| [Webots](simulation/webots/README.md) | غير مستقرة | `docker compose run webots` |
| [CoppeliaSim](simulation/coppeliasim/README.md) | لم يتم اختباره | محاكاة خارجية |
| [نفيديا Isaac نعم](simulation/isaac_sim/README.md) | لم يتم اختباره | محاكاة خارجية |

**بداية سريعة (Docker):**

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

انظروا [دليل المحاكاة](simulation/README.md) لإعداد كامل، تفاصيل الهندسة المعمارية، والقيادة الروبوتية.

---

<a id="-community-mods"></a>
## ⁇  أدوات المجتمع

تغيرات من المقبض التي بنيتها المجتمع، كل منها مستقل في [`community/`](../../../community):

| الوسائل | المؤلف | وصف |
|-----|--------|-------------|
| [تاريخولوجيا سلايت جريبر](community/histology-slide-gripper/README.md) | [مايكل فياشيسلافوف](https://github.com/histochemichael) | مقبضات لقطرات الميكروسكوب 75 × 25 مليمتر ومرقوقات/شاحنات ملونة، بالإضافة إلى حامل Arducam ذو زاوية لمراقبة الاحتفاظ. |

<div align="center">

<a href="community/histology-slide-gripper/README.md"><img src="../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg" alt="Histology slide gripper mod holding a microscope slide" width="400"></a>

*تاريخولوجيا Slide Gripper mod  ⁇  انقر على الوصف الكامل وملفات CAD و التجربة*

</div>

---

<a id="-contributing"></a>
## ⁇  المساهمة

نرحب بالمساهمات! من فضلك لا تتردد في:
- ⁇  تقرير الأخطاء والقضايا
- ⁇  اقترح ميزات جديدة
- ⁇  إرسال طلبات السحب
- ⁇  تحسين الوثائق

---

<a id="-license"></a>
## ⁇  ترخيص

حقوق الطبع والنشر (ج) 2025 Robonine. هذا المشروع متعدد الترخيصات  ⁇  أنواع مختلفة من
المواد تحمل رخص مختلفة:

| المادة | الترخيص |
|---|---|
| تصميمات الأجهزة  ⁇ `models/`، CAD المجتمعية، الشبكات اللاصقة | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| البرمجيات `software/`, `examples/`, `simulation/`، رمز المحاكاة في `community/` | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| الوثائق والصور `docs/`, `assets/`، جميعها `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

انظروا [`LICENSING.md`](LICENSING.md) للخريطة الدقيقة لكل ملف و
[`REUSE.toml`](../../../REUSE.toml) للنسخة القراءة الآلية.

**ليس كل شيء هنا Robonineالعمل.** (الـ) SO-ARM101 يتم استنباط شبكات الذراع
من [TheRobotStudioمشروع فوق التيار](https://github.com/TheRobotStudio/SO-ARM100)
والبقاء Apache-2.0؛ المساهمة في ضغط المضربات هيستولوجية
[@histochemichael](https://github.com/histochemichael). انظروا [`NOTICE`](../../../NOTICE)
قبل إعادة استخدام أي شبكة.

الإفراجات حتى و بما في ذلك `v0.3.1` تم نشرها بموجب GPL-3.0 ومازال
المتاحة بموجب هذه الشروط  ⁇  انظر [`RELICENSING.md`](RELICENSING.md).

---

<a id="-links"></a>
## ⁇  الروابط

- [Feetech STS3215 الخدمة](https://www.feetechrc.com/525603.html)
- [Waveshare مُعدّل خدمة الحافلة](https://www.waveshare.com/bus-servo-adapter-a.htm)
- [STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python)

---

<a id="-engineering-team"></a>
## ⁇  فريق الهندسة

| الاسم | الدور | الاتصال |
|------|------|---------|
| **بوريس كوتوف** | مهندس البرمجيات | [تلغرام](https://t.me/bkotov) |
| **(آلان سوبين)** | مهندس تصميم | [لينكدين](https://www.linkedin.com/in/alan-subin/) |

---

<div align="center">

**بنيت لمجتمع الروبوتات من قبل [Robonine](https://robonine.com)** 🤖

**أسئلة؟ نحن هنا لمساعدة!**
⁇  البريد الإلكتروني: [مرحباً@robonine.com](mailto:hello@robonine.com)

</div>
<!-- /translated-content -->
