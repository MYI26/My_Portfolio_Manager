import sys
import requests
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)

class TransactionClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Client - Transactions Server")
        self.setGeometry(100, 100, 550, 450)
        self.api_base = "https://localhost:7207/api/Transactions"

        # ✅ Identifiant utilisateur (statique ou récupéré dynamiquement)
        self.USER_ID = "user123"  # À remplacer par ton vrai ID

        layout = QVBoxLayout()

        # --- Nom de l'action ---
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("Nom de l'action :"))
        self.name_input = QLineEdit("Apple")
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)

        # --- Quantité ---
        qty_layout = QHBoxLayout()
        qty_layout.addWidget(QLabel("Quantité :"))
        self.qty_input = QLineEdit("1")
        qty_layout.addWidget(self.qty_input)
        layout.addLayout(qty_layout)

        # --- Prix unitaire ---
        price_layout = QHBoxLayout()
        price_layout.addWidget(QLabel("Prix unitaire (€) :"))
        self.price_input = QLineEdit("100.0")
        price_layout.addWidget(self.price_input)
        layout.addLayout(price_layout)

        # --- Boutons ---
        btn_layout = QHBoxLayout()
        self.buy_btn = QPushButton("Acheter")
        self.sell_btn = QPushButton("Vendre")
        self.refresh_btn = QPushButton("Afficher l'historique")
        btn_layout.addWidget(self.buy_btn)
        btn_layout.addWidget(self.sell_btn)
        btn_layout.addWidget(self.refresh_btn)
        layout.addLayout(btn_layout)

        # --- Historique ---
        self.history_display = QTextEdit()
        self.history_display.setReadOnly(True)
        layout.addWidget(QLabel("Historique des transactions :"))
        layout.addWidget(self.history_display)

        self.setLayout(layout)

        # Connexions
        self.buy_btn.clicked.connect(lambda: self.send_transaction("buy"))
        self.sell_btn.clicked.connect(lambda: self.send_transaction("sell"))
        self.refresh_btn.clicked.connect(self.load_history)

    def send_transaction(self, operation):
        try:
            name = self.name_input.text().strip()
            qty = int(self.qty_input.text())
            price = float(self.price_input.text())

            payload = {
                "userId": self.USER_ID,
                "stockName": name,
                "quantity": qty,
                "pricePerUnit": price
            }

            url = f"{self.api_base}/{operation}"  # ex: /buy ou /sell
            response = requests.post(url, json=payload, verify=False)

            if response.status_code == 200:
                QMessageBox.information(self, "Succès", f"{operation.capitalize()} effectué avec succès.")
                self.load_history()
            else:
                QMessageBox.warning(self, "Erreur", f"Erreur {response.status_code} : {response.text}")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Exception : {e}")

    def load_history(self):
        try:
            url = f"{self.api_base}/history/{self.USER_ID}"  # ✅ userId dans le PATH
            response = requests.get(url, verify=False)

            if response.status_code == 200:
                history = response.json()
                self.history_display.clear()
                for item in history:
                    self.history_display.append(
                        f"{item['date']} - {item['type']} : {item['quantity']} x {item['stockName']} à {item['pricePerUnit']}€"
                    )
            else:
                QMessageBox.warning(self, "Erreur", f"Erreur {response.status_code} : {response.text}")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Exception : {e}")


if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    app = QApplication(sys.argv)
    window = TransactionClient()
    window.show()
    sys.exit(app.exec())
