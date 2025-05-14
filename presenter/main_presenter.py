# 📄 presenter/main_presenter.py

from view.main_window_view import MainWindowView
from view.portfolio_view import PortfolioView
from view.history_view import HistoryView
from model.portfolio_model import PortfolioModel
from model.transactions_model import TransactionModel

class MainPresenter:
    def __init__(self, balance):
        self.window = MainWindowView()
        self.current_view = None
        # חיבור כפתור home
        self.window.ui.pushButton_hom.clicked.connect(self.load_portfolio)
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.model = PortfolioModel()
        self.balance = balance
        self.load_portfolio()
        self.history_view = HistoryView()
        self.transaction_model = TransactionModel()
        self.window.ui.pushButton_hom_2.clicked.connect(self.load_history)
        self.transaction_history_data = []
        self.history_view.on_filter_changed(self.on_filter_changed)  # 🔁 Ajout ici


    def load_portfolio(self):
        # ניקוי ה-layout של frame_content
        self.clear_layout(self.window.ui.frame_content.layout())

        portfolio_view = PortfolioView()
        self.window.ui.frame_content.layout().addWidget(portfolio_view)
        self.current_view = portfolio_view
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
        capital_total, valeur_actuelle_total, performance_total_d, performance_total_p, self.balance
        )

    # def load_history(self):
    #     # ניקוי ה-layout של frame_content
    #     self.clear_layout(self.window.ui.frame_content.layout())

    #     history = HistoryView()
    #     self.window.ui.frame_content.layout().addWidget(history)
    #     self.current_view = history

    def load_history(self):
        self.clear_layout(self.window.ui.frame_content.layout())
        self.window.ui.frame_content.layout().addWidget(self.history_view)
        self.current_view = self.history_view

        self.history_view.on_filter_changed(self.on_filter_changed)

        # Nouvelle ligne : on charge les données depuis le modèle
        self.load_transaction_history("ben")  # ⚠️ adapter le nom de l’utilisateur

    def load_transaction_history(self, user_id):
        # operations = self.transaction_model.fetch_history(user_id)
        # print("[DEBUG] Réponse brute reçue du serveur TRANSACTIONS:", operations) 
        
        # for op in operations:
        #     symbol = op["stockName"]
        #     company = symbol  # temporaire, en attendant mieux
        #     date = op["date"].split("T")[0]
        #     order_type = op["type"]
        #     price = op["pricePerUnit"]
        #     qty = op["quantity"]
        #     total = price * qty

        #     logo_path = f"resources/logos/apple.png"

        #     # on passe les données à la vue
        #     self.current_view.add_history_item(logo_path, company, date, order_type, price, qty, total)
        self.transaction_history_data = self.transaction_model.fetch_history(user_id)
        self.display_filtered_history()

    def clear_layout(self, layout):
        """מנקה את כל הווידג'טים מה-layout."""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def show_view(self):
        self.window.show()

    def display_filtered_history(self):
        if not self.current_view:
            return

        selected_filter = self.current_view.get_selected_filter()
        self.current_view.clear_history()

        for op in self.transaction_history_data:
            if op["userId"] != "ben":
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

            logo_path = f"resources/logos/{symbol.lower()}.png"
            self.current_view.add_history_item(logo_path, company, date, order_type, price, qty, total)

    def on_filter_changed(self):
        self.display_filtered_history()
