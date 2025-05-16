from PySide6.QtWidgets import QFrame, QListWidgetItem 
from view.ui_python.ui_history import Ui_Frame_History
from PySide6.QtGui import QFont, QPixmap 
from PySide6.QtCore import Qt, QSize 
from PySide6.QtWidgets import QLabel, QHBoxLayout 
from urllib.request import urlopen, Request
import ssl
from PySide6.QtCore import QByteArray 

class HistoryView(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame_History()
        self.ui.setupUi(self)

        self.ui.listWidgetOrders.setLayoutDirection(Qt.LeftToRight)
        self.ui.listWidgetOrders.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidgetOrders.setStyleSheet("""
            QListWidget {
                border: 1px solid rgb(40, 75, 107);
                border-radius: 5px;
                background-color: white;
            }
            QScrollBar:vertical {
                width: 12px;
                border-radius: 100px;
                background-color: white;
                border: 2px solid rgb(240, 240, 240);
                left: 0px;
            }
            QScrollBar::handle:vertical {
                background-color: rgb(40, 75, 107);
                border-radius: 15px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
        """)

    def add_history_item(self, logo_path, company, date, order_type, stock_price, amount, total_price):
        item = QListWidgetItem(self.ui.listWidgetOrders)
        item.setSizeHint(QSize(950, 50))  # שימוש ב-QSize

        widget = QFrame()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(30, 5, 30, 5)
        layout.setSpacing(50)

        # לוגו
        label_logo = QLabel()
        try:
            req = Request(logo_path, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(req, context=ssl._create_unverified_context()) as response:
                data = response.read()
                pixmap = QPixmap()
                pixmap.loadFromData(QByteArray(data))
                if not pixmap.isNull():
                    label_logo.setPixmap(pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        except Exception:
            pass
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