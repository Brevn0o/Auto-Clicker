import threading
import time

import pyautogui
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer, Qt
from pynput.mouse import Listener


class PickWindow:

    def __init__(self):
        self.clicked = False

    class Ui_Form(object):
        def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.setFixedSize(115, 46)
            Form.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
            self.label = QtWidgets.QLabel(parent=Form)
            self.label.setGeometry(QtCore.QRect(3, 0, 121, 20))
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(parent=Form)
            self.label_2.setGeometry(QtCore.QRect(3, 20, 121, 20))
            self.label_2.setObjectName("label_2")

            self.retranslateUi(Form)
            QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.label.setText(_translate("Form", "Click to pick location"))
            self.label_2.setText(_translate("Form", "X: ?  Y: ?"))

    def move_window(self):
        try:
            if self.clicked:
                return
            cursor_pos = pyautogui.position()
            window_pos = self.Form.mapFromGlobal(QtGui.QCursor.pos())
            self.Form.move(self.Form.mapToParent(QtCore.QPoint(window_pos.x() + 10, window_pos.y() + 5)))
            pos_text = f"X: {cursor_pos.x} Y: {cursor_pos.y}"
            self.ui.label_2.setText(pos_text)
        except:
            pass

    def on_click(self, x, y, button, pressed):
        try:
            clicked = True
            print(1)
            # raise
            self.Form.hide()
            # time.sleep(1)
            # self.Form.show()
        except:
            pass

    def listen(self):
        with Listener(on_click=self.on_click) as listener:
            listener.join()

    def start_program(self):
        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        self.Form = QtWidgets.QWidget()
        self.ui = self.Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        timer = QTimer()
        timer.timeout.connect(self.move_window)
        timer.start(20)
        threading.Thread(target=self.listen).start()
        sys.exit(self.app.exec())