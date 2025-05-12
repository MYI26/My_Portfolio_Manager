import sys
from PySide6.QtWidgets import QApplication
from presenter.stock_presenter import StockPresenter

API_URL = "https://localhost:7229/api/market"  # העברת ה-URL למשתנה גלובלי

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # יצירת ה-Presenter של המידע על המניה
    presenter = StockPresenter(api_url=API_URL)
    presenter.show_view()

    sys.exit(app.exec())