# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_chart.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_StockChart(object):
    def setupUi(self, StockChart):
        if not StockChart.objectName():
            StockChart.setObjectName(u"StockChart")
        StockChart.resize(1009, 400)
        StockChart.setMinimumSize(QSize(600, 300))
        self.mainLayout = QVBoxLayout(StockChart)
        self.mainLayout.setObjectName(u"mainLayout")
        self.widgetRangeSelector = QWidget(StockChart)
        self.widgetRangeSelector.setObjectName(u"widgetRangeSelector")

        self.mainLayout.addWidget(self.widgetRangeSelector)

        self.scrollArea = QScrollArea(StockChart)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContent = QWidget()
        self.scrollAreaContent.setObjectName(u"scrollAreaContent")
        self.scrollAreaContent.setGeometry(QRect(0, 0, 989, 364))
        self.scrollLayout = QVBoxLayout(self.scrollAreaContent)
        self.scrollLayout.setObjectName(u"scrollLayout")
        self.frameChart = QFrame(self.scrollAreaContent)
        self.frameChart.setObjectName(u"frameChart")
        self.frameChart.setFrameShape(QFrame.StyledPanel)
        self.chartLayout = QVBoxLayout(self.frameChart)
        self.chartLayout.setObjectName(u"chartLayout")
        self.label = QLabel(self.frameChart)
        self.label.setObjectName(u"label")

        self.chartLayout.addWidget(self.label)


        self.scrollLayout.addWidget(self.frameChart)

        self.scrollArea.setWidget(self.scrollAreaContent)

        self.mainLayout.addWidget(self.scrollArea)


        self.retranslateUi(StockChart)

        QMetaObject.connectSlotsByName(StockChart)
    # setupUi

    def retranslateUi(self, StockChart):
        self.label.setText("")
        pass
    # retranslateUi

