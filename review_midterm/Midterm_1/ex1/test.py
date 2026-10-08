from ex1 import calc_NPV,is_investment

from PyQt6.QtWidgets import QApplication, QMainWindow
from review_midterm.Midterm_1.ex1.ui.NPVMainWindowEx import MainWindowEx
app = QApplication([])
myui=MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()
# c0=1000000
# ct=4250
# r=7
# t=3
# NPV=calc_NPV(c0,ct,r,t)
# print(NPV)
# is_investment(NPV)