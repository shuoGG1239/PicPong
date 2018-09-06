# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_PicPong.ui'
#
# Created: Wed Sep  5 16:17:08 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_picPong(object):
    def setupUi(self, picPong):
        picPong.setObjectName("picPong")
        picPong.resize(490, 329)
        self.widgetSide = QtWidgets.QWidget(picPong)
        self.widgetSide.setGeometry(QtCore.QRect(0, 0, 41, 331))
        self.widgetSide.setMinimumSize(QtCore.QSize(40, 200))
        self.widgetSide.setMaximumSize(QtCore.QSize(71, 2000))
        self.widgetSide.setObjectName("widgetSide")
        self.pushButtonUp = QtWidgets.QPushButton(self.widgetSide)
        self.pushButtonUp.setGeometry(QtCore.QRect(8, 10, 25, 25))
        self.pushButtonUp.setObjectName("pushButtonUp")
        self.pushButtonView = QtWidgets.QPushButton(self.widgetSide)
        self.pushButtonView.setGeometry(QtCore.QRect(8, 49, 25, 25))
        self.pushButtonView.setObjectName("pushButtonView")
        self.pushButtonCut = QtWidgets.QPushButton(self.widgetSide)
        self.pushButtonCut.setGeometry(QtCore.QRect(8, 89, 25, 25))
        self.pushButtonCut.setObjectName("pushButtonCut")
        self.pushButtonConfig = QtWidgets.QPushButton(self.widgetSide)
        self.pushButtonConfig.setGeometry(QtCore.QRect(8, 291, 25, 25))
        self.pushButtonConfig.setObjectName("pushButtonConfig")

        self.retranslateUi(picPong)
        QtCore.QMetaObject.connectSlotsByName(picPong)

    def retranslateUi(self, picPong):
        _translate = QtCore.QCoreApplication.translate
        picPong.setWindowTitle(_translate("picPong", "Form"))
        self.pushButtonUp.setText(_translate("picPong", "1"))
        self.pushButtonView.setText(_translate("picPong", "2"))
        self.pushButtonCut.setText(_translate("picPong", "3"))
        self.pushButtonConfig.setText(_translate("picPong", "c"))

