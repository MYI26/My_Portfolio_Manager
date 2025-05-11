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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        Form.setStyleSheet(u"background-color: rgb(248, 248, 248);\n"
"border: none;\n"
"")
        self.mainLayout = QVBoxLayout(Form)
        self.mainLayout.setObjectName(u"mainLayout")
        self.frameHeader = QFrame(Form)
        self.frameHeader.setObjectName(u"frameHeader")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameHeader.sizePolicy().hasHeightForWidth())
        self.frameHeader.setSizePolicy(sizePolicy)
        self.frameHeader.setMinimumSize(QSize(0, 0))
        self.frameHeader.setStyleSheet(u"color: rgb(40, 73, 107);\n"
"background-color: rgb(255, 255, 255);")
        self.headerLayout = QHBoxLayout(self.frameHeader)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(-1, 30, -1, 40)
        self.frameActions = QFrame(self.frameHeader)
        self.frameActions.setObjectName(u"frameActions")
        self.frameActions.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameActions.sizePolicy().hasHeightForWidth())
        self.frameActions.setSizePolicy(sizePolicy1)
        self.frameActions.setMinimumSize(QSize(200, 0))
        self.actionsLayout = QVBoxLayout(self.frameActions)
        self.actionsLayout.setObjectName(u"actionsLayout")
        self.actionsLayout.setContentsMargins(40, -1, 40, -1)
        self.btnSale = QPushButton(self.frameActions)
        self.btnSale.setObjectName(u"btnSale")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnSale.sizePolicy().hasHeightForWidth())
        self.btnSale.setSizePolicy(sizePolicy2)
        self.btnSale.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.btnSale.setFont(font)
        self.btnSale.setCursor(QCursor(Qt.ArrowCursor))
        self.btnSale.setMouseTracking(False)
        self.btnSale.setStyleSheet(u"color: white; \n"
"background-color: rgb(82, 183, 77);\n"
"border-color: rgb(157, 157, 157);")

        self.actionsLayout.addWidget(self.btnSale)

        self.btnBuy = QPushButton(self.frameActions)
        self.btnBuy.setObjectName(u"btnBuy")
        sizePolicy2.setHeightForWidth(self.btnBuy.sizePolicy().hasHeightForWidth())
        self.btnBuy.setSizePolicy(sizePolicy2)
        self.btnBuy.setMinimumSize(QSize(120, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.btnBuy.setFont(font1)
        self.btnBuy.setStyleSheet(u"color: white;\n"
"background-color: rgb(228, 60, 76);\n"
"border-color: rgb(117, 117, 117);")

        self.actionsLayout.addWidget(self.btnBuy)


        self.headerLayout.addWidget(self.frameActions, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame = QFrame(self.frameHeader)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.headerLayout.addWidget(self.frame)

        self.frameData = QFrame(self.frameHeader)
        self.frameData.setObjectName(u"frameData")
        sizePolicy1.setHeightForWidth(self.frameData.sizePolicy().hasHeightForWidth())
        self.frameData.setSizePolicy(sizePolicy1)
        self.frameData.setMinimumSize(QSize(150, 0))
        self.frameData.setStyleSheet(u"")
        self.dataLayout = QVBoxLayout(self.frameData)
        self.dataLayout.setObjectName(u"dataLayout")
        self.dataLayout.setContentsMargins(20, -1, -1, -1)
        self.labelOpen = QLabel(self.frameData)
        self.labelOpen.setObjectName(u"labelOpen")

        self.dataLayout.addWidget(self.labelOpen)

        self.openPriceValue = QLabel(self.frameData)
        self.openPriceValue.setObjectName(u"openPriceValue")
        self.openPriceValue.setFont(font1)
        self.openPriceValue.setMargin(0)

        self.dataLayout.addWidget(self.openPriceValue)

        self.labelClose = QLabel(self.frameData)
        self.labelClose.setObjectName(u"labelClose")
        self.labelClose.setStyleSheet(u"margin-top: 10px;")
        self.labelClose.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelClose.setMargin(0)

        self.dataLayout.addWidget(self.labelClose)

        self.ClosePriceValue = QLabel(self.frameData)
        self.ClosePriceValue.setObjectName(u"ClosePriceValue")
        self.ClosePriceValue.setFont(font1)

        self.dataLayout.addWidget(self.ClosePriceValue)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dataLayout.addItem(self.verticalSpacer_2)


        self.headerLayout.addWidget(self.frameData)

        self.frameName = QFrame(self.frameHeader)
        self.frameName.setObjectName(u"frameName")
        sizePolicy1.setHeightForWidth(self.frameName.sizePolicy().hasHeightForWidth())
        self.frameName.setSizePolicy(sizePolicy1)
        self.frameName.setMinimumSize(QSize(150, 0))
        self.frameName.setAutoFillBackground(False)
        self.frameName.setStyleSheet(u"")
        self.nameLayout = QVBoxLayout(self.frameName)
        self.nameLayout.setSpacing(4)
        self.nameLayout.setObjectName(u"nameLayout")
        self.nameLayout.setContentsMargins(20, -1, -1, -1)
        self.labelSymbol = QLabel(self.frameName)
        self.labelSymbol.setObjectName(u"labelSymbol")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(15)
        font2.setKerning(True)
        self.labelSymbol.setFont(font2)
        self.labelSymbol.setStyleSheet(u"")

        self.nameLayout.addWidget(self.labelSymbol)

        self.labelCompany = QLabel(self.frameName)
        self.labelCompany.setObjectName(u"labelCompany")
        self.labelCompany.setStyleSheet(u"")

        self.nameLayout.addWidget(self.labelCompany)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.nameLayout.addItem(self.verticalSpacer)

        self.labelCurntPriceValue = QLabel(self.frameName)
        self.labelCurntPriceValue.setObjectName(u"labelCurntPriceValue")
        font3 = QFont()
        font3.setPointSize(13)
        self.labelCurntPriceValue.setFont(font3)
        self.labelCurntPriceValue.setStyleSheet(u"margin-top: -0px;")

        self.nameLayout.addWidget(self.labelCurntPriceValue)

        self.labelChange = QLabel(self.frameName)
        self.labelChange.setObjectName(u"labelChange")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        self.labelChange.setFont(font4)
        self.labelChange.setStyleSheet(u"color: rgb(82, 183, 77);")

        self.nameLayout.addWidget(self.labelChange)


        self.headerLayout.addWidget(self.frameName)

        self.frameLogo = QFrame(self.frameHeader)
        self.frameLogo.setObjectName(u"frameLogo")
        sizePolicy1.setHeightForWidth(self.frameLogo.sizePolicy().hasHeightForWidth())
        self.frameLogo.setSizePolicy(sizePolicy1)
        self.frameLogo.setMinimumSize(QSize(150, 0))
        self.frameLogo.setFrameShape(QFrame.StyledPanel)
        self.frameLogo.setFrameShadow(QFrame.Raised)
        self.labelLogo = QLabel(self.frameLogo)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(30, 0, 101, 121))
        self.labelLogo.setPixmap(QPixmap(u"../../../resources/logos/logo.png"))
        self.labelLogo.setScaledContents(True)

        self.headerLayout.addWidget(self.frameLogo)


        self.mainLayout.addWidget(self.frameHeader)

        self.frameChart = QFrame(Form)
        self.frameChart.setObjectName(u"frameChart")
        self.chartLayout = QVBoxLayout(self.frameChart)
        self.chartLayout.setObjectName(u"chartLayout")

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
        self.labelCurntPriceValue.setText(QCoreApplication.translate("Form", u"80.25 USD", None))
        self.labelChange.setText(QCoreApplication.translate("Form", u"0.5%", None))
        self.labelLogo.setText("")
        pass
    # retranslateUi

