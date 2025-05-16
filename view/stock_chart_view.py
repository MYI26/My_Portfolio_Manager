from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLabel, QSizePolicy
from PySide6.QtCharts import QChartView
from PySide6.QtGui import QFont, QPainter

class StockChartView(QWidget):
    range_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layout
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Title
        self.title_label = QLabel("Tesla – Price History")
        self.title_label.setFont(QFont("Segoe UI", 12))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: rgb(40,73,107); margin-top: 0px; margin-bottom: 0px;")
        self.layout.addWidget(self.title_label)

        # Range combo box
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Last Week", "Last Month", "Last 3 Months"])
        self.combo_box.currentIndexChanged.connect(self.on_range_changed)
        self.combo_box.setStyleSheet("""
            QComboBox {
                background-color: rgb(255,255,255);
                color: #28496b;
                border: 1px solid #28496b;
                border-radius: 5px;
                padding: 8px;
                font-size: 12px;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        self.layout.addWidget(self.combo_box)

        # Chart view
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setStyleSheet("""
            QChartView {
                background-color: #ffffff;
                border: none;
            }
        """)
        self.chart_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.chart_view.setMinimumHeight(300)
        self.chart_view.setMaximumHeight(400)
        self.layout.addWidget(self.chart_view)

    def on_range_changed(self):
        range_type = self.combo_box.currentText()
        self.range_changed.emit(range_type)

    def update_chart(self, chart):
        if chart:
            self.chart_view.setChart(chart)