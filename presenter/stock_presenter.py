from PySide6.QtCore import QTimer
from model.stock_model import StockModel
from view.stock_info_view import StockInfoView
from presenter.stock_chart_presenter import StockChartPresenter
from view.stock_buy_view import StockBuyView
from view.stock_sale_view import StockSaleView

class StockPresenter:
    def __init__(self, api_url):
        self.model = StockModel(api_url)
        self.view = StockInfoView(self)

        # יצירת ה-StockChartPresenter
        self.chart_presenter = StockChartPresenter(self.view.get_chart_view(),api_url )
        self.stock_buy_view = StockBuyView()
        self.stock_sale_view = StockSaleView()

        # חיבור הסיגנל של כפתור ה-Buy
        self.view.buy_clicked.connect(self.on_buy_clicked)


         # חיבור הסיגנל של כפתור ה-Buy
        self.view.sale_clicked.connect(self.on_sale_clicked)

        # טיימר לעדכון מחירים מהשרת
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stock_info)
        self.timer.start(60000)  # כל 5 שניות

        # קריאה ראשונית
        self.update_stock_info()

            # חיבור הסיגנל של תיבת הטקסט
        self.stock_buy_view.text_changed_frame_money_amount.connect(self.on_text_changed_frame_money_amount)
        self.stock_sale_view.text_changed_frame_money_amount.connect(self.on_text_changed_frame_money_amount_sale)


        # חיבור דו-כיווני בין label_money ל-label_stock
        #self.stock_buy_view.label_money_changed.connect(self.on_label_money_changed)
        #self.stock_buy_view.label_stock_changed.connect(self.on_label_stock_changed)

    def update_stock_info(self, symbol="AAPL"):
        """
        טוען נתוני מניה מה-Model ומעדכן את ה-View.
        """
        stock_data = self.model.fetch_stock_data(symbol)
        if stock_data:
            self.view.update_stock_info(stock_data)
        else:
            print(f"Failed to fetch stock data for symbol: {symbol}")
            # במקרה של כשל, הצגת נתונים סטטיים
            static_data = self.model.get_static_data()
            self.view.update_stock_info(static_data)

       

    def on_buy_clicked(self):
        """
        מטפל בלחיצה על כפתור ה-Buy.
        """
        print("[StockPresenter] Buy button clicked")  # בדיקה
        # חיבור הסיגנלים של StockBuyView
        #self.stock_buy_view.text_changed_frame_money_amount.connect(self.on_text_changed_frame_money_amount)
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


    def on_sale_clicked(self):
        """
        מטפל בלחיצה על כפתור ה-Sale.
        """
        print("[StockPresenter] Sale button clicked")  # בדיקה 


        # חיבור הסיגנלים של StockBuyView
        #self.stock_buy_view.text_changed_frame_money_amount.connect(self.on_text_changed_frame_money_amount)
        #self.stock_buy_view.text_changed_frame_5.connect(self.on_text_changed_frame_5)
        #self.stock_buy_view.return_to_chart.connect(self.on_return_to_chart)

        # החלפת הפריים של frame_chart בפריים החדש
        layout = self.view.ui.frameChart.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)  # הסרת ה-widget הישן

        layout.addWidget(self.stock_sale_view)
        print("[StockPresenter] StockSaleView loaded")  # בדיקה

    
    # def on_text_changed_frame_money_amount(self, text):
    #     """
    #     מטפל בשינוי הטקסט ב-frame_money_amount.
    #     """
    #     print(f"[StockPresenter] Text received for frame_money_amount: {text}")  # בדיקה

    #     # עדכון הלייבל ב-frame_money_amount
    #     self.stock_buy_view.update_label_money(text)

    # def on_text_changed_frame_5(self, text):
    #     """
    #     מטפל בשינוי הטקסט ב-frame_5.
    #     """
    #     print(f"[StockPresenter] Text received for frame_5: {text}")  # בדיקה

    #     # עדכון הלייבל ב-frame_5
    #     self.stock_buy_view.update_label_stock(text)

    # def on_label_money_changed(self, text: str):
    #     """
    #     מטפל בשינוי הערך של label_money.
    #     """
    #     try:
    #         investment = float(text)
    #     except ValueError:
    #         investment = 0

    #     shares = self.model.calculate_label_stock_from_label_money(investment)
    #     self.stock_buy_view.update_label_stock(f"{shares:.2f}")

    # #def on_label_stock_changed(self, text: str):
    #     """
    #     מטפל בשינוי הערך של label_stock.
    #     """
    #     try:
    #      #   shares = float(text)
    #     #except ValueError:
    #     #    shares = 0

    #    # investment = self.model.calculate_label_money_from_label_stock(shares)
    #  #   self.stock_buy_view.update_label_money(f"{investment:.2f}")
    def on_text_changed_frame_money_amount(self, text: str):
        """
        מטפל בשינוי הטקסט בתיבת הטקסט ב-frame_money_amount.
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
        self.stock_buy_view.update_label_money(f"{investment:.2f}")
        self.stock_buy_view.update_label_stock(f"{shares:.2f}")

    def on_text_changed_frame_money_amount_sale(self, text: str):
        """
        מטפל בשינוי הטקסט בתיבת הטקסט ב-frame_money_amount.
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
        self.stock_sale_view.update_label_money(f"{investment:.2f}")
        self.stock_sale_view.update_label_stock(f"{shares:.2f}")


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