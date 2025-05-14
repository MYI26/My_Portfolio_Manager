# 📄 presenter/main_presenter.py

from view.main_window_view import MainWindowView
from view.portfolio_view import PortfolioView
from view.history_view import HistoryView
from view.new_action_view import NewActionView
from model.portfolio_model import PortfolioModel

class MainPresenter:
    def __init__(self):
        self.window = MainWindowView()
        self.current_view = None

        # חיבור כפתור history
        self.window.ui.pushButton_hom_2.clicked.connect(self.load_history)

        # חיבור כפתור home
        self.window.ui.pushButton_hom.clicked.connect(self.load_portfolio)
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.model = PortfolioModel()
        self.load_portfolio()



        # חיבור כפתור new action
        self.window.ui.pushButton_action.clicked.connect(self.load_new_action)

    def load_portfolio(self):
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
        capital_total, valeur_actuelle_total, performance_total_d, performance_total_p
        )

    def load_history(self):
        self.clear_layout(self.window.ui.frame_content.layout())
        history = HistoryView()
        self.window.ui.frame_content.layout().addWidget(history)
        self.current_view = history

    def load_new_action(self):
        self.clear_layout(self.window.ui.frame_content.layout())
        new_action = NewActionView()
        self.window.ui.frame_content.layout().addWidget(new_action)
        self.current_view = new_action

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def show_view(self):
        self.window.show()
