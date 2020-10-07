# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(966, 690)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(966, 690))
        Form.setMaximumSize(QSize(966, 690))
        Form.setFocusPolicy(Qt.NoFocus)
        Form.setContextMenuPolicy(Qt.NoContextMenu)
        Form.setAcceptDrops(False)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 966, 690))
        self.label.setPixmap(QPixmap(u"imgs/back_ground.png"))
        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(50, 120, 281, 411))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(11)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.plainTextEdit.setAutoFillBackground(False)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 550, 281, 91))
        font1 = QFont()
        font1.setFamily(u"Impact")
        font1.setPointSize(28)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.plainTextEdit_2 = QPlainTextEdit(Form)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(420, 140, 501, 231))
        font2 = QFont()
        font2.setPointSize(12)
        self.plainTextEdit_2.setFont(font2)
        self.plainTextEdit_3 = QPlainTextEdit(Form)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(420, 400, 501, 231))
        self.plainTextEdit_3.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u042d\u0426\u041f  -  RSA", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"START", None))
    # retranslateUi

