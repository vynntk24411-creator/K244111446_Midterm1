from review_midterm.Midterm_1.ex1.ui.NPVMainWindow import Ui_MainWindow
from review_midterm.Midterm_1.ex1.ex1 import calc_NPV, is_investment

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_calcNPV.clicked.connect(self.process_NPV)

    def process_NPV(self):
        c0=float(self.c0LineEdit.text())
        ct=float(self.cTLineEdit.text())
        r=float(self.rateRLineEdit.text())
        t=int(self.thIGianTLineEdit.text())
        NPV=calc_NPV(c0,ct,r,t)
        text=is_investment(NPV)
        self.resultLineEdit.setText(str(NPV))
        self.nPVLineEdit.setText(text)