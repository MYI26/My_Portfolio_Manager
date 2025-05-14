# 📄 presenter/main_presenter.py

from view.main_window_view import MainWindowView
from view.portfolio_view import PortfolioView
from view.history_view import HistoryView
from view.new_action_view import NewActionView

class MainPresenter:
    def __init__(self):
        self.window = MainWindowView()
        self.current_view = None
        self.load_portfolio()

        # חיבור כפתור history
        self.window.ui.pushButton_hom_2.clicked.connect(self.load_history)

        # חיבור כפתור home
        self.window.ui.pushButton_hom.clicked.connect(self.load_portfolio)

        # חיבור כפתור new action
        self.window.ui.pushButton_action.clicked.connect(self.load_new_action)

    def load_portfolio(self):
        self.clear_layout(self.window.ui.frame_content.layout())
        portfolio = PortfolioView()
        self.window.ui.frame_content.layout().addWidget(portfolio)
        self.current_view = portfolio

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
