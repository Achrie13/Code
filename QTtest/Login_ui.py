# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        Form.resize(700, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(700, 500))
        Form.setMaximumSize(QSize(700, 500))
        self.Login = QPushButton(Form)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(220, 310, 200, 30))
        self.Username = QSplitter(Form)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(220, 210, 200, 30))
        self.Username.setOrientation(Qt.Horizontal)
        self.img1 = QLabel(self.Username)
        self.img1.setObjectName(u"img1")
        self.img1.setPixmap(QPixmap(u"images/YXC.jpg"))
        self.Username.addWidget(self.img1)
        self.username = QLineEdit(self.Username)
        self.username.setObjectName(u"username")
        self.Username.addWidget(self.username)
        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(220, 260, 200, 30))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.img2 = QLabel(self.splitter_2)
        self.img2.setObjectName(u"img2")
        self.img2.setPixmap(QPixmap(u"images/YXC.jpg"))
        self.splitter_2.addWidget(self.img2)
        self.password = QLineEdit(self.splitter_2)
        self.password.setObjectName(u"password")
        self.splitter_2.addWidget(self.password)
        self.Title = QSplitter(Form)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(190, 90, 300, 50))
        self.Title.setOrientation(Qt.Horizontal)
        self.Logo = QLabel(self.Title)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setPixmap(QPixmap(u"images/YXC.jpg"))
        self.Title.addWidget(self.Logo)
        self.title = QLabel(self.Title)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setWordWrap(False)
        self.Title.addWidget(self.title)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.Login.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.img1.setText("")
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.img2.setText("")
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.Logo.setText("")
        self.title.setText(QCoreApplication.translate("Form", u"WB\u5b66\u9662\u7ba1\u7406\u7cfb\u7edf", None))
    # retranslateUi

