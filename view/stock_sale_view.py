from PySide6.QtWidgets import QFrame, QWidget, QLineEdit, QMessageBox
from PySide6.QtCore import Qt, Signal  # ייבוא Qt עבור LayoutDirection ו-Signal
from view.ui_python.ui_stock_sale import Ui_frame_root

class StockSaleView(QFrame):  
    return_to_chart = Signal()  
    text_changed_frame_money_amount = Signal(str) 
    sell_requested = Signal(float) 

    def __init__(self):
        super().__init__()
        self.ui = Ui_frame_root()
        self.ui.setupUi(self)

        # direction layout
        self.ui.frame_info.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_header.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_action_buttn.setLayoutDirection(Qt.RightToLeft)

        #signal connections
        self.ui.commandLinkButton.clicked.connect(self.on_return_to_chart_clicked)
        self.ui.lineEdit.textChanged.connect(self.on_text_changed_frame_money_amount)

        self.ui.label_money.setText("100.0")  # ערך דפולטיבי עבור label_money
        self.ui.label_stock.setText("1.25")  # ערך דפולטיבי עבור label_stock

        self.ui.button_sale.clicked.connect(self.on_sell_clicked)

    def on_return_to_chart_clicked(self):
        self.return_to_chart.emit()

    def on_text_changed_frame_money_amount(self, text):
        self.text_changed_frame_money_amount.emit(text)

    def update_label_money(self, text):
        self.ui.label_money.setText(text)

    def update_label_stock(self, text):
        self.ui.label_stock.setText(text)
        
    def set_balance_display(self, value: float):
        self.ui.label_11.setText(f"{value:.2f}$")

    def on_sell_clicked(self):
        try:
            quantity = float(self.ui.label_stock.text())
            self.sell_requested.emit(quantity)  
        except ValueError:
            self.show_error("Quantité invalide.")

    def show_message(self, text: str):
        QMessageBox.information(self, "Info", text)

    def show_error(self, text: str):
        QMessageBox.critical(self, "Erreur", text)

    def update_label_total(self, text):
        self.ui.label_total.setText(text)