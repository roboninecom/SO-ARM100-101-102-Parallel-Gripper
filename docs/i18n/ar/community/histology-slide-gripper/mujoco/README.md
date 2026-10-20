<!-- translation-navigation -->
[English](../../../../en/community/histology-slide-gripper/mujoco/README.md) · [Русский](../../../../ru/community/histology-slide-gripper/mujoco/README.md) · [Español](../../../../es/community/histology-slide-gripper/mujoco/README.md) · [Français](../../../../fr/community/histology-slide-gripper/mujoco/README.md) · [Deutsch](../../../../de/community/histology-slide-gripper/mujoco/README.md) · [Português (Brasil)](../../../../pt-BR/community/histology-slide-gripper/mujoco/README.md) · [简体中文](../../../../zh-CN/community/histology-slide-gripper/mujoco/README.md) · [日本語](../../../../ja/community/histology-slide-gripper/mujoco/README.md) · [हिन्दी](../../../../hi/community/histology-slide-gripper/mujoco/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../../../../community/histology-slide-gripper/mujoco/README.md)

[العربية](../../../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="microscope-slide-gripper-in-mujoco"></a>
# ميكروسكوب سلايد جريبر في MuJoCo

(الـ) SO-ARM101 مع الوقود الموازي للزفافات الهستولوجية ، المصدر من Fusion ووضع في مكان المقاعد Robo9 clamps.

تم اختبارها `mujoco` 3.4.0 في `lerobot` البيئة لا , لا ROS 2 أو مطلوب Docker.

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py                      # full arm + slide gripper
python view.py scene_gripper.xml    # gripper alone on a testbench
python test_grasp.py                # headless grasp-and-lift check -> grasp_check.png
```

<a id="mujoco-simulation-preview"></a>
## MuJoCo عرض مقدم للمحاكاة

![SO-ARM101 المقبضات السريعة التشغيل في MuJoCo](../../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

هذا المشهد يظهر SO-ARM101 مع ضغط متوازي للانزلاق الهستولوجي مثبت على
معصم اليد، باستخدام نفس MuJoCo النموذج الذي أطلقه:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python view.py
```

<a id="what-is-modelled"></a>
## ما هو النموذج

| الرابط | المصدر | الجماهير |
|---|---|---|
| `slide_gripper_base` | الهيكل الرئيسي, STS3215، قضبان الدليل، طلاء، حامل الكاميرا، Arducam OV9281 | 0.20 كجم |
| `sg_jaw_right` / `sg_jaw_left` | RB9.01.062.020 صمام + RB9.01.062.030 الرف (m0.8) | 0.035 كجم لكل |
| `sg_pinion` | RB9.01.062.040 التجهيزات غير المتحركة، 18 T، 0.8 الوحدة | 0.008 كجم |

السرعة التي تم أخذها من المفاصل المكونة في تجميع Fusion
(`Slide_Jaw_Right`, `Slide_Jaw_Left`, `Drive_Pinion`), والتي تكون متسقة:
يمتلك محرك 18 T / 0.8 قطر مساحة 7.2 مم، و7.2 مم x 4.9306 rad =
**35.5 ملم** من رحلة رف لكل فخذ  ⁇  بالضبط الحدود السريعة في CAD.

<a id="control"></a>
## التحكم

محرك واحد `sg_grip`، أُمرت في **أمتار سفر الفك**:

| `ctrl` | سفر الفك | فتحة بين وجوه السكين |
|---|---|---|
| `0.0` | 0 ملم | **84 ملم** (مفتوح تماما) |
| `0.0295` | 29.5 ملم | 25 مليمتر (سلائد مجهري) |
| `0.0355` | 35.5 ملم | **13 مم** (غلق بالكامل) |

كلتا الفكاهين مدفوعة من المنعطف الواحد، لذلك `sg_jaw_left_joint` و
`sg_pinion_joint` يتم استيعابهم `sg_jaw_right_joint` بواسطة `<equality>` القيود
يدور الجهاز بشكل مرئي مع الفك. القيادة *الماضي* الكائن الذي سيتم ضغطه:
إغلاق على كائن من 25 مليمتر مع `ctrl=0.0355` يعطي حوالي 4.7 N في الأقمشة.

يحتفظ المفاصل الخمسة بأسمها URDF (`base_link_to_link1` ... `link4_to_link5`).

<a id="collision-geometry"></a>
## هندسة التصادم

الجيمات الشبكة هي **بصرية فقط** (`contype=0`), لأن MuJoCo الجهاز:
هيكل الفك الحجري يملأ الفجوة التي تحاول أن تمسك بها الاتصال هو
يتم حملها بواسطة صناديق على سطحي المقبضين لكل ففة (مجموعة3، مخبأة في
التعبيرات):

- `sg_pad_*` ⁇  شفرة سلائد 30 ملم، CAD x 42 ⁇ 50، z 26 ⁇ 31
- `sg_mid_*` ⁇  القطاع الوسط الأوسع، CAD x 42 ⁇ 58, z 18.5 ⁇ 38.5

موقع TCP `sg_tcp` يجلس بين الشفرات `sg_camera` هو الإطار البصري Arducam.

<a id="files"></a>
## الملفات

- `so101_slide_gripper.xml` ⁇  الروبوت الكامل `build_full.py`)
- `scene_gripper.xml` ⁇  مقبض وحده، مع محور رفع للتجربة
- `gripper_assets.xml` / `gripper_body.xml` / `gripper_actuation.xml` ⁇  المقبض ،
  كما يشمل قابلة للاستخدام من كلا النماذج وحدة درجة وحدة راديان
