# 📄 presenter/main_presenter.py

from view.main_window_view import MainWindowView
from view.portfolio_view import PortfolioView
from view.history_view import HistoryView
from view.new_action_view import NewActionView
from view.ask_AI_chat_view import AskAIChatView
from model.portfolio_model import PortfolioModel
from threading import Timer

class MainPresenter:
    def __init__(self):
        self.main_window_view = MainWindowView()
        self.ask_ai_chat_view = AskAIChatView()

        # חיבור סיגנלים
        self.main_window_view.signal_ask_ai_chat_clicked.connect(self.show_ask_ai_chat)
        self.ask_ai_chat_view.signal_clear_clicked.connect(self._on_clear_clicked)
        self.ask_ai_chat_view.signal_question_submitted.connect(self._on_question_submitted)

    def show_view(self):
        """הצגת החלון הראשי."""
        self.main_window_view.show()

    def show_ask_ai_chat(self):
        """הצגת פריים Ask AI Chat."""
        layout = self.main_window_view.ui.frame_content.layout()
        if layout is not None:
            # נקה את התוכן הקיים
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            # הוסף את הפריים החדש
            layout.addWidget(self.ask_ai_chat_view)

    def load_portfolio(self):
        self.clear_layout(self.main_window_view.ui.frame_content.layout())

        portfolio_view = PortfolioView()
        self.main_window_view.ui.frame_content.layout().addWidget(portfolio_view)
        self.current_view = portfolio_view

        data = self.model.get_user_portfolio("ben")
        invested = self.model.get_invested_capital("ben")
        detailed_data = []
        capital_total = 0.0
        valeur_actuelle_total = 0.0

        for symbol, qty in data.items():
            current_price = self.model.get_current_price(symbol)
            initial_capital = invested.get(symbol, 0.0)

            perf_d = current_price * qty - initial_capital
            perf_p = (perf_d / initial_capital * 100) if initial_capital != 0 else 0
            total_current_price = current_price * qty

            detailed_data.append({
                "symbol": symbol,
                "quantity": qty,
                "current_price": total_current_price,
                "invested_capital": initial_capital,
                "perf_d": perf_d,
                "perf_p": perf_p
            })

            capital_total += initial_capital
            valeur_actuelle_total += total_current_price

        performance_total_d = valeur_actuelle_total - capital_total
        performance_total_p = (performance_total_d / capital_total * 100) if capital_total != 0 else 0    
        print("[DEBUG] Données envoyées à la vue :", detailed_data)
        portfolio_view.display_portfolio(detailed_data)
        portfolio_view.display_portfolio_totals(
        capital_total, valeur_actuelle_total, performance_total_d, performance_total_p
        )

    def load_history(self):
        self.clear_layout(self.main_window_view.ui.frame_content.layout())
        history = HistoryView()
        self.main_window_view.ui.frame_content.layout().addWidget(history)
        self.current_view = history

    def load_new_action(self):
        self.clear_layout(self.main_window_view.ui.frame_content.layout())
        new_action = NewActionView()
        self.main_window_view.ui.frame_content.layout().addWidget(new_action)
        self.current_view = new_action

    def _on_clear_clicked(self):
        """טיפול בלחיצה על כפתור Clear."""
        print("Clear button clicked")

    def _on_question_submitted(self, question):
        """טיפול בשאלה שנשלחה."""
        print(f"[DEBUG] שאלה שנשלחה: {question}")
        self.ask_ai_chat_view.show_loading()
        self._simulate_long_answer()

    def _simulate_long_answer(self):
        """סימולציה של תגובה ארוכה."""
        predefined_answer = (
            "This is a long response from the AI. It is designed to test the scrolling "
            "functionality and ensure that the UI behaves correctly when displaying a "
            "large amount of text. The answer continues with more details, explanations, "
            "and examples to simulate a realistic response. This is only a test, so the "
            "content is static and does not come from an actual server. Thank you for "
            "testing the Ask AI Chat feature!"
        )

        # הצגת התשובה לאחר 5 שניות (במקום 20 שניות)
        Timer(10.0, lambda: self.ask_ai_chat_view.show_answer(predefined_answer)).start()

    def clear_layout(self, layout):
        """ניקוי תוכן הלייאאוט."""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
