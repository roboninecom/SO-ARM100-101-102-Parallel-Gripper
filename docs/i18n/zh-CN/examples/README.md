<!-- translation-navigation -->
[English](../../en/examples/README.md) · [Русский](../../ru/examples/README.md) · [Español](../../es/examples/README.md) · [Français](../../fr/examples/README.md) · [Deutsch](../../de/examples/README.md) · [Português (Brasil)](../../pt-BR/examples/README.md) · [简体中文](README.md) · [日本語](../../ja/examples/README.md) · [हिन्दी](../../hi/examples/README.md) · [العربية](../../ar/examples/README.md)

[英文原文](../../../../examples/README.md)

[简体中文](../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="examples---parallel-gripper"></a>
# 举个例子:平行抓住器

本目录包含示例代码,说明如何在各种场景中使用平行抓住器.

<a id="available-examples"></a>
## 现有的例子

<a id="basic_usagepy"></a>
### `basic_usage.py`
展示了基本的抓住器操作:
- 连接到抓住器
- 转移到特定位置
- 阅读状态信息
- 基本错误处理

**使用:**
```bash
cd examples
python basic_usage.py
```

<a id="configuration"></a>
## 配置

通过现有的接力器连接 SO-ARM100/101 服务器和控制器.
使用控制器的USB串行端口,设置 `STS_ID` 按 ⁇ 器的伺服ID (通常是6 SO-ARM101),
关闭使用该端口的其他应用程序.

在运行示例之前,您可能需要调整配置参数:

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

<a id="common-issues"></a>
## 常见的问题

<a id="connection-problems"></a>
### 连接问题
- **窗户**: 检查设备管理器是否正确的COM端口
- **基于 Linux**:确保用户可访问串行端口 (`sudo usermod -a -G dialout $USER`)
- **macOS**使用: `/dev/cu.usbserial-*` 或 `/dev/tty.usbserial-*`

<a id="permission-errors"></a>
### 许可错误
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

<a id="stservo-sdk-issues"></a>
### STServo SDK问题
确保 STServo SDK 正确安装:
1. 克隆 [Feetech STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python).
2. 复制 `STservo_sdk` 文件 ⁇  (包含文件 ⁇ 本身) `software/python/` 文件目录

<a id="creating-your-own-examples"></a>
## 创造自己的榜样

在创建新例子时:

1. **进口抓紧器模块**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **用优雅的方式处理错误**
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

3. **包含适当的文件**
   - 清晰描述例子所做的
   - 要求的硬件设置
   - 预期的行为

<a id="safety-notes"></a>
## 安全说明

⚠️ **重要安全考虑因素:**
- 始终监控温度和电流的吸收
- 执行适当的错误处理
- 首先用低力进行测试
- 确保适当的机械配置
- 保持手指远离移动部分

<a id="contributing-examples"></a>
## 贡献的例子

我们欢迎新的例子! 请问:
- 遵循现有的代码风格
- 包含详细的评论
- 在提交之前进行彻底检测
- 添加到本 README 中的输入

---

**快乐的编码!** 🤖
<!-- /translated-content -->
