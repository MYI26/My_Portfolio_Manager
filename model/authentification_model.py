import requests 

AUTH_URL = "https://localhost:7229/api/Auth"  

class AuthModel:
    def __init__(self):
        pass

    def signup_user(self, email, password):
        try:
            url = f"{AUTH_URL}/register"
            payload = {
                "email": email,
                "password": password
            }
            response = requests.post(url, json=payload, verify=False) 
            response.raise_for_status()
            return response.json()  #contient Utilisateur 
        except Exception as e:
            print(f"[Model] Erreur lors de l'inscription : {e}")
            return {"error": str(e)}

    def login_user(self, email, password):
        try:
            url = f"{AUTH_URL}/login"
            payload = {
                "email": email,
                "password": password
            }
            response = requests.post(url, json=payload, verify=False)
            response.raise_for_status()
            return response.json()  #contient Token
        except Exception as e:
            print(f"[Model] Erreur lors de la connexion : {e}")
            return {"error": str(e)}
