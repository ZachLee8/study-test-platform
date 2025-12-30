


import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot



app = QApplication(sys.argv)
button = QPushButton("点击")


button.show()



@Slot()
def on_click():
    print("点击了按钮")


button.clicked.connect(on_click)
app.exec()