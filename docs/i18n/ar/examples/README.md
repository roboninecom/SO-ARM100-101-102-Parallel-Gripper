<!-- translation-navigation -->
[English](../../en/examples/README.md) · [Русский](../../ru/examples/README.md) · [Español](../../es/examples/README.md) · [Français](../../fr/examples/README.md) · [Deutsch](../../de/examples/README.md) · [Português (Brasil)](../../pt-BR/examples/README.md) · [简体中文](../../zh-CN/examples/README.md) · [日本語](../../ja/examples/README.md) · [हिन्दी](../../hi/examples/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../../examples/README.md)

[العربية](../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="examples---parallel-gripper"></a>
# الأمثلة - المقبض المتوازي

يحتوي هذا الإداري على رمز مثالي يوضح كيفية استخدام الوقود الموازي في مختلف الحالات.

<a id="available-examples"></a>
## الأمثلة المتاحة

<a id="basic_usagepy"></a>
### `basic_usage.py`
يظهر عمليات الوقوف الأساسية:
- الاتصال بالقبض
- الانتقال إلى مواقف محددة
- معلومات حالة القراءة
- التعامل مع الأخطاء الأساسية

**استخدام:**
```bash
cd examples
python basic_usage.py
```

<a id="configuration"></a>
## الإعداد

قبل تشغيل الأمثلة، قد تحتاج إلى تعديل معايير التكوين:

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

<a id="common-issues"></a>
## القضايا الشائعة

<a id="connection-problems"></a>
### مشاكل الاتصال
- **النوافذ**: تحقق من إدارة الجهاز لمواجهة COM الصحيحة
- **لينكس**: ضمان وصول المستخدم إلى البوابات المتسلسلة`sudo usermod -a -G dialout $USER`)
- **macOS**استخدام: `/dev/cu.usbserial-*` أو `/dev/tty.usbserial-*`

<a id="permission-errors"></a>
### أخطاء الإذن
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

<a id="stservo-sdk-issues"></a>
### STServo قضايا SDK
تأكد من STServo يتم تركيب SDK بشكل صحيح:
1. تحميل من: [STServo Python SDK](https://files.waveshare.com/wiki/Bus-Servo-Adapter-(A)/STServo_Python.zip)
2. استخراج ملف ZIP المنزول ونسخ `STservo_sdk` المجلد (مع المجلد نفسه) إلى `software/python/` الإداري

<a id="creating-your-own-examples"></a>
## إنشاء مثالاتك الخاصة

عند إنشاء أمثلة جديدة:

1. **استيراد وحدات الوقوف**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **التعامل مع الأخطاء بجد**
   ```python
   try:
       gripper = ParallelGripper()
       if not gripper.connect():
           print("Connection failed!")
           return
       # Your code here
   finally:
       gripper.disconnect()
   ```

3. **إضافة وثائق مناسبة**
   - وصف واضح لما يفعله المثال
   - إعدادات الأجهزة المطلوبة
   - السلوك المتوقع

<a id="safety-notes"></a>
## ملاحظات السلامة

⚠️ **الاعتبارات المهمة للسلامة:**
- دائماً مراقبة درجة الحرارة والسحب الزمني
- تنفيذ معالجة الأخطاء بشكل صحيح
- اختبار بقوى منخفضة أولاً
- تأمين الإعداد الميكانيكي المناسب
- أبق أصابعك بعيدة عن الأجزاء المتحركة

<a id="contributing-examples"></a>
## أمثلة مساهمة

نحن نرحب بأمثلة جديدة! من فضلكم
- اتبع أسلوب الرمز الحالي
- إضافة تعليقات شاملة
- الاختبار الدقيق قبل التقديم
- إضافة الإدخال إلى هذا README

---

**-تعافى عن التشفير** 🤖
<!-- /translated-content -->
