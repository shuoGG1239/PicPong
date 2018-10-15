# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ViewWidget.ui'
#
# Created: Mon Oct 15 20:44:09 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widgetView(object):
    def setupUi(self, widgetView):
        widgetView.setObjectName("widgetView")
        widgetView.resize(450, 320)
        self.pushButtonDel = QtWidgets.QPushButton(widgetView)
        self.pushButtonDel.setGeometry(QtCore.QRect(18, 280, 411, 23))
        self.pushButtonDel.setObjectName("pushButtonDel")
        self.labelImage = QtWidgets.QLabel(widgetView)
        self.labelImage.setGeometry(QtCore.QRect(18, 10, 411, 261))
        self.labelImage.setFrameShape(QtWidgets.QFrame.Box)
        self.labelImage.setText("")
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setObjectName("labelImage")

        self.retranslateUi(widgetView)
        QtCore.QMetaObject.connectSlotsByName(widgetView)

    def retranslateUi(self, widgetView):
        _translate = QtCore.QCoreApplication.translate
        widgetView.setWindowTitle(_translate("widgetView", "Form"))
        self.pushButtonDel.setText(_translate("widgetView", "Delete"))