- `meshes/{base,jaw_right,jaw_left,pinion}.stl` ⁇  صادرات من Fusion في **التجميع
  الإحداثيات**، لذا كل جزء في مكانه الصحيح (لا أصل لكل جزء للاحتفال)
- `meshes/arm/` ⁇  شبكات الذراع من Robo9 repo
- `build_arm.py` ⁇  الشريطات من xacro `so_101.urdf.xacro`، يُسقط قوائم الأسهم، ويتجمّع إلى MJCF
- `build_full.py` ⁇  يزرع المقبض على `link5`; **تحرير `MOUNT_POS`/`MOUNT_QUAT` هنا**

<a id="how-the-gripper-was-located-on-the-wrist"></a>
## كيف تم تحديد المقبض على المعصم

`link5_1.stl` في ريبو روبو9 ليس فقط المعصم
المقبض (الهيكل، العصا التوجيهية، الكاميرا). لذلك هو الجزء الذي يبدله تصميم المقبضات،
`build_full.py` يزيل شبكتها ويقلل كتلتها من 0.556 كجم إلى 0.08 كغ.

تم حل وضع الجبل، وليس تخمين: `base.stl` تم تركيبها ضد
`link5_1.stl` على الهندسة التي يتشاركونها (الإطار الرئيسي + العصا التوجيه) عن طريق البحث في جميع
24 دورة على المحور وتسجيل المسافة القريبة من الجيران. أفضل تناسب هو
**+90 درجة حول X** (CAD + Y -> link5 + Z، CAD + Z -> link5 - Y) مع متوسط 2.0 mm
بقية  ⁇  العقبات المنزلية معلقة عمودياً على العقبات الحادة لـ Robo9 ، مماثلة
تجميع الاندماج

<a id="stability"></a>
## الاستقرار

النموذج يستقر على `max|qvel| = 0` و يبقى هناك إذا رأيته يرتعش
أول شيء يجب التحقق منه هو الاتصالات الضائعة (`ncon` في لوحة المعلومات للمشاهد يجب أن يكون 0
مع الذراع في الراحة). ثلاثة أشياء كانت ضرورية:

