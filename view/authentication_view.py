from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Qt
from view.ui_authentication import Ui_Frame_authentication
from view.ui_login import Ui_Frame as Ui_Login
from view.ui_sginup import Ui_Frame as Ui_SignUp
from view.ui_reset_pasword import Ui_Frame as Ui_ResetPassword


class AuthenticationView(QWidget):
    signal_login_clicked = Signal()
    signal_signup_clicked = Signal()
    signal_reset_password_clicked = Signal()
    signal_authentication_success = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame_authentication()
        self.ui.setupUi(self)

        # יצירת הפריימים הפנימיים פעם אחת בלבד
        self.login_view = QWidget()
        self.signup_view = QWidget()
        self.reset_password_view = QWidget()

        self.login_ui = Ui_Login()
        self.signup_ui = Ui_SignUp()
        self.reset_password_ui = Ui_ResetPassword()

        self.login_ui.setupUi(self.login_view)
        self.signup_ui.setupUi(self.signup_view)
        self.reset_password_ui.setupUi(self.reset_password_view)

        # הגדרת כיוון פריסה שמאל לימין לכל פריים פנימי
        self.login_view.setLayoutDirection(Qt.LeftToRight)
        self.signup_view.setLayoutDirection(Qt.LeftToRight)
        self.reset_password_view.setLayoutDirection(Qt.LeftToRight)

        # שמות הלייבלים בתפריט
        self.menu_labels = {
            "login": self.ui.label_login,
            "signup": self.ui.label_2,
            "reset": self.ui.label_3,
        }

        # עיצוב בסיסי לכל הלייבלים (כולל hover)
        base_style = """
            QLabel {
                padding-bottom: 2px;
            }
            QLabel:hover {
                border-bottom: 1px solid #2d7be5;
            }
        """
        for label in self.menu_labels.values():
            label.setStyleSheet(base_style)

        # חיבור אירועים
        self.ui.label_login.mousePressEvent = self._on_login_clicked
        self.ui.label_2.mousePressEvent = self._on_signup_clicked
        self.ui.label_3.mousePressEvent = self._on_reset_password_clicked

        # חיבור הכפתורים הירוקים לסיגנל
        self.login_ui.pushButton.clicked.connect(self._on_authentication_success)
        self.signup_ui.pushButton.clicked.connect(self._on_authentication_success)
        self.reset_password_ui.pushButton.clicked.connect(self._on_authentication_success)

        # טעינת פריים ברירת המחדל (login)
        self.set_content(self.login_view)
        self.set_active_menu("login")

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

    def set_active_menu(self, active):
        for key, label in self.menu_labels.items():
            if key == active:
                # קו תחתון קבוע + hover
                label.setStyleSheet("""
                    QLabel {
                        border-bottom: 2px solid #2d7be5;
                        padding-bottom: 2px;
                        font-weight: bold;
                    }
                    QLabel:hover {
                        border-bottom: 2px solid #2d7be5;
                    }
                """)
            else:
                # רק hover
                label.setStyleSheet("""
                    QLabel {
                        padding-bottom: 2px;
                    }
                    QLabel:hover {
                        border-bottom: 2px solid #2d7be5;
                    }
                """)

    def _on_login_clicked(self, event):
        """מעבר לפריים login."""
        self.set_content(self.login_view)
        self.set_active_menu("login")

    def _on_signup_clicked(self, event):
        """מעבר לפריים signup."""
        self.set_content(self.signup_view)
        self.set_active_menu("signup")

    def _on_reset_password_clicked(self, event):
        """מעבר לפריים reset_password."""
        self.set_content(self.reset_password_view)
        self.set_active_menu("reset")

    def _on_authentication_success(self):
        """שחרור סיגנל כאשר לוחצים על כפתור ירוק."""
        self.signal_authentication_success.emit()