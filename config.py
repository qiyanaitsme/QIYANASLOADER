import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(SCRIPT_DIR, 'icon.ico')

DARK_THEME = """
    QMainWindow, QWidget { background-color: #1a1a1a; }
    QLabel { color: white; font-size: 14px; }
    QPushButton {
        background-color: #333333;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
    }
    QPushButton:hover { background-color: #404040; }
    QPushButton:disabled { background-color: #2a2a2a; color: #666666; }
    QProgressBar {
        border: 2px solid #333333;
        border-radius: 5px;
        text-align: center;
        color: white;
    }
    QProgressBar::chunk { background-color: #32CD32; }
    QListWidget {
        background-color: #333333;
        color: white;
        border-radius: 5px;
    }
    QComboBox {
        background-color: #333333;
        color: white;
        border: none;
        padding: 5px;
        border-radius: 5px;
    }
"""

LIGHT_THEME = """
    QMainWindow, QWidget { background-color: #f0f0f0; }
    QLabel { color: black; font-size: 14px; }
    QPushButton {
        background-color: #e0e0e0;
        color: black;
        border: none;
        padding: 10px;
        border-radius: 5px;
    }
    QPushButton:hover { background-color: #d0d0d0; }
    QPushButton:disabled { background-color: #cccccc; color: #666666; }
    QProgressBar {
        border: 2px solid #cccccc;
        border-radius: 5px;
        text-align: center;
        color: black;
    }
    QProgressBar::chunk { background-color: #32CD32; }
    QListWidget {
        background-color: white;
        color: black;
        border-radius: 5px;
    }
    QComboBox {
        background-color: white;
        color: black;
        border: 1px solid #cccccc;
        padding: 5px;
        border-radius: 5px;
    }
"""

NEON_THEME = """
    QMainWindow, QWidget { background-color: #0a192f; }
    QLabel { color: #64ffda; font-size: 14px; }
    QPushButton {
        background-color: #172a45;
        color: #64ffda;
        border: 2px solid #64ffda;
        padding: 10px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #233554;
        border-color: #64ffda;
    }
    QPushButton:disabled {
        background-color: #172a45;
        border-color: #233554;
        color: #233554;
    }
    QProgressBar {
        border: 2px solid #64ffda;
        border-radius: 5px;
        text-align: center;
        color: #64ffda;
    }
    QProgressBar::chunk { background-color: #64ffda; }
    QListWidget {
        background-color: #172a45;
        color: #64ffda;
        border: 2px solid #64ffda;
        border-radius: 5px;
    }
    QComboBox {
        background-color: #172a45;
        color: #64ffda;
        border: 2px solid #64ffda;
        padding: 5px;
        border-radius: 5px;
    }
"""