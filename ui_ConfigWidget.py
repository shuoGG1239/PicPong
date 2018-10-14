# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ConfigWidget.ui'
#
# Created: Sun Oct 14 18:34:40 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_configWidget(object):
    def setupUi(self, configWidget):
        configWidget.setObjectName("configWidget")
        configWidget.resize(450, 320)
        self.checkBoxMin = QtWidgets.QCheckBox(configWidget)
        self.checkBoxMin.setGeometry(QtCore.QRect(30, 20, 121, 16))
        self.checkBoxMin.setObjectName("checkBoxMin")

        self.retranslateUi(configWidget)
        QtCore.QMetaObject.connectSlotsByName(configWidget)

    def retranslateUi(self, configWidget):
        _translate = QtCore.QCoreApplication.translate
        configWidget.setWindowTitle(_translate("configWidget", "Form"))
        self.checkBoxMin.setText(_translate("configWidget", "截图时最小化"))

