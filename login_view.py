from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from auth_service import AuthService

class LoginView(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.auth_service = AuthService()

        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mot de passe")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.status_label = QLabel("")

        login_button = QPushButton("Se connecter")
        login_button.clicked.connect(self.login)

        signup_button = QPushButton("Créer un compte")
        signup_button.clicked.connect(self.goto_signup)

        layout.addWidget(QLabel("Connexion"))
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)
        layout.addWidget(signup_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        token = self.auth_service.login(email, password)
        if token:
            self.status_label.setText("Connexion réussie ✅")
        else:
            self.status_label.setText("Erreur de connexion ❌")

    def goto_signup(self):
        self.parent.setCurrentWidget(self.parent.signup_view)
