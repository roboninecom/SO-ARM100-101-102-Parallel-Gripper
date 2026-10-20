<!-- translation-navigation -->
[English](CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[English source](../../../CONTRIBUTING.md)

[English](README.md)

> Complete English source copy. Images, code, CAD, and original PDFs are shared.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing-to-open-source-parallel-gripper"></a>
# Contributing to Open-Source Parallel Gripper

Thank you for your interest in contributing to this project! We welcome contributions from the robotics community.

<a id="ways-to-contribute"></a>
## Ways to Contribute

<a id="-bug-reports"></a>
### 🐛 Bug Reports
- Use the GitHub issue tracker
- Include detailed reproduction steps
- Provide system information (OS, Python version, servo model)
- Attach logs or error messages

<a id="-feature-requests"></a>
### 💡 Feature Requests
- Check existing issues first
- Describe the use case clearly
- Consider implementation complexity
- Discuss with maintainers before large changes

<a id="-code-contributions"></a>
### 🔧 Code Contributions
- Fork the repository
- Create a feature branch
- Follow coding standards
- Add tests where appropriate
- Update documentation

<a id="-documentation"></a>
### 📚 Documentation
- Improve existing documentation
- Add usage examples
- Create tutorials or guides
- Fix typos or unclear explanations

<a id="-hardware-improvements"></a>
### 🛠️ Hardware Improvements
- Design modifications or improvements
- Alternative part suggestions
- New servo compatibility
- Mechanical optimizations

<a id="development-setup"></a>
## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/parallel-gripper.git
   cd parallel-gripper
   ```

2. **Install dependencies**
   ```bash
   pip install -r software/python/requirements.txt
   ```

3. **Install STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cp -r STServo_SDK_Python/STservo_sdk ./software/python/
   ```

<a id="coding-standards"></a>
## Coding Standards

<a id="python-code"></a>
### Python Code
- Follow PEP 8 style guide
- Use type hints where appropriate
- Add docstrings to all functions/classes
- Maximum line length: 88 characters
- Use meaningful variable names

<a id="documentation"></a>
### Documentation
- Use Markdown format
- Include code examples
- Keep language clear and concise
- Update README if needed

<a id="3d-models"></a>
### 3D Models
- Provide STL files in binary format
- Include source files if possible (STEP, Fusion 360, etc.)
- Test print before submitting
- Document print settings

<a id="pull-request-process"></a>
## Pull Request Process

1. **Before Starting**
   - Check existing issues and PRs
   - Discuss major changes first
   - Ensure you can test your changes

2. **Making Changes**
   - Create a descriptive branch name
   - Make atomic commits with clear messages
   - Test your changes thoroughly
   - Update documentation as needed

3. **Submitting PR**
   - Fill out the PR template
   - Link related issues
   - Provide clear description of changes
   - Include testing information

4. **Review Process**
   - Address reviewer feedback
   - Keep discussions constructive
   - Be patient with the review process

<a id="testing-guidelines"></a>
## Testing Guidelines

<a id="software-testing"></a>
### Software Testing
- Test on your hardware setup
- Verify cross-platform compatibility
- Check error handling
- Test edge cases

<a id="hardware-testing"></a>
### Hardware Testing
- Verify 3D prints work correctly
- Test assembly procedures
- Check mechanical tolerances
- Validate with different materials

<a id="communication"></a>
## Communication

<a id="channels"></a>
### Channels
- GitHub Issues: Bug reports, feature requests
- GitHub Discussions: General questions, ideas
- Pull Requests: Code review, technical discussion

<a id="guidelines"></a>
### Guidelines
- Be respectful and constructive
- Search before posting
- Provide context and details
- Help others when possible

<a id="recognition"></a>
## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

<a id="license"></a>
## License

This project is multi-licensed — see [`LICENSING.md`](LICENSING.md) for the full map.

By submitting a contribution you certify that you have the right to submit it,
and you agree that it is licensed under the licence that applies to the part of
the repository it lands in:

| You are changing | Your contribution is licensed |
|---|---|
| Hardware / CAD | CERN-OHL-P-2.0 |
| Software | Apache-2.0 |
| Documentation and images | CC BY 4.0 |

In other words, inbound = outbound: whatever licence a file is already under,
your change to it is under the same licence.

**Third-party material.** If your contribution includes anything you did not
create yourself, say so in the pull request so it can be recorded in
[`NOTICE`](../../../NOTICE). Please do not commit binaries you cannot license — that
includes vendor tools and firmware.

**New files** must be covered by [`REUSE.toml`](../../../REUSE.toml). `reuse lint` runs in
pre-commit and in CI, and will fail if any file lacks copyright and licence
information.

<a id="questions"></a>
## Questions?

Feel free to open an issue or start a discussion if you have questions about contributing!

---

**Thank you for helping make this project better!** 🤝
<!-- /translated-content -->
