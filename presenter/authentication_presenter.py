from PySide6.QtCore import QObject, Signal # type: ignore
from view.authentication_view import AuthenticationView
from model.authentification_model import AuthModel

class AuthenticationPresenter(QObject):
    signal_authentication_success = Signal(str)

    def __init__(self):
        super().__init__()

        self.model = AuthModel()   
        self.view = AuthenticationView()

        self.view.signal_push_button_signup.connect(self.handle_signup)
        self.view.signal_push_button_login.connect(self.handle_login)

    def show_view(self):
         self.view.show()

    def close_view(self):
         self.view.close()

    def _on_authentication_success(self, email):
        self.signal_authentication_success.emit(email)

    def handle_signup(self, email, password):
        result = self.model.signup_user(email, password)
        print(f"[Presenter] Résultat de l'inscription : {result}")
        if result.get("message") == "Utilisateur créé avec succès.":
            self.view.show_message("Inscription réussie !")
        else:
            self.view.show_error(result.get("Erreur", "Erreur inconnue"))

    def handle_login(self, email, password):
        result = self.model.login_user(email, password)
        print(f"[Presenter] Résultat de la connexion : {result}")
        if "token" in result:
            self.view.show_message("Connexion réussie !")
            self._on_authentication_success(email)
        else:
            self.view.show_error(result.get("Erreur", "Erreur inconnue"))

