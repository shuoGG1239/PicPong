import json
import threading
from PyQt5.QtCore import pyqtSlot, QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget

import ui_ViewWidget
from util import sm_util

# 资源路径
ROOT_URL = './asset/'


class ViewWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.ui = ui_ViewWidget.Ui_widgetView()
        self.ui.setupUi(self)
        self.del_url = str()

    @pyqtSlot(QPixmap)
    def slot_recv_img(self, pixmap):
        self.__set_image(pixmap)

    @pyqtSlot(str)
    def slot_recv_resp(self, resp_json):
        if resp_json != '':
            ret = json.loads(resp_json)
            self.del_url = ret.get('delete')

    @pyqtSlot()
    def on_pushButtonDel_clicked(self):
        print('del: ' + self.del_url)
        if self.del_url is not None and self.del_url != '':
            threading.Thread(target=sm_util.delete_img, args=(self.del_url,)).start()
            self.del_url = ''
            self.ui.labelImage.clear()

    def __set_image(self, pixmap):
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
