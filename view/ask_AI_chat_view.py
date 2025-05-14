from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from view.ui_ask_AI_chat import Ui_AskAIChat  # Import the generated UI class

class AskAIChatView(QWidget):
    signal_clear_clicked = Signal()
    signal_question_submitted = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_AskAIChat()
        self.ui.setupUi(self)

        # Connect signals
        self.ui.button_clear.clicked.connect(self._on_clear_clicked)
        self.ui.button_send.clicked.connect(self._on_send_clicked)

    def _on_clear_clicked(self):
        """Clear the text input."""
        self.ui.text_input.clear()
        self.signal_clear_clicked.emit()

    def _on_send_clicked(self):
        """Emit the question submitted signal when the Send button is clicked."""
        question = self.ui.text_input.toPlainText().strip()
        if question:
            self.signal_question_submitted.emit(question)

    def show_loading(self):
        """Show the loading message."""
        self.ui.label_loading.setStyleSheet("color: #52b74d; font-size: 16px;")  # שינוי צבע וגודל הטקסט
        self.ui.label_loading.setVisible(True)  # הצגת הודעת ההמתנה
        self.ui.label_answer.setText("")  # ניקוי אזור התשובה

    def show_answer(self, answer):
        """Show the AI's answer."""
        self.ui.label_loading.setVisible(False)  # הסתרת הודעת ההמתנה
        self.ui.label_answer.setStyleSheet("padding: 10px; font-size: 14px;")  # הוספת רווח פנימי וגודל פונט
        self.ui.label_answer.setText(answer)  # הצגת התשובה