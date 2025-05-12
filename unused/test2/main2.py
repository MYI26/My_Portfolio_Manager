import sys
from PySide6.QtWidgets import QApplication, QStackedWidget
from test2.login_view import LoginView
from test2.signup_view import SignUpView

class AuthApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.login_view = LoginView(self)
        self.signup_view = SignUpView(self)

        self.addWidget(self.login_view)
        self.addWidget(self.signup_view)

        self.setCurrentWidget(self.login_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthApp()
    window.setWindowTitle("Auth0 PySide6 Login")
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
