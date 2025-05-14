from PySide6.QtWidgets import QFrame, QListWidgetItem # type: ignore
from view.ui_history import Ui_Frame_History
from PySide6.QtGui import QFont, QPixmap # type: ignore
from PySide6.QtCore import Qt, QSize # type: ignore
from PySide6.QtWidgets import QLabel, QHBoxLayout # type: ignore


class HistoryView(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame_History()
        self.ui.setupUi(self)

        # הגדרת כיוון ה-QListWidget לשמאל לימין
        self.ui.listWidgetOrders.setLayoutDirection(Qt.LeftToRight)

        # # דוגמה סטטית: יצירת שלושה אייטמים
        # self.add_history_item("resources/logos/apple.png", "Apple Inc.", "2025-05-12", "Buy", 150.0, 10, 1500.0)
        # self.add_history_item("resources/logos/tesla.png", "Tesla", "2025-05-11", "Sell", 200.0, 5, 1000.0)
        # self.add_history_item("resources/logos/nvidia.png", "NVIDIA", "2025-05-10", "Buy", 300.0, 3, 900.0)
        # self.add_history_item("resources/logos/google.png", "Google", "2025-05-09", "Sell", 250.0, 4, 1000.0)
        # self.add_history_item("resources/logos/microsoft.png", "Microsoft", "2025-05-08", "Buy", 400.0, 2, 800.0)

    def add_history_item(self, logo_path, company, date, order_type, stock_price, amount, total_price):
        item = QListWidgetItem(self.ui.listWidgetOrders)
        item.setSizeHint(QSize(950, 50))  # שימוש ב-QSize

        widget = QFrame()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(30, 5, 30, 5)
        layout.setSpacing(50)

        # לוגו
        label_logo = QLabel()
        pixmap = QPixmap(logo_path)
        if not pixmap.isNull():
            label_logo.setPixmap(pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(label_logo)

        # שם מסחרי
        label_company = QLabel(company)
        label_company.setFont(QFont("Segoe UI", 10))
        layout.addWidget(label_company)

        # תאריך
        label_date = QLabel(date)
        label_date.setFont(QFont("Segoe UI", 10))
        layout.addWidget(label_date)

        # סוג פעולה
        label_order = QLabel(order_type)
        label_order.setFont(QFont("Segoe UI", 10))
        layout.addWidget(label_order)

        # מחיר מניה
        label_stock_price = QLabel(f"{stock_price:.2f} $")
        layout.addWidget(label_stock_price)

        # כמות
        label_amount = QLabel(str(amount))
        layout.addWidget(label_amount)

        # מחיר כולל
        label_total_price = QLabel(f"{total_price:.2f} $")
        layout.addWidget(label_total_price)

        widget.setLayout(layout)
        self.ui.listWidgetOrders.setItemWidget(item, widget)

    def get_selected_filter(self):
        return self.ui.comboBox.currentText()
    
    def on_filter_changed(self, callback):
        self.ui.comboBox.currentTextChanged.connect(callback)

    def clear_history(self):
        self.ui.listWidgetOrders.clear()