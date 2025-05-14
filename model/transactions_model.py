import requests # type: ignore

TRANSACTIONS_URL = "https://localhost:7229/api/Transactions"  

class TransactionModel:
    def __init__(self):
        pass

    def fetch_history(self, user_id):
        try:
            url = f"{TRANSACTIONS_URL}/history/{user_id}"  
            response = requests.get(url, verify=False)  # Désactiver la vérification SSL pour le développement
            response.raise_for_status()
            return response.json()  
        except Exception as e:
            print(f"[Model] Erreur lors de la récupération de l'historique : {e}")
            return []
