# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1065, 887)
        self.label_login = QtWidgets.QLabel(login)
        self.label_login.setGeometry(QtCore.QRect(170, 10, 641, 331))
        self.label_login.setStyleSheet("font: 100pt \"Blackadder ITC\";")
        self.label_login.setObjectName("label_login")
        self.label_userName = QtWidgets.QLabel(login)
        self.label_userName.setGeometry(QtCore.QRect(180, 360, 101, 41))
        self.label_userName.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.label_userName.setObjectName("label_userName")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(180, 420, 111, 61))
        self.label_3.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.label_3.setObjectName("label_3")
        self.input_userName = QtWidgets.QLineEdit(login)
        self.input_userName.setGeometry(QtCore.QRect(310, 370, 371, 20))
        self.input_userName.setObjectName("input_userName")
        self.input_Password = QtWidgets.QLineEdit(login)
        self.input_Password.setGeometry(QtCore.QRect(310, 440, 371, 20))
        self.input_Password.setObjectName("input_Password")
        self.button_commit = QtWidgets.QPushButton(login)
        self.button_commit.setGeometry(QtCore.QRect(300, 520, 271, 81))
        self.button_commit.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.button_commit.setObjectName("button_commit")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.label_login.setText(_translate("login", "LOGIN"))
        self.label_userName.setText(_translate("login", "USERNAME:"))
        self.label_3.setText(_translate("login", "PASSWORD:"))
        self.button_commit.setText(_translate("login", "commit"))