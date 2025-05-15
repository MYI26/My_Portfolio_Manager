from view.main_window_view import MainWindowView
from view.portfolio_view import PortfolioView
from view.history_view import HistoryView
from view.new_action_view import NewActionView
from view.ask_AI_chat_view import AskAIChatView
from model.ask_AI_chat_model import AIModel
from model.portfolio_model import PortfolioModel
from model.transactions_model import TransactionModel
from threading import Timer
from presenter.authentication_presenter import AuthenticationPresenter
from presenter.stock_presenter import StockPresenter


class MainPresenter:

    def __init__(self, balance):
        self.balance = balance
        

        self.authentication_presenter = AuthenticationPresenter()

        self.authentication_presenter.signal_authentication_success.connect(self._on_authentication_success)

        self.main_window_view = MainWindowView()
        self.new_action_view = NewActionView()
        self.ask_ai_chat_view = AskAIChatView()
        self.ask_ai_chat_model = AIModel()
        self.current_view = None

        
        self.main_window_view.signal_new_action_clicked.connect(self.show_new_action)
        self.main_window_view.signal_ask_ai_chat_clicked.connect(self.show_ask_ai_chat)
        self.new_action_view.stock_selected.connect(self.on_stock_selected)
        self.ask_ai_chat_view.signal_clear_clicked.connect(self._on_clear_clicked)
        self.ask_ai_chat_view.signal_question_submitted.connect(self.on_question_submitted)
       
        self.main_window_view.ui.pushButton_hom.clicked.connect(self.show_main_window)
        
        self.model = PortfolioModel()
        self.portfolio_view = PortfolioView()
        self.portfolio_view.stock_selected.connect(self.on_stock_selected)
        self.history_view = HistoryView()
        self.transaction_model = TransactionModel()


        self.portfolio_view.stock_selected.connect(self.on_stock_selected)
        self.main_window_view.ui.pushButton_hom_2.clicked.connect(self.load_history)
        self.transaction_history_data = []
        self.history_view.on_filter_changed(self.on_filter_changed)  

    def show_view(self):
        self.authentication_presenter.show_view()

    def _on_authentication_success(self, email):
        MainPresenter.user_id = email
        self.show_main_window()
        self.authentication_presenter.close_view()

    def show_main_window(self):
        self.load_portfolio(MainPresenter.user_id)
        self.main_window_view.show()

    def show_new_action(self):
        layout = self.main_window_view.ui.frame_content.layout()
        self.clear_layout(layout)
        layout.addWidget(self.new_action_view)

    def show_ask_ai_chat(self):
        layout = self.main_window_view.ui.frame_content.layout()
        self.clear_layout(layout)
        layout.addWidget(self.ask_ai_chat_view)

    def load_portfolio(self, user_id):
        self.clear_layout(self.main_window_view.ui.frame_content.layout())
        self.main_window_view.ui.frame_content.layout().addWidget(self.portfolio_view)
        self.current_view = self.portfolio_view

        data = self.model.get_user_portfolio(user_id)
        invested = self.model.get_invested_capital(user_id)
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
        self.portfolio_view.display_portfolio(detailed_data, self.user_id)
        self.portfolio_view.display_portfolio_totals(
        capital_total, valeur_actuelle_total, performance_total_d, performance_total_p, self.balance
        )

    def load_history(self):
        self.clear_layout(self.main_window_view.ui.frame_content.layout())
        self.main_window_view.ui.frame_content.layout().addWidget(self.history_view)
        self.current_view = self.history_view

        self.history_view.on_filter_changed(self.on_filter_changed)

        self.load_transaction_history(self.user_id)  

    def load_transaction_history(self, user_id):
        self.transaction_history_data = self.transaction_model.fetch_history(user_id)
        self.display_filtered_history(self.user_id)

    def _on_clear_clicked(self):
        print("Clear button clicked")

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)  # ⬅️ au lieu de widget.deleteLater()


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
            public_id = f"logos/{user_id}_{symbol}"  
            logo_url = f"https://res.cloudinary.com/{cloud_name}/image/upload/{public_id}.png"
            print(f"[DEBUG] Logo URL: {logo_url}")
            self.current_view.add_history_item(logo_url, company, date, order_type, price, qty, total)

    def on_filter_changed(self):
        self.display_filtered_history(self.user_id)

    def on_stock_selected(self, symbol):
        self.stock_presenter = StockPresenter(balance=self.balance, user_id=self.user_id)
        self.clear_layout(self.main_window_view.ui.frame_content.layout())
        self.main_window_view.ui.frame_content.layout().addWidget(self.stock_presenter.view)
        self.current_view = self.stock_presenter.view

        self.stock_presenter.update_stock_info(symbol)

    def on_question_submitted(self, question: str):
        self.ask_ai_chat_view.display_loading()
        Timer(0.001, lambda: self.ask_ai_chat_view.display_response(self.ask_ai_chat_model.ask_ai_question(question))).start()

