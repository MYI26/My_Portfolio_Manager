# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_info.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(637, 403)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.mainLayout = QVBoxLayout(Form)
        self.mainLayout.setObjectName(u"mainLayout")
        self.frameHeader = QFrame(Form)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setStyleSheet(u"")
        self.headerLayout = QHBoxLayout(self.frameHeader)
        self.headerLayout.setObjectName(u"headerLayout")
        self.frameActions = QFrame(self.frameHeader)
        self.frameActions.setObjectName(u"frameActions")
        self.actionsLayout = QVBoxLayout(self.frameActions)
        self.actionsLayout.setObjectName(u"actionsLayout")
        self.btnSale = QPushButton(self.frameActions)
        self.btnSale.setObjectName(u"btnSale")
        font = QFont()
        font.setPointSize(10)
        self.btnSale.setFont(font)
        self.btnSale.setStyleSheet(u"color: white; background: green")

        self.actionsLayout.addWidget(self.btnSale)

        self.btnBuy = QPushButton(self.frameActions)
        self.btnBuy.setObjectName(u"btnBuy")
        self.btnBuy.setFont(font)
        self.btnBuy.setStyleSheet(u"color: white; background: red")

        self.actionsLayout.addWidget(self.btnBuy)


        self.headerLayout.addWidget(self.frameActions, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frameData = QFrame(self.frameHeader)
        self.frameData.setObjectName(u"frameData")
        self.dataLayout = QVBoxLayout(self.frameData)
        self.dataLayout.setObjectName(u"dataLayout")
        self.labelOpen = QLabel(self.frameData)
        self.labelOpen.setObjectName(u"labelOpen")

        self.dataLayout.addWidget(self.labelOpen)

        self.openPriceValue = QLabel(self.frameData)
        self.openPriceValue.setObjectName(u"openPriceValue")
        font1 = QFont()
        font1.setPointSize(12)
        self.openPriceValue.setFont(font1)

        self.dataLayout.addWidget(self.openPriceValue)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.dataLayout.addItem(self.verticalSpacer_2)

        self.labelClose = QLabel(self.frameData)
        self.labelClose.setObjectName(u"labelClose")

        self.dataLayout.addWidget(self.labelClose)

        self.ClosePriceValue = QLabel(self.frameData)
        self.ClosePriceValue.setObjectName(u"ClosePriceValue")
        self.ClosePriceValue.setFont(font1)

        self.dataLayout.addWidget(self.ClosePriceValue)


        self.headerLayout.addWidget(self.frameData, 0, Qt.AlignmentFlag.AlignTop)

        self.frameName = QFrame(self.frameHeader)
        self.frameName.setObjectName(u"frameName")
        self.frameName.setAutoFillBackground(False)
        self.frameName.setStyleSheet(u"")
        self.nameLayout = QVBoxLayout(self.frameName)
        self.nameLayout.setSpacing(4)
        self.nameLayout.setObjectName(u"nameLayout")
        self.labelSymbol = QLabel(self.frameName)
        self.labelSymbol.setObjectName(u"labelSymbol")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(15)
        font2.setWeight(QFont.DemiBold)
        font2.setKerning(True)
        self.labelSymbol.setFont(font2)

        self.nameLayout.addWidget(self.labelSymbol)

        self.labelCompany = QLabel(self.frameName)
        self.labelCompany.setObjectName(u"labelCompany")

        self.nameLayout.addWidget(self.labelCompany)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.nameLayout.addItem(self.verticalSpacer)

        self.labelCurrentPrice = QLabel(self.frameName)
        self.labelCurrentPrice.setObjectName(u"labelCurrentPrice")
        self.labelCurrentPrice.setStyleSheet(u"")

        self.nameLayout.addWidget(self.labelCurrentPrice, 0, Qt.AlignmentFlag.AlignBottom)

        self.labelCurntPriceValue = QLabel(self.frameName)
        self.labelCurntPriceValue.setObjectName(u"labelCurntPriceValue")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setWeight(QFont.DemiBold)
        self.labelCurntPriceValue.setFont(font3)
        self.labelCurntPriceValue.setStyleSheet(u"margin-top: -0px")

        self.nameLayout.addWidget(self.labelCurntPriceValue)

        self.labelChange = QLabel(self.frameName)
        self.labelChange.setObjectName(u"labelChange")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        self.labelChange.setFont(font4)
        self.labelChange.setStyleSheet(u"color: green;")

        self.nameLayout.addWidget(self.labelChange)


        self.headerLayout.addWidget(self.frameName, 0, Qt.AlignmentFlag.AlignTop)

        self.frameLogo = QFrame(self.frameHeader)
        self.frameLogo.setObjectName(u"frameLogo")
        self.frameLogo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.labelLogo = QLabel(self.frameLogo)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(20, 30, 101, 121))
        self.labelLogo.setPixmap(QPixmap(u"../resource/logos/logo.png"))
        self.labelLogo.setScaledContents(True)

        self.headerLayout.addWidget(self.frameLogo)


        self.mainLayout.addWidget(self.frameHeader)

        self.frameChart = QFrame(Form)
        self.frameChart.setObjectName(u"frameChart")
        self.chartLayout = QVBoxLayout(self.frameChart)
        self.chartLayout.setObjectName(u"chartLayout")
        self.labelChartTitle = QLabel(self.frameChart)
        self.labelChartTitle.setObjectName(u"labelChartTitle")

        self.chartLayout.addWidget(self.labelChartTitle)

        self.labelChartArea = QLabel(self.frameChart)
        self.labelChartArea.setObjectName(u"labelChartArea")
        self.labelChartArea.setMinimumSize(QSize(64, 64))

        self.chartLayout.addWidget(self.labelChartArea)


        self.mainLayout.addWidget(self.frameChart)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.btnSale.setText(QCoreApplication.translate("Form", u"Sale", None))
        self.btnBuy.setText(QCoreApplication.translate("Form", u"Buy", None))
        self.labelOpen.setText(QCoreApplication.translate("Form", u"Open Price: ", None))
        self.openPriceValue.setText(QCoreApplication.translate("Form", u"80.15 USD", None))
        self.labelClose.setText(QCoreApplication.translate("Form", u"Close Price: ", None))
        self.ClosePriceValue.setText(QCoreApplication.translate("Form", u"80.40 USD", None))
        self.labelSymbol.setText(QCoreApplication.translate("Form", u"TSLA", None))
        self.labelCompany.setText(QCoreApplication.translate("Form", u"TESLA LTD", None))
        self.labelCurrentPrice.setText(QCoreApplication.translate("Form", u"Current price:", None))
        self.labelCurntPriceValue.setText(QCoreApplication.translate("Form", u"80.25 USD", None))
        self.labelChange.setText(QCoreApplication.translate("Form", u"0.5%", None))
        self.labelLogo.setText("")
        self.labelChartTitle.setText(QCoreApplication.translate("Form", u"PERFORMANCE / GRAPHIQUE", None))
        self.labelChartArea.setText(QCoreApplication.translate("Form", u"Chart Placeholder", None))
        pass
    # retranslateUi

