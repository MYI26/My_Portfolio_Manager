import requests 

AI_URL = "https://localhost:7229/api/ai/ask"  # Gateway vers l’agent AI

class AIModel:
    def __init__(self):
        pass

    def ask_ai_question(self, question):
        try:
            payload = {"question": question}
            response = requests.post(AI_URL, json=payload, verify=False)
            response.raise_for_status()
            return response.json().get("response", "Réponse inconnue")
  
        except Exception as e:
            print(f"[Model] Erreur lors de l'envoi de la question à l'agent AI : {e}")
            return "Erreur lors de la communication avec l'agent AI."
