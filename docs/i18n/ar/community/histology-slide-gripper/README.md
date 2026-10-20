<!-- translation-navigation -->
[English](../../../en/community/histology-slide-gripper/README.md) · [Русский](../../../ru/community/histology-slide-gripper/README.md) · [Español](../../../es/community/histology-slide-gripper/README.md) · [Français](../../../fr/community/histology-slide-gripper/README.md) · [Deutsch](../../../de/community/histology-slide-gripper/README.md) · [Português (Brasil)](../../../pt-BR/community/histology-slide-gripper/README.md) · [简体中文](../../../zh-CN/community/histology-slide-gripper/README.md) · [日本語](../../../ja/community/histology-slide-gripper/README.md) · [हिन्दी](../../../hi/community/histology-slide-gripper/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../../../community/histology-slide-gripper/README.md)

[العربية](../../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="histology-slide-gripper-community-mod"></a>
# التشابك السليدي (مود المجتمع)

إختلاف مجتمعي SO-ARM100/101 "المساوية" من خلال [مايكل فياشيسلافوف](https://github.com/histochemichael)، مُعدّل لتحسين التهزيم والتكنولوجيا الهستولوجية: تحميل خفيف لسلايت المجهر القياسي 75 × 25 ملي متر، وسلايتات تلوين السلايت/الرفات، ورؤية كاميرات قريبة من الاعتراض.

<div align="center">

![التجربة المميزة](../../../../../community/histology-slide-gripper/assets/histology-slide-gripper-demo.gif)

*SO-ARM100/101 المقبض المتوازي باستخدام القواصب المخصصة للتعامل مع شرائح الميكروسكوب ومرقصة اللون / رف.*

</div>

<a id="what-changed-vs-the-base-gripper"></a>
## ما الذي تغيّر مقابل المقبض الأساسي

| الإضافة | وصف |
|----------|-------------|
| مقبضات الميكروسكوب | هندسة المقبضات الطويلة والسطحية تدعم التقاط مباشر للوحة المجهرية القياسية 75 × 25 مم. |
| التعامل مع قفازات السلائيد/المغطس | يشارك مسافة المضغوطات والقواص في غسيل اللون على السلائد / الرف مثل غسيل اللون على السلائد Medicus Health المرتبط أدناه. |
| حامل Arducam الزاوية | يستهدف حامل قابل للطباعة كاميرا أردوكام العالمية في فخذ الوقود لمراقبة القريبة من التقاط السلائد والرف. |
| التجميع الكامل CAD | مجموعة كاملة للطباعة STL والتحرير STEP هي في [`cad/`](../../../../../community/histology-slide-gripper/cad). |

<a id="gallery"></a>
## المعرض

<div align="center">

| تحميل شرائح واحدة | التلوين المزق/التقاط الرف | عرض محفظة الأردوكام |
|:-:|:-:|:-:|
| ![ضغط يحمل شرائح الميكروسكوب](../../../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg) | ![المقبض المتوافق مع غطاء لون السلائد](../../../../../community/histology-slide-gripper/assets/slide-gripper-staining-dipper.jpg) | ![حامل آلة التشغيل فوق فخذات المقبض](../../../../../community/histology-slide-gripper/assets/arducam-holder-front.jpg) |

| منظر الأمام | هندسية الخنجر | المجموعة المتوازنة |
|:-:|:-:|:-:|
| <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-front.png" alt="Front CAD view of the microscope slide gripper mod" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-side.png" alt="Angled CAD view showing the microscope slide jaw geometry" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-isometric.png" alt="Isometric CAD view of the full microscope slide gripper assembly" width="250"> |

</div>

<a id="cad-files"></a>
## ملفات CAD

| الملف | تنسيق | الاستخدام |
|------|--------|-----|
| [`cad/the-parallel-microscope-slide-gripper.stl`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.stl) | الـ (STL) | التجميع الكامل للطباعة لمصطلح الجهاز المجهري. |
| [`cad/the-parallel-microscope-slide-gripper.step`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.step) | الخطوة | مصدر CAD قابل للتحرير لجميع الجمعية. |

<a id="add-on-bill-of-materials"></a>
## وثيقة المواد الإضافية

هذه العناصر محددة لسيارة العمل / رف ولا تشكل جزءًا من المقبض الأساسي. [(بوم)](../../docs/bom.md).

| المكون | القيادة | الملاحظات | الرابط |
|-----------|:---:|-------|------|
| كاميرا أردوكام 100fps Mono Global Shutter USB ، OV9281 | 1 | الكاميرا المستخدمة مع حامل الزاوية لمشاهدة التزلج و رف التقاط بالقرب من الفك. | [أمازون المملكة المتحدة](https://www.amazon.co.uk/Arducam-Shutter-Distortion-Computer-Raspberry/dp/B0FXWWF55X) |
| علبة بلاستيكية للوحام | 1+ | الهدف المرجعي للوضوء في الغطس / الرف؛ مصمم للشرائح القياسية 75 × 25 مليمتر. | [صحة المريض](https://www.medicus-health.com/slide-staining-dipper.html) |
| تجميع مقبضات المجهر المتوازي | 1 | الطباعة `the-parallel-microscope-slide-gripper.stl`ملف STEP متضمن للتحرير. | [`cad/`](../../../../../community/histology-slide-gripper/cad) |

<a id="mujoco-simulation"></a>
## MuJoCo المحاكاة

<div align="center">

![SO-ARM101 المقبضات السريعة التشغيل في MuJoCo](../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

*SO-ARM101 مع ضغط الزرقة الهستولوجية مثبت ويتم تشغيله MuJoCo.*

</div>

شخص مستقل MuJoCo النموذج 3.4.0 متاح في [`mujoco/`](mujoco/README.md). وتشمل الكامل SO-ARM101 النموذج، الشبكات المقبضة، مقعد اختبار مستقل للمقبض، بناء السيناريوهات، ومراقبة قبضة ورفع بدون رأس.

من جذور مخزن:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py
```

استخدم `sg_grip` السيطرة في MuJoCo المشاهد لفتح وإغلاق الفك انظروا [محاكاة README](mujoco/README.md) للتفاصيل النموذجية والتحكمات والتحقق من المصادقة وإرشادات إعادة البناء.

<a id="notes"></a>
## الملاحظات

- مصممة أصابع المقبضات للشرائح المصنوعة من الميكروسكوب القياسية 75 × 25 مم والشرائح التي تلوين الغطس / الرف.
- يضع الجمعية وجهة الكاميرا نحو فخذات المقبض حتى تتمكن الكاميرا من مراقبة السلائد والحافظة.
- اختبر أولاً مع شرائح غير حرجة وتحدد مواد الطباعة والملء وقوة الوقود لتدفق العمل الخاص بك.

<a id="links"></a>
## الروابط

- 🎥 [التجربة: تحميل سلائد وملونات (LinkedIn)](https://www.linkedin.com/posts/michael-viacheslavov_histology-histotechnology-robotics-ugcPost-7482570199859240960-Gqpw/)
<!-- /translated-content -->
