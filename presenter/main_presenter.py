# 📄 presenter/main_presenter.py

from view.main_window_view import MainWindowView
from view.portfolio_view import PortfolioView
from view.history_view import HistoryView
from view.new_action_view import NewActionView
from view.ask_AI_chat_view import AskAIChatView
from model.portfolio_model import PortfolioModel
from model.transactions_model import TransactionModel
from threading import Timer


class MainPresenter:
    def __init__(self, balance, user_id):
        self.main_window_view = MainWindowView()
        self.new_action_view = NewActionView()
        self.ask_ai_chat_view = AskAIChatView()

        # חיבור סיגנלים
        self.main_window_view.signal_new_action_clicked.connect(self.show_new_action)
        self.main_window_view.signal_ask_ai_chat_clicked.connect(self.show_ask_ai_chat)

        self.user_id = user_id
        self.current_view = None

        self.ask_ai_chat_view.signal_clear_clicked.connect(self._on_clear_clicked)
        self.ask_ai_chat_view.signal_question_submitted.connect(self._on_question_submitted)
        # חיבור כפתור home
        self.main_window_view.ui.pushButton_hom.clicked.connect(self.load_portfolio)
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.model = PortfolioModel()
        self.balance = balance
        self.load_portfolio()
        self.history_view = HistoryView()
        self.transaction_model = TransactionModel()
        self.main_window_view.ui.pushButton_hom_2.clicked.connect(self.load_history)
        self.transaction_history_data = []
        self.history_view.on_filter_changed(self.on_filter_changed)  # 🔁 Ajout ici

    def show_view(self):
        self.main_window_view.show()

    def show_new_action(self):
        """הצגת פריים New Action."""
        layout = self.main_window_view.ui.frame_content.layout()
        self.clear_layout(layout)
        layout.addWidget(self.new_action_view)

    def show_ask_ai_chat(self):
        """הצגת פריים Ask AI Chat."""
        layout = self.main_window_view.ui.frame_content.layout()
        self.clear_layout(layout)
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
        portfolio_view.display_portfolio(detailed_data, self.user_id)
        portfolio_view.display_portfolio_totals(
        capital_total, valeur_actuelle_total, performance_total_d, performance_total_p, self.balance
        )

    def load_history(self):
        self.clear_layout(self.main_window_view.ui.frame_content.layout())
        self.main_window_view.ui.frame_content.layout().addWidget(self.history_view)
        self.current_view = self.history_view

        self.history_view.on_filter_changed(self.on_filter_changed)

        # Nouvelle ligne : on charge les données depuis le modèle
        self.load_transaction_history(self.user_id)  # ⚠️ adapter le nom de l’utilisateur

    def load_transaction_history(self, user_id):
        self.transaction_history_data = self.transaction_model.fetch_history(user_id)
        self.display_filtered_history(self.user_id)

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

    def display_filtered_history(self, user_id):
        if not self.current_view:
            return

        selected_filter = self.current_view.get_selected_filter()
        self.current_view.clear_history()

        for op in self.transaction_history_data:
            if op["userId"] != user_id:
                continue

            if selected_filter == "Buy" and op["type"].upper() != "BUY":
                continue
            if selected_filter == "Sale" and op["type"].upper() != "SELL":
                continue

            symbol = op["stockName"]
            company = symbol
            date = op["date"].split("T")[0]
            order_type = op["type"].capitalize()
            price = op["pricePerUnit"]
            qty = op["quantity"]
            total = price * qty

            cloud_name = 'dialozuw5'
            public_id = f"logos/{user_id}_{symbol}"  # Ex: logos/user123_AAPL
            logo_url = f"https://res.cloudinary.com/{cloud_name}/image/upload/{public_id}.png"
            print(f"[DEBUG] Logo URL: {logo_url}")
            self.current_view.add_history_item(logo_url, company, date, order_type, price, qty, total)

    def on_filter_changed(self):
        self.display_filtered_history(self.user_id)
