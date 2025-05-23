from PySide6.QtWidgets import QFrame, QListWidgetItem
from view.ui_python.ui_portfolio import Ui_Frame_Portfolio
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import QLabel, QHBoxLayout
from urllib.request import urlopen, Request
import ssl
from PySide6.QtCore import QByteArray

class PortfolioView(QFrame):
    stock_selected = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame_Portfolio()
        self.ui.setupUi(self)

        self.ui.listWidgetStocks.setLayoutDirection(Qt.LeftToRight)
        self.ui.listWidgetStocks.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidgetStocks.setStyleSheet("""
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
        self.ui.listWidgetStocks.itemClicked.connect(self._on_item_clicked)

        # Static example items
        self.add_stock_item("resources/logos/apple.png", "Apple Inc.", 15, 2200, 2400, 200, 9.1)
        self.add_stock_item("resources/logos/tesla.png", "Tesla", 8, 1600, 1700, 100, 6.25)
        self.add_stock_item("resources/logos/nvidia.png", "NVIDIA", 5, 1400, 1300, -100, -7.1)
        self.add_stock_item("resources/logos/google.png", "Google", 10, 3000, 3100, 100, 3.33)
        self.add_stock_item("resources/logos/microsoft.png", "Microsoft", 12, 2400, 2500, 100, 4.17)

    def _on_item_clicked(self, item):
        symbol = item.data(Qt.UserRole)
        if symbol:
            self.stock_selected.emit(symbol)

    def add_stock_item(self, logo_path, company, stock, total_price, current_price, perf_d, perf_p):
        item = QListWidgetItem(self.ui.listWidgetStocks)
        item.setSizeHint(QSize(950, 50))
        item.setData(Qt.UserRole, company)

        widget = QFrame()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(30, 5, 30, 5)
        layout.setSpacing(50)

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

        label_company = QLabel(company)
        label_company.setFont(QFont("Segoe UI", 10))
        layout.addWidget(label_company)

        label_stock = QLabel(str(stock))
        layout.addWidget(label_stock)

        label_total = QLabel(f"{total_price:.2f} $")
        layout.addWidget(label_total)

        label_current = QLabel(f"{current_price:.2f} $")
        layout.addWidget(label_current)

        label_perf_d = QLabel(f"{perf_d:+.2f} $")
        label_perf_d.setStyleSheet("color: green;" if perf_d >= 0 else "color: red;")
        layout.addWidget(label_perf_d)

        label_perf_p = QLabel(f"{perf_p:+.2f} %")
        label_perf_p.setStyleSheet("color: green;" if perf_p >= 0 else "color: red;")
        layout.addWidget(label_perf_p)

        widget.setLayout(layout)
        self.ui.listWidgetStocks.setItemWidget(item, widget)

    def display_portfolio(self, portfolio_data: list, user_id: str):
        self.ui.listWidgetStocks.clear()
        for data in portfolio_data:
            symbol = data["symbol"]
            quantity = data["quantity"]
            current_price = data["current_price"]
            total_price = data["invested_capital"]
            perf_d = data["perf_d"]
            perf_p = data["perf_p"]
            cloud_name = 'dialozuw5'
            public_id = f"logos/{user_id}_{symbol}"
            logo_path = f"https://res.cloudinary.com/{cloud_name}/image/upload/{public_id}.png"
            company_name = symbol
            self.add_stock_item(logo_path, company_name, quantity, total_price, current_price, perf_d, perf_p)

    def display_portfolio_totals(self, capital_total, valeur_totale, perf_d, perf_p, balance):
        perf_d = round(perf_d, 2)
        perf_p = round(perf_p, 2)
        self.ui.label_2.setText(f"{capital_total:.2f} $")
        self.ui.label_4.setText(f"{valeur_totale:.2f} $")
        self.ui.label_6.setText(f"{perf_d:+.2f} $")
        self.ui.label_8.setText(f"{perf_p:+.2f} %")
        current_cash = balance
        portfolio_value = balance + perf_d
        self.ui.label_10.setText(f"{current_cash} $")
        self.ui.label_12.setText(f"{portfolio_value} $")
        color = "green" if perf_d >= 0 else "red"
        self.ui.label_6.setStyleSheet(f"color: {color}")
        self.ui.label_8.setStyleSheet(f"color: {color}")

    def set_balance_display(self, balance):
        self.ui.label_10.setText(f"{balance:.2f} $")
        self.ui.label_12.setText(f"{balance:.2f} $")
