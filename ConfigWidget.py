from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

import ui_ConfigWidget


class ConfigWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.ui = ui_ConfigWidget.Ui_configWidget()
        self.ui.setupUi(self)
        self.minWhenCut = self.ui.checkBoxMin.isChecked()

    @pyqtSlot(int)
    def on_checkBoxMin_stateChanged(self, state):
        if state == 0:
            self.minWhenCut = False
        else:
            self.minWhenCut = True
