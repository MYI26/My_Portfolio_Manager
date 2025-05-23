from datetime import datetime, timedelta
import random
import requests # type: ignore

MARKET_URL = "https://localhost:7229/api/market"

class StockChartModel:
    def __init__(self):
        pass

    def get_static_data(self, range_type: str, symbol: str):
        print(f"[Model] Fetching REAL data for {symbol} with range: {range_type}")

        try:
            url = f"{MARKET_URL}/history/{symbol}"  
            response = requests.get(url, verify=False) 
            if response.status_code == 404:
                print(f"[Model] Error: Data not found for {symbol} at {url}")
                return [], []
            response.raise_for_status()
            data = response.json()

            print(f"[Model] Requesting: {url}")
            print(f"[Model] Response status: {response.status_code}")
            print(f"[Model] Data for 3 months: {data}")


            # Juste après avoir reçu range_type
            range_type = range_type.strip()

            # On choisit la bonne clé dans la réponse
            if range_type == "Last Week":
                history = data["lastWeek"]
            elif range_type == "Last Month":
                history = data["lastMonth"]
            elif range_type == "Last 3 Months":
                history = data["last3Months"]
            else:
                print(f"[Model] Unknown range_type: '{range_type}'")
                return [], []

            # On trie les données par date si besoin (normalement déjà triées)
            history.sort(key=lambda x: x["datetime"])

            prices = [point["close"] for point in history]
            labels = [datetime.strptime(point["datetime"], "%Y-%m-%dT%H:%M:%S").strftime('%d/%m') for point in history]

            print(f"[Model] Prices: {prices}")
            print(f"[Model] Labels: {labels}")
            return prices, labels

        except Exception as e:
            print(f"[Model] Error fetching real data: {e}")
            return [], []