from PySide6.QtWidgets import QFrame, QVBoxLayout
from PySide6.QtCore import Qt, Signal
from view.ui_main_window import Ui_Frame_main_window
from view.portfolio_view import PortfolioView

class MainWindowView(QFrame):
    signal_new_action_clicked = Signal()
    signal_ask_ai_chat_clicked = Signal()
    signal_home_clicked = Signal()
    signal_history_clicked = Signal()  # הוספה

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Frame_main_window()
        self.ui.setupUi(self)

        self.ui.frame_header.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_content.setLayoutDirection(Qt.RightToLeft)

        
        self.ui.frame_content_layout = QVBoxLayout(self.ui.frame_content)
        self.ui.frame_content.setLayout(self.ui.frame_content_layout)

        self.portfolio_view = PortfolioView()
        self.ui.frame_content.layout().addWidget(self.portfolio_view)

        
        self.menu_buttons = {
            "home": self.ui.pushButton_hom,
            "action": self.ui.pushButton_action,
            "ai": self.ui.pushButton_AiChat,
            "history": self.ui.pushButton_hom_2,  # הוספה
        }

        # --- עיצוב בסיסי לכל הכפתורים ---
        base_style = """
            QPushButton {
                border: none;
                background: transparent;
                padding-bottom: 2px;
                font-size: 18px;
            }
            QPushButton:hover {
                border-bottom: 2px solid #2d7be5;
            }
            QPushButton:focus {
                outline: none;
                border: none;
            }
        """
        for btn in self.menu_buttons.values():
            btn.setStyleSheet(base_style)

        # חיבור הכפתורים לסיגנלים
        self.ui.pushButton_action.clicked.connect(self._on_new_action_clicked)
        self.ui.pushButton_AiChat.clicked.connect(self._on_ask_ai_chat_clicked)
        self.ui.pushButton_hom.clicked.connect(self._on_home_clicked)
        self.ui.pushButton_hom_2.clicked.connect(self._on_history_clicked)  # הוספה

        # ברירת מחדל - הבית דלוק
        self.set_active_menu_button("home")

    def set_active_menu_button(self, active):
        for key, btn in self.menu_buttons.items():
            if key == active:
                btn.setStyleSheet("""
                    QPushButton {
                        border: none;
                        background: transparent;
                        border-bottom: 1px solid #2d7be5;
                        padding-bottom: 2px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        border-bottom: 1px solid #2d7be5;
                    }
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton {
                        border: none;
                        background: transparent;
                        padding-bottom: 2px;
                        font-size: 14px;
                    }
                    QPushButton:hover {
                        border-bottom: 1px solid #2d7be5;
                    }
                """)

    def _on_new_action_clicked(self):
        self.signal_new_action_clicked.emit()
        self.set_active_menu_button("action")

    def _on_ask_ai_chat_clicked(self):
        self.signal_ask_ai_chat_clicked.emit()
        self.set_active_menu_button("ai")

    def _on_home_clicked(self):
        self.signal_home_clicked.emit()
        self.set_active_menu_button("home")

    def _on_history_clicked(self):
        self.signal_history_clicked.emit()
        self.set_active_menu_button("history")
