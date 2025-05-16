from PySide6.QtCore import QTimer, Signal,QObject  # type: ignore
from model.stock_model import StockModel
from view.stock_info_view import StockInfoView
from presenter.stock_chart_presenter import StockChartPresenter
from view.stock_buy_view import StockBuyView
from view.stock_sale_view import StockSaleView

class StockPresenter(QObject):
    on_balance_changed = Signal(float)

    def __init__(self, balance, user_id):
        super().__init__()
        self.model = StockModel(balance)
        self.view = StockInfoView(self)
        self.user_id = user_id

        self.chart_presenter = StockChartPresenter(self.view.get_chart_view())
        self.stock_buy_view = StockBuyView()
        self.stock_sale_view = StockSaleView()

        self.view.buy_clicked.connect(self.on_buy_clicked)

        self.view.sale_clicked.connect(self.on_sale_clicked)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stock_info)
        self.timer.start(60000)  

        self.update_stock_info(symbol="AAPL")  # Example symbol, replace with actual symbol

        self.stock_buy_view.text_changed_frame_money_amount.connect(self.on_text_changed_frame_money_amount)

        self.refresh_balance_view()
        self.stock_buy_view.buy_requested.connect(self.handle_buy)
        self.stock_sale_view.sell_requested.connect(self.handle_sell)
      
        self.stock_buy_view.label_money_changed.connect(self.on_text_changed_frame_money_amount)

    def update_stock_info(self, symbol):     
        stock_data = self.model.fetch_stock_data(symbol)
        if stock_data:
            self.view.update_stock_info(stock_data)
        else:
            print(f"Failed to fetch stock data for symbol: {symbol}")
            static_data = self.model.get_static_data()
            self.view.update_stock_info(static_data)
       
    def on_buy_clicked(self):
        print("[StockPresenter] Buy button clicked")  

        self.stock_buy_view.text_changed_frame_money_amount.connect(self.on_text_changed_frame_money_amount)
        self.stock_buy_view.return_to_chart.connect(self.on_return_to_chart)

        layout = self.view.ui.frameChart.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None) 

        layout.addWidget(self.stock_buy_view)
        print("[StockPresenter] StockBuyView loaded") 


    def on_sale_clicked(self):
        print("[StockPresenter] Sale button clicked")  

        self.stock_buy_view.text_changed_frame_money_amount.connect(self.on_text_changed_frame_money_amount)
        self.stock_buy_view.return_to_chart.connect(self.on_return_to_chart)

        layout = self.view.ui.frameChart.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)  

        layout.addWidget(self.stock_sale_view)
        print("[StockPresenter] StockSaleView loaded") 

    def on_text_changed_frame_money_amount(self, text: str):
        try:
            investment = float(text)
        except ValueError:
            investment = 0.0

        self.stock_buy_view.update_label_money(f"{investment:.2f}")

        stock_price = self.view.get_current_stock_price()
        shares = investment / stock_price if stock_price > 0 else 0.0
        self.stock_buy_view.update_label_stock(f"{shares:.2f}")

        service_price = 0.0
        total = investment + service_price
        self.stock_buy_view.update_label_total(f"{total:.2f}$")

    def on_return_to_chart(self):
        print("[StockPresenter] Returning to chart view")  

        layout = self.view.ui.frameChart.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)  

        print("[StockPresenter] Recreating StockChartView and StockChartPresenter...")  
        self.chart_presenter = StockChartPresenter(self.view.get_chart_view())

        layout.addWidget(self.view.get_chart_view())
        print("[StockPresenter] StockChartView added to layout")  

    def show_view(self):
        self.view.show()

    def refresh_balance_view(self):
        balance = self.model.get_balance()
        self.stock_buy_view.set_balance_display(balance)
        self.stock_sale_view.set_balance_display(balance)
        #envoie un signal au main_window_presenter pour mettre à jour le label de l'argent
        self.on_balance_changed.emit(balance)

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
            logo_path = self.view.get_current_logo_url()  
            self.model.upload_stock_logo_to_cloudinary(logo_path, stock_name, self.user_id)  
            self.stock_buy_view.show_message("Achat effectué avec succès !")
        else:
            self.stock_buy_view.show_error("Fonds insuffisants pour acheter.")

    def handle_sell(self, quantity: float):
        stock_price = self.view.get_current_stock_price()
        total_gain = stock_price * quantity
        self.model.update_balance(total_gain)

        stock_name = self.view.get_current_stock_name()

        try:
            self.model.send_sell_transaction(self.user_id, stock_name, quantity, stock_price)
        except Exception as e:
            self.stock_sale_view.show_error(f"Erreur serveur Transaction : {e}")
            return   
        
        self.refresh_balance_view()
        self.stock_sale_view.show_message("Vente effectuée !")

    def update_label_money(self, money_text: str):
        self.ui.label_money_amount.setText(money_text)

    def update_label_stock(self, stock_text: str):
        self.ui.label_stock_amount.setText(stock_text)

    def update_label_total_amount(self, total_text: str):
        self.ui.label_total_amount.setText(total_text)