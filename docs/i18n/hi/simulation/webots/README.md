<!-- translation-navigation -->
[English](../../../en/simulation/webots/README.md) · [Русский](../../../ru/simulation/webots/README.md) · [Español](../../../es/simulation/webots/README.md) · [Français](../../../fr/simulation/webots/README.md) · [Deutsch](../../../de/simulation/webots/README.md) · [Português (Brasil)](../../../pt-BR/simulation/webots/README.md) · [简体中文](../../../zh-CN/simulation/webots/README.md) · [日本語](../../../ja/simulation/webots/README.md) · [हिन्दी](README.md) · [العربية](../../../ar/simulation/webots/README.md)

[अंग्रेज़ी मूल](../../../../../simulation/webots/README.md)

[हिन्दी](../../README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="webots"></a>
# Webots

> **स्थितिः अस्थिर** -- Webots एकीकरण कार्य करता है लेकिन प्रदर्शन और रेंडरिंग के मुद्दों को जानता है। केवल डॉकर का उपयोग करने की सिफारिश की जाती है।

Webots प्रयोग करके सिमुलेशन `webots_ros2_control`. इनका Webots ड्राइवर नियंत्रक प्रबंधक एम्बेड करता है।

<a id="prerequisites"></a>
## पूर्व शर्तें

**डॉकर (अनुशंसित):**
- डॉकर डेस्कटॉप

**स्वदेशी ROS2:**
- ROS2 विनम्र
- [Webots](https://cyberbotics.com/) R2023b+
- `ros-humble-webots-ros2`
- `urdf2webots` पाइप पैकेज

<a id="launch"></a>
## लॉन्च

<a id="docker"></a>
### डॉकर

```bash
cd simulation/so_arm_101_description
docker compose run webots
```

> **नोट**: Webots डॉकर सेवा में कोई वॉल्यूम माउंट नहीं है। विश्व फ़ाइल निर्माण के समय छवि के अंदर उत्पन्न की जाती है। यदि आप URDF को संशोधित करते हैं, तो आपको पुनर्निर्माण करना होगाः `docker compose build webots`.

<a id="native-ros2"></a>
### स्वदेशी ROS2

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
## यह कैसे काम करता है

1. `scripts/setup_webots.py` URDF को एक Webots रोबोट नोड `urdf2webots` और उत्पन्न करता है `worlds/webots_sim.wbt`
2. इनका `WebotsLauncher` दुनिया फ़ाइल में खोलता है Webots
3. `WebotsController` आईपीसी के माध्यम से रोबोट से जुड़ता है और शुरू करता है `ros2_control` चालक
4. नियंत्रक `<extern>` दुनिया फ़ाइल में टैग अनुमति देता है `webots_ros2_driver` कार्यभार संभालने के लिए
5. एक पूर्व विस्तारित URDF (`so_101_webots.urdf`) की आवश्यकता है क्योंकि `WebotsController` फ़ाइल पथ की आवश्यकता होती है, इनलाइन XML नहीं

<a id="world-settings"></a>
### दुनिया की सेटिंग्स

- `basicTimeStep`: 16ms (भौतिक स्थिरता के लिए डिफ़ॉल्ट से घटाया गया)
- `maxContactJoints`: 4 (विस्तृत जाल से टकराव ओवरहेड को सीमित करता है)

<a id="known-issues"></a>
## ज्ञात मुद्दे

- **X11 पर धीमी दुनिया लोडिंग**: दुनिया लोड करने के लिए ~ 120s लेता है जब X11 के माध्यम से रेंडरिंग अग्रेषित किया जाता है। नियंत्रक spawner समय सीमा 180s यह समायोजित करने के लिए सेट किया गया है।
- **विंडोज पर वायरफ़्रेम रेंडरिंग**: VcXsrv केवल OpenGL 1.4 प्रदान करता है, लेकिन Webots OpenGL 3.3 की आवश्यकता होती है। सिमुलेशन चलाता है लेकिन वायरफ्रेम मोड में प्रस्तुत करता है।
- **WSL2 का पता लगाना**: WSL2 पर डॉकर WSL कर्नेल नाम विरासत में मिलता है, जिससे `webots_ros2_driver` खोजना `webots.exe`. डॉकरफ़ाइल पैच `is_wsl()` हमेशा लौटने के लिए `False`.
- **भौतिकी चेतावनी**: "आपकी दुनिया बहुत जटिल हो सकती है" चेतावनी उच्च-पोली टकराव जाल के कारण दिखाई दे सकती है।

<a id="troubleshooting"></a>
## समस्या निवारण

- **`WEBOTS_HOME` नहीं मिला**सुनिश्चित करनाः `WEBOTS_HOME=/usr/local/webots` सेट है। डॉकर छवि यह स्वचालित रूप से सेट करता है।
- **नियंत्रक समय**: यदि नियंत्रक सक्रिय करने में विफल रहते हैं, तो टाइमआउट को बढ़ाएं `launch/sim.launch.py` (वर्तमान में 180s).
- **कोई प्रदर्शन नहीं**: Webots X11 की जरूरत है। विंडोज पर, VcXsrv का उपयोग करें `-ac -wgl` ध्वज।
<!-- /translated-content -->
