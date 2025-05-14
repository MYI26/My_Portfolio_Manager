# 📄 view/portfolio_view.py

from PySide6.QtWidgets import QFrame, QListWidgetItem
from view.ui_portfolio import Ui_Frame_Portfolio
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QLabel, QHBoxLayout


class PortfolioView(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame_Portfolio()
        self.ui.setupUi(self)

        # הגדרת כיוון ה-QListWidget לשמאל לימין
        self.ui.listWidgetStocks.setLayoutDirection(Qt.LeftToRight)

        # דוגמה סטטית: יצירת שלושה אייטמים
        self.add_stock_item("resources/logos/apple.png", "Apple Inc.", 15, 2200, 2400, 200, 9.1)
        self.add_stock_item("resources/logos/tesla.png", "Tesla", 8, 1600, 1700, 100, 6.25)
        self.add_stock_item("resources/logos/nvidia.png", "NVIDIA", 5, 1400, 1300, -100, -7.1)
        self.add_stock_item("resources/logos/google.png", "Google", 10, 3000, 3100, 100, 3.33)
        self.add_stock_item("resources/logos/microsoft.png", "Microsoft", 12, 2400, 2500, 100, 4.17)

    def add_stock_item(self, logo_path, company, stock, total_price, current_price, perf_d, perf_p):
        item = QListWidgetItem(self.ui.listWidgetStocks)
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

        # STOCKS
        label_stock = QLabel(str(stock))
        layout.addWidget(label_stock)

        # TOTAL PRICE
        label_total = QLabel(f"{total_price:.2f} $")
        layout.addWidget(label_total)

        # CURRENT PRICE
        label_current = QLabel(f"{current_price:.2f} $")
        layout.addWidget(label_current)

        # PERFORMANCE $
        label_perf_d = QLabel(f"{perf_d:+.2f} $")
        label_perf_d.setStyleSheet("color: green;" if perf_d >= 0 else "color: red;")
        layout.addWidget(label_perf_d)

        # PERFORMANCE %
        label_perf_p = QLabel(f"{perf_p:+.2f} %")
        label_perf_p.setStyleSheet("color: green;" if perf_p >= 0 else "color: red;")
        layout.addWidget(label_perf_p)

        widget.setLayout(layout)
        self.ui.listWidgetStocks.setItemWidget(item, widget)

    def display_portfolio(self, portfolio_data: list):
        self.ui.listWidgetStocks.clear()

        for data in portfolio_data:
            symbol = data["symbol"]
            quantity = data["quantity"]
            current_price = data["current_price"]
            total_price = data["invested_capital"]
            perf_d = data["perf_d"]
            perf_p = data["perf_p"]

            logo_path = f"resources/logos/apple.png"
            company_name = symbol  # pour l’instant on affiche le symbole

            self.add_stock_item(logo_path, company_name, quantity, total_price, current_price, perf_d, perf_p)

    def display_portfolio_totals(self, capital_total, valeur_totale, perf_d, perf_p):
        print("[INFO] TOTALS")
        print(f"Capital investi total : {capital_total:.2f} $")
        print(f"Valeur actuelle totale : {valeur_totale:.2f} $")
        print(f"Performance totale : {perf_d:+.2f} $ ({perf_p:+.2f} %)")

        self.ui.label_2.setText(f"{capital_total:.2f} $")
        self.ui.label_4.setText(f"{valeur_totale:.2f} $")
        self.ui.label_6.setText(f"{perf_d:+.2f} $")
        self.ui.label_8.setText(f"{perf_p:+.2f} %")

        color = "green" if perf_d >= 0 else "red"
        self.ui.label_6.setStyleSheet(f"color: {color}")
        self.ui.label_8.setStyleSheet(f"color: {color}")
