import threading

import ui_ViewWidget
from PyQt5.QtCore import pyqtSlot, QFileInfo, pyqtSignal, QBuffer, QByteArray, QIODevice, QSize, Qt
from PyQt5.QtGui import QMovie, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel
import requests
import os
import json
from util import system_util
from util import sm_util

# 资源路径
ROOT_URL = './asset/'
UPLOAD_ICON_URL = 'upload.png'
LOADING_GIF_URL = 'loading.gif'


class ViewWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.ui = ui_ViewWidget.Ui_widgetView()
        self.ui.setupUi(self)
        self.del_url = str()

    @pyqtSlot(QPixmap)
    def slot_recv_img(self, pixmap):
        self.set_image(pixmap)

    @pyqtSlot(str)
    def slot_recv_resp(self, resp_json):
        if resp_json is not '':
            ret = json.loads(resp_json)
            self.del_url = ret['delete']

    def set_image(self, pixmap):
        """
        pixmap适应label
        :param label:
        :param pixmap:
        :return:
        """
        label = self.ui.labelImage
        if pixmap.width() > self.ui.labelImage.width() or pixmap.height() > self.ui.labelImage.height():
            label.setPixmap(pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio))
        else:
            label.setPixmap(pixmap)

    @pyqtSlot()
    def on_pushButtonDel_clicked(self):
        print('del: ' + self.del_url)
        if self.del_url is not None and self.del_url is not '':
            sm_util.delete_img(self.del_url)

    def beautify_button(self, button, image_url):
        """
        美化按键
        :param button:  QPushButton
        :param image_url: str
        :return: None
        """
        button.setText('')
        button.setIcon(QIcon(image_url))
        icon_width = button.height() >> 1
        button.setIconSize(QSize(icon_width, icon_width))
        button.setFlat(True)

    def beautify_button0(self, button, image_url):
        """
        美化按键(背景透明)
        :param button:  QPushButton
        :param image_url: str
        :return: None
        """
        pic = QPixmap(image_url)
        button.setText('')
        button.setIcon(QIcon(pic))
        button.setStyleSheet("QPushButton{background: transparent;border:none}")
        icon_width = button.height() >> 1
        button.setIconSize(QSize(icon_width, icon_width))
        button.setFlat(True)
