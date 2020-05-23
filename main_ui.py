# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(830, 566)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 0))
        Form.setFocusPolicy(Qt.NoFocus)
        Form.setContextMenuPolicy(Qt.NoContextMenu)
        Form.setAcceptDrops(False)
        Form.setStyleSheet(u"")
        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(300, 120, 411, 161))
        font = QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(u"")
        self.plainTextEdit_2 = QPlainTextEdit(Form)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QRect(300, 320, 411, 161))
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color: white;\n"
"}")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(720, 180, 91, 51))
        font1 = QFont()
        font1.setPointSize(10)
        self.pushButton.setFont(font1)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 91, 31))
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 90, 131, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 290, 111, 31))
        self.label_3.setFont(font)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(720, 370, 91, 51))
        self.pushButton_2.setFont(font1)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 490, 161, 51))
        self.pushButton_3.setFont(font1)
        self.plainTextEdit_3 = QPlainTextEdit(Form)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setEnabled(True)
        self.plainTextEdit_3.setGeometry(QRect(20, 40, 261, 441))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(12)
        self.plainTextEdit_3.setFont(font3)
        self.plainTextEdit_3.setStyleSheet(u"background-color: white")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(190, 490, 91, 51))
        self.pushButton_4.setFont(font1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 10, 191, 31))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(340, 50, 161, 21))
        self.lineEdit.setFont(font1)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(550, 50, 161, 21))
        self.lineEdit_2.setFont(font1)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 40, 51, 31))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(500, 40, 51, 31))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u042d\u0426\u041f  -  RSA", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \n"
"\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043d\u0441\u043e\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c \u0410", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c \u0411", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \n"
"\u042d\u0426\u041f", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c\n"
"\u043a\u043e\u043d\u0441\u043e\u043b\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0440\u043e\u0441\u0442\u044b\u0435 \u0447\u0438\u0441\u043b\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"p", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"q", None))
    # retranslateUi

