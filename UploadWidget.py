import threading
import ui_UploadWidget
from PyQt5.QtCore import pyqtSlot, QFileInfo, pyqtSignal, QBuffer, QByteArray, QIODevice, QSize
from PyQt5.QtGui import QMovie, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel
import requests
import os
import json

# 资源路径
ROOT_URL = './asset/'
UPLOAD_ICON_URL = 'upload.png'
LOADING_GIF_URL = 'loading.gif'


class UploadWidget(QWidget):
    signal_response = pyqtSignal(str)  # sm应答信号

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
        self.setStyleSheet("QWidget#widgetView{background: #FFFFFF;border:none}")
        self.__btn_style3()

    def __btn_style3(self):
        self.beautify_button3(self.ui.pushButtonUpload, ROOT_URL, 'upload.png', 'upload_hover.png', 'upload.png', 'upload.png')

    def __btn_style1(self):
        self.beautify_button(self.ui.pushButtonUpload, ROOT_URL + 'upload.png')

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
        resp_json = str()
        try:
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
                resp_json = json.dumps({'url': view_url, 'delete': del_url})
                print(view_url)
                print(del_url)
                return view_url
            elif result['code'] == 'error':
                print('upload failed! Reason:' + result['msg'])
            else:
                print("upload failed! Unknown reason...")
        finally:
            self.signal_response.emit(resp_json)

    @pyqtSlot(str)
    def __slot_sm_response(self, resp_json):
        self.loadingLabel.hide()
        if resp_json is not '':
            ret = json.loads(resp_json)
            self.ui.lineEdit.setText(ret['url'])

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
            urlList = event.mimeData().urls()
            fileInfo = QFileInfo(urlList[0].toLocalFile())
            img_full_path = fileInfo.filePath()
            self.run_upload_async(img_full_path)
            event.acceptProposedAction()

    def run_upload_async(self, url):
        if self.loadingLabel is not None:
            self.loadingLabel.setVisible(True)
        threading.Thread(target=self.upload_image, args=(url,)).start()