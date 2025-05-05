import requests

class AuthService:
    def __init__(self):
        self.api_url = "https://localhost:7229/api/auth"
        self.token = None

    def login(self, email, password):
        url = f"{self.api_url}/login"
        data = {"email": email, "password": password}
        try:
            response = requests.post(url, json=data,verify=False)
            if response.status_code == 200:
                self.token = response.json().get("token")
                print("Token JWT :", self.token)
                return self.token
            else:
                print("Erreur de login :", response.status_code)
                return None
        except Exception as e:
            print("Exception :", e)
            return None

    def signup(self, email, password):
        url = f"{self.api_url}/register"
        data = {"email": email, "password": password}
        try:
            response = requests.post(url, json=data,verify=False)
            return response.status_code == 200
        except Exception as e:
            print("Exception :", e)
            return False
