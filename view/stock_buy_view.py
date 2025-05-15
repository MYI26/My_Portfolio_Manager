from PySide6.QtWidgets import QFrame, QWidget, QLineEdit, QMessageBox # type: ignore
from PySide6.QtCore import Qt, Signal # type: ignore
from view.ui_stock_buy import Ui_frame_root

class StockBuyView(QFrame): 
    return_to_chart = Signal() 
    text_changed_frame_money_amount = Signal(str)  
    label_money_changed = Signal(str)

    buy_requested = Signal(float) 
    def __init__(self):
        super().__init__()
        self.ui = Ui_frame_root()
        self.ui.setupUi(self)

        self.ui.frame_info.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_header.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_action_buttn.setLayoutDirection(Qt.RightToLeft)

        self.ui.button_bay.clicked.connect(self.on_confirm_clicked)

        self.ui.commandLinkButton.clicked.connect(self.on_return_to_chart_clicked)

        self.ui.lineEdit.textChanged.connect(self.on_text_changed_frame_money_amount)
        self.ui.lineEdit.textChanged.connect(self.label_money_changed)

        self.ui.label_money.setText("100.0")  
        self.ui.label_stock.setText("1.25")  

    def on_return_to_chart_clicked(self):
        print("[StockBuyView] Return to chart clicked")  
        self.return_to_chart.emit()

    def on_text_changed_frame_money_amount(self, text):
        print(f"[StockBuyView] Text changed in frame_money_amount: {text}")  
        self.text_changed_frame_money_amount.emit(text)

    def update_label_money(self, text):
        self.ui.label_money.setText(text)

    def update_label_stock(self, text):
        self.ui.label_stock.setText(text)

    def update_label_total(self, text):
        self.ui.label_total.setText(text)

    def set_balance_display(self, value: float):
        self.ui.label_11.setText(f"{value:.2f}$")

    def on_confirm_clicked(self):
        try:
            quantity = float(self.ui.label_stock.text())       
            self.buy_requested.emit(quantity)   
        except ValueError:
            self.show_error("Veuillez entrer une quantité valide.")

    def show_message(self, text: str):
        QMessageBox.information(self, "Info", text)

    def show_error(self, text: str):
        QMessageBox.critical(self, "Erreur", text)