from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget
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
            {"logo": "resources/logos/apple.png", "name": "Apple Inc.", "price": 150.0},
            {"logo": "resources/logos/tesla.png", "name": "Tesla", "price": 200.0},
            {"logo": "resources/logos/nvidia.png", "name": "NVIDIA", "price": 300.0},
            {"logo": "resources/logos/google.png", "name": "Google", "price": 250.0},
            {"logo": "resources/logos/microsoft.png", "name": "Microsoft", "price": 400.0},
            {"logo": "resources/logos/meta.png", "name": "Meta", "price": 350.0},
            {"logo": "resources/logos/intel.png", "name": "Intel", "price": 100.0},
            {"logo": "resources/logos/amazon.png", "name": "Amazon", "price": 500.0},
            {"logo": "resources/logos/samsung.png", "name": "Samsung", "price": 120.0},
        ]

        self.populate_grid(stocks)

    def populate_grid(self, stocks):
        """ממלא את הגריד עם מניות מובילות."""
        grid_layout = self.ui.gridLayout
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
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # לוגו
        label_logo = QLabel()
        pixmap = QPixmap(logo_path)
        if not pixmap.isNull():
            label_logo.setPixmap(pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        label_logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_logo)

        # שם החברה
        label_name = QLabel(name)
        label_name.setFont(QFont("Segoe UI", 10))
        label_name.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_name)

        # מחיר
        label_price = QLabel(f"{price:.2f} $")
        label_price.setFont(QFont("Segoe UI", 10))
        label_price.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_price)

        return widget