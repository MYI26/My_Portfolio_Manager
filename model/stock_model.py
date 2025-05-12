import requests

class StockModel:
    def __init__(self, api_url):
        self.api_url = api_url

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