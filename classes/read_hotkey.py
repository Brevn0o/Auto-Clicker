import keyboard
from PyQt6.QtCore import QThread, pyqtSignal


class ReadHotkey(QThread):
    finished = pyqtSignal(str)

    def run(self):
        hotkey = keyboard.read_hotkey(suppress=False)
        self.finished.emit(hotkey)
