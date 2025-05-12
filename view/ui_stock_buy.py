# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_buy.ui'
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
        self.frame_header.setLayoutDirection(Qt.LeftToRight)
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
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
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
        self.commandLinkButton.setLayoutDirection(Qt.LeftToRight)
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
        self.frame_data.setStyleSheet(u"#frame_data{	\n"
"	\n"
"	\n"
"	color: rgb(40, 73, 107);\n"
"}\n"
"")
        self.frame_data.setFrameShape(QFrame.NoFrame)
        self.frame_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_data)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame_data)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(250, 30))
        font3 = QFont()
        font3.setPointSize(4)
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setFrame(True)

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setLineWidth(0)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_6)
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


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_data)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)
        self.lineEdit_3.setMinimumSize(QSize(250, 30))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.lineEdit_3)


        self.horizontalLayout_10.addWidget(self.frame_10)

        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setLineWidth(0)

        self.horizontalLayout_12.addWidget(self.label_5)


        self.horizontalLayout_10.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_5)
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


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_data)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.frame_16 = QFrame(self.frame_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lineEdit_4 = QLineEdit(self.frame_16)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy2.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy2)
        self.lineEdit_4.setMinimumSize(QSize(250, 30))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.lineEdit_4)


        self.horizontalLayout_14.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_8)


        self.horizontalLayout_14.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_9 = QLabel(self.frame_18)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_9)


        self.horizontalLayout_14.addWidget(self.frame_18)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_data)


        self.verticalLayout_2.addWidget(self.frame_info)

        self.frame_actio_buttn = QFrame(frame_root)
        self.frame_actio_buttn.setObjectName(u"frame_actio_buttn")
        self.frame_actio_buttn.setMinimumSize(QSize(0, 50))
        self.frame_actio_buttn.setFrameShape(QFrame.NoFrame)
        self.frame_actio_buttn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_actio_buttn)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.button_bay = QPushButton(self.frame_actio_buttn)
        self.button_bay.setObjectName(u"button_bay")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_bay.sizePolicy().hasHeightForWidth())
        self.button_bay.setSizePolicy(sizePolicy3)
        self.button_bay.setMinimumSize(QSize(150, 35))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        self.button_bay.setFont(font4)
        self.button_bay.setStyleSheet(u"border: 2px solid #274b6f;\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"background-color: #52b74d;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.button_bay.setAutoRepeatDelay(5)
        self.button_bay.setAutoRepeatInterval(5)
        self.button_bay.setFlat(False)

        self.horizontalLayout_18.addWidget(self.button_bay)


        self.verticalLayout_2.addWidget(self.frame_actio_buttn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(frame_root)

        self.button_bay.setDefault(False)


        QMetaObject.connectSlotsByName(frame_root)
    # setupUi

    def retranslateUi(self, frame_root):
        frame_root.setWindowTitle(QCoreApplication.translate("frame_root", u"Frame", None))
        self.commandLinkButton.setText("")
        self.label_11.setText(QCoreApplication.translate("frame_root", u"1000$", None))
        self.label_10.setText(QCoreApplication.translate("frame_root", u"Balance:", None))
        self.label_7.setText("")
        self.label_2.setText(QCoreApplication.translate("frame_root", u"100$", None))
        self.label.setText(QCoreApplication.translate("frame_root", u"Total price", None))
        self.label_5.setText(QCoreApplication.translate("frame_root", u"1.5 stocks", None))
        self.label_6.setText(QCoreApplication.translate("frame_root", u"Stocks amount", None))
        self.label_8.setText(QCoreApplication.translate("frame_root", u"5.5$", None))
        self.label_9.setText(QCoreApplication.translate("frame_root", u"Service price", None))
        self.button_bay.setText(QCoreApplication.translate("frame_root", u"Bay Now", None))
    # retranslateUi

