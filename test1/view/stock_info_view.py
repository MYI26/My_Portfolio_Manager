import os
import requests
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer
from view.ui_stock_info import Ui_Form

class StockInfoView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Chargement du logo
        logo_path = os.path.join("resources", "logos", "logo.png")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            self.ui.labelLogo.setPixmap(pixmap)
            self.ui.labelLogo.setScaledContents(True)
        else:
            print(f"❌ Logo not found at: {logo_path}")

        # ➜ Nouvelle URL de la Gateway
        self.api_url = "https://localhost:7229//api/market/price/AAPL"  # Port de la Gateway

        # Timer pour appel périodique
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stock_info)
        self.timer.start(5000)  # toutes les 5 secondes

        # Appel initial
        self.update_stock_info()

    def update_stock_info(self):
        try:
            response = requests.get(self.api_url, verify=False)
            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")

            if response.status_code == 200:
                data = response.json()
                print(f"Data: {data}")

                # Mise à jour de l'interface avec les données reçues
                self.ui.labelSymbol.setText(data.get("ticker", "N/A"))
                self.ui.labelCompany.setText(data.get("name", "Unknown"))
                self.ui.labelCurntPriceValue.setText(f"{data.get('price', 'N/A')} USD")
                self.ui.openPriceValue.setText(f"{data.get('open', 'N/A')} USD")
                self.ui.ClosePriceValue.setText(f"{data.get('close', 'N/A')} USD")
                self.ui.labelChange.setText(f"{data.get('pourcentage', 'N/A')} %")
            else:
                print(f"Erreur API Gateway: {response.status_code}")
        except Exception as e:
            print(f"Erreur de connexion à la Gateway: {e}")
