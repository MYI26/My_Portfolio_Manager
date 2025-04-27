import os
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from view.ui_stock_info import Ui_Form

class StockInfoView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

# נתיב יחסי ללוגו
        logo_path = os.path.join("resources", "logos", "logo.png")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            self.ui.labelLogo.setPixmap(pixmap)
            self.ui.labelLogo.setScaledContents(True)
        else:
            print(f"❌ Logo not found at: {logo_path}")


       
