from PySide6.QtWidgets import QWidget, QMessageBox # type: ignore
from PySide6.QtCore import Signal, Qt # type: ignore
from view.ui_authentication import Ui_Frame_authentication
from view.ui_login import Ui_Frame as Ui_Login
from view.ui_sginup import Ui_Frame as Ui_SignUp
from view.ui_reset_pasword import Ui_Frame as Ui_ResetPassword


class AuthenticationView(QWidget):
    "icon menu signals"
    signal_login_clicked = Signal()
    signal_signup_clicked = Signal()
    signal_reset_password_clicked = Signal()
    "push button signals"
    signal_push_button_signup = Signal(str,str)  
    signal_push_button_login = Signal(str,str)
    signal_push_button_reset_password = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame_authentication()
        self.ui.setupUi(self)

        #réglages
        self.login_view = QWidget()
        self.signup_view = QWidget()
        self.reset_password_view = QWidget()
        self.login_ui = Ui_Login()
        self.signup_ui = Ui_SignUp()
        self.reset_password_ui = Ui_ResetPassword()
        self.login_ui.setupUi(self.login_view)
        self.signup_ui.setupUi(self.signup_view)
        self.reset_password_ui.setupUi(self.reset_password_view)

        self.login_view.setLayoutDirection(Qt.LeftToRight)
        self.signup_view.setLayoutDirection(Qt.LeftToRight)
        self.reset_password_view.setLayoutDirection(Qt.LeftToRight)

        #icon menu
        self.ui.label_login.mousePressEvent = self._on_login_clicked
        self.ui.label_2.mousePressEvent = self._on_signup_clicked
        self.ui.label_3.mousePressEvent = self._on_reset_password_clicked

        #push button
        self.signup_ui.pushButton.clicked.connect(self._on_push_button_signup)
        self.login_ui.pushButton.clicked.connect(self._on_push_button_login)
        self.reset_password_ui.pushButton.clicked.connect(self._on_push_button_reset_password)

        # טעינת פריים ברירת המחדל (login)
        self.set_content(self.login_view)

    def set_content(self, widget):
        """מחליף את התוכן בפריים התחתון."""
        layout = self.ui.frame_content.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget_to_remove = item.widget()
                if widget_to_remove:
                    widget_to_remove.setParent(None)  # הסרת הווידג'ט מבלי למחוק אותו
            layout.addWidget(widget)

    "icon menu actions"
    def _on_login_clicked(self, event):
        self.set_content(self.login_view)

    def _on_signup_clicked(self, event):
        self.set_content(self.signup_view)

    def _on_reset_password_clicked(self, event):
        self.set_content(self.reset_password_view)

    "push button actions"
    def _on_push_button_signup(self):
        email=self.signup_ui.lineEdit.text()
        password=self.signup_ui.lineEdit_3.text()
        self.signal_push_button_signup.emit(email, password)

    def _on_push_button_login(self):
        email = self.login_ui.lineEdit.text()
        password = self.login_ui.lineEdit_2.text()
        self.signal_push_button_login.emit(email, password)

    def _on_push_button_reset_password(self):
        email = self.reset_password_ui.lineEdit_email.text()
        self.signal_push_button_reset_password.emit(email)

    "show message"
    def show_message(self, text: str):
        QMessageBox.information(self, "Info", text)

    def show_error(self, text: str):
        QMessageBox.critical(self, "Erreur", text)