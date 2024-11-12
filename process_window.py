from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt
import time

class ProcessWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Process Log")
        self.setFixedSize(400, 300)
        self.setWindowFlag(Qt.FramelessWindowHint)

        layout = QVBoxLayout(self)

        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)

        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                border: 2px solid #32CD32;
                border-radius: 5px;
            }
            QTextEdit {
                color: #32CD32;
                background-color: #000000;
                border: none;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 12px;
            }
        """)

    def add_log(self, message):
        self.log_text.append(f"[{time.strftime('%H:%M:%S')}] {message}")