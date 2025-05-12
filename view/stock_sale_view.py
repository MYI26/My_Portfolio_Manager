from PySide6.QtWidgets import QFrame, QWidget, QLineEdit
from PySide6.QtCore import Qt, Signal  # ייבוא Qt עבור LayoutDirection ו-Signal
from view.ui_stock_sale import Ui_frame_root

class StockSaleView(QFrame):  # ירושה מ-QFrame
    return_to_chart = Signal()  # סיגנל לחזרה לגרף
    text_changed_frame_money_amount = Signal(str)  # סיגנל עבור frame_money_amount

    def __init__(self):
        super().__init__()
        self.ui = Ui_frame_root()
        self.ui.setupUi(self)

        # הגדרת כיוון פריסת הלייאאוטים
        self.ui.frame_info.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_header.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_action_buttn.setLayoutDirection(Qt.RightToLeft)

        # חיבור כפתור ה-sale לאירוע
        self.ui.button_sale.clicked.connect(self.on_confirm_clicked)

        # חיבור commandLinkButton לסיגנל
        self.ui.commandLinkButton.clicked.connect(self.on_return_to_chart_clicked)

        # חיבור תיבות הטקסט לסיגנלים
        self.ui.lineEdit.textChanged.connect(self.on_text_changed_frame_money_amount)

        # הגדרת ערכים דפולטיביים ללייבלים
        self.ui.label_money.setText("100.0")  # ערך דפולטיבי עבור label_money
        self.ui.label_stock.setText("1.25")  # ערך דפולטיבי עבור label_stock

    def on_confirm_clicked(self):
        """
        מטפל בלחיצה על כפתור ה-sale.
        """
        print("[StocksaleView] sale button clicked")  # בדיקה

    def on_return_to_chart_clicked(self):
        """
        משדר סיגנל לחזרה לגרף.
        """
        print("[StocksaleView] Return to chart clicked")  # בדיקה
        self.return_to_chart.emit()

    def on_text_changed_frame_money_amount(self, text):
        """
        משדר את הטקסט שהוזן ב-frame_money_amount ל-Presenter.
        """
        print(f"[StocksaleView] Text changed in frame_money_amount: {text}")  # בדיקה
        self.text_changed_frame_money_amount.emit(text)

    def update_label_money(self, text):
        """
        מעדכן את הטקסט של label_money.
        """
        self.ui.label_money.setText(text)

    def update_label_stock(self, text):
        """
        מעדכן את הטקסט של label_stock.
        """
        self.ui.label_stock.setText(text)