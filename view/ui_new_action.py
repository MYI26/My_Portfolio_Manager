# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_action.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Frame_New_Action(object):
    def setupUi(self, Frame_New_Action):
        if not Frame_New_Action.objectName():
            Frame_New_Action.setObjectName(u"Frame_New_Action")
        Frame_New_Action.resize(1067, 600)
        Frame_New_Action.setStyleSheet(u"#Frame_New_Action {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(Frame_New_Action)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(Frame_New_Action)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"font-size: 24px; font-weight: bold; color: rgb(40, 75, 107);")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitle)

        self.lineEditSearch = QLineEdit(Frame_New_Action)
        self.lineEditSearch.setObjectName(u"lineEditSearch")
        self.lineEditSearch.setStyleSheet(u"border: 1px solid rgb(40, 75, 107); border-radius: 5px; padding: 8px; font-size: 14px;")

        self.verticalLayout.addWidget(self.lineEditSearch)

        self.scrollArea = QScrollArea(Frame_New_Action)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1047, 497))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Frame_New_Action)

        QMetaObject.connectSlotsByName(Frame_New_Action)
    # setupUi

    def retranslateUi(self, Frame_New_Action):
        self.labelTitle.setText(QCoreApplication.translate("Frame_New_Action", u"New Action", None))
        self.lineEditSearch.setPlaceholderText(QCoreApplication.translate("Frame_New_Action", u"Search for a stock...", None))
        pass
    # retranslateUi

