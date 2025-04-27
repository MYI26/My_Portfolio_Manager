# 📄 main.py
from PySide6.QtWidgets import QApplication
from view.stock_info_view import StockInfoView
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockInfoView()
    window.show()
    sys.exit(app.exec())