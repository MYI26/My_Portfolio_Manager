import sys
from PySide6.QtWidgets import QApplication # type: ignore
from presenter.stock_presenter import StockPresenter
from presenter.main_presenter import MainPresenter

API_URL = "https://localhost:7229/api/market"  # העברת ה-URL למשתנה גלובלי
BALANCE = 2000.0 

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # יצירת ה-Presenter של המידע על המניה
    #presenter = StockPresenter(api_url=API_URL, balance=BALANCE) 
    presenter = MainPresenter() 
    presenter.show_view()

    sys.exit(app.exec())