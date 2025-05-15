# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sginup.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, # type: ignore
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, # type: ignore
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel, # type: ignore
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1027, 494)
        Frame.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 30, -1, 100)
        self.label_6 = QLabel(Frame)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(40, 75, 107);")

        self.verticalLayout.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(40, 75, 107)")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.frame_user_info = QFrame(Frame)
        self.frame_user_info.setObjectName(u"frame_user_info")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_user_info.sizePolicy().hasHeightForWidth())
        self.frame_user_info.setSizePolicy(sizePolicy)
        self.frame_user_info.setMinimumSize(QSize(600, 250))
        self.frame_user_info.setMaximumSize(QSize(600, 500))
        self.frame_user_info.setLayoutDirection(Qt.LeftToRight)
        self.frame_user_info.setStyleSheet(u"#frame_user_info{	\n"
"	\n"
"	border: 1px solid rgb(40, 75, 107);\n"
"	padding: 5px;\n"
"	color: rgb(40, 75, 107);\n"
"border-radius: 10;\n"
"}")
        self.frame_user_info.setFrameShape(QFrame.Box)
        self.frame_user_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_user_info)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 20, 30, 20)
        self.frame_3 = QFrame(self.frame_user_info)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setLayoutDirection(Qt.RightToLeft)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 2, -1, 2)
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(350, 0))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(40, 75, 107);")
        self.lineEdit_2.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_2, 0, Qt.AlignRight)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setStyleSheet(u"color: rgb(40, 75, 107);")

        self.horizontalLayout_4.addWidget(self.label_5, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_2 = QFrame(self.frame_user_info)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setLayoutDirection(Qt.RightToLeft)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 2, -1, 2)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(350, 0))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(40, 75, 107);")
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setStyleSheet(u"color: rgb(40, 75, 107);")

        self.horizontalLayout_2.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.frame_user_info)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setLayoutDirection(Qt.RightToLeft)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 2, -1, 2)
        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QSize(350, 0))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(40, 75, 107);")
        self.lineEdit_3.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setStyleSheet(u"color: rgb(40, 75, 107);")

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.frame_user_info)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 0))
        self.pushButton.setStyleSheet(u"border: 1px solid rgb(82, 183, 77);\n"
"padding: 5px;\n"
"color: rgb(40, 75, 107);\n"
"border-radius: 10;\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame_user_info)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLayoutDirection(Qt.RightToLeft)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setUnderline(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 161);")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_user_info, 0, Qt.AlignHCenter)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label_6.setText(QCoreApplication.translate("Frame", u"Welcome to your Stocks Portfolio!", None))
        self.label.setText(QCoreApplication.translate("Frame", u"Create your new account...", None))
        self.label_5.setText(QCoreApplication.translate("Frame", u"User name:", None))
        self.label_4.setText(QCoreApplication.translate("Frame", u"Email address", None))
        self.label_8.setText(QCoreApplication.translate("Frame", u"New password:", None))
        self.pushButton.setText(QCoreApplication.translate("Frame", u"Create account", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"Click here to Login", None))
        self.label_3.setText(QCoreApplication.translate("Frame", u"Do yo have already an  account? ", None))
    # retranslateUi

