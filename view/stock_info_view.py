import os
from PySide6.QtWidgets import QWidget, QScrollArea, QBoxLayout # type: ignore
from PySide6.QtGui import QPixmap # type: ignore
from PySide6.QtCore import Qt, Signal # type: ignore
from view.ui_stock_info import Ui_Form
from view.stock_chart_view import StockChartView
from urllib.request import urlopen
from PySide6.QtCore import QByteArray # type: ignore
import urllib3 # type: ignore
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from urllib.request import urlopen, Request
import ssl


class StockInfoView(QWidget):
    buy_clicked = Signal() 
    sale_clicked = Signal()  

    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.ui.headerLayout.setDirection(QBoxLayout.RightToLeft)
        self.ui.frameChart.setMinimumHeight(300)

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

         # חיבור כפתור ה-Sale לסיגנל
        self.ui.btnSale.clicked.connect(self.on_sale_clicked)

        self.logo_path = ""


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
        logo_url = stock_data.get("logoUrl")
        self.logo_path = logo_url
        logo_path = os.path.join("resources", "logos", "logo.png")
        if logo_url:
            req = Request(
            logo_url,
            headers={'User-Agent': 'Mozilla/5.0'}  # Fait croire que c'est un navigateur
            )
            try:
                with urlopen(req, context=ssl._create_unverified_context()) as response:
                    data = response.read()
                    pixmap = QPixmap()
                    pixmap.loadFromData(QByteArray(data))
                    self.ui.labelLogo.setPixmap(pixmap)
                    self.ui.labelLogo.setScaledContents(True)
            except Exception as e:
                print(f"❌ Failed to load logo from URL: {logo_url} ({e})")
                if os.path.exists(logo_path):
                    pixmap = QPixmap(logo_path)
                    self.ui.labelLogo.setPixmap(pixmap)
                    self.ui.labelLogo.setScaledContents(True)

    def get_chart_view(self):
        return self.chart_view

    def on_buy_clicked(self):
        print("[StockInfoView] Buy button clicked")  # בדיקה
        self.buy_clicked.emit()

    def on_sale_clicked(self):
        print("[StockInfoView] Sale button clicked")  # בדיקה
        self.sale_clicked.emit()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def get_current_stock_name(self) -> str:
        return self.ui.labelSymbol.text()  # ou label du nom d'action

    def get_current_stock_price(self) -> float:
        price_text = self.ui.labelCurntPriceValue.text().split()[0]  # Extract the numeric part
        return float(price_text)
    
    def get_current_logo_url(self) -> str:
        return self.logo_path