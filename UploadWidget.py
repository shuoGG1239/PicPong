import json
import os
import threading

from PyQt5.QtCore import pyqtSlot, QFileInfo, pyqtSignal, QSize
from PyQt5.QtGui import QMovie, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel

import ui_UploadWidget
from util import sm_util
from util import system_util

# 资源路径
ROOT_URL = './asset/'
UPLOAD_ICON_URL = 'upload.png'
LOADING_GIF_URL = 'loading.gif'


class UploadWidget(QWidget):
    signal_fail = pyqtSignal(str)
    signal_response = pyqtSignal(str)  # sm应答信号
    signal_img = pyqtSignal(QPixmap)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.ui = ui_UploadWidget.Ui_uploadWidget()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.ui.pushButtonUpload.setAcceptDrops(False)
        self.signal_response.connect(self.__slot_sm_response)
        self.__init_loading_gif()
        self.__init_style()

    def __init_style(self):
        """
        带button外壳的imageButton
        :return:
        """
        self.setStyleSheet("QWidget#widgetView{background: #FFFFFF;border:none}")
        self.__btn_style3()

    def __btn_style1(self):
        """
        只带图片的imageButton, 但只有单态
        :return:
        """
        self.beautify_button(self.ui.pushButtonUpload, ROOT_URL + 'upload.png')

    def __btn_style3(self):
        """
        三态button
        :return:
        """
        self.beautify_button3(self.ui.pushButtonUpload, ROOT_URL, 'upload.png', 'upload_hover.png', 'upload.png',
                              'upload.png')

    def beautify_button3(self, button, root, norm, hover, press, disable):
        qss = str()
        qss += "QPushButton{background:transparent; background-image:url(%s); border:none}" % (
                root + norm)
        qss += "QPushButton:hover{background:transparent; background-image:url(%s)}" % (
                root + hover)
        qss += "QPushButton:pressed{background:transparent; background-image:url(%s)}" % (
                root + press)
        qss += "QPushButton:disabled{background:transparent; background-image:url(%s)}" % (
                root + disable)
        button.setStyleSheet(qss)
        button.setText('')

    @pyqtSlot()
    def on_pushButtonUpload_clicked(self):
        self.ui.lineEdit.clear()
        img_full_path = QFileDialog.getOpenFileName()[0]
        if img_full_path is None or img_full_path == '':
            return
        _, name = os.path.split(img_full_path)
        self.signal_img.emit(QPixmap(img_full_path))
        self.run_upload_async(img_full_path)

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
        result_dict = dict()
        try:
            result_dict = sm_util.upload_img(image_path)
            return result_dict['url']
        except:
            self.signal_fail.emit('上传失败!')
        finally:
            self.signal_response.emit(json.dumps(result_dict))

    @pyqtSlot(str)
    def __slot_sm_response(self, resp_json):
        self.loadingLabel.hide()
        if resp_json is not '':
            ret = json.loads(resp_json)
            md_image = '![' + ret['filename'] + '](' + ret['url'] + ')'
            self.ui.lineEdit.setText(md_image)
            system_util.set_clipboard_text(md_image)

    def __init_loading_gif(self):
        """
        初始化loading动画
        :return:
        """
        gif = QMovie(ROOT_URL + LOADING_GIF_URL)
        gif.start()
        x, y = 190, 110
        self.loadingLabel = QLabel(self)
        self.loadingLabel.setMovie(gif)
        self.loadingLabel.adjustSize()
        self.loadingLabel.setGeometry(x, y, self.loadingLabel.width(), self.loadingLabel.height())
        self.loadingLabel.setVisible(False)

    def dragEnterEvent(self, event):
        if (event.mimeData().hasUrls()):
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if (event.mimeData().hasUrls()):
            event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            self.ui.lineEdit.clear()
            urlList = event.mimeData().urls()
            fileInfo = QFileInfo(urlList[0].toLocalFile())
            img_full_path = fileInfo.filePath()
            self.signal_img.emit(QPixmap(img_full_path))
            self.run_upload_async(img_full_path)
            event.acceptProposedAction()

    def run_upload_async(self, url):
        if self.loadingLabel is not None:
            self.loadingLabel.setVisible(True)
        threading.Thread(target=self.upload_image, args=(url,)).start()
