from PySide6.QtCore import QTimer # type: ignore
from model.stock_model import StockModel
from view.stock_info_view import StockInfoView
from presenter.stock_chart_presenter import StockChartPresenter
from view.stock_buy_view import StockBuyView
from view.stock_sale_view import StockSaleView

class StockPresenter:
    def __init__(self, balance, user_id):
        self.model = StockModel(balance)
        self.view = StockInfoView(self)
        self.user_id = user_id

        # יצירת ה-StockChartPresenter
        self.chart_presenter = StockChartPresenter(self.view.get_chart_view())
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

        """"""""""""""""""""""""""""""""""""""""""""""""
        self.refresh_balance_view()
        self.stock_buy_view.buy_requested.connect(self.handle_buy)
        self.stock_sale_view.sell_requested.connect(self.handle_sell)
      


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

    def on_text_changed_frame_money_amount(self, text: str):
   
        try:
            investment = float(text)
        except ValueError:
         investment = 0.0

        # עדכון המודל
        self.model.set_investment_amount(investment)
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
        #shares = self.model.calculate_shares()

        # עדכון ה-View
        # self.stock_sale_view.update_label_money(f"{investment:.2f}")
        # self.stock_sale_view.update_label_stock(f"{shares:.2f}")


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

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def refresh_balance_view(self):
        balance = self.model.get_balance()
        self.stock_buy_view.set_balance_display(balance)
        self.stock_sale_view.set_balance_display(balance)

    def handle_buy(self,quantity: float):
        stock_price = self.view.get_current_stock_price()
        total_cost = stock_price * quantity
        if self.model.can_afford(total_cost):
            self.model.update_balance(-total_cost)
            stock_name = self.view.get_current_stock_name()
            try:
                self.model.send_transaction(self.user_id, stock_name, quantity, stock_price)
            except Exception as e:
                self.stock_buy_view.show_error(f"Erreur serveur Transaction : {e}")
                return
            
            self.refresh_balance_view()
            logo_path = self.view.get_current_logo_url()  # Chemin de la photo
            self.model.upload_stock_logo_to_cloudinary(logo_path, stock_name, self.user_id)   #lors de l'achat: enregistrer la photo sur CLOUDINARY
            self.stock_buy_view.show_message("Achat effectué avec succès !")
        else:
            self.stock_buy_view.show_error("Fonds insuffisants pour acheter.")

    def handle_sell(self, quantity: float):
        stock_price = self.view.get_current_stock_price()
        total_gain = stock_price * quantity
        self.model.update_balance(total_gain)

        stock_name = self.view.get_current_stock_name()
        user_id = "user123"  # À remplacer plus tard

        try:
            self.model.send_sell_transaction(user_id, stock_name, quantity, stock_price)
        except Exception as e:
            self.stock_sale_view.show_error(f"Erreur serveur Transaction : {e}")
            return   
        
        self.refresh_balance_view()
        self.stock_sale_view.show_message("Vente effectuée !")

    