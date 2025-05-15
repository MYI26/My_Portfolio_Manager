import sys
from PySide6.QtWidgets import QApplication # type: ignore
from presenter.stock_presenter import StockPresenter
from presenter.main_presenter import MainPresenter
 
BALANCE = 2000.0 

if __name__ == "__main__":

    app = QApplication(sys.argv)

    presenter = MainPresenter(balance=BALANCE) 

    presenter.show_view()

    sys.exit(app.exec())