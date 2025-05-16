# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_sale.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_frame_root(object):
    def setupUi(self, frame_root):
        if not frame_root.objectName():
            frame_root.setObjectName(u"frame_root")
        frame_root.resize(782, 377)
        font = QFont()
        font.setPointSize(11)
        frame_root.setFont(font)
        frame_root.setAcceptDrops(False)
        frame_root.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        frame_root.setFrameShape(QFrame.NoFrame)
        frame_root.setFrameShadow(QFrame.Plain)
        frame_root.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(frame_root)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.frame_header = QFrame(frame_root)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 0))
        self.frame_header.setLayoutDirection(Qt.RightToLeft)
        self.frame_header.setStyleSheet(u"#frame_header {\n"
"    border: 1px solid #284b6b;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame_header.setFrameShape(QFrame.NoFrame)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.frame_header.setLineWidth(1)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(9, 0, -1, 0)
        self.frame_21 = QFrame(self.frame_header)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_21)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 20, -1)
        self.commandLinkButton = QCommandLinkButton(self.frame_21)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy)
        self.commandLinkButton.setMinimumSize(QSize(30, 15))
        self.commandLinkButton.setMaximumSize(QSize(30, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        self.commandLinkButton.setFont(font1)
        self.commandLinkButton.setMouseTracking(False)
        self.commandLinkButton.setLayoutDirection(Qt.RightToLeft)
        self.commandLinkButton.setStyleSheet(u"color: rgb(40, 75, 107);\n"
"border-color: rgb(40, 75, 107);")
        self.commandLinkButton.setIconSize(QSize(25, 25))
        self.commandLinkButton.setAutoRepeatDelay(5)
        self.commandLinkButton.setAutoRepeatInterval(5)

        self.verticalLayout_4.addWidget(self.commandLinkButton)


        self.horizontalLayout_19.addWidget(self.frame_21, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_19 = QFrame(self.frame_header)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(115, 16777215))
        self.frame_19.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_19.setLineWidth(0)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, -1, 0, -1)
        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, -1, -1, -1)
        self.label_11 = QLabel(self.frame_22)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: rgb(82, 183, 77);")

        self.horizontalLayout_22.addWidget(self.label_11)


        self.horizontalLayout_20.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, -1, -1, -1)
        self.label_10 = QLabel(self.frame_23)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: rgb(40, 75, 107);")

        self.horizontalLayout_21.addWidget(self.label_10)


        self.horizontalLayout_20.addWidget(self.frame_23)


        self.horizontalLayout_19.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_header)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(80, 16777215))
        self.frame_20.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_20)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 51, 41))
        self.label_7.setPixmap(QPixmap(u"../../../Users/1/Pictures/Screenshots/\u05e6\u05d9\u05dc\u05d5\u05dd \u05de\u05e1\u05da 2025-05-12 012640.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.frame_20)


        self.verticalLayout_2.addWidget(self.frame_header)

        self.frame_info = QFrame(frame_root)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMinimumSize(QSize(0, 200))
        self.frame_info.setFont(font)
        self.frame_info.setStyleSheet(u"color: rgb(40, 75, 107);")
        self.frame_info.setFrameShape(QFrame.NoFrame)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_info)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(80, -1, 80, -1)
        self.frame_data = QFrame(self.frame_info)
        self.frame_data.setObjectName(u"frame_data")
        self.frame_data.setFont(font)
        self.frame_data.setStyleSheet(u"\n"
"#frame_data{	\n"
"	\n"
"	border: 1px solid #274b6f;\n"
"	border-radius: 5px;\n"
"	padding: 5px 10px;\n"
"	color: rgb(40, 73, 107);\n"
"}\n"
"")
        self.frame_data.setFrameShape(QFrame.NoFrame)
        self.frame_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_data)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_money_amount = QFrame(self.frame_data)
        self.frame_money_amount.setObjectName(u"frame_money_amount")
        self.frame_money_amount.setFont(font)
        self.frame_money_amount.setStyleSheet(u"color: rgb(40, 75, 107);")
        self.frame_money_amount.setFrameShape(QFrame.NoFrame)
        self.frame_money_amount.setFrameShadow(QFrame.Raised)
        self.frame_money_amount.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_money_amount)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.frame_9 = QFrame(self.frame_money_amount)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setFont(font)
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(250, 30))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setFrame(True)

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_label_money = QFrame(self.frame_money_amount)
        self.frame_label_money.setObjectName(u"frame_label_money")
        self.frame_label_money.setFrameShape(QFrame.NoFrame)
        self.frame_label_money.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_label_money)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_money = QLabel(self.frame_label_money)
        self.label_money.setObjectName(u"label_money")
        self.label_money.setFont(font)
        self.label_money.setFrameShadow(QFrame.Raised)
        self.label_money.setLineWidth(0)

        self.horizontalLayout_4.addWidget(self.label_money)


        self.horizontalLayout_2.addWidget(self.frame_label_money)

        self.frame_7 = QFrame(self.frame_money_amount)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_5.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame_money_amount)

        self.frame_stock_amount = QFrame(self.frame_data)
        self.frame_stock_amount.setObjectName(u"frame_stock_amount")
        self.frame_stock_amount.setFont(font)
        self.frame_stock_amount.setStyleSheet(u"color: rgb(40, 75, 107);")
        self.frame_stock_amount.setFrameShape(QFrame.NoFrame)
        self.frame_stock_amount.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_stock_amount)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.frame_10 = QFrame(self.frame_stock_amount)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(268, 0))
        self.frame_10.setFont(font)
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.horizontalLayout_10.addWidget(self.frame_10)

        self.frame_label_stock = QFrame(self.frame_stock_amount)
        self.frame_label_stock.setObjectName(u"frame_label_stock")
        self.frame_label_stock.setFrameShape(QFrame.StyledPanel)
        self.frame_label_stock.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_label_stock)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_stock = QLabel(self.frame_label_stock)
        self.label_stock.setObjectName(u"label_stock")
        self.label_stock.setFont(font)
        self.label_stock.setLineWidth(0)

        self.horizontalLayout_12.addWidget(self.label_stock)


        self.horizontalLayout_10.addWidget(self.frame_label_stock)

        self.frame_15 = QFrame(self.frame_stock_amount)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_6)


        self.horizontalLayout_10.addWidget(self.frame_15)


        self.verticalLayout_3.addWidget(self.frame_stock_amount)

        self.frame_service_and_total = QFrame(self.frame_data)
        self.frame_service_and_total.setObjectName(u"frame_service_and_total")
        self.frame_service_and_total.setMinimumSize(QSize(0, 0))
        self.frame_service_and_total.setFont(font)
        self.frame_service_and_total.setStyleSheet(u"color: rgb(40, 75, 107);")
        self.frame_service_and_total.setFrameShape(QFrame.NoFrame)
        self.frame_service_and_total.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_service_and_total)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_total = QFrame(self.frame_service_and_total)
        self.frame_total.setObjectName(u"frame_total")
        sizePolicy1.setHeightForWidth(self.frame_total.sizePolicy().hasHeightForWidth())
        self.frame_total.setSizePolicy(sizePolicy1)
        self.frame_total.setMinimumSize(QSize(268, 0))
        self.frame_total.setMaximumSize(QSize(16777215, 16777215))
        self.frame_total.setStyleSheet(u"background-color: rgb(40, 75, 107);\n"
"color: rgb(255, 255, 255);")
        self.frame_total.setFrameShape(QFrame.NoFrame)
        self.frame_total.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_total)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, 0, 20, 0)
        self.frame_2 = QFrame(self.frame_total)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_total = QLabel(self.frame_2)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_total)


        self.horizontalLayout_6.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_total)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_3)


        self.horizontalLayout_6.addWidget(self.frame)


        self.horizontalLayout_9.addWidget(self.frame_total)

        self.frame_17 = QFrame(self.frame_service_and_total)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_8)


        self.horizontalLayout_9.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_service_and_total)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_9 = QLabel(self.frame_18)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_9)


        self.horizontalLayout_9.addWidget(self.frame_18)


        self.verticalLayout_3.addWidget(self.frame_service_and_total)


        self.horizontalLayout.addWidget(self.frame_data)


        self.verticalLayout_2.addWidget(self.frame_info)

        self.frame_action_buttn = QFrame(frame_root)
        self.frame_action_buttn.setObjectName(u"frame_action_buttn")
        self.frame_action_buttn.setMinimumSize(QSize(0, 50))
        self.frame_action_buttn.setFrameShape(QFrame.NoFrame)
        self.frame_action_buttn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_action_buttn)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.button_sale = QPushButton(self.frame_action_buttn)
        self.button_sale.setObjectName(u"button_sale")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_sale.sizePolicy().hasHeightForWidth())
        self.button_sale.setSizePolicy(sizePolicy2)
        self.button_sale.setMinimumSize(QSize(150, 35))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.button_sale.setFont(font3)
        self.button_sale.setStyleSheet(u"border: 2px solid #274b6f;\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"background-color: #e43c4c;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.button_sale.setAutoRepeatDelay(5)
        self.button_sale.setAutoRepeatInterval(5)
        self.button_sale.setAutoDefault(False)

        self.horizontalLayout_18.addWidget(self.button_sale)


        self.verticalLayout_2.addWidget(self.frame_action_buttn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(frame_root)

        self.button_sale.setDefault(False)


        QMetaObject.connectSlotsByName(frame_root)
    # setupUi

    def retranslateUi(self, frame_root):
        frame_root.setWindowTitle(QCoreApplication.translate("frame_root", u"Frame", None))
        self.commandLinkButton.setText("")
        self.commandLinkButton.setDescription("")
        self.label_11.setText(QCoreApplication.translate("frame_root", u"1000$", None))
        self.label_10.setText(QCoreApplication.translate("frame_root", u"Balance:", None))
        self.label_7.setText("")
        self.label_money.setText(QCoreApplication.translate("frame_root", u"100$", None))
        self.label.setText(QCoreApplication.translate("frame_root", u"Money amount", None))
        self.label_stock.setText(QCoreApplication.translate("frame_root", u"1.5 stocks", None))
        self.label_6.setText(QCoreApplication.translate("frame_root", u"Stocks amount", None))
        self.label_total.setText(QCoreApplication.translate("frame_root", u"105.5$", None))
        self.label_3.setText(QCoreApplication.translate("frame_root", u"Total amount:", None))
        self.label_8.setText(QCoreApplication.translate("frame_root", u"0.0$", None))
        self.label_9.setText(QCoreApplication.translate("frame_root", u"Service price", None))
        self.button_sale.setText(QCoreApplication.translate("frame_root", u"Sell Now", None))
    # retranslateUi

