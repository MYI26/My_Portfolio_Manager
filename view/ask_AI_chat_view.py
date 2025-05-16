from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from view.ui_python.ui_ask_AI_chat import Ui_AskAIChat

class AskAIChatView(QWidget):
    signal_clear_clicked = Signal()
    signal_question_submitted = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_AskAIChat()
        self.ui.setupUi(self)

        # Signals
        self.ui.button_clear.clicked.connect(self._on_clear_clicked)
        self.ui.button_send.clicked.connect(self._on_send_clicked)
        self.ui.label_loading.setVisible(False)

    def _on_clear_clicked(self):
        self.ui.text_input.clear()
        self.signal_clear_clicked.emit()

    def _on_send_clicked(self):
        question = self.ui.text_input.toPlainText().strip()
        if question:
            self.signal_question_submitted.emit(question)

    def display_loading(self):
        self.ui.label_loading.setStyleSheet("color: #52b74d; font-size: 16px;")
        self.ui.label_loading.setVisible(True)
        self.ui.label_answer.setText("")

    def display_response(self, answer):
        self.ui.label_loading.setVisible(False)
        self.ui.label_answer.setStyleSheet("padding: 10px; font-size: 14px;")
        self.ui.label_answer.setText(answer)
