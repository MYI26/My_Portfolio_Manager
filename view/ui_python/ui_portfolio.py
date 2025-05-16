# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'portfolio.ui'
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
    QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Frame_Portfolio(object):
    def setupUi(self, Frame_Portfolio):
        if not Frame_Portfolio.objectName():
            Frame_Portfolio.setObjectName(u"Frame_Portfolio")
        Frame_Portfolio.resize(1067, 484)
        Frame_Portfolio.setLayoutDirection(Qt.RightToLeft)
        Frame_Portfolio.setStyleSheet(u"#Frame_Portfolio{	\n"
"	\n"
"	border: 1px solid #274b6f;\n"
"	border-radius: 5px;\n"
"	padding: 5px 10px;\n"
"	color: rgb(40, 73, 107);\n"
"	background-color: rgb(249, 249, 249);\n"
"}\n"
"\n"
"")
        Frame_Portfolio.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout = QVBoxLayout(Frame_Portfolio)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.labelTitle = QLabel(Frame_Portfolio)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"font-weight: bold; font-size: 18px;\n"
"color: rgb(40, 75, 107);")
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.labelTitle.setMargin(20)

        self.verticalLayout.addWidget(self.labelTitle)

        self.frameHeaderRow = QFrame(Frame_Portfolio)
        self.frameHeaderRow.setObjectName(u"frameHeaderRow")
        self.frameHeaderRow.setLayoutDirection(Qt.LeftToRight)
        self.frameHeaderRow.setStyleSheet(u"#frameHeaderRow{	\n"
"	\n"
"	border: 1px solid #274b6f;\n"
"	border-radius: 10;\n"
"	color: rgb(40, 73, 107);\n"
"}")
        self.frameHeaderRow.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.frameHeaderRow)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.labelCompany = QLabel(self.frameHeaderRow)
        self.labelCompany.setObjectName(u"labelCompany")
        self.labelCompany.setStyleSheet(u"color: rgb(40, 75, 107);")

        self.horizontalLayout_9.addWidget(self.labelCompany)

        self.labelStocks = QLabel(self.frameHeaderRow)
        self.labelStocks.setObjectName(u"labelStocks")

        self.horizontalLayout_9.addWidget(self.labelStocks)

        self.label_14 = QLabel(self.frameHeaderRow)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.labelTotalPrice = QLabel(self.frameHeaderRow)
        self.labelTotalPrice.setObjectName(u"labelTotalPrice")

        self.horizontalLayout_9.addWidget(self.labelTotalPrice)

        self.labelCurrentPrice = QLabel(self.frameHeaderRow)
        self.labelCurrentPrice.setObjectName(u"labelCurrentPrice")

        self.horizontalLayout_9.addWidget(self.labelCurrentPrice)

        self.labelPerfDollar = QLabel(self.frameHeaderRow)
        self.labelPerfDollar.setObjectName(u"labelPerfDollar")

        self.horizontalLayout_9.addWidget(self.labelPerfDollar)

        self.labelPerfPercent = QLabel(self.frameHeaderRow)
        self.labelPerfPercent.setObjectName(u"labelPerfPercent")

        self.horizontalLayout_9.addWidget(self.labelPerfPercent)


        self.verticalLayout.addWidget(self.frameHeaderRow)

        self.listWidgetStocks = QListWidget(Frame_Portfolio)
        self.listWidgetStocks.setObjectName(u"listWidgetStocks")
        self.listWidgetStocks.setLayoutDirection(Qt.LeftToRight)
        self.listWidgetStocks.setFrameShape(QFrame.NoFrame)
        self.listWidgetStocks.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidgetStocks.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.listWidgetStocks)

        self.frameSummary = QFrame(Frame_Portfolio)
        self.frameSummary.setObjectName(u"frameSummary")
        self.frameSummary.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setPointSize(11)
        self.frameSummary.setFont(font)
        self.frameSummary.setStyleSheet(u"color: rgb(40, 75, 107);")
        self.horizontalLayout = QHBoxLayout(self.frameSummary)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 250, -1)
        self.frame = QFrame(self.frameSummary)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setBold(False)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(82, 183, 77);")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: rgb(82, 183, 77);")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_8.addWidget(self.label_13)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frameSummary)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(82, 183, 77);")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(82, 183, 77);")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frameSummary)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(82, 183, 77);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(82, 183, 77);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frameSummary)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 16, -1, -1)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frameSummary)


        self.retranslateUi(Frame_Portfolio)

        self.listWidgetStocks.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(Frame_Portfolio)
    # setupUi

    def retranslateUi(self, Frame_Portfolio):
        self.labelTitle.setText(QCoreApplication.translate("Frame_Portfolio", u"Portfolio Overview", None))
        self.labelCompany.setText(QCoreApplication.translate("Frame_Portfolio", u"COMPANY", None))
        self.labelStocks.setText(QCoreApplication.translate("Frame_Portfolio", u"STOCKS", None))
        self.label_14.setText(QCoreApplication.translate("Frame_Portfolio", u"QUANTITY", None))
        self.labelTotalPrice.setText(QCoreApplication.translate("Frame_Portfolio", u"TOTAL PRICE", None))
        self.labelCurrentPrice.setText(QCoreApplication.translate("Frame_Portfolio", u"CURRENT PRICE", None))
        self.labelPerfDollar.setText(QCoreApplication.translate("Frame_Portfolio", u"PERFORMANCE $", None))
        self.labelPerfPercent.setText(QCoreApplication.translate("Frame_Portfolio", u"PERFORMANCE %", None))
        self.label_10.setText(QCoreApplication.translate("Frame_Portfolio", u"15 $", None))
        self.label_11.setText(QCoreApplication.translate("Frame_Portfolio", u"Current liquidity", None))
        self.label_12.setText(QCoreApplication.translate("Frame_Portfolio", u"12 $", None))
        self.label_13.setText(QCoreApplication.translate("Frame_Portfolio", u"Portfolio value", None))
        self.label_6.setText(QCoreApplication.translate("Frame_Portfolio", u"15 $", None))
        self.label_7.setText(QCoreApplication.translate("Frame_Portfolio", u"Performance $", None))
        self.label_8.setText(QCoreApplication.translate("Frame_Portfolio", u"12 $", None))
        self.label_9.setText(QCoreApplication.translate("Frame_Portfolio", u"Performence %", None))
        self.label_2.setText(QCoreApplication.translate("Frame_Portfolio", u"160 $", None))
        self.label_3.setText(QCoreApplication.translate("Frame_Portfolio", u"Stock value initial", None))
        self.label_4.setText(QCoreApplication.translate("Frame_Portfolio", u"175 $", None))
        self.label_5.setText(QCoreApplication.translate("Frame_Portfolio", u"stock value Curent", None))
        self.label.setText(QCoreApplication.translate("Frame_Portfolio", u"Total of Portfolio:", None))
        pass
    # retranslateUi

