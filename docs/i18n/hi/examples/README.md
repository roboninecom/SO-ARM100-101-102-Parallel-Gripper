<!-- translation-navigation -->
[English](../../en/examples/README.md) · [Русский](../../ru/examples/README.md) · [Español](../../es/examples/README.md) · [Français](../../fr/examples/README.md) · [Deutsch](../../de/examples/README.md) · [Português (Brasil)](../../pt-BR/examples/README.md) · [简体中文](../../zh-CN/examples/README.md) · [日本語](../../ja/examples/README.md) · [हिन्दी](README.md) · [العربية](../../ar/examples/README.md)

[अंग्रेज़ी मूल](../../../../examples/README.md)

[हिन्दी](../README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="examples---parallel-gripper"></a>
# उदाहरण - समानांतर पकड़

इस निर्देशिका में उदाहरण कोड है जो विभिन्न परिदृश्यों में समानांतर पकड़ का उपयोग कैसे किया जाए, इसका प्रदर्शन करता है।

<a id="available-examples"></a>
## उपलब्ध उदाहरण

<a id="basic_usagepy"></a>
### `basic_usage.py`
ग्रिप के बुनियादी संचालन का प्रदर्शन करता हैः
- ग्रिपर से कनेक्ट करना
- विशिष्ट पदों पर स्थानांतरण
- पढ़ने की स्थिति की जानकारी
- मूल त्रुटि प्रसंस्करण

**उपयोगः**
```bash
cd examples
python basic_usage.py
```

<a id="configuration"></a>
## विन्यास

मौजूदा के माध्यम से पकड़ कनेक्ट करें SO-ARM100/101 सर्वो बस और नियंत्रक।
नियंत्रक का उपयोग करें यूएसबी सीरियल पोर्ट, सेट `STS_ID` पकाने वाले इमदादी आईडी (आमतौर पर 6 पर) SO-ARM101),
और उस बंदरगाह का उपयोग करके अन्य अनुप्रयोगों को बंद करें।

उदाहरण चलाने से पहले, आपको कॉन्फ़िगरेशन पैरामीटर समायोजित करने की आवश्यकता हो सकती हैः

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

<a id="common-issues"></a>
## आम मुद्दे

<a id="connection-problems"></a>
### कनेक्टिविटी समस्याएँ
- **खिड़कियाँ**: सही COM पोर्ट के लिए डिवाइस प्रबंधक की जाँच करें
- **लिनक्स**: यह सुनिश्चित करना कि उपयोगकर्ता को सीरियल पोर्ट तक पहुंच हो (`sudo usermod -a -G dialout $USER`)
- **macOS**उपयोगः `/dev/cu.usbserial-*` या `/dev/tty.usbserial-*`

<a id="permission-errors"></a>
### अनुमति त्रुटियां
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

<a id="stservo-sdk-issues"></a>
### STServo एसडीके मुद्दे
सुनिश्चित करें कि STServo SDK ठीक से स्थापित हैः
1. क्लोन [Feetech STServo Python एसडीके](https://github.com/FEETECH-RC/STServo_SDK_Python).
2. प्रतिलिपि `STservo_sdk` फ़ोल्डर (फ़ोल्डर के साथ) को `software/python/` निर्देशिका।

<a id="creating-your-own-examples"></a>
## अपना खुद का उदाहरण बनाएं

नए उदाहरण बनाते समयः

1. **पकड़ मॉड्यूल आयात करें**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **त्रुटियों को भव्यता से संभालें**
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

3. **उचित दस्तावेज शामिल करें**
   - उदाहरण का स्पष्ट वर्णन
   - आवश्यक हार्डवेयर सेटअप
   - अपेक्षित व्यवहार

<a id="safety-notes"></a>
## सुरक्षा नोट्स

⚠️ **महत्वपूर्ण सुरक्षा विचार:**
- हमेशा तापमान और वर्तमान की निगरानी करें
- त्रुटियों का उचित प्रबंधन करें
- कम बल के साथ परीक्षण पहले
- उचित यांत्रिक व्यवस्था सुनिश्चित करें
- चलती भागों से अपनी उंगलियों को दूर रखें

<a id="contributing-examples"></a>
## योगदान देने वाले उदाहरण

हम नए उदाहरणों का स्वागत करते हैं! कृपया:
- मौजूदा कोड शैली का पालन करें
- व्यापक टिप्पणियाँ शामिल करें
- प्रस्तुत करने से पहले सावधानीपूर्वक परीक्षण करें
- इस README में प्रविष्टि जोड़ें

---

**खुश कोडिंग!** 🤖
<!-- /translated-content -->
