



from PySide6.QtWidgets import QApplication, QMainWindow

import sys

from test_ui import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)


window.show()
app.exec()

