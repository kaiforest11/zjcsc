# 冷钱包助记词生成器

一个安全的BIP39助记词生成器，支持生成12个和24个单词的助记词，用于创建加密货币钱包。

## 功能特性

- 支持生成12个或24个单词的BIP39助记词
- 提供命令行界面（CLI）和图形用户界面（GUI）
- 遵循BIP39标准，确保兼容性
- 内置安全提示，提醒用户妥善保管助记词
- 无需网络连接，确保安全性

## 安装与使用

### 图形界面版本（推荐）

直接下载预编译的可执行文件：

- **Windows**: [MnemonicGeneratorGUI.exe](./build/exe.win-amd64-3.10/MnemonicGeneratorGUI.exe)（已打包，无需安装Python）

### 命令行版本

1. 确保已安装Python 3.6+
2. 安装依赖：
   ```bash
   pip install mnemonic
   ```
3. 运行命令行版本：
   ```bash
   python argparse.py -n 12  # 生成12个单词的助记词
   python argparse.py -n 24  # 生成24个单词的助记词
   ```

## 安全说明

⚠️ **重要安全提示**：

1. 生成的助记词是访问您钱包资产的唯一凭证，请务必安全保存
2. 助记词一旦丢失，钱包资产将无法找回
3. 请在安全的离线环境中使用此工具
4. 不要将助记词分享给任何人
5. 建议将助记词写在纸上并保存在多个安全位置

## 项目结构

```
zjcsc/
├── argparse.py          # 命令行版本源码
├── gui_mnemonic_generator.py  # GUI版本源码
├── setup.py             # cx_Freeze打包配置（CLI版）
├── setup_gui.py         # cx_Freeze打包配置（GUI版）
├── build/               # 打包输出目录
│   └── exe.win-amd64-3.10/  # Windows可执行文件
│       ├── MnemonicGeneratorGUI.exe
│       └── MnemonicGeneratorCLI.exe
└── README.md            # 本文件
```

## 开发

### 依赖库

- [mnemonic](https://pypi.org/project/mnemonic/): BIP39助记词生成库
- [PyQt5](https://pypi.org/project/PyQt5/): GUI界面库

### 打包

使用cx_Freeze打包应用程序：

```bash
# 打包GUI版本
python setup_gui.py build

# 打包CLI版本
python setup.py build
```

## 许可证

本项目仅供学习和参考使用，请遵守当地法律法规，谨慎使用加密货币相关工具。

## 免责声明

本软件按"现状"提供，不提供任何形式的保证。使用此软件产生的任何后果由用户自行承担。生成的助记词和相关资产的安全性完全由用户负责。
