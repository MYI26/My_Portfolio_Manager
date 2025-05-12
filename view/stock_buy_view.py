from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Qt  # ייבוא Qt עבור LayoutDirection
from view.ui_stock_buy import Ui_frame_root

class StockBuyView(QFrame):  # ירושה מ-QFrame
    def __init__(self):
        super().__init__()
        self.ui = Ui_frame_root()
        self.ui.setupUi(self)

        # הגדרת כיוון פריסת הלייאאוטים
        self.ui.frame_info.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_header.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_actio_buttn.setLayoutDirection(Qt.RightToLeft)

        # חיבור כפתור ה-Buy לאירוע
        self.ui.button_bay.clicked.connect(self.on_confirm_clicked)

    def on_confirm_clicked(self):
        """
        מטפל בלחיצה על כפתור ה-Buy.
        """
        print("[StockBuyView] Buy button clicked")  # בדיקה