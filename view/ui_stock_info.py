# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_info.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1040, 524)
        Form.setStyleSheet(u"background-color: rgb(248, 248, 248);\n"
"border: none;\n"
"")
        self.mainLayout = QVBoxLayout(Form)
        self.mainLayout.setObjectName(u"mainLayout")
        self.frameHeader = QFrame(Form)
        self.frameHeader.setObjectName(u"frameHeader")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameHeader.sizePolicy().hasHeightForWidth())
        self.frameHeader.setSizePolicy(sizePolicy)
        self.frameHeader.setMinimumSize(QSize(0, 0))
        self.frameHeader.setLayoutDirection(Qt.LeftToRight)
        self.frameHeader.setStyleSheet(u"color: rgb(40, 73, 107);\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.frameHeader)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(40, -1, 300, -1)
        self.frameLogo = QFrame(self.frameHeader)
        self.frameLogo.setObjectName(u"frameLogo")
        sizePolicy.setHeightForWidth(self.frameLogo.sizePolicy().hasHeightForWidth())
        self.frameLogo.setSizePolicy(sizePolicy)
        self.frameLogo.setMinimumSize(QSize(0, 0))
        self.frameLogo.setFrameShape(QFrame.NoFrame)
        self.frameLogo.setFrameShadow(QFrame.Raised)
        self.frameLogo.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frameLogo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelLogo = QLabel(self.frameLogo)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setPixmap(QPixmap(u"../../resources/logos/tesla.png"))
        self.labelLogo.setScaledContents(False)

        self.verticalLayout_4.addWidget(self.labelLogo, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frameLogo, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frameName = QFrame(self.frameHeader)
        self.frameName.setObjectName(u"frameName")
        sizePolicy.setHeightForWidth(self.frameName.sizePolicy().hasHeightForWidth())
        self.frameName.setSizePolicy(sizePolicy)
        self.frameName.setMinimumSize(QSize(0, 0))
        self.frameName.setMaximumSize(QSize(65, 16777215))
        font = QFont()
        font.setPointSize(1)
        self.frameName.setFont(font)
        self.frameName.setAutoFillBackground(False)
        self.frameName.setStyleSheet(u"")
        self.frameName.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frameName)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelSymbol = QLabel(self.frameName)
        self.labelSymbol.setObjectName(u"labelSymbol")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(13)
        font1.setKerning(True)
        self.labelSymbol.setFont(font1)
        self.labelSymbol.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.labelSymbol)

        self.labelCompany = QLabel(self.frameName)
        self.labelCompany.setObjectName(u"labelCompany")
        self.labelCompany.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.labelCompany)


        self.horizontalLayout_2.addWidget(self.frameName, 0, Qt.AlignVCenter)

        self.frame_2 = QFrame(self.frameHeader)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(130, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 9, 0)
        self.labelCurntPriceValue = QLabel(self.frame_2)
        self.labelCurntPriceValue.setObjectName(u"labelCurntPriceValue")
        font2 = QFont()
        font2.setPointSize(11)
        self.labelCurntPriceValue.setFont(font2)
        self.labelCurntPriceValue.setStyleSheet(u"margin-top: -0px;")

        self.verticalLayout_2.addWidget(self.labelCurntPriceValue, 0, Qt.AlignTop)

        self.labelChange = QLabel(self.frame_2)
        self.labelChange.setObjectName(u"labelChange")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(9)
        self.labelChange.setFont(font3)
        self.labelChange.setStyleSheet(u"color: rgb(82, 183, 77);")

        self.verticalLayout_2.addWidget(self.labelChange)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignVCenter)

        self.frameData = QFrame(self.frameHeader)
        self.frameData.setObjectName(u"frameData")
        sizePolicy.setHeightForWidth(self.frameData.sizePolicy().hasHeightForWidth())
        self.frameData.setSizePolicy(sizePolicy)
        self.frameData.setMinimumSize(QSize(0, 0))
        self.frameData.setMaximumSize(QSize(80, 16777215))
        self.frameData.setStyleSheet(u"")
        self.frameData.setLineWidth(0)
        self.dataLayout = QVBoxLayout(self.frameData)
        self.dataLayout.setSpacing(4)
        self.dataLayout.setObjectName(u"dataLayout")
        self.dataLayout.setContentsMargins(0, 0, 0, 0)
        self.labelOpen = QLabel(self.frameData)
        self.labelOpen.setObjectName(u"labelOpen")

        self.dataLayout.addWidget(self.labelOpen, 0, Qt.AlignLeft)

        self.openPriceValue = QLabel(self.frameData)
        self.openPriceValue.setObjectName(u"openPriceValue")
        font4 = QFont()
        font4.setPointSize(10)
        self.openPriceValue.setFont(font4)
        self.openPriceValue.setMargin(0)

        self.dataLayout.addWidget(self.openPriceValue)


        self.horizontalLayout_2.addWidget(self.frameData, 0, Qt.AlignVCenter)

        self.frame = QFrame(self.frameHeader)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.labelClose = QLabel(self.frame)
        self.labelClose.setObjectName(u"labelClose")
        self.labelClose.setStyleSheet(u"")
        self.labelClose.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelClose.setMargin(0)

        self.verticalLayout_3.addWidget(self.labelClose)

        self.ClosePriceValue = QLabel(self.frame)
        self.ClosePriceValue.setObjectName(u"ClosePriceValue")
        self.ClosePriceValue.setFont(font4)

        self.verticalLayout_3.addWidget(self.ClosePriceValue)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignVCenter)

        self.frameActions = QFrame(self.frameHeader)
        self.frameActions.setObjectName(u"frameActions")
        self.frameActions.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frameActions.sizePolicy().hasHeightForWidth())
        self.frameActions.setSizePolicy(sizePolicy)
        self.frameActions.setMinimumSize(QSize(0, 0))
        self.actionsLayout = QVBoxLayout(self.frameActions)
        self.actionsLayout.setObjectName(u"actionsLayout")
        self.actionsLayout.setContentsMargins(0, 0, 0, 0)
        self.btnBuy = QPushButton(self.frameActions)
        self.btnBuy.setObjectName(u"btnBuy")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnBuy.sizePolicy().hasHeightForWidth())
        self.btnBuy.setSizePolicy(sizePolicy1)
        self.btnBuy.setMinimumSize(QSize(120, 30))
        self.btnBuy.setFont(font2)
        self.btnBuy.setStyleSheet(u"border: 1px solid #274b6f;\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"background-color: #52b74d;\n"
"color: rgb(255, 255, 255);")

        self.actionsLayout.addWidget(self.btnBuy)

        self.btnSale = QPushButton(self.frameActions)
        self.btnSale.setObjectName(u"btnSale")
        sizePolicy1.setHeightForWidth(self.btnSale.sizePolicy().hasHeightForWidth())
        self.btnSale.setSizePolicy(sizePolicy1)
        self.btnSale.setMinimumSize(QSize(120, 30))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setKerning(True)
        self.btnSale.setFont(font5)
        self.btnSale.setCursor(QCursor(Qt.ArrowCursor))
        self.btnSale.setMouseTracking(False)
        self.btnSale.setStyleSheet(u"border: 1px solid #28496a;\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"background-color: #ef384c;\n"
"color: rgb(255, 255, 255);")

        self.actionsLayout.addWidget(self.btnSale)


        self.horizontalLayout_2.addWidget(self.frameActions, 0, Qt.AlignVCenter)


        self.mainLayout.addWidget(self.frameHeader, 0, Qt.AlignTop)

        self.frameChart = QFrame(Form)
        self.frameChart.setObjectName(u"frameChart")
        self.frameChart.setMinimumSize(QSize(0, 400))
        self.chartLayout = QVBoxLayout(self.frameChart)
        self.chartLayout.setObjectName(u"chartLayout")

        self.mainLayout.addWidget(self.frameChart)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.labelLogo.setText("")
        self.labelSymbol.setText(QCoreApplication.translate("Form", u"TSLA", None))
        self.labelCompany.setText(QCoreApplication.translate("Form", u"TESLA LTD", None))
        self.labelCurntPriceValue.setText(QCoreApplication.translate("Form", u"80.25 USD", None))
        self.labelChange.setText(QCoreApplication.translate("Form", u"0.5%", None))
        self.labelOpen.setText(QCoreApplication.translate("Form", u"Open Price: ", None))
        self.openPriceValue.setText(QCoreApplication.translate("Form", u"80.15 USD", None))
        self.labelClose.setText(QCoreApplication.translate("Form", u"Close Price: ", None))
        self.ClosePriceValue.setText(QCoreApplication.translate("Form", u"80.40 USD", None))
        self.btnBuy.setText(QCoreApplication.translate("Form", u"Buy", None))
        self.btnSale.setText(QCoreApplication.translate("Form", u"Sale", None))
        pass
    # retranslateUi

