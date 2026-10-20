<!-- translation-navigation -->
[English](README.md) · [Русский](../../ru/examples/README.md) · [Español](../../es/examples/README.md) · [Français](../../fr/examples/README.md) · [Deutsch](../../de/examples/README.md) · [Português (Brasil)](../../pt-BR/examples/README.md) · [简体中文](../../zh-CN/examples/README.md) · [日本語](../../ja/examples/README.md) · [हिन्दी](../../hi/examples/README.md) · [العربية](../../ar/examples/README.md)

[English source](../../../../examples/README.md)

[English](../README.md)

> Complete English source copy. Images, code, CAD, and original PDFs are shared.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="examples---parallel-gripper"></a>
# Examples - Parallel Gripper

This directory contains example code demonstrating how to use the parallel gripper in various scenarios.

<a id="available-examples"></a>
## Available Examples

<a id="basic_usagepy"></a>
### `basic_usage.py`
Demonstrates fundamental gripper operations:
- Connecting to the gripper
- Moving to specific positions
- Reading status information
- Basic error handling

**Usage:**
```bash
cd examples
python basic_usage.py
```

<a id="configuration"></a>
## Configuration

Connect the gripper through the existing SO-ARM100/101 servo bus and controller.
Use the controller USB serial port, set `STS_ID` to the gripper servo ID (typically 6 on SO-ARM101),
and close other applications using that port.

Before running examples, you may need to adjust configuration parameters:

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

<a id="common-issues"></a>
## Common Issues

<a id="connection-problems"></a>
### Connection Problems
- **Windows**: Check Device Manager for correct COM port
- **Linux**: Ensure user has access to serial ports (`sudo usermod -a -G dialout $USER`)
- **macOS**: Use `/dev/cu.usbserial-*` or `/dev/tty.usbserial-*`

<a id="permission-errors"></a>
### Permission Errors
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

<a id="stservo-sdk-issues"></a>
### STServo SDK Issues
Make sure the STServo SDK is properly installed:
1. Clone the [Feetech STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python).
2. Copy the `STservo_sdk` folder (with the folder itself) to `software/python/` directory.

<a id="creating-your-own-examples"></a>
## Creating Your Own Examples

When creating new examples:

1. **Import the gripper module**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **Handle errors gracefully**
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

3. **Include proper documentation**
   - Clear description of what the example does
   - Required hardware setup
   - Expected behavior

<a id="safety-notes"></a>
## Safety Notes

⚠️ **Important Safety Considerations:**
- Always monitor temperature and current draw
- Implement proper error handling
- Test with low forces first
- Ensure proper mechanical setup
- Keep fingers clear of moving parts

<a id="contributing-examples"></a>
## Contributing Examples

We welcome new examples! Please:
- Follow the existing code style
- Include comprehensive comments
- Test thoroughly before submitting
- Add entry to this README

---

**Happy coding!** 🤖
<!-- /translated-content -->
