import ui_PicPong
from PyQt5.QtCore import pyqtSlot, QFileInfo, pyqtSignal, QBuffer, QByteArray, QIODevice, QSize
from PyQt5.QtGui import QMovie, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel
from QCandyUi.CandyWindow import colorful
import requests
import os
import json

# 资源路径
CUT_ICON_URL = './asset/scissors.png'
CONFIG_ICON_URL = './asset/config.png'
SET_ICON_URL = './asset/set.png'
VIEW_ICON_URL = './asset/view.png'
OPEN_FILE_ICON_URL = './asset/file.png'
FRAME_FILE_ICON_URL = './asset/frame.png'


@colorful('blueGreen')
class PicPong(QWidget):
    signal1 = pyqtSignal()  # 定义信号
    signal2 = pyqtSignal(int)  # 定义信息

    def __init__(self):
        QWidget.__init__(self)
        self.ui = ui_PicPong.Ui_picPong()
        self.ui.setupUi(self)
        self.beautify_button0(self.ui.pushButtonCut, CUT_ICON_URL)
        self.beautify_button0(self.ui.pushButtonSet, SET_ICON_URL)
        self.beautify_button0(self.ui.pushButtonView, VIEW_ICON_URL)
        self.beautify_button0(self.ui.pushButtonConfig, CONFIG_ICON_URL)
        self.beautify_button0(self.ui.pushButtonUpload, FRAME_FILE_ICON_URL)
        self.__init_style()


    def __init_style(self):
        self.ui.widgetSide.setStyleSheet("QWidget{background: #33CCCC;border:none}")


    @pyqtSlot()
    def on_pushButtonCut_clicked(self):
        print("cut")

    @pyqtSlot()
    def on_pushButtonView_clicked(self):
        print("view")

    @pyqtSlot()
    def on_pushButtonSet_clicked(self):
        print("set")

    @pyqtSlot()
    def on_pushButtonConfig_clicked(self):
        print("config")

    @pyqtSlot()
    def on_pushButtonUpload_clicked(self):
        print("upload")
        # self.upload_image()

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
        美化按键
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

    def upload_image(self):
        files_map = [('smfile', r'E:\Picture\menhera\26765571@2x.png')]
        params = {
            'ssl': False,
            'format': 'png'
        }
        multi_files = list(map(lambda x: (x[0], (os.path.split(x[1])[1], open(x[1], 'rb'))), files_map))
        resp = requests.post("https://sm.ms/api/upload", data=params, files=multi_files)
        print(resp.text)
        result = json.loads(resp.text)
        if result['code'] == 'success':
            view_url = result['data']['url']
            del_url = result['data']['delete']
            print(view_url)
            print(del_url)
        elif result['code'] == 'error':
            print('upload failed! Reason:' + result['msg'])
        else:
            print("upload failed! Unknown reason...")
