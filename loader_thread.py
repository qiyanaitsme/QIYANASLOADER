from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QFileInfo
import time
import random

class LoaderThread(QThread):
    progress_update = pyqtSignal(int)
    file_update = pyqtSignal(str)
    log_update = pyqtSignal(str)

    def __init__(self, files):
        super().__init__()
        self.files = files
        self.process_messages = [
            "Initializing QIYANA's DLL loader...",
            "Checking system compatibility...",
            "Scanning target process...",
            "Analyzing memory regions...",
            "Preparing injection vectors...",
            "Allocating memory space...",
            "Creating remote thread...",
            "Mapping DLL sections...",
            "Resolving dependencies...",
            "Executing DLL entry point...",
            "Verifying injection status...",
            "Cleaning up traces...",
            "Establishing hooks...",
            "Patching memory...",
            "Bypassing security...",
            "Initializing DLL functions...",
            "Loading exports table...",
            "Resolving imports...",
            "Finalizing installation..."
        ]

    def run(self):
        total_duration = random.uniform(10, 20)
        step_duration = total_duration / len(self.process_messages)

        total_files = len(self.files)
        for i, file in enumerate(self.files):
            filename = QFileInfo(file).fileName()
            self.file_update.emit(filename)

            for msg in self.process_messages:
                self.log_update.emit(msg)
                time.sleep(step_duration)
                self.progress_update.emit(
                    int((i * 100 + self.process_messages.index(msg) * 5) / total_files)
                )

        self.log_update.emit("Installation completed successfully!")
        self.progress_update.emit(100)