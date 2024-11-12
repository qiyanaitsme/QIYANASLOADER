import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from config import *
from process_window import ProcessWindow
from loader_thread import LoaderThread


class LoaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setWindowFlags(self.windowFlags() | Qt.Window)

        self.setWindowTitle("QIYANAS DLL INSTALLER")
        self.setFixedSize(600, 400)
        self.selected_files = []

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(15)

        title = QLabel("QIYANAS DLL INSTALLER")
        title.setStyleSheet("color: #32CD32; font-size: 28px; font-weight: bold; letter-spacing: 2px;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.select_btn = QPushButton("Select DLL Files (Max 2)")
        self.select_btn.clicked.connect(self.select_dll_files)
        layout.addWidget(self.select_btn)

        self.files_list = QListWidget()
        self.files_list.setMaximumHeight(80)
        layout.addWidget(self.files_list)

        self.current_file = QLabel("Waiting for files...")
        self.current_file.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.current_file)

        self.progress = QProgressBar()
        self.progress.setFixedHeight(20)
        layout.addWidget(self.progress)

        self.start_btn = QPushButton("START INSTALLATION")
        self.start_btn.clicked.connect(self.start_loading)
        self.start_btn.setEnabled(False)
        layout.addWidget(self.start_btn)

        style_combo = QComboBox()
        style_combo.addItems(["Dark Theme", "Light Theme", "Neon Blue"])
        style_combo.currentTextChanged.connect(self.change_style)
        layout.addWidget(style_combo)

        self.change_style("Dark Theme")

    def select_dll_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select DLL Files", "", "DLL Files (*.dll)")
        if files:
            if len(files) > 2:
                QMessageBox.warning(self, "Warning", "You can select maximum 2 files!")
                files = files[:2]
            self.selected_files = files
            self.files_list.clear()
            for file in files:
                self.files_list.addItem(QFileInfo(file).fileName())
            self.start_btn.setEnabled(True)

    def start_loading(self):
        if not self.selected_files:
            return

        self.progress.setValue(0)
        self.process_window = ProcessWindow()
        self.process_window.move(
            self.x() + self.width() + 10,
            self.y()
        )
        self.process_window.show()

        self.worker = LoaderThread(self.selected_files)
        self.worker.progress_update.connect(self.update_progress)
        self.worker.file_update.connect(self.update_file)
        self.worker.log_update.connect(self.process_window.add_log)
        self.worker.finished.connect(self.process_window.close)
        self.worker.start()

        self.start_btn.setEnabled(False)
        self.select_btn.setEnabled(False)

    def update_progress(self, value):
        self.progress.setValue(value)
        if value == 100:
            self.start_btn.setEnabled(True)
            self.select_btn.setEnabled(True)
            QMessageBox.information(
                self,
                "Success",
                "DLL injection completed successfully!\n\n"
                "✓ Files processed\n"
                "✓ Memory allocated\n"
                "✓ Injection successful\n"
                "✓ Traces cleaned"
            )

    def update_file(self, filename):
        self.current_file.setText(f"Installing: {filename}")

    def change_style(self, style):
        if style == "Dark Theme":
            self.setStyleSheet(DARK_THEME)
        elif style == "Light Theme":
            self.setStyleSheet(LIGHT_THEME)
        else:
            self.setStyleSheet(NEON_THEME)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(ICON_PATH))
    window = LoaderWindow()
    window.show()
    sys.exit(app.exec_())
