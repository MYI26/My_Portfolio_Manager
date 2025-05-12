# 📄 test1/view/stock_info_view.py

import os
from PySide6.QtWidgets import QWidget, QScrollArea, QBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal
from view.ui_stock_info import Ui_Form
from view.stock_chart_view import StockChartView


class StockInfoView(QWidget):
    buy_clicked = Signal()  # סיגנל ללחיצה על כפתור ה-Buy

    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.headerLayout.setDirection(QBoxLayout.RightToLeft)
        self.ui.frameChart.setMinimumHeight(300)

        # טעינת לוגו
        logo_path = os.path.join("resources", "logos", "logo.png")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            self.ui.labelLogo.setPixmap(pixmap)
            self.ui.labelLogo.setScaledContents(True)
        else:
            print(f"❌ Logo not found at: {logo_path}")

        # הוספת גרף עם גלילה אופקית
        self.chart_view = StockChartView()  # יצירת StockChartView ללא פרמטרים
        self.chart_view.setMinimumWidth(600)
        self.chart_view.setFixedHeight(360)

        scroll = QScrollArea()
        scroll.setWidget(self.chart_view)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ui.frameChart.layout().addWidget(scroll)

        # חיבור כפתור ה-Buy לסיגנל
        self.ui.btnBuy.clicked.connect(self.on_buy_clicked)

    def update_stock_info(self, stock_data):
        """
        מעדכן את התצוגה עם נתוני המניה שהתקבלו.
        """
        self.ui.labelSymbol.setText(stock_data.get("ticker", "N/A"))
        self.ui.labelCompany.setText(stock_data.get("name", "Unknown"))
        self.ui.labelCurntPriceValue.setText(f"{stock_data.get('price', 'N/A')} USD")
        self.ui.openPriceValue.setText(f"{stock_data.get('open', 'N/A')} USD")
        self.ui.ClosePriceValue.setText(f"{stock_data.get('close', 'N/A')} USD")
        self.ui.labelChange.setText(f"{stock_data.get('pourcentage', 'N/A')} %")

    def get_chart_view(self):
        """
        מחזיר את ה-StockChartView.
        """
        return self.chart_view

    def on_buy_clicked(self):
        """
        משדר סיגנל כאשר לוחצים על כפתור ה-Buy.
        """
        print("[StockInfoView] Buy button clicked")  # בדיקה
        self.buy_clicked.emit()
