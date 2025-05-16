# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from resources import resources_rc

class Ui_Frame_main_window(object):
    def setupUi(self, Frame_main_window):
        if not Frame_main_window.objectName():
            Frame_main_window.setObjectName(u"Frame_main_window")
        Frame_main_window.resize(1067, 600)
        font = QFont()
        font.setPointSize(10)
        Frame_main_window.setFont(font)
        Frame_main_window.setStyleSheet(u"background-color: rgb(248, 248, 248);\n"
"gridline-color: none;\n"
"color: rgb(40, 75, 107);")
        self.verticalLayout = QVBoxLayout(Frame_main_window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 30, 20, 0)
        self.frame_header = QFrame(Frame_main_window)
        self.frame_header.setObjectName(u"frame_header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_header.sizePolicy().hasHeightForWidth())
        self.frame_header.setSizePolicy(sizePolicy)
        self.frame_header.setMaximumSize(QSize(16777215, 80))
        self.frame_header.setFont(font)
        self.frame_header.setStyleSheet(u"background-color: rgb(40, 75, 107);\n"
"color: rgb(255, 255, 255);")
        self.frame_header.setFrameShape(QFrame.NoFrame)
        self.frame_header.setFrameShadow(QFrame.Plain)
        self.frame_header.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.fram_sespace = QFrame(self.frame_header)
        self.fram_sespace.setObjectName(u"fram_sespace")
        self.fram_sespace.setMinimumSize(QSize(200, 0))
        self.fram_sespace.setFrameShape(QFrame.StyledPanel)
        self.fram_sespace.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.fram_sespace)

        self.frame_chatAi = QFrame(self.frame_header)
        self.frame_chatAi.setObjectName(u"frame_chatAi")
        self.frame_chatAi.setFrameShape(QFrame.StyledPanel)
        self.frame_chatAi.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_chatAi)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_AiChat = QPushButton(self.frame_chatAi)
        self.pushButton_AiChat.setObjectName(u"pushButton_AiChat")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_AiChat.sizePolicy().hasHeightForWidth())
        self.pushButton_AiChat.setSizePolicy(sizePolicy1)
        self.pushButton_AiChat.setMinimumSize(QSize(120, 35))
        self.pushButton_AiChat.setFont(font)

        self.horizontalLayout_6.addWidget(self.pushButton_AiChat)


        self.horizontalLayout.addWidget(self.frame_chatAi)

        self.frame_action = QFrame(self.frame_header)
        self.frame_action.setObjectName(u"frame_action")
        self.frame_action.setFrameShape(QFrame.StyledPanel)
        self.frame_action.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_action)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_action = QPushButton(self.frame_action)
        self.pushButton_action.setObjectName(u"pushButton_action")
        sizePolicy1.setHeightForWidth(self.pushButton_action.sizePolicy().hasHeightForWidth())
        self.pushButton_action.setSizePolicy(sizePolicy1)
        self.pushButton_action.setMinimumSize(QSize(120, 35))
        self.pushButton_action.setFont(font)

        self.horizontalLayout_5.addWidget(self.pushButton_action)


        self.horizontalLayout.addWidget(self.frame_action)

        self.frame_history = QFrame(self.frame_header)
        self.frame_history.setObjectName(u"frame_history")
        self.frame_history.setFrameShape(QFrame.NoFrame)
        self.frame_history.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_history)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_hom_2 = QPushButton(self.frame_history)
        self.pushButton_hom_2.setObjectName(u"pushButton_hom_2")
        sizePolicy1.setHeightForWidth(self.pushButton_hom_2.sizePolicy().hasHeightForWidth())
        self.pushButton_hom_2.setSizePolicy(sizePolicy1)
        self.pushButton_hom_2.setMinimumSize(QSize(120, 35))
        self.pushButton_hom_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_hom_2)


        self.horizontalLayout.addWidget(self.frame_history)

        self.frame_home = QFrame(self.frame_header)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setFrameShape(QFrame.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.frame_home.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_hom = QPushButton(self.frame_home)
        self.pushButton_hom.setObjectName(u"pushButton_hom")
        sizePolicy1.setHeightForWidth(self.pushButton_hom.sizePolicy().hasHeightForWidth())
        self.pushButton_hom.setSizePolicy(sizePolicy1)
        self.pushButton_hom.setMinimumSize(QSize(120, 35))
        self.pushButton_hom.setFont(font)
        self.pushButton_hom.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.pushButton_hom, 0, Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_home)

        self.frame_user = QFrame(self.frame_header)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setMinimumSize(QSize(0, 0))
        self.frame_user.setFont(font)
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(40, 0, 0, 0)
        self.frame = QFrame(self.frame_user)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(160000, 1600000))
        font1 = QFont()
        font1.setPointSize(11)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_icon__user = QLabel(self.frame)
        self.label_icon__user.setObjectName(u"label_icon__user")
        self.label_icon__user.setMinimumSize(QSize(40, 35))
        self.label_icon__user.setMaximumSize(QSize(40, 30))
        self.label_icon__user.setFont(font)
        self.label_icon__user.setPixmap(QPixmap(u":/icons/wallet.png"))
        self.label_icon__user.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_icon__user, 0, Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.frame_user, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_header)

        self.frame_content = QFrame(Frame_main_window)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content.setLineWidth(0)

        self.verticalLayout.addWidget(self.frame_content)


        self.retranslateUi(Frame_main_window)

        QMetaObject.connectSlotsByName(Frame_main_window)
    # setupUi

    def retranslateUi(self, Frame_main_window):
        Frame_main_window.setWindowTitle(QCoreApplication.translate("Frame_main_window", u"Frame", None))
        self.pushButton_AiChat.setText(QCoreApplication.translate("Frame_main_window", u"Ask Ai Chat", None))
        self.pushButton_action.setText(QCoreApplication.translate("Frame_main_window", u"New action", None))
        self.pushButton_hom_2.setText(QCoreApplication.translate("Frame_main_window", u"History", None))
        self.pushButton_hom.setText(QCoreApplication.translate("Frame_main_window", u"Home", None))
        self.label_icon__user.setText("")
    # retranslateUi

