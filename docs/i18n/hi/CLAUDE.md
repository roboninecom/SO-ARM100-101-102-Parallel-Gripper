<!-- translation-navigation -->
[English](../en/CLAUDE.md) · [Русский](../ru/CLAUDE.md) · [Español](../es/CLAUDE.md) · [Français](../fr/CLAUDE.md) · [Deutsch](../de/CLAUDE.md) · [Português (Brasil)](../pt-BR/CLAUDE.md) · [简体中文](../zh-CN/CLAUDE.md) · [日本語](../ja/CLAUDE.md) · [हिन्दी](CLAUDE.md) · [العربية](../ar/CLAUDE.md)

[अंग्रेज़ी मूल](../../../CLAUDE.md)

[हिन्दी](README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="claudemd"></a>
# CLAUDE.md

इस फ़ाइल में इस रिपॉजिटरी में कोड के साथ काम करते समय क्लाउड कोड (claude.ai/code) को मार्गदर्शन प्रदान किया गया है।

<a id="what-this-repository-is"></a>
## यह भंडार क्या है

एक ओपन-सोर्स हार्डवेयर परियोजनाः 3 डी मुद्रित समानांतर पकड़ के लिए SO-ARM100/101 रोबोट हाथ द्वारा Robonine). मल्टी-लाइसेन्स: CERN-OHL-P-2.0 हार्डवेयर/CAD के लिए, Apache-2.0 सॉफ्टवेयर के लिए, CC BY 4.0 डॉक्स के लिए  ⁇  नक्शा में है `LICENSING.md`, मशीन-पठनीय संस्करण में `REUSE.toml`, तीसरे पक्ष के लिए श्रेय `NOTICE`. नई फ़ाइलों को कवर किया जाना चाहिए `REUSE.toml`; `reuse lint` पूर्व-कमिट में चलाता है। अधिकांश रेपो CAD मॉडल हैं (`models/`), प्रलेखन (`docs/`), और छवियों (`assets/`). कोड दो स्थानों पर रहता हैः

- `software/python/gripper_control.py` ⁇  स्टैंडअलोन सर्वो नियंत्रण स्क्रिप्ट Feetech STS3215 (उपक्रम पर निर्भर करता है) STServo SDK, जिसे मैन्युअल रूप से क्लोन किया जाता है  ⁇  देखें `software/python/requirements.txt`; यह PyPI पर नहीं है) । `examples/basic_usage.py` एक `sys.path` हैक.
- `simulation/so_arm_101_description/` — a ROS2 5 भौतिकी इंजनों में आर्म + ग्रिपर का अनुकरण करने वाला (नम्र) विवरण पैकेज। यह है जहां सभी परीक्षण और अधिकांश आईसी रहते हैं.

<a id="commands"></a>
## आदेश

```bash
# Lint (what CI runs; hooks exclude STL/STEP files)
pre-commit run --all-files

# Offline tests (65 pytest tests; deps: pytest trimesh numpy mujoco pyyaml)
cd simulation/so_arm_101_description
python -m pytest test/ -v

# Single test file / single test
python -m pytest test/test_urdf_structure.py -v
python -m pytest test/test_config.py -k <name> -v

# Validate xacro/URDF XML without ROS2
python simulation/so_arm_101_description/scripts/validate_xml.py simulation/so_arm_101_description/urdf/*.xacro

# Docker (from simulation/so_arm_101_description/; no ROS2 install needed)
docker compose run test          # run pytest suite
docker compose run validate      # xacro + check_urdf for all 5 backends
docker compose run check-launch  # verify launch files parse
docker compose run gazebo        # or: mujoco, webots, rviz (need X11)
```

आईसी (`.github/workflows/ci.yaml`) रनः पूर्व प्रतिबद्धता, XML/YAML सत्यापन, `xacro ... sim_backend:=<backend> | check_urdf` एक के भीतर सभी 5 बैकेंड के लिए `ros:humble` कंटेनर, और पिटेस्ट सूट. एक URDF परिवर्तन के लिए वैध रहना चाहिए **सभी** बैकेंड्स, न केवल वह जो आप लक्षित कर रहे हैं।

<a id="simulation-architecture"></a>
## सिमुलेशन वास्तुकला

एक पैरामीटर रोबोट विवरण प्रत्येक सिम्युलेटर चलाता हैः

- `urdf/so_101.urdf.xacro` सत्य का एकमात्र स्रोत है। एक्सैक्रो आरजी `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` चुनता है `ros2_control` प्लगइन (मार्फत `urdf/so_101.ros2_control.xacro`) विस्तार के समय।
- `config/controllers.yaml` सभी बैकेंड के लिए समान जोड़ों/नियंत्रकों को परिभाषित करता है; `launch/sim.launch.py` के साथ `sim:=<backend>` एक ही प्रवेश बिंदु है।
- रोबोटः 5-डीओएफ हाथ + पकड़ के साथ 2 प्रिस्मेटिक क्लैंप जोड़ों, जहां बाएं क्लैंप दाईं ओर प्रतिबिंबित करता है `<mimic>`.
- मेषों को विभाजित किया जाता हैः `meshes/visual/` (उच्च पोली) बनाम `meshes/collision/` (कंकल पतवारों, पुनरुत्थान के साथ `scripts/generate_collision_meshes.py`).

जोड़ों, लिंक या नियंत्रक नाम में परिवर्तन के लिए सामान्य रूप से xacro फ़ाइलों पर समन्वयित संपादन की आवश्यकता होती है, `controllers.yaml`, और परीक्षणों में `test/`.

<a id="cad-models-and-part-numbering"></a>
## सीएडी मॉडल और भाग अंकन

भागों में `models/parts/` उपयोग Robonine भाग संख्याएँ (जैसे `RB9.01.062.010 Main frame.STL`). इन संख्याओं का सारांश `README.md` (प्रिंट टेबल), `docs/bom.md`और `docs/assembly-guide.md` ⁇  किसी भाग को जोड़ने या नाम बदलने से उन दस्तावेजों को भी अद्यतन करना होता है। एसटीएल बाइनरी हैं; वैरिएंट फाइलनाम में फिट टॉलरेंस को एन्कोड करते हैं (जैसे `RB9.01.062.021 (D6.1) Clamp.STL` विभिन्न छड़ व्यास के लिए) । पूर्व-प्रतिबंध हुक (सफ़ेद स्थान, ईओएफ, लाइन अंत) जानबूझकर बाहर करना `.stl/.STL/.STEP` फ़ाइलें, और 1 एमबी से अधिक फ़ाइलों को अस्वीकार कर रहे हैं `check-added-large-files`.

<a id="conventions"></a>
## अधिवेशन

- Python: flake8 के साथ `--max-line-length=100`, काले प्रोफ़ाइल के साथ क्रमबद्ध (पूर्व-प्रतिबंध द्वारा लागू; `software/` और `examples/` फ्लेक से बाहर हैं8) ।
- दस्तावेजों को डिजाइन द्वारा दोहराया जाता है (README सारांशित करता है bom.md, specifications.md, assembly-guide.md)  ⁇  विनिर्देशों, भागों या कीमतों में बदलाव करते समय उन्हें स्थिर रखें।
- एक जोड़ना नहीं `Co-Authored-By: Claude` प्रतिबद्धता के लिए लाइन।
<!-- /translated-content -->
