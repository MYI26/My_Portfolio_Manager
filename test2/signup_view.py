from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from test2.auth_service import AuthService

class SignUpView(QWidget):
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

        signup_button = QPushButton("Créer le compte")
        signup_button.clicked.connect(self.signup)

        back_button = QPushButton("Retour à la connexion")
        back_button.clicked.connect(self.goto_login)

        layout.addWidget(QLabel("Créer un compte"))
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(signup_button)
        layout.addWidget(back_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def signup(self):
        email = self.email_input.text()
        password = self.password_input.text()
        success = self.auth_service.signup(email, password)
        if success:
            self.status_label.setText("Compte créé ✅")
        else:
            self.status_label.setText("Erreur lors de la création ❌")

    def goto_login(self):
        self.parent.setCurrentWidget(self.parent.login_view)
