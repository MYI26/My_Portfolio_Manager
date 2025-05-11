# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'time_range_selector.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnWeek = QPushButton(Form)
        self.btnWeek.setObjectName(u"btnWeek")

        self.horizontalLayout.addWidget(self.btnWeek)

        self.btnMonth = QPushButton(Form)
        self.btnMonth.setObjectName(u"btnMonth")

        self.horizontalLayout.addWidget(self.btnMonth)

        self.btnThreeMonths = QPushButton(Form)
        self.btnThreeMonths.setObjectName(u"btnThreeMonths")

        self.horizontalLayout.addWidget(self.btnThreeMonths)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.btnWeek.setText(QCoreApplication.translate("Form", u"\u05e9\u05d1\u05d5\u05e2", None))
        self.btnMonth.setText(QCoreApplication.translate("Form", u"\u05d7\u05d5\u05d3\u05e9", None))
        self.btnThreeMonths.setText(QCoreApplication.translate("Form", u"3 \u05d7\u05d5\u05d3\u05e9\u05d9\u05dd", None))
        pass
    # retranslateUi

