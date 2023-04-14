import threading
import time

import pyautogui
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer, Qt, QThread, pyqtSignal
from pynput import mouse


# class PickLocation(QThread):
#     finished = pyqtSignal(list)
#
#     def __init__(self):
#         super().__init__()
#         self.clicked = False
#
#     class Ui_Form(object):
#         def setupUi(self, Form):
#             Form.setObjectName("Form")
#             Form.setFixedSize(115, 46)
#             Form.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
#             self.label = QtWidgets.QLabel(parent=Form)
#             self.label.setGeometry(QtCore.QRect(3, 0, 121, 20))
#             self.label.setObjectName("label")
#             self.label_2 = QtWidgets.QLabel(parent=Form)
#             self.label_2.setGeometry(QtCore.QRect(3, 20, 121, 20))
#             self.label_2.setObjectName("label_2")
#
#             self.retranslateUi(Form)
#             QtCore.QMetaObject.connectSlotsByName(Form)
#
#         def retranslateUi(self, Form):
#             _translate = QtCore.QCoreApplication.translate
#             Form.setWindowTitle(_translate("Form", "Form"))
#             self.label.setText(_translate("Form", "Click to pick location"))
#             self.label_2.setText(_translate("Form", "X: ?  Y: ?"))
#
#     class ListenClick(QThread):
#         pass
#
#     class Q(QThread):
#         finished = pyqtSignal(list)
#
#         def __init__(self, app):
#             super().__init__()
#             self.app = app
#         def run(self):
#             self.app.exec()
#
#     def run(self):
#         import sys
#         self.app = QtWidgets.QApplication(sys.argv)
#         self.Form = QtWidgets.QWidget()
#         self.ui = self.Ui_Form()
#         self.ui.setupUi(self.Form)
#         self.Form.show()
#         q = self.Q(self.app)
#         q.start()
#         # self.app.exec()








# class PickLocation(QThread):
#
#     def __init__(self):
#         super().__init__()
#         self.clicked = False
#
    # class Ui_Form(object):
    #     def setupUi(self, Form):
    #         Form.setObjectName("Form")
    #         Form.setFixedSize(115, 46)
    #         Form.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
    #         self.label = QtWidgets.QLabel(parent=Form)
    #         self.label.setGeometry(QtCore.QRect(3, 0, 121, 20))
    #         self.label.setObjectName("label")
    #         self.label_2 = QtWidgets.QLabel(parent=Form)
    #         self.label_2.setGeometry(QtCore.QRect(3, 20, 121, 20))
    #         self.label_2.setObjectName("label_2")
    #
    #         self.retranslateUi(Form)
    #         QtCore.QMetaObject.connectSlotsByName(Form)
#
        # def retranslateUi(self, Form):
        #     _translate = QtCore.QCoreApplication.translate
        #     Form.setWindowTitle(_translate("Form", "Form"))
        #     self.label.setText(_translate("Form", "Click to pick location"))
        #     self.label_2.setText(_translate("Form", "X: ?  Y: ?"))
#
#     class ListenClick(QThread):
#         finished = pyqtSignal(list)
#
#         def on_click(self, x, y, button, pressed):
#             if button == mouse.Button.left and pressed:
#                 return False
#         def run(self):
#             print('Hel')
#             listener = mouse.Listener(on_click=self.on_click)
#             listener.start()
#             listener.join()
#             print('ttt')
#             self.finished.emit([121, 890])
#
#     def move_window(self):
#         try:
#             # if self.clicked:
#             #     return
#             cursor_pos = pyautogui.position()
#             window_pos = self.Form.mapFromGlobal(QtGui.QCursor.pos())
#             self.Form.move(self.Form.mapToParent(QtCore.QPoint(window_pos.x() + 10, window_pos.y() + 5)))
#             pos_text = f"X: {cursor_pos.x} Y: {cursor_pos.y}"
#             self.ui.label_2.setText(pos_text)
#         except:
#             pass
#
#
#     # def listen(self):
#     #     with Listener(on_click=self.on_click) as listener:
#     #         listener.join()
#
    # def run(self):
    #     import sys
    #     self.app = QtWidgets.QApplication(sys.argv)
    #     self.Form = QtWidgets.QWidget()
    #     self.ui = self.Ui_Form()
    #     self.ui.setupUi(self.Form)
    #     self.Form.show()
    #     # timer = QTimer()
    #     # timer.timeout.connect(self.move_window)
    #     # timer.start(200)
    #     # threading.Thread(target=self.listen).start()
    #     sys.exit(self.app.exec())
#
#
# # s = PickLocation()
# # s.start_program()