1. **`<exclude body1="world" body2="link1_1"/>`** -الحل الحقيقي المستورد من URDF
   الاندماج `base_link` في `worldbody`و MuJoCo تفوت الصدامات بين الوالدين والطفل
   *ما عدا* عندما يكون الوالد هو الجسم العالمي. إذاً الشبكة الأساسية والشبكة الرابطة1
   يختلط في الكتف ، مما ينتج عن اتصال دائم الذي يضبط الصخرة
   المحرك عند حد +-1.5 N.m هذا وحده أخذ تسوية `|qvel|` من 4.78 إلى 0.
2. `sg_pinion_joint` المعدات 1e-6 -> **1e-4**. المشترك الذي يخضع لمساواة صلبة مع
   تقريباً لا توجد ترددات (كانت تصل إلى ذروتها في 12 راد/س)
3. المساواة `solref` 0.002 -> **0.01**. مستمرة الزمن القييد مساوية لخطوة الوقت
   هو صلب جدا لتحل نظيفا؛ وهذا أيضا جعلت الجهاز الهبوط بالضبط على -282.5 درجة مئوية
   بدلاً من -280 درجة مئوية

<a id="caveats"></a>
## الكهوف

- **تفترض الكتلة، لا تقاس.** التآكل يبلغ عن كل جسم كصلب (الفك
  يتم إصدار 221 غرام لكل منها) ، والقيم أعلاه هي تقديرات لـ PLA و Hardware. إذا كنت
  تعيين المواد الحقيقية في Fusion، تحديث `mass=` الصفات في `gripper_body.xml`.
- النخاطية مشتقة من: MuJoCo من شكل الشبكة بالإضافة إلى تلك الكتلة، وليس من تنسور Fusion.
- الحدود المفصلة للذراع، التخفيف والاحتكاك هي الوراثة من URDF
  لم يتم إعادة ضبطها.
- **كتلة الرابط في الذراع كثافة الفولاذ أيضا**، نفس العيب الذي يعاني منه المقبض:
  إجمالي الـ URDF **2.81 كجم** مقابل حوالي 1 كيلوغرام لـ SO-101 الحقيقي، و `link2_to_link3`
  يحتاج إلى 1.91 N.m لتحمل نفسها ضد 1.5 N.m الحد المحرك، لذلك فإنه ينخفض. هذا هو
  لا يسبب الارتعاش (انظر أعلاه) ولكنه يجعل الذراع تتصرف مثل ثقيلة بكثير
  آلة. قياس كل كتلة ربط الذراع و `diaginertia` بـ 0.36 يصل إجمالي
  1.19 كجم وتكفّر من التشبع. STS3215 أيضاً أقرب 2.9 N.m من
  إنّ الرقم المحافظ لـ (الـ URDF) هو 1.5.
- بقية التوجه 2 مليمتر هي حقيقية: "المتابع الرئيسي_125 الإطار" ليس متطابق
  إلى الإطار المخبوز `link5_1.stl`.
- `sg_pinion_joint` هو التجميل - فإنه لا يحمل أي حمولة، لأن الرفين متصلان
  إلى بعضهم البعض مباشرة إنها موجودة حتى تتحول العجلة في الاتجاه الصحيح على الشاشة.

<a id="driving-it-in-the-mujoco-viewer"></a>
## القيادة في MuJoCo المشاهد

استخدم **`sg_grip` المنزلق في لوحة التحكم**. السلايدات في *المشترك* اللوحة
كتابة `qpos` بشكل مباشر وتحايل على قيود المساواة، وبالتالي سحب تلك (خاصة
أثناء التوقف) يخلل من المزاد من الفكية. الضغط على "الركض" يعيد تحويلها.

<a id="re-exporting-after-a-cad-change"></a>
## إعادة التصدير بعد تغيير في CAD

تم تصديرها من خلال الاتصال Fusion MCP: فإنه يمر كل حدث، مجموعات
الأجسام في الربعة الروابط الصلبة، ويكتب STL الثنائية في إحداثيات الجمع
(م) إعادة الصادرة مع تصميم Fusion مفتوح لتجديد الشبكات في
لا شيء آخر يحتاج إلى تغيير ما لم تتحرك المشترك.
<!-- /translated-content -->
