from PySide6.QtCharts import QChart, QLineSeries, QValueAxis, QCategoryAxis, QScatterSeries
from PySide6.QtGui import QPen, QColor
from PySide6.QtCore import QPointF, QMargins, Qt
from model.stock_chart_model import StockChartModel
from view.stock_chart_view import StockChartView

class StockChartPresenter:
    def __init__(self, chart_view, api_url):
        self.model = StockChartModel(api_url)
        self.view = chart_view

        # חיבור הסיגנל מה-View לפונקציה ב-Presenter
        self.view.range_changed.connect(self.on_range_changed)

        # ברירת מחדל: הצגת גרף שבוע
        self.update_chart("Last Week")

    def on_range_changed(self, range_type: str):
        """
        מטפל בשינוי הבחירה בתפריט.
        """
        print(f"[ChartPresenter] Range changed to: {range_type}")  # בדיקה
        self.update_chart(range_type)

    def update_chart(self, range_type: str, symbol="AAPL"):
        print(f"[ChartPresenter] Updating chart for range: {range_type}, symbol: {symbol}")  # בדיקה
        prices, labels = self.model.get_static_data(range_type, symbol)
        print(f"[ChartPresenter] Prices: {prices}, Labels: {labels}")  # בדיקה
        chart = self.create_chart(prices, labels)
        self.view.update_chart(chart)
        print("[ChartPresenter] Chart updated in view")  # בדיקה


    def create_chart(self, prices, labels):
        """
        יוצר גרף חדש עם הנתונים.
        """
        if not prices or not labels:
            print("[ChartPresenter] No data to display.")
            return QChart()  # retourne un graphique vide sans planter
        

        print("[ChartPresenter] Creating chart...")  # בדיקה
        chart = QChart()
        chart.legend().hide()

        # יצירת סדרה
        series = QLineSeries()
        for i, price in enumerate(prices):
            series.append(QPointF(i, price))

        pen = QPen(QColor("#28496b"))
        pen.setWidth(2)
        series.setPen(pen)
        chart.addSeries(series)

        # הוספת נקודות על הגרף
        scatter_series = QScatterSeries()
        scatter_series.setMarkerSize(8)
        scatter_series.setColor(QColor("#28496b"))
        scatter_series.setBorderColor(QColor("#28496b"))
        for i, price in enumerate(prices):
            scatter_series.append(QPointF(i, price))
        chart.addSeries(scatter_series)

        # ציר X
        axis_x = QCategoryAxis()
        for i, label in enumerate(labels):
            axis_x.append(label, i)
        axis_x.setRange(0, len(prices) - 1)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)
        scatter_series.attachAxis(axis_x)

        # ציר Y
        axis_y = QValueAxis()
        axis_y.setRange(min(prices) - 5, max(prices) + 5)
        axis_y.setTickCount(10)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)
        scatter_series.attachAxis(axis_y)

        print("[ChartPresenter] Chart created with axes and series")  # בדיקה
        return chart
   
