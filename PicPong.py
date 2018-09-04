import ui_PicPong
from PyQt5.QtCore import pyqtSlot, QFileInfo, pyqtSignal, QBuffer, QByteArray, QIODevice, QSize
from PyQt5.QtGui import QMovie, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel
from QCandyUi.CandyWindow import colorful
import requests
import os
import json

# 资源路径
ROOT_URL = './asset/'
CUT_ICON_URL = 'scissors.png'
CONFIG_ICON_URL = 'config.png'
SET_ICON_URL = 'set.png'
VIEW_ICON_URL = 'view.png'
OPEN_FILE_ICON_URL = 'file.png'
FRAME_FILE_ICON_URL = 'frame.png'


@colorful('blueGreen')
class PicPong(QWidget):
    signal1 = pyqtSignal()  # 定义信号
    signal2 = pyqtSignal(int)  # 定义信息

    def __init__(self):
        QWidget.__init__(self)
        self.ui = ui_PicPong.Ui_picPong()
        self.ui.setupUi(self)
        self.__init_style()

    def __btn_style3(self):
        self.beautify_button3(self.ui.pushButtonCut, ROOT_URL, 'scissors.png', 'scissors.png', 'scissors.png', 'scissors.png')
        self.beautify_button3(self.ui.pushButtonSet, ROOT_URL, 'set.png', 'set.png', 'set.png', 'set.png')
        self.beautify_button3(self.ui.pushButtonView, ROOT_URL, 'view.png', 'view.png', 'view.png', 'view.png')
        self.beautify_button3(self.ui.pushButtonConfig, ROOT_URL, 'config.png', 'config_hover.png', 'config.png', 'config.png')
        self.beautify_button3(self.ui.pushButtonUpload, ROOT_URL, 'frame.png', 'frame.png', 'frame.png', 'frame.png')

    def __btn_style1(self):
        self.beautify_button(self.ui.pushButtonCut, ROOT_URL + 'scissors.png')
        self.beautify_button(self.ui.pushButtonSet, ROOT_URL + 'set.png')
        self.beautify_button(self.ui.pushButtonView, ROOT_URL + 'view.png')
        self.beautify_button(self.ui.pushButtonConfig, ROOT_URL + 'config.png')
        self.beautify_button(self.ui.pushButtonUpload, ROOT_URL + 'frame.png')

    def __init_style(self):
        self.ui.widgetSide.setStyleSheet("QWidget{background: #33CCCC;border:none}")
        self.ui.widgetView.setStyleSheet("QWidget#widgetView{background: #FFFFFF;border:none}")
        self.__btn_style1()

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
        img_full_path = QFileDialog.getOpenFileName()[0]
        if img_full_path is None or img_full_path == '':
            return
        _, name = os.path.split(img_full_path)
        view_url = self.upload_image(img_full_path)
        md_url = '![%s](%s)' % (name, view_url)
        self.ui.lineEdit.setText(md_url)

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

    def upload_image(self, image_path):
        files_map = [('smfile', image_path)]
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
            return view_url
        elif result['code'] == 'error':
            print('upload failed! Reason:' + result['msg'])
        else:
            print("upload failed! Unknown reason...")

    def beautify_button3(self, button, root, norm, hover, press, disable):
        qss = str()
        qss += "QPushButton{background:transparent; border-image:url(%s); border:none}" % (
            root + norm)
        qss += "QPushButton:hover{background:transparent; border-image:url(%s)}" % (
            root + hover)
        qss += "QPushButton:pressed{background:transparent; border-image:url(%s)}" % (
            root + press)
        qss += "QPushButton:disabled{background:transparent; border-image:url(%s)}" % (
            root + disable)
        button.setStyleSheet(qss)
        button.setText('')
        button.setFlat(True)
