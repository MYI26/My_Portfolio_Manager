import sys
from PySide6.QtWidgets import QApplication
from presenter.stock_presenter import StockPresenter

API_URL = "https://localhost:7229/api/market"  # העברת ה-URL למשתנה גלובלי
BALANCE = 2000.0 

if __name__ == "__main__":

    app = QApplication(sys.argv)
    presenter = StockPresenter(api_url=API_URL, balance=BALANCE)  
    presenter.show_view()

    sys.exit(app.exec())