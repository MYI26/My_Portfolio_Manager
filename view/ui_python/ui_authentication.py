# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authentication.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)
from resources import resources_rc

class Ui_Frame_authentication(object):
    def setupUi(self, Frame_authentication):
        if not Frame_authentication.objectName():
            Frame_authentication.setObjectName(u"Frame_authentication")
        Frame_authentication.resize(1067, 600)
        font = QFont()
        font.setPointSize(10)
        Frame_authentication.setFont(font)
        Frame_authentication.setLayoutDirection(Qt.LeftToRight)
        Frame_authentication.setStyleSheet(u"background-color: rgb(248, 248, 248);\n"
"gridline-color: none;\n"
"color: rgb(40, 75, 107);")
        self.verticalLayout = QVBoxLayout(Frame_authentication)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 30, 20, 0)
        self.frame_header = QFrame(Frame_authentication)
        self.frame_header.setObjectName(u"frame_header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_header.sizePolicy().hasHeightForWidth())
        self.frame_header.setSizePolicy(sizePolicy)
        self.frame_header.setMaximumSize(QSize(16777215, 70))
        self.frame_header.setFont(font)
        self.frame_header.setStyleSheet(u"background-color: rgb(40, 75, 107);\n"
"color: rgb(255, 255, 255);")
        self.frame_header.setFrameShape(QFrame.NoFrame)
        self.frame_header.setFrameShadow(QFrame.Plain)
        self.frame_header.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_header)
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(40, -1, -1, -1)
        self.label_icon__user = QLabel(self.frame_header)
        self.label_icon__user.setObjectName(u"label_icon__user")
        self.label_icon__user.setMinimumSize(QSize(40, 35))
        self.label_icon__user.setMaximumSize(QSize(40, 30))
        self.label_icon__user.setFont(font)
        self.label_icon__user.setPixmap(QPixmap(u":/icons/wallet.png"))
        self.label_icon__user.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_icon__user)

        self.label_login = QLabel(self.frame_header)
        self.label_login.setObjectName(u"label_login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_login.sizePolicy().hasHeightForWidth())
        self.label_login.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_login)

        self.label_2 = QLabel(self.frame_header)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_header)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_header)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_4)

        self.frame = QFrame(self.frame_header)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_header)

        self.frame_content = QFrame(Frame_authentication)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_content)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 40, -1, -1)

        self.verticalLayout.addWidget(self.frame_content)


        self.retranslateUi(Frame_authentication)

        QMetaObject.connectSlotsByName(Frame_authentication)
    # setupUi

    def retranslateUi(self, Frame_authentication):
        Frame_authentication.setWindowTitle(QCoreApplication.translate("Frame_authentication", u"Frame", None))
        self.label_icon__user.setText("")
        self.label_login.setText(QCoreApplication.translate("Frame_authentication", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Frame_authentication", u"SignUp", None))
        self.label_3.setText(QCoreApplication.translate("Frame_authentication", u"Reset password", None))
        self.label_4.setText(QCoreApplication.translate("Frame_authentication", u"Remove acount", None))
    # retranslateUi

