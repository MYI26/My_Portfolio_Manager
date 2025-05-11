# 📄 test1/view/time_range_selector_view.py

from PySide6.QtWidgets import QWidget
from view.ui_time_range_selector import Ui_Form

class TimeRangeSelectorView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # החצנת הכפתורים לצורך שימוש חיצוני (כמו ב־StockChartView)
        self.btnWeek = self.ui.btnWeek
        self.btnMonth = self.ui.btnMonth
        self.btnThreeMonths = self.ui.btnThreeMonths

        # אירועים לדוגמה (כרגע רק מדפיסים לקונסול)
        self.btnWeek.clicked.connect(lambda: self.on_range_selected("week"))
        self.btnMonth.clicked.connect(lambda: self.on_range_selected("month"))
        self.btnThreeMonths.clicked.connect(lambda: self.on_range_selected("3months"))

    def on_range_selected(self, range_id: str):
        print(f"🔁 טווח נבחר: {range_id}")
        # כאן בעתיד תוכל לשדר את זה ל־Presenter או ל־Model לפי תבנית MVP
