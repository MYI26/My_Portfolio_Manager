import requests # type: ignore
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import ssl
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

cloudinary.config(
  cloud_name = 'dialozuw5',     
  api_key = '428831338893553', 
  api_secret = 'Sfi4gj8l2LrHsIOu5OljiPXPyfU'
)

MARKET_URL = "https://localhost:7229/api/market" 

class StockModel:
    def __init__(self, balance):
        self._balance = balance  

    def fetch_stock_data(self, symbol):
        try:
            url = f"{MARKET_URL}/price/{symbol}"  
            response = requests.get(url, verify=False)
            response.raise_for_status()
            return response.json()  
        except requests.RequestException as e:
            print(f"Error fetching stock data: {e}")
            return None

    def get_static_data(self):
        return {
            "ticker": "TSLA",
            "name": "TESLA LTD",
            "price": 80.25,
            "open": 80.15,
            "close": 80.40,
            "pourcentage": 0.5
        }

    def get_balance(self) -> float:
        return self._balance

    def update_balance(self, amount: float):
        self._balance += amount  # Positif = gain, négatif = achat

    def can_afford(self, amount: float) -> bool:
        return self._balance >= amount
    
    def send_transaction(self, user_id: str, stock_name: str, quantity: float, price_per_unit: float):
        url = "https://localhost:7229/api/Transactions/buy"
        data = {
            "userId": user_id,
            "stockName": stock_name,
            "quantity": quantity,
            "pricePerUnit": price_per_unit
        }
        print("Payload envoyé :", data)  # pour debug
        response = requests.post(url, json=data, verify=False)
        response.raise_for_status()


    def send_sell_transaction(self, user_id: str, stock_name: str, quantity: float, price_per_unit: float):

        print("Envoi de la transaction de vente...")
        url = "https://localhost:7229/api/Transactions/sell"  # ⚠️ Vérifie que cette route existe bien dans ton API
        payload = {
            "userId": user_id,
            "stockName": stock_name,
            "quantity": quantity,
            "pricePerUnit": price_per_unit
        }
        response = requests.post(url, json=payload, verify=False)
        response.raise_for_status()


    def upload_stock_logo_to_cloudinary(self, logo_url: str, ticker: str, user_id: str):

        if not logo_url:
            print(f"❌ Aucune URL de logo fournie pour {ticker}")
            return None

        # Création d'une requête avec un User-Agent (sinon 403)
        req = Request(logo_url, headers={'User-Agent': 'Mozilla/5.0'})

        try:
            # 2. Télécharger l'image
            with urlopen(req, context=ssl._create_unverified_context()) as response:
                image_data = response.read()

                # 3. Sauvegarder temporairement le fichier localement (Cloudinary prend un chemin ou binaire)
                temp_filename = f"temp_{ticker}_{user_id}.png"
                with open(temp_filename, "wb") as f:
                    f.write(image_data)

            # 4. Upload sur Cloudinary avec un ID clair
            public_id = f"logos/{user_id}_{ticker}"  # Exemple: logos/user123_AAPL
            result = cloudinary.uploader.upload(
                temp_filename,
                public_id=public_id,
                overwrite=True
            )

            print(f"✅ Logo {ticker} uploadé avec succès pour l'utilisateur {user_id} : {result['secure_url']}")

            # 5. Supprimer le fichier temporaire
            os.remove(temp_filename)

            return result['secure_url']

        except HTTPError as e:
            print(f"❌ HTTP Error lors du téléchargement du logo : {e}")
        except URLError as e:
            print(f"❌ URL Error lors du téléchargement du logo : {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")

        return None
