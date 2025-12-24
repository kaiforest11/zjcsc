import sys
from cx_Freeze import setup, Executable

# 依赖项检测
build_exe_options = {
    "packages": ["mnemonic", "urllib"],
    "excludes": ["tkinter", "unittest", "email", "http", "xml", "pydoc", 
                 "PyQt5.QtQml", "PyQt5.QtQuick", "PyQt5.QtQuickWidgets", "PyQt5.QtQuickControls2"],
    "include_files": [],
    "optimize": 2
}

# 定义可执行文件 - 仅GUI版本
executables = [
    Executable(
        "gui_mnemonic_generator.py",
        target_name="MnemonicGeneratorGUI.exe",
        base="Win32GUI" if sys.platform == "win32" else None,  # 隐藏控制台窗口
        icon=None  # 可以指定图标文件
    )
]

# 项目元数据
setup(
    name="MnemonicGeneratorGUI",
    version="1.0.0",
    description="冷钱包助记词生成器 - GUI版本",
    options={"build_exe": build_exe_options},
    executables=executables
)