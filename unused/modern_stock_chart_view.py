from PySide6.QtWidgets import QWidget, QVBoxLayout
from pyqtgraph import PlotWidget, InfiniteLine, TextItem, AxisItem
import pyqtgraph as pg
import numpy as np
from datetime import datetime, timedelta


class DayAxis(AxisItem):
    def __init__(self, day_labels, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.day_labels = day_labels

    def tickStrings(self, values, scale, spacing):
        indexes = [int(v) for v in values]
        return [self.day_labels[i] if 0 <= i < len(self.day_labels) else "" for i in indexes]


class ModernStockChartView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TSLA Chart – Modern Weekly View")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.day_labels = self.get_last_week_labels()

        self.plot_widget = PlotWidget(axisItems={'bottom': DayAxis(self.day_labels, orientation='bottom')})
        layout.addWidget(self.plot_widget)

        self.setup_chart()

    def get_last_week_labels(self):
        today = datetime.today()
        return [(today - timedelta(days=i)).strftime('%a') for i in reversed(range(7))]

    def setup_chart(self):
        prices = [80.25, 80.10, 80.55, 80.20, 80.40, 80.65, 80.50]
        x = np.arange(len(prices))

        # עיצוב כללי
        self.plot_widget.setBackground("w")
        self.plot_widget.showGrid(x=True, y=True, alpha=0.2)

        # עיצוב קו
        pen = pg.mkPen(color="#1e88e5", width=3)
        self.line = self.plot_widget.plot(x, prices, pen=pen, symbol='o', symbolSize=10, symbolBrush="#2196f3")

        # כותרות
        self.plot_widget.setTitle("Tesla Stock – Last 7 Days", color="#333", size="14pt")
        self.plot_widget.setLabel("left", "Price", units="USD")
        self.plot_widget.getAxis("left").setStyle(tickFont=pg.QtGui.QFont("Segoe UI", 10))
        self.plot_widget.getAxis("bottom").setStyle(tickFont=pg.QtGui.QFont("Segoe UI", 10))

        # קווי עכבר
        self.vline = InfiniteLine(angle=90, movable=False, pen=pg.mkPen(color="#999", style=pg.QtCore.Qt.DotLine))
        self.hline = InfiniteLine(angle=0, movable=False, pen=pg.mkPen(color="#999", style=pg.QtCore.Qt.DotLine))
        self.plot_widget.addItem(self.vline, ignoreBounds=True)
        self.plot_widget.addItem(self.hline, ignoreBounds=True)

        # טול־טיפ להצגת ערך
        self.text = TextItem("", anchor=(0.5, 1.5), color="black", fill="white")
        self.plot_widget.addItem(self.text)

        self.plot_widget.scene().sigMouseMoved.connect(self.mouse_moved)

    def mouse_moved(self, evt):
        pos = evt
        vb = self.plot_widget.getPlotItem().vb
        if self.plot_widget.sceneBoundingRect().contains(pos):
            mouse_point = vb.mapSceneToView(pos)
            x = int(mouse_point.x())
            y = mouse_point.y()
            if 0 <= x < len(self.line.yData):
                price = self.line.yData[x]
                self.vline.setPos(x)
                self.hline.setPos(price)
                self.text.setHtml(f"<span style='font-size: 12pt'><b>{self.day_labels[x]}:</b> {price:.2f} USD</span>")
                self.text.setPos(x, price)
