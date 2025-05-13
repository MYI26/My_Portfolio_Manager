# 📄 presenter/main_presenter.py

from view.main_window_view import MainWindowView
from view.portfolio_view import PortfolioView

class MainPresenter:
    def __init__(self):
        self.window = MainWindowView()
        self.load_portfolio()

    def load_portfolio(self):
        # ניקוי ה-layout של frame_content
        self.clear_layout(self.window.ui.frame_content.layout())

        portfolio = PortfolioView()
        self.window.ui.frame_content.layout().addWidget(portfolio)

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
