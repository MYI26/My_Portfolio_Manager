from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
from view.ui_new_action import Ui_Frame_New_Action


class NewActionView(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame_New_Action()
        self.ui.setupUi(self)

        # דוגמה סטטית: יצירת 9 מניות מובילות
        stocks = [
            {"logo": "resources/logos/logo_images/apple.png", "name": "Apple Inc.", "price": 150.0},
            {"logo": "resources/logos/logo_images/tesla.png", "name": "Tesla", "price": 200.0},
            {"logo": "resources/logos/logo_images/nvidia.png", "name": "NVIDIA", "price": 300.0},
            {"logo": "resources/logos/logo_images/google.png", "name": "Google", "price": 250.0},
            {"logo": "resources/logos/logo_images/microsoft.png", "name": "Microsoft", "price": 400.0},
            {"logo": "resources/logos/logo_images/meta.png", "name": "Meta", "price": 350.0},
            {"logo": "resources/logos/logo_images/intel.png", "name": "Intel", "price": 100.0},
            {"logo": "resources/logos/logo_images/amazon.png", "name": "Amazon", "price": 500.0},
            {"logo": "resources/logos/logo_images/samsung.png", "name": "Samsung", "price": 120.0},
        ]

        self.populate_grid(stocks)
        self.customize_scroll_area()

    def populate_grid(self, stocks):
        """ממלא את הגריד עם מניות מובילות."""
        grid_layout = self.ui.gridLayout
        grid_layout.setHorizontalSpacing(40)  # רווח אופקי בין אייטמים
        grid_layout.setVerticalSpacing(40)  # רווח אנכי בין אייטמים
        grid_layout.setContentsMargins(30, 30, 30, 30)  # שוליים מסביב לכל האייטמים
        row, col = 0, 0

        for stock in stocks:
            widget = self.create_stock_widget(stock["logo"], stock["name"], stock["price"])
            grid_layout.addWidget(widget, row, col)

            col += 1
            if col == 3:  # 3 עמודות בשורה
                col = 0
                row += 1

    def create_stock_widget(self, logo_path, name, price):
        """יוצר ווידג'ט עבור מניה."""
        widget = QFrame()
        widget.setObjectName("stockItem")  # שם ייחודי למסגרת החיצונית
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

        # לוגו
        label_logo = QLabel()
        pixmap = QPixmap(logo_path)
        if not pixmap.isNull():
            label_logo.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        label_logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_logo)

        # שם החברה והמחיר בשורה אחת
        name_price_layout = QHBoxLayout()
        name_price_layout.setContentsMargins(0, 0, 0, 0)
        name_price_layout.setSpacing(10)  
        name_price_layout.setAlignment(Qt.AlignCenter)

        # שם החברה
        label_name = QLabel(name)
        label_name.setFont(QFont("Segoe UI", 10))
        label_name.setStyleSheet("color: rgb(40, 75, 107);")
        label_name.setAlignment(Qt.AlignCenter)  # ממורכז
        name_price_layout.addWidget(label_name)

        # מחיר
        label_price = QLabel(f"{price:.2f} $")
        label_price.setFont(QFont("Segoe UI", 10))
        label_price.setStyleSheet("color: #52b74d;")
        label_price.setAlignment(Qt.AlignCenter)  # ממורכז
        name_price_layout.addWidget(label_price)

        layout.addLayout(name_price_layout)

        return widget

    def customize_scroll_area(self):
        """התאמה אישית של ה-Scroll Area."""
        scroll_area = self.ui.scrollArea

        # הגדרת כיוון ה-Scrollbar לשמאל
        scroll_area.setLayoutDirection(Qt.RightToLeft)
        scroll_area.widget().setLayoutDirection(Qt.LeftToRight)  # שמירה על כיוון התוכן משמאל לימין

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
            }
            QScrollBar::handle:vertical {
                background-color: rgb(40, 75, 107);
                border-radius: 15px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
        """)