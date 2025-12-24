import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QComboBox, 
                             QTextEdit, QMessageBox, QGroupBox, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from mnemonic import Mnemonic


class MnemonicGeneratorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("冷钱包助记词生成器")
        self.setGeometry(300, 300, 600, 500)
        
        # 设置主窗口部件
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # 创建主布局
        main_layout = QVBoxLayout(main_widget)
        
        # 标题
        title_label = QLabel("冷钱包助记词生成器")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin: 20px;")
        
        main_layout.addWidget(title_label)
        
        # 创建设置区域
        settings_group = QGroupBox("生成设置")
        settings_layout = QVBoxLayout(settings_group)
        
        # 助记词数量选择
        num_layout = QHBoxLayout()
        num_label = QLabel("助记词数量:")
        self.num_combo = QComboBox()
        self.num_combo.addItems(["12个单词", "24个单词"])
        num_layout.addWidget(num_label)
        num_layout.addWidget(self.num_combo)
        num_layout.addStretch()
        
        settings_layout.addLayout(num_layout)
        
        # 生成按钮
        self.generate_btn = QPushButton("生成助记词")
        self.generate_btn.clicked.connect(self.generate_mnemonic)
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        
        settings_layout.addWidget(self.generate_btn)
        
        main_layout.addWidget(settings_group)
        
        # 助记词显示区域
        mnemonic_group = QGroupBox("生成的助记词")
        mnemonic_layout = QVBoxLayout(mnemonic_group)
        
        self.mnemonic_display = QTextEdit()
        self.mnemonic_display.setReadOnly(True)
        self.mnemonic_display.setMinimumHeight(150)
        self.mnemonic_display.setStyleSheet("""
            QTextEdit {
                font-family: 'Courier New', monospace;
                font-size: 12px;
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                padding: 10px;
            }
        """)
        
        mnemonic_layout.addWidget(self.mnemonic_display)
        
        # 复制按钮
        copy_layout = QHBoxLayout()
        copy_layout.addStretch()
        self.copy_btn = QPushButton("复制到剪贴板")
        self.copy_btn.clicked.connect(self.copy_to_clipboard)
        self.copy_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 8px 16px;
                font-size: 12px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        copy_layout.addWidget(self.copy_btn)
        
        mnemonic_layout.addLayout(copy_layout)
        
        main_layout.addWidget(mnemonic_group)
        
        # 安全提示区域
        security_group = QGroupBox("安全提示")
        security_layout = QVBoxLayout(security_group)
        
        security_text = QTextEdit()
        security_text.setReadOnly(True)
        security_text.setMaximumHeight(120)
        security_text.setHtml("""
        <div style="font-size: 12px; line-height: 1.6;">
            <p><b>重要安全提示:</b></p>
            <ul>
                <li>请将助记词保存在安全的地方</li>
                <li>千万不要将助记词分享给任何人</li>
                <li>助记词一旦丢失，钱包资产将无法找回</li>
                <li>建议将助记词离线保存多份副本</li>
                <li>确保在安全的环境中使用此工具</li>
            </ul>
        </div>
        """)
        security_text.setStyleSheet("""
            QTextEdit {
                background-color: #fff3cd;
                border: 1px solid #ffeaa7;
                padding: 10px;
                border-radius: 4px;
            }
        """)
        
        security_layout.addWidget(security_text)
        
        main_layout.addWidget(security_group)
        
        # 添加弹性空间
        main_layout.addStretch()
        
        # 状态栏
        self.statusBar().showMessage("就绪")
    
    def generate_mnemonic(self):
        """生成助记词"""
        try:
            # 获取选择的数量
            num_words = 12 if self.num_combo.currentText() == "12个单词" else 24
            
            # 生成助记词
            mnemo = Mnemonic("english")
            strength = 128 if num_words == 12 else 256
            mnemonic_phrase = mnemo.generate(strength)
            
            # 显示助记词
            self.mnemonic_display.setPlainText(mnemonic_phrase)
            
            # 更新状态栏
            self.statusBar().showMessage(f"已生成{num_words}个单词的助记词", 3000)
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"生成助记词时出错: {str(e)}")
    
    def copy_to_clipboard(self):
        """复制助记词到剪贴板"""
        mnemonic_text = self.mnemonic_display.toPlainText()
        if mnemonic_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(mnemonic_text)
            self.statusBar().showMessage("助记词已复制到剪贴板", 2000)
        else:
            QMessageBox.information(self, "提示", "请先生成助记词")


def main():
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyle("Fusion")
    
    window = MnemonicGeneratorGUI()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()