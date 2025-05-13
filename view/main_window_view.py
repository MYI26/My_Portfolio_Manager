import os
from PySide6.QtWidgets import QFrame, QScrollArea, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal
from view.ui_main_window import Ui_Frame_main_window
from view.portfolio_view import PortfolioView


class MainWindowView(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Frame_main_window()
        self.ui.setupUi(self)
        

        # הגדרת כיוון פריסת הלייאאוט
        self.ui.frame_header.setLayoutDirection(Qt.RightToLeft)
        self.ui.frame_content.setLayoutDirection(Qt.RightToLeft)

        # הוספת QVBoxLayout ל-frame_content
        self.ui.frame_content_layout = QVBoxLayout(self.ui.frame_content)
        self.ui.frame_content.setLayout(self.ui.frame_content_layout)

        self.portfolio_view = PortfolioView()
        self.ui.frame_content.layout().addWidget(self.portfolio_view)
