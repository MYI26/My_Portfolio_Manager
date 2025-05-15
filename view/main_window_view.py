from PySide6.QtWidgets import QFrame, QVBoxLayout  # הוספת QFrame לייבוא
from PySide6.QtCore import Qt, Signal
from view.ui_main_window import Ui_Frame_main_window
from view.portfolio_view import PortfolioView


class MainWindowView(QFrame):  # שינוי הירושה ל-QFrame
    signal_new_action_clicked = Signal()
    signal_ask_ai_chat_clicked = Signal()  # הגדרת הסיגנל

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Frame_main_window()
        self.ui.setupUi(self)

        # הגדרת כיוון פריסת הלייאאוט
        self.ui.frame_header.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_content.setLayoutDirection(Qt.RightToLeft)

        # הוספת QVBoxLayout ל-frame_content
        self.ui.frame_content_layout = QVBoxLayout(self.ui.frame_content)
        self.ui.frame_content.setLayout(self.ui.frame_content_layout)

        self.portfolio_view = PortfolioView()
        self.ui.frame_content.layout().addWidget(self.portfolio_view)

        # חיבור הכפתורים לסיגנלים
        self.ui.pushButton_action.clicked.connect(self._on_new_action_clicked)  # עדכון השם
        self.ui.pushButton_AiChat.clicked.connect(self._on_ask_ai_chat_clicked)

    def _on_new_action_clicked(self):
        """Emit the signal when the 'New Action' button is clicked."""
        self.signal_new_action_clicked.emit()

    def _on_ask_ai_chat_clicked(self):
        """Emit the signal when the 'Ask AI Chat' button is clicked."""
        self.signal_ask_ai_chat_clicked.emit()
