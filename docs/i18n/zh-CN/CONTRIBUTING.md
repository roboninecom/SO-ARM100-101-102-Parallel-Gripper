<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[英文原文](../../../CONTRIBUTING.md)

[简体中文](README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing-to-open-source-parallel-gripper"></a>
# 贡献开源平行抓取器

感谢您对此项目的兴趣! 我们欢迎机器人界的贡献.

<a id="ways-to-contribute"></a>
## 捐款方式

<a id="-bug-reports"></a>
### ⁇  虫子报告
- 使用GitHub问题追踪器
- 包含详细的繁殖步骤
- 提供系统信息 (OS, Python 版本,伺服型号)
- 添加日志或错误消息

<a id="-feature-requests"></a>
### ⁇ 特征要求
- 首先检查现有问题
- 清楚描述使用情况
- 考虑实施复杂性
- 在发生重大变化之前,请与维护人员讨论

<a id="-code-contributions"></a>
### ⁇ 代码贡献
- ⁇ 开仓库
- 创建一个功能分支
- 遵循编码标准
- 适当时添加测试
- 更新文件

<a id="-documentation"></a>
### ⁇ 文件
- 改进现有文档
- 添加使用例
- 创建教程或指南
- 修复字体错误或不清楚的解释

<a id="-hardware-improvements"></a>
### ⁇ ️硬件改进
- 设计修改或改进
- 其他部分建议
- 新的伺服器兼容性
- 机械优化

<a id="development-setup"></a>
## 发展设置

1. **克隆存储库**
   ```bash
   git clone https://github.com/your-org/parallel-gripper.git
   cd parallel-gripper
   ```

2. **安装依赖性**
   ```bash
   pip install -r software/python/requirements.txt
   ```

3. **安装 STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cp -r STServo_SDK_Python/STservo_sdk ./software/python/
   ```

<a id="coding-standards"></a>
## 编码标准

<a id="python-code"></a>
### Python 代码
- 遵循PEP 8风格指南
- 在适当的情况下使用类型提示
- 在所有函数/类中添加docstrings
- 最长行长:88个字符
- 使用有意义的变量名称

<a id="documentation"></a>
### 文件
- 使用Markdown格式
- 包含代码示例
- 保持清晰和简洁的语言
- 如果需要,更新README

<a id="3d-models"></a>
### 3D模型
- 提供二进制格式的STL文件
- 如果可能,包括源文件 (STEP,Fusion 360,等).
- 在提交之前的测试打印
- 文件打印设置

<a id="pull-request-process"></a>
## 拉动请求过程

1. **在开始之前**
   - 检查现有问题和公关
   - 首先讨论重大变化
   - 确保您可以测试自己的变化

2. **改变**
   - 创建描述分支名称
   - 通过明确的信息进行原子承诺
   - 仔细检查自己的变化
   - 根据需要更新文档

3. **提交公关**
   - 填写公关模板
   - 链接相关问题
   - 提供变化的明确描述
   - 包含测试信息

4. **审查过程**
   - 地址评审员的反 ⁇
   - 保持建设性的讨论
   - 在审查过程中要有耐心

<a id="testing-guidelines"></a>
## 测试指南

<a id="software-testing"></a>
### 软件测试
- 测试您的硬件设置
- 验证跨平台兼容性
- 检查错误处理
- 测试边缘盒

<a id="hardware-testing"></a>
### 硬件测试
- 验证3D打印正确运行
- 测试组装程序
- 检查机械宽容
- 用不同材料验证

<a id="communication"></a>
## 沟通

<a id="channels"></a>
### 频道
- GitHub问题:错误报告,功能请求
- 基特哈布讨论:一般问题,想法
- 撤销要求:审查代码,技术讨论

<a id="guidelines"></a>
### 准则
- 尊重和建设性
- 在发布之前搜索
- 提供文本和细节
- 尽可能帮助别人

<a id="recognition"></a>
## 认可

贡献者将在:
- README.md 贡献者部分
- 发布说明
- 项目文件

<a id="license"></a>
## 许可证

这项项目拥有多个许可证 [`LICENSING.md`](LICENSING.md) 对于整个地图.

通过提交捐款,您证明您有权提交捐款.
您同意根据适用于该部分的许可证授权
它登陆的仓库:

| 你正在改变 | 你的贡献已获得许可. |
|---|---|
| 硬件/CAD | CERN-OHL-P-2.0 |
| 软件 | Apache-2.0 |
| 文件和图像 | CC BY 4.0 |

换句话说,入境 =出境:无论文件是否已获得许可证,
您的变更在同一许可证下.

**第三方的材料.** 如果您的捐款包括您未做过任何事
在拉动请求中说,这样就可以记录在
[`NOTICE`](../../../NOTICE). 请不要提交二进制,你不能授权
包括供应商工具和固件.

**新的文件** 必须由: [`REUSE.toml`](../../../REUSE.toml). `reuse lint` 进入
任何文件都缺乏版权和许可证,
信息.

<a id="questions"></a>
## 有什么问题?

如果您有任何关于捐款的问题,请随时开放一本问题或开始讨论!

---

**谢谢你帮助这个项目变得更好!** 🤝
<!-- /translated-content -->
