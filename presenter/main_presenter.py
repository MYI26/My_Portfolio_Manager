# 📄 presenter/main_presenter.py

from view.main_window_view import MainWindowView
from view.portfolio_view import PortfolioView
from view.history_view import HistoryView

class MainPresenter:
    def __init__(self):
        self.window = MainWindowView()
        self.current_view = None
        self.load_portfolio()

        # חיבור כפתור history
        self.window.ui.pushButton_hom_2.clicked.connect(self.load_history)

        # חיבור כפתור home
        self.window.ui.pushButton_hom.clicked.connect(self.load_portfolio)

    def load_portfolio(self):
        # ניקוי ה-layout של frame_content
        self.clear_layout(self.window.ui.frame_content.layout())

        portfolio = PortfolioView()
        self.window.ui.frame_content.layout().addWidget(portfolio)
        self.current_view = portfolio

    def load_history(self):
        # ניקוי ה-layout של frame_content
        self.clear_layout(self.window.ui.frame_content.layout())

        history = HistoryView()
        self.window.ui.frame_content.layout().addWidget(history)
        self.current_view = history

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
