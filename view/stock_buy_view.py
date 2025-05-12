from PySide6.QtWidgets import QFrame, QWidget, QLineEdit
from PySide6.QtCore import Qt, Signal  # ייבוא Qt עבור LayoutDirection ו-Signal
from view.ui_stock_buy import Ui_frame_root

class StockBuyView(QFrame):  # ירושה מ-QFrame
    return_to_chart = Signal()  # סיגנל לחזרה לגרף
    text_changed_frame_6 = Signal(str)  # סיגנל עבור frame_6

    def __init__(self):
        super().__init__()
        self.ui = Ui_frame_root()
        self.ui.setupUi(self)

        # הגדרת כיוון פריסת הלייאאוטים
        self.ui.frame_info.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_header.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_action_buttn.setLayoutDirection(Qt.RightToLeft)

        # חיבור כפתור ה-Buy לאירוע
        self.ui.button_bay.clicked.connect(self.on_confirm_clicked)

        # חיבור commandLinkButton לסיגנל
        self.ui.commandLinkButton.clicked.connect(self.on_return_to_chart_clicked)

        # חיבור תיבות הטקסט לסיגנלים
        self.ui.lineEdit.textChanged.connect(self.on_text_changed_frame_6)

        # הגדרת ערכים דפולטיביים ללייבלים
        self.ui.label_2.setText("100.0")  # ערך דפולטיבי עבור label_2
        self.ui.label_5.setText("1.25")  # ערך דפולטיבי עבור label_5

    def on_confirm_clicked(self):
        """
        מטפל בלחיצה על כפתור ה-Buy.
        """
        print("[StockBuyView] Buy button clicked")  # בדיקה

    def on_return_to_chart_clicked(self):
        """
        משדר סיגנל לחזרה לגרף.
        """
        print("[StockBuyView] Return to chart clicked")  # בדיקה
        self.return_to_chart.emit()

    def on_text_changed_frame_6(self, text):
        """
        משדר את הטקסט שהוזן ב-frame_6 ל-Presenter.
        """
        print(f"[StockBuyView] Text changed in frame_6: {text}")  # בדיקה
        self.text_changed_frame_6.emit(text)

    def update_label_2(self, text):
        """
        מעדכן את הטקסט של label_2.
        """
        self.ui.label_2.setText(text)

    def update_label_5(self, text):
        """
        מעדכן את הטקסט של label_5.
        """
        self.ui.label_5.setText(text)