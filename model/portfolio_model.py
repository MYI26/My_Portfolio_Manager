import requests # type: ignore
from collections import deque

TRANSACTIONS_URL = "https://localhost:7229/api/Transactions"  
MARKET_URL = "https://localhost:7229/api/Market" 

class PortfolioModel:
    def get_user_portfolio(self, user_id,):
        url = f"{TRANSACTIONS_URL}/history/{user_id}"
        response = requests.get(url, verify=False)
        events = response.json()

        print("[DEBUG] Événements reçus :", events)

        portfolio = {}

        # Dictionnaire de correspondance (si jamais certains envoient des noms commerciaux)
        corrections = {
            "APPLE": "AAPL",
            "APPL": "AAPL",  # faute de frappe
            "TESLA": "TSLA"
        }

        for event in events:
            # 1. Vérifie que l’event appartient bien à l’utilisateur concerné
            if event.get("userId") != user_id:
                continue

            raw_symbol = event.get("stockName", "").strip().upper()
            symbol = corrections.get(raw_symbol, raw_symbol)  # corriger si besoin

            quantity = event.get("quantity", 0)

            if symbol not in portfolio:
                portfolio[symbol] = 0

            if event.get("type") in ["BUY", "StockPurchasedEvent"]:
                portfolio[symbol] += quantity
            elif event.get("type") in ["SELL", "StockSoldEvent"]:
                portfolio[symbol] -= quantity

        # Nettoyage final : retirer ceux à 0
        portfolio = {k: v for k, v in portfolio.items() if v > 0}

        print("[DEBUG] Portefeuille calculé :", portfolio)
        return portfolio

    def get_current_price(self, symbol):
        try:
            url = f"{MARKET_URL}/price/{symbol}"
            response = requests.get(url, verify=False)
            data = response.json()
            return data.get("price", 0.0)
        except Exception as e:
            print(f"[ERREUR] get_current_price({symbol}):", e)
            return 0.0

    def get_invested_capital(self, user_id):
        url = f"{TRANSACTIONS_URL}/history/{user_id}"
        response = requests.get(url, verify=False)
        events = response.json()

        # { "AAPL": deque([(2, 150), (1, 170)]) }
        purchases = {}

        # Dictionnaire pour corriger les noms
        corrections = {
            "APPLE": "AAPL", "APPL": "AAPL",
            "TESLA": "TSLA"
        }

        for event in events:
            if event.get("userId") != user_id:
                continue

            raw_symbol = event.get("stockName", "").strip().upper()
            symbol = corrections.get(raw_symbol, raw_symbol)
            quantity = event.get("quantity", 0)
            price = event.get("pricePerUnit", 0.0)
            event_type = event.get("type")
            if symbol not in purchases:
                purchases[symbol] = deque()

            if event_type in ["BUY", "StockPurchasedEvent"]:
                purchases[symbol].append((quantity, price))

            elif event_type in ["SELL", "StockSoldEvent"]:
                qty_to_sell = quantity

                while qty_to_sell > 0 and purchases[symbol]:
                    qty_available, unit_price = purchases[symbol][0]
                    if qty_available <= qty_to_sell:
                        qty_to_sell -= qty_available
                        purchases[symbol].popleft()
                    else:
                        # Partie vendue sur la dernière tranche
                        purchases[symbol][0] = (qty_available - qty_to_sell, unit_price)
                        qty_to_sell = 0

        # Calcul final du capital investi
        invested_capital = {}
        for symbol, qlist in purchases.items():
            total = sum(q * p for q, p in qlist)
            if total > 0:
                invested_capital[symbol] = total
        print("[DEBUG] Capital investi :", invested_capital)

        return invested_capital