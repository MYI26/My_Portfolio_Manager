import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
)
from PySide6.QtCore import Qt
import urllib3
urllib3.disable_warnings()



class InvestmentAdvisorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conseiller IA Boursier")
        self.setMinimumSize(600, 400)

        # Interface layout
        self.layout = QVBoxLayout()

        self.title = QLabel("Pose ta question d'investissement à l'IA")
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)

        self.input_question = QTextEdit()
        self.input_question.setPlaceholderText("Ex : Est-ce un bon moment pour acheter des actions Tesla ?")
        self.layout.addWidget(self.input_question)

        self.send_button = QPushButton("Envoyer à l'IA")
        self.send_button.clicked.connect(self.ask_ai)
        self.layout.addWidget(self.send_button)

        self.response_label = QLabel("Réponse de l'IA :")
        self.layout.addWidget(self.response_label)

        self.response_text = QTextEdit()
        self.response_text.setReadOnly(True)
        self.layout.addWidget(self.response_text)

        self.setLayout(self.layout)

    def ask_ai(self):
        question = self.input_question.toPlainText().strip()
        if not question:
            self.response_text.setText("❌ Veuillez entrer une question.")
            return

        try:
            response = requests.post(
                "https://localhost:7087/api/investment/ask",
                json={"question": question},
                verify=False
            )
            if response.status_code == 200:
                answer = response.json().get("response", "Pas de réponse.")
                self.response_text.setText(answer)
            else:
                self.response_text.setText(f"Erreur {response.status_code} : {response.text}")
        except Exception as e:
            self.response_text.setText(f"Exception : {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InvestmentAdvisorUI()
    window.show()
    sys.exit(app.exec())
