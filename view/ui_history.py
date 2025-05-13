# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Frame_History(object):
    def setupUi(self, Frame_History):
        if not Frame_History.objectName():
            Frame_History.setObjectName(u"Frame_History")
        Frame_History.resize(1067, 484)
        Frame_History.setLayoutDirection(Qt.RightToLeft)
        Frame_History.setStyleSheet(u"#Frame_Portfolio{	\n"
"	\n"
"	border: 1px solid #274b6f;\n"
"	border-radius: 5px;\n"
"	padding: 5px 10px;\n"
"	color: rgb(40, 73, 107);\n"
"	background-color: rgb(249, 249, 249);\n"
"}\n"
"\n"
"")
        Frame_History.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout = QVBoxLayout(Frame_History)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.labelTitle = QLabel(Frame_History)
        self.labelTitle.setObjectName(u"labelTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setStyleSheet(u"font-weight: bold; font-size: 18px;\n"
"color: rgb(40, 75, 107);")
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.labelTitle.setMargin(10)

        self.verticalLayout.addWidget(self.labelTitle, 0, Qt.AlignBottom)

        self.frame_combo_box = QFrame(Frame_History)
        self.frame_combo_box.setObjectName(u"frame_combo_box")
        self.frame_combo_box.setMinimumSize(QSize(0, 0))
        self.frame_combo_box.setFrameShape(QFrame.StyledPanel)
        self.frame_combo_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_combo_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, 20)
        self.comboBox = QComboBox(self.frame_combo_box)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setStyleSheet(u"#comboBox{\n"
"background-color: rgb(40, 75, 107);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"padding 5px;\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addWidget(self.frame_combo_box, 0, Qt.AlignRight)

        self.frameHeaderRow = QFrame(Frame_History)
        self.frameHeaderRow.setObjectName(u"frameHeaderRow")
        self.frameHeaderRow.setLayoutDirection(Qt.LeftToRight)
        self.frameHeaderRow.setStyleSheet(u"#frameHeaderRow{	\n"
"	\n"
"	border-bottom: 2px solid #274b6f;\n"
"	padding: 5px;\n"
"	color: rgb(40, 73, 107);\n"
"}")
        self.frameHeaderRow.setFrameShape(QFrame.Box)
        self.headerLayout = QHBoxLayout(self.frameHeaderRow)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(20, -1, 20, -1)
        self.label_symbole = QLabel(self.frameHeaderRow)
        self.label_symbole.setObjectName(u"label_symbole")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_symbole.setFont(font1)
        self.label_symbole.setStyleSheet(u"color: rgb(40, 75, 107);")

        self.headerLayout.addWidget(self.label_symbole)

        self.labelCompany = QLabel(self.frameHeaderRow)
        self.labelCompany.setObjectName(u"labelCompany")
        self.labelCompany.setStyleSheet(u"color: rgb(40, 75, 107);")

        self.headerLayout.addWidget(self.labelCompany)

        self.labelDate = QLabel(self.frameHeaderRow)
        self.labelDate.setObjectName(u"labelDate")

        self.headerLayout.addWidget(self.labelDate)

        self.labelOrder = QLabel(self.frameHeaderRow)
        self.labelOrder.setObjectName(u"labelOrder")

        self.headerLayout.addWidget(self.labelOrder)

        self.labelStockPrice = QLabel(self.frameHeaderRow)
        self.labelStockPrice.setObjectName(u"labelStockPrice")

        self.headerLayout.addWidget(self.labelStockPrice)

        self.labelAmount = QLabel(self.frameHeaderRow)
        self.labelAmount.setObjectName(u"labelAmount")

        self.headerLayout.addWidget(self.labelAmount)

        self.labelTotalPrice_2 = QLabel(self.frameHeaderRow)
        self.labelTotalPrice_2.setObjectName(u"labelTotalPrice_2")

        self.headerLayout.addWidget(self.labelTotalPrice_2)


        self.verticalLayout.addWidget(self.frameHeaderRow)

        self.listWidgetOrders = QListWidget(Frame_History)
        self.listWidgetOrders.setObjectName(u"listWidgetOrders")
        self.listWidgetOrders.setLayoutDirection(Qt.LeftToRight)
        self.listWidgetOrders.setFrameShape(QFrame.NoFrame)
        self.listWidgetOrders.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.listWidgetOrders)


        self.retranslateUi(Frame_History)

        self.listWidgetOrders.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(Frame_History)
    # setupUi

    def retranslateUi(self, Frame_History):
        self.labelTitle.setText(QCoreApplication.translate("Frame_History", u"Order History", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Frame_History", u"All", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Frame_History", u"Buy", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Frame_History", u"Sale", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Frame_History", u"All", None))
        self.label_symbole.setText(QCoreApplication.translate("Frame_History", u"SYMBOLE", None))
        self.labelCompany.setText(QCoreApplication.translate("Frame_History", u"COMPANY", None))
        self.labelDate.setText(QCoreApplication.translate("Frame_History", u"DATE", None))
        self.labelOrder.setText(QCoreApplication.translate("Frame_History", u"ORDER", None))
        self.labelStockPrice.setText(QCoreApplication.translate("Frame_History", u"STOCK PRICE", None))
        self.labelAmount.setText(QCoreApplication.translate("Frame_History", u"AMOUNT", None))
        self.labelTotalPrice_2.setText(QCoreApplication.translate("Frame_History", u"TOTAL PRICE", None))
        pass
    # retranslateUi

