from PySide6.QtCore import QTimer
from model.stock_model import StockModel
from view.stock_info_view import StockInfoView
from presenter.stock_chart_presenter import StockChartPresenter
from view.stock_buy_view import StockBuyView

class StockPresenter:
    def __init__(self, api_url):
        self.model = StockModel(api_url)
        self.view = StockInfoView(self)

        # יצירת ה-StockChartPresenter
        self.chart_presenter = StockChartPresenter(self.view.get_chart_view())

        # חיבור הסיגנל של כפתור ה-Buy
        self.view.buy_clicked.connect(self.on_buy_clicked)

        # טיימר לעדכון מחירים מהשרת
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stock_info)
        self.timer.start(5000)  # כל 5 שניות

        # קריאה ראשונית
        self.update_stock_info()

    def update_stock_info(self):
        """
        טוען נתוני מניה מה-Model ומעדכן את ה-View.
        """
        stock_data = self.model.fetch_stock_data()
        if stock_data:
            self.view.update_stock_info(stock_data)
        else:
            print("Failed to fetch stock data")
            # במקרה של כשל, הצגת נתונים סטטיים
            static_data = self.model.get_static_data()
            self.view.update_stock_info(static_data)

    def on_buy_clicked(self):
        """
        מטפל בלחיצה על כפתור ה-Buy.
        """
        print("[StockPresenter] Buy button clicked")  # בדיקה

        # יצירת הפריים החדש של StockBuyView
        stock_buy_view = StockBuyView()

        # החלפת הפריים של frame_chart בפריים החדש
        layout = self.view.ui.frameChart.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)  # הסרת ה-widget הישן

        layout.addWidget(stock_buy_view)
        print("[StockPresenter] StockBuyView loaded")  # בדיקה

    def show_view(self):
        """
        מציג את ה-View.
        """
        self.view.show()