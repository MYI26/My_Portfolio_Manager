import os
import requests  # pour faire l'appel API
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer
from view.ui_stock_info import Ui_Form

class StockInfoView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # נתיב יחסי ללוגו
        logo_path = os.path.join("resources", "logos", "logo.png")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            self.ui.labelLogo.setPixmap(pixmap)
            self.ui.labelLogo.setScaledContents(True)
        else:
            print(f"❌ Logo not found at: {logo_path}")

        # Configurer l'appel périodique à l'API
        self.api_url = "https://localhost:7105/api/Data_Market_/price/AAPL"
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stock_info)
        self.timer.start(5000)  # toutes les 5 secondes

        # Appel initial
        self.update_stock_info()

    def update_stock_info(self):
        try:
            response = requests.get(self.api_url, verify=False)  # Assurez-vous que l'URL est correcte
            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")  # ➜ Voir le contenu même s'il y a une erreur
            if response.status_code == 200:
                data = response.json()
                print(f"Data: {data}")  # ➜ voir la vraie structure des données
                self.ui.labelSymbol.setText(data.get("ticker", "N/A"))
                self.ui.labelCompany.setText(data.get("name", "Unknown"))
                self.ui.labelCurntPriceValue.setText(f"{data.get('price', 'N/A')} USD")
                self.ui.openPriceValue.setText(f"{data.get('open', 'N/A')} USD")
                self.ui.ClosePriceValue.setText(f"{data.get('close', 'N/A')} USD")
                self.ui.labelChange.setText(f"{data.get('pourcentage', 'N/A')} %")
            else:
                print(f"Erreur API: {response.status_code}")
        except Exception as e:
            print(f"Erreur de connexion à l'API: {e}")
