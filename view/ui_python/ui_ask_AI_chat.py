# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ask_AI_chat.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AskAIChat(object):
    def setupUi(self, AskAIChat):
        if not AskAIChat.objectName():
            AskAIChat.setObjectName(u"AskAIChat")
        AskAIChat.resize(1067, 484)
        AskAIChat.setLayoutDirection(Qt.LeftToRight)
        AskAIChat.setStyleSheet(u"#AskAIChat{	\n"
"	\n"
"	border: 1px solid #274b6f;\n"
"	border-radius: 5px;\n"
"	padding: 5px 10px;\n"
"	color: rgb(40, 73, 107);\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.horizontalLayout = QHBoxLayout(AskAIChat)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(AskAIChat)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 300))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.label_title = QLabel(self.frame_2)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setEnabled(True)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setMargin(20)

        self.verticalLayout_2.addWidget(self.label_title)

        self.text_input = QTextEdit(self.frame_2)
        self.text_input.setObjectName(u"text_input")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_input.sizePolicy().hasHeightForWidth())
        self.text_input.setSizePolicy(sizePolicy)
        self.text_input.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(11)
        self.text_input.setFont(font)
        self.text_input.setStyleSheet(u"\n"
"	border: 1px solid #274b6f;\n"
"	border-radius: 5px;\n"
"	padding: 5px 10px;\n"
"	color: rgb(40, 73, 107);\n"
"	background-color: rgb(249, 249, 249);\n"
"")

        self.verticalLayout_2.addWidget(self.text_input)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.button_send = QPushButton(self.frame)
        self.button_send.setObjectName(u"button_send")
        self.button_send.setStyleSheet(u"\n"
"       background-color: rgb(40, 75, 107);\n"
"       color: white;\n"
"       padding: 5px;\n"
"	border-radius: 5px;\n"
"      ")

        self.verticalLayout_3.addWidget(self.button_send)

        self.button_clear = QPushButton(self.frame)
        self.button_clear.setObjectName(u"button_clear")
        font1 = QFont()
        self.button_clear.setFont(font1)
        self.button_clear.setStyleSheet(u"\n"
"       background-color: rgb(228, 60, 76);\n"
"       color: white;\n"
"       padding: 5px;\n"
"	border-radius: 5px;\n"
"      ")

        self.verticalLayout_3.addWidget(self.button_clear)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.label_loading = QLabel(self.frame_2)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setVisible(True)
        self.label_loading.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_loading)

        self.scroll_area = QScrollArea(self.frame_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setLineWidth(0)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget = QWidget()
        self.scroll_area_widget.setObjectName(u"scroll_area_widget")
        self.scroll_area_widget.setGeometry(QRect(0, 0, 847, 191))
        self.scroll_area_widget.setStyleSheet(u"border: none;")
        self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_layout.setObjectName(u"scroll_area_layout")
        self.label_answer = QLabel(self.scroll_area_widget)
        self.label_answer.setObjectName(u"label_answer")
        self.label_answer.setFont(font1)
        self.label_answer.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_answer.setWordWrap(True)

        self.scroll_area_layout.addWidget(self.label_answer)

        self.scroll_area.setWidget(self.scroll_area_widget)

        self.verticalLayout_2.addWidget(self.scroll_area)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(AskAIChat)

        QMetaObject.connectSlotsByName(AskAIChat)
    # setupUi

    def retranslateUi(self, AskAIChat):
        AskAIChat.setWindowTitle(QCoreApplication.translate("AskAIChat", u"Ask AI Chat", None))
        self.label_title.setStyleSheet(QCoreApplication.translate("AskAIChat", u"\n"
"       font-size: 18px;\n"
"       font-weight: bold;\n"
"       color: rgb(40, 75, 107);\n"
"      ", None))
        self.label_title.setText(QCoreApplication.translate("AskAIChat", u"Ask AI Chat", None))
        self.text_input.setHtml(QCoreApplication.translate("AskAIChat", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_input.setPlaceholderText(QCoreApplication.translate("AskAIChat", u"Type your question here...", None))
        self.button_send.setText(QCoreApplication.translate("AskAIChat", u"Send", None))
        self.button_clear.setText(QCoreApplication.translate("AskAIChat", u"Clear", None))
        self.label_loading.setStyleSheet(QCoreApplication.translate("AskAIChat", u"\n"
"       font-size: 14px;\n"
"       color: rgb(150, 150, 150);\n"
"      ", None))
        self.label_loading.setText(QCoreApplication.translate("AskAIChat", u"Your answer is on the way...", None))
        self.label_answer.setStyleSheet(QCoreApplication.translate("AskAIChat", u"\n"
"           font-size: 14px;\n"
"           color: rgb(40, 75, 107);\n"
"          ", None))
        self.label_answer.setText("")
    # retranslateUi

