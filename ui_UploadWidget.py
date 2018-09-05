# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_UploadWidget.ui'
#
# Created: Wed Sep  5 15:58:35 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_uploadWidget(object):
    def setupUi(self, uploadWidget):
        uploadWidget.setObjectName("uploadWidget")
        uploadWidget.resize(450, 320)
        self.lineEdit = QtWidgets.QLineEdit(uploadWidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 278, 411, 31))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonUpload = QtWidgets.QPushButton(uploadWidget)
        self.pushButtonUpload.setGeometry(QtCore.QRect(40, 11, 370, 258))
        self.pushButtonUpload.setObjectName("pushButtonUpload")

        self.retranslateUi(uploadWidget)
        QtCore.QMetaObject.connectSlotsByName(uploadWidget)

    def retranslateUi(self, uploadWidget):
        _translate = QtCore.QCoreApplication.translate
        uploadWidget.setWindowTitle(_translate("uploadWidget", "Form"))
        self.pushButtonUpload.setText(_translate("uploadWidget", "Upload"))

