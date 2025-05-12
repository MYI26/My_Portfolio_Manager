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
        self.stock_buy_view = StockBuyView()

        # חיבור הסיגנל של כפתור ה-Buy
        self.view.buy_clicked.connect(self.on_buy_clicked)

        # טיימר לעדכון מחירים מהשרת
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stock_info)
        self.timer.start(60000)  # כל 60 שניות

        # קריאה ראשונית
        self.update_stock_info()

        # חיבור הסיגנל של תיבת הטקסט
        self.stock_buy_view.text_changed_frame_6.connect(self.on_text_changed_frame_6)

        # חיבור דו-כיווני בין label_2 ל-label_5
        #self.stock_buy_view.label_2_changed.connect(self.on_label_2_changed)
        #self.stock_buy_view.label_5_changed.connect(self.on_label_5_changed)

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

        # חיבור הסיגנלים של StockBuyView
        #self.stock_buy_view.text_changed_frame_6.connect(self.on_text_changed_frame_6)
        #self.stock_buy_view.text_changed_frame_5.connect(self.on_text_changed_frame_5)
        #self.stock_buy_view.return_to_chart.connect(self.on_return_to_chart)

        # החלפת הפריים של frame_chart בפריים החדש
        layout = self.view.ui.frameChart.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)  # הסרת ה-widget הישן

        layout.addWidget(self.stock_buy_view)
        print("[StockPresenter] StockBuyView loaded")  # בדיקה

    
    # def on_text_changed_frame_6(self, text):
    #     """
    #     מטפל בשינוי הטקסט ב-frame_6.
    #     """
    #     print(f"[StockPresenter] Text received for frame_6: {text}")  # בדיקה

    #     # עדכון הלייבל ב-frame_6
    #     self.stock_buy_view.update_label_2(text)

    # def on_text_changed_frame_5(self, text):
    #     """
    #     מטפל בשינוי הטקסט ב-frame_5.
    #     """
    #     print(f"[StockPresenter] Text received for frame_5: {text}")  # בדיקה

    #     # עדכון הלייבל ב-frame_5
    #     self.stock_buy_view.update_label_5(text)

    # def on_label_2_changed(self, text: str):
    #     """
    #     מטפל בשינוי הערך של label_2.
    #     """
    #     try:
    #         investment = float(text)
    #     except ValueError:
    #         investment = 0

    #     shares = self.model.calculate_label_5_from_label_2(investment)
    #     self.stock_buy_view.update_label_5(f"{shares:.2f}")

    # #def on_label_5_changed(self, text: str):
    #     """
    #     מטפל בשינוי הערך של label_5.
    #     """
    #     try:
    #      #   shares = float(text)
    #     #except ValueError:
    #     #    shares = 0

    #    # investment = self.model.calculate_label_2_from_label_5(shares)
    #  #   self.stock_buy_view.update_label_2(f"{investment:.2f}")
    def on_text_changed_frame_6(self, text: str):
        """
        מטפל בשינוי הטקסט בתיבת הטקסט ב-frame_6.
        """
        try:
            investment = float(text)
        except ValueError:
            investment = 0.0

        # עדכון המודל
        self.model.set_investment_amount(investment)

        # חישוב כמות המניות
        shares = self.model.calculate_shares()

        # עדכון ה-View
        self.stock_buy_view.update_label_2(f"{investment:.2f}")
        self.stock_buy_view.update_label_5(f"{shares:.2f}")

    def on_return_to_chart(self):
        """
        מחליף את הפריים של StockBuyView בפריים של הגרפים.
        """
        print("[StockPresenter] Returning to chart view")  # בדיקה

        # הסרת כל הווידג'טים מה-layout של frameChart
        layout = self.view.ui.frameChart.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)  # הסרת ה-widget הישן

        # יצירת StockChartView ו-StockChartPresenter חדשים
        print("[StockPresenter] Recreating StockChartView and StockChartPresenter...")  # בדיקה
        self.chart_presenter = StockChartPresenter(self.view.get_chart_view())

        # הוספת ה-ChartView החדש ל-layout
        layout.addWidget(self.view.get_chart_view())
        print("[StockPresenter] StockChartView added to layout")  # בדיקה

    def show_view(self):
        """
        מציג את ה-View.
        """
        self.view.show()