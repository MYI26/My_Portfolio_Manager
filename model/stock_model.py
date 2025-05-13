import requests

class StockModel:
    def __init__(self, api_url, balance):
        self.api_url = api_url
        self.stock_price = 80.25  # שווי מניה סטטי לדוגמה
        self.investment_amount = 0.0  # כמות הכסף שהוזנה
        """"""""""""""""""""""""""""""""""""""""""""""""
        self._balance = balance  # Initialisation dynamique

    def fetch_stock_data(self, symbol):
        """
        שולח בקשה לשרת ומחזיר נתוני מניה בפורמט JSON.
        """
        try:
            url = f"{self.api_url}/price/{symbol}"  # מוסיף את הסימבול לכתובת ה-URL
            response = requests.get(url, verify=False)
            response.raise_for_status()
            return response.json()  # מחזיר את הנתונים בפורמט JSON
        except requests.RequestException as e:
            print(f"Error fetching stock data: {e}")
            return None

    def get_static_data(self):
        """
        מחזיר נתונים סטטיים במקרה של כשל.
        """
        return {
            "ticker": "TSLA",
            "name": "TESLA LTD",
            "price": "80.25",
            "open": "80.15",
            "close": "80.40",
            "pourcentage": "0.5"
        }

    def set_investment_amount(self, amount: float):
        """
        שומר את כמות הכסף שהוזנה.
        """
        print(f"[StockModel] Investment amount set to: {amount}")
        self.investment_amount = amount

    def calculate_shares(self) -> float:
        """
        מחשב את כמות המניות שניתן לקנות עבור כמות הכסף שהוזנה.
        """
        if self.stock_price == 0:
            return 0
        return self.investment_amount / self.stock_price


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
        