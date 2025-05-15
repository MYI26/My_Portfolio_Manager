from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout # type: ignore
from PySide6.QtGui import QPixmap, QFont, QCursor # type: ignore
from PySide6.QtCore import Qt, Signal, QEvent # type: ignore
from view.ui_new_action import Ui_Frame_New_Action

class NewActionView(QFrame):
    stock_selected = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame_New_Action()
        self.ui.setupUi(self)

        stocks = [
            {"logo": "resources/logos/logo_images/apple.png", "name": "AAPL", "price": 150.0},
            {"logo": "resources/logos/logo_images/tesla.png", "name": "TSLA", "price": 200.0},
            {"logo": "resources/logos/logo_images/nvidia.png", "name": "NVDA", "price": 300.0},
            {"logo": "resources/logos/logo_images/google.png", "name": "GOOGL", "price": 250.0},
            {"logo": "resources/logos/logo_images/microsoft.png", "name": "MSFT", "price": 400.0},
            {"logo": "resources/logos/logo_images/meta.png", "name": "META", "price": 350.0},
            {"logo": "resources/logos/logo_images/intel.png", "name": "INTC", "price": 100.0},
            {"logo": "resources/logos/logo_images/amazon.png", "name": "AMZN", "price": 500.0},
            {"logo": "resources/logos/logo_images/samsung.png", "name": "005930.KS", "price": 120.0},
        ]

        self.stock_widgets = []
        self.selected_widget = None
        self.populate_grid(stocks)
        self.customize_scroll_area()

    def populate_grid(self, stocks):
        grid_layout = self.ui.gridLayout
        grid_layout.setHorizontalSpacing(40)
        grid_layout.setVerticalSpacing(40)
        grid_layout.setContentsMargins(30, 30, 30, 30)
        row, col = 0, 0

        for stock in stocks:
            widget = self.create_stock_widget(stock["logo"], stock["name"])
            widget.symbol = stock["name"]
            widget.installEventFilter(self)
            widget.setCursor(QCursor(Qt.PointingHandCursor))
            self.stock_widgets.append(widget)
            grid_layout.addWidget(widget, row, col)
            col += 1
            if col == 3:
                col = 0
                row += 1

    def create_stock_widget(self, logo_path, name):
        widget = QFrame()
        widget.setObjectName("stockItem")
        widget.setStyleSheet("""
            QFrame#stockItem {
                border: 1px solid rgb(40, 75, 107);
                border-radius: 5px;
                background-color: white;
                padding: 10px;
            }
        """)
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)

        label_logo = QLabel()
        pixmap = QPixmap(logo_path)
        if not pixmap.isNull():
            label_logo.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        label_logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_logo)

        name_price_layout = QHBoxLayout()
        name_price_layout.setContentsMargins(0, 0, 0, 0)
        name_price_layout.setSpacing(10)
        name_price_layout.setAlignment(Qt.AlignCenter)

        label_name = QLabel(name)
        label_name.setFont(QFont("Segoe UI", 10))
        label_name.setStyleSheet("color: rgb(40, 75, 107);")
        label_name.setAlignment(Qt.AlignCenter)
        name_price_layout.addWidget(label_name)

        layout.addLayout(name_price_layout)

        return widget

    def customize_scroll_area(self):
        scroll_area = self.ui.scrollArea
        scroll_area.setLayoutDirection(Qt.RightToLeft)
        scroll_area.widget().setLayoutDirection(Qt.LeftToRight)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: 1px solid rgb(40, 75, 107);
                border-radius: 5px;
                background-color: white;
            }
            QScrollBar:vertical {
                width: 12px;
                border-radius: 100px;
                background-color: white;
                border: 2px solid rgb(240, 240, 240);
                left: 0px;
            }
            QScrollBar::handle:vertical {
                background-color: rgb(40, 75, 107);
                border-radius: 15px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
        """)

    def eventFilter(self, obj, event):
        if obj in self.stock_widgets:
            if event.type() == QEvent.Enter:
                self._highlight_widget(obj)
            elif event.type() == QEvent.Leave:
                if obj != self.selected_widget:
                    self._unhighlight_widget(obj)
            elif event.type() == QEvent.MouseButtonPress:
                self._select_widget(obj)
                self.stock_selected.emit(obj.symbol)
        return super().eventFilter(obj, event)

    def _highlight_widget(self, widget):
        widget.setStyleSheet("""
            QFrame#stockItem {
                border: 2px solid #2d7be5;
                border-radius: 5px;
                background-color: #f8fbfd;
                padding: 10px;
            }
        """)

    def _unhighlight_widget(self, widget):
        widget.setStyleSheet("""
            QFrame#stockItem {
                border: 1px solid rgb(40, 75, 107);
                border-radius: 5px;
                background-color: white;
                padding: 10px;
            }
        """)

    def _select_widget(self, widget):
        if self.selected_widget and self.selected_widget != widget:
            self._unhighlight_widget(self.selected_widget)
        self.selected_widget = widget
        self._highlight_widget(widget)

    #je veux une fonction pour lorsque je clique sur un des items