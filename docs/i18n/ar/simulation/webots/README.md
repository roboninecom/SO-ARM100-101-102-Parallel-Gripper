<!-- translation-navigation -->
[English](../../../en/simulation/webots/README.md) · [Русский](../../../ru/simulation/webots/README.md) · [Español](../../../es/simulation/webots/README.md) · [Français](../../../fr/simulation/webots/README.md) · [Deutsch](../../../de/simulation/webots/README.md) · [Português (Brasil)](../../../pt-BR/simulation/webots/README.md) · [简体中文](../../../zh-CN/simulation/webots/README.md) · [日本語](../../../ja/simulation/webots/README.md) · [हिन्दी](../../../hi/simulation/webots/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../../../simulation/webots/README.md)

[العربية](../../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="webots"></a>
# Webots

> **الحالة: غير مستقرة** -- Webots العمل التكامل ولكن لديه مشاكل معروفة في الأداء والتصوير. يوصى بإستخدام المرفق فقط.

Webots المحاكاة باستخدام `webots_ros2_control`. (الـ) Webots السائق يدمج مدير التحكم.

<a id="prerequisites"></a>
## الشروط المسبقة

**Docker (موصى به):**
- أداة المكتب

**الأصلي ROS2:**
- ROS2 التواضع
- [Webots](https://cyberbotics.com/) R2023b+
- `ros-humble-webots-ros2`
- `urdf2webots` حزمة النفط

<a id="launch"></a>
## إطلاق

<a id="docker"></a>
### (دوكر)

```bash
cd simulation/so_arm_101_description
docker compose run webots
```

> **ملاحظة**: Webots خدمة المرفأ لا تملك مقياس حجم. يتم إنشاء ملف العالم داخل الصورة في وقت بناءها. إذا قمت بتعديل URDF، يجب عليك إعادة بناء: `docker compose build webots`.

<a id="native-ros2"></a>
### الأصلي ROS2

```bash
pip install urdf2webots

# Generate the Webots world file
python scripts/setup_webots.py

# Generate pre-expanded URDF for the Webots driver
xacro urdf/so_101.urdf.xacro sim_backend:=webots > urdf/so_101_webots.urdf

# Launch
ros2 launch so_arm_101_description sim.launch.py sim:=webots
```

<a id="how-it-works"></a>
## كيف يعمل

1. `scripts/setup_webots.py` تحويل URDF إلى Webots عقدة الروبوت عبر `urdf2webots` وتوليد `worlds/webots_sim.wbt`
2. (الـ) `WebotsLauncher` يفتح ملف العالم في Webots
3. `WebotsController` يربط بالروبوت عن طريق IPC ويبدأ `ros2_control` السائق
4. جهاز التحكم `<extern>` علامة في الملف العالم يسمح `webots_ros2_driver` ليتولى الأمر
5. (توسع مسبقًا لـ URDF)`so_101_webots.urdf`) ضروري لأن `WebotsController` يتطلب مسار الملف ، وليس XML داخل الخط

<a id="world-settings"></a>
### الإعدادات العالمية

- `basicTimeStep`: 16ms (تقلل من الافتراض لمستقر الفيزياء)
- `maxContactJoints`: 4 (تحد من تكاليف التصادم العلوي من الشبكات المفصلة)

<a id="known-issues"></a>
## القضايا المعروفة

- **التحميل العالمي البطيء فوق X11**: يستغرق العالم ~ 120s لتحميل عندما يتم إرسال التصوير عبر X11. ويعد الوقت المطلوب لـ "السيطرة" إلى 180 ثانية لتلبية هذا.
- **إعادة تشكيل الإطارات على Windows**: VcXsrv يقدم فقط OpenGL 1.4 ، ولكن Webots يتطلب OpenGL 3.3 المحاكاة تعمل ولكن يعطي في وضع الإطار السلكي.
- **الكشف عن WSL2**: Docker على WSL2 يرث اسم نواة WSL، مما يسبب `webots_ros2_driver` للبحث عن `webots.exe`. ملفات الدوكر `is_wsl()` أن أعود دائماً `False`.
- **تحذيرات الفيزياء**: قد تظهر تحذيرات "قد يكون عالمك معقدًا جدًا" بسبب شبكات اصطدام عالية الكليات.

<a id="troubleshooting"></a>
## حل المشاكل

- **`WEBOTS_HOME` لم يجد**: التأكد `WEBOTS_HOME=/usr/local/webots` لقد تم تحديدها صورة (دوكر) تعيين هذا تلقائياً
- **توقيت المراقب**: إذا فشل التحكم في تنشيطها، قم بزيادة فترة الإنتظار `launch/sim.launch.py` (في الوقت الحالي 180s).
- **لا يوجد عرض**: Webots احتاج X11. على Windows، استخدم VcXsrv مع `-ac -wgl` العلامات
<!-- /translated-content -->
