from review_midterm.Midterm_1.ex2.ui.FlowerMainWindow import Ui_MainWindow
from review_midterm.Midterm_1.ex2.ex2 import calc_da_lat_revenue, calc_sapa_revenue, calc_total_revenue


class FlowerMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_process.clicked.connect(self.process_calculate)

    def process_calculate(self):
        da_lat_qty = self.daLatQuantitySpinBox_2.value()
        sapa_qty = self.sapaQuantitySpinBox.value()

        da_lat_revenue = calc_da_lat_revenue(da_lat_qty)
        sapa_revenue = calc_sapa_revenue(sapa_qty)
        total_revenue = calc_total_revenue(da_lat_revenue, sapa_revenue)

        self.daLatSoldLineEdit.setText(str(da_lat_qty))
        self.daLatRevenueTextEdit.setPlainText(f"{da_lat_revenue:,.0f} VND")
        self.sapaSoldLineEdit.setText(str(sapa_qty))
        self.sapaSoldTextEdit.setPlainText(f"{sapa_revenue:,.0f} VND")
        self.totalRevenueLineEdit.setText(f"{total_revenue:,.0f} VND")