from PySide6.QtCharts import QChart, QLineSeries, QValueAxis, QCategoryAxis, QScatterSeries # type: ignore
from PySide6.QtGui import QPen, QColor # type: ignore
from PySide6.QtCore import QPointF, QMargins, Qt # type: ignore
from model.stock_chart_model import StockChartModel
from view.stock_chart_view import StockChartView

class StockChartPresenter:
    def __init__(self, chart_view):
        self.model = StockChartModel()
        self.view = chart_view

        self.view.range_changed.connect(self.on_range_changed)

        self.update_chart("Last Week")

    def on_range_changed(self, range_type: str):
        print(f"[ChartPresenter] Range changed to: {range_type}")  
        self.update_chart(range_type)

    def update_chart(self, range_type: str, symbol="AAPL"):
        print(f"[ChartPresenter] Updating chart for range: {range_type}, symbol: {symbol}") 
        prices, labels = self.model.get_static_data(range_type, symbol)
        print(f"[ChartPresenter] Prices: {prices}, Labels: {labels}")  
        chart = self.create_chart(prices, labels)
        self.view.update_chart(chart)
        print("[ChartPresenter] Chart updated in view")  


    def create_chart(self, prices, labels):
        if not prices or not labels:
            print("[ChartPresenter] No data to display.")
            return QChart() 
        
        print("[ChartPresenter] Creating chart...")  
        chart = QChart()
        chart.legend().hide()

        series = QLineSeries()
        for i, price in enumerate(prices):
            series.append(QPointF(i, price))

        pen = QPen(QColor("#28496b"))
        pen.setWidth(2)
        series.setPen(pen)
        chart.addSeries(series)

        scatter_series = QScatterSeries()
        scatter_series.setMarkerSize(8)
        scatter_series.setColor(QColor("#28496b"))
        scatter_series.setBorderColor(QColor("#28496b"))
        for i, price in enumerate(prices):
            scatter_series.append(QPointF(i, price))
        chart.addSeries(scatter_series)

        axis_x = QCategoryAxis()
        for i, label in enumerate(labels):
            axis_x.append(label, i)
        axis_x.setRange(0, len(prices) - 1)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)
        scatter_series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setRange(min(prices) - 5, max(prices) + 5)
        axis_y.setTickCount(10)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)
        scatter_series.attachAxis(axis_y)

        print("[ChartPresenter] Chart created with axes and series")  
        return chart
   
