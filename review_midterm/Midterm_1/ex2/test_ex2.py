from PyQt6.QtWidgets import QApplication, QMainWindow
from review_midterm.Midterm_1.ex2.ui.FlowerMainWindowEx import FlowerMainWindowEx

app = QApplication([])
myui = FlowerMainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()