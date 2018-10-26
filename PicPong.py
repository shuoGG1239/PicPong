from PyQt5.QtCore import pyqtSlot, QSize, QRect, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget
from QCandyUi.CandyWindow import colorful

import ui_PicPong
from ConfigWidget import ConfigWidget
from UploadWidget import UploadWidget
from ViewWidget import ViewWidget
from screen_capture import CaptureScreen

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
    def __init__(self):
        QWidget.__init__(self)
        self.ui = ui_PicPong.Ui_picPong()
        self.ui.setupUi(self)
        self.widgetUpload = UploadWidget(self)
        self.widgetUpload.setGeometry(QRect(41, 0, 450, 360))
        self.widgetView = ViewWidget(self)
        self.widgetView.setGeometry(QRect(41, 0, 450, 360))
        self.widgetView.hide()
        self.widgetConfig = ConfigWidget(self)
        self.widgetConfig.setGeometry(QRect(41, 0, 450, 360))
        self.widgetConfig.hide()
        self.widgetUpload.signal_img.connect(self.widgetView.slot_recv_img)
        self.widgetUpload.signal_response.connect(self.widgetView.slot_recv_resp)
        self.widgetUpload.signal_fail.connect(self.__slot_showTip)
        self.__init_style()
        self.ui.pushButtonCut.setToolTip('ctrl+shift+alt+F8')

    def __init_style(self):
        self.ui.widgetSide.setStyleSheet("QWidget{background: #33CCCC;border:none}")
        self.widgetUpload.setStyleSheet("QWidget#uploadWidget{background: #FFFFFF;border:none}")
        self.__btn_style3()

    def __btn_style3(self):
        self.beautify_button3(self.ui.pushButtonUp, ROOT_URL, 'up.png', 'up_hover.png', 'up.png', 'up.png')
        self.beautify_button3(self.ui.pushButtonView, ROOT_URL, 'view.png', 'view_hover.png', 'view.png', 'view.png')
        self.beautify_button3(self.ui.pushButtonCut, ROOT_URL, 'scissors.png', 'scissors_hover.png', 'scissors.png',
                              'scissors.png')
        self.beautify_button3(self.ui.pushButtonConfig, ROOT_URL, 'config.png', 'config_hover.png', 'config.png',
                              'config.png')

    def __btn_style1(self):
        self.beautify_button(self.ui.pushButtonUp, ROOT_URL + 'set.png')
        self.beautify_button(self.ui.pushButtonView, ROOT_URL + 'view.png')
        self.beautify_button(self.ui.pushButtonCut, ROOT_URL + 'scissors.png')
        self.beautify_button(self.ui.pushButtonConfig, ROOT_URL + 'config.png')

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
    def on_pushButtonUp_clicked(self):
        self.widgetUpload.show()
        self.widgetConfig.hide()
        self.widgetView.hide()

    @pyqtSlot()
    def on_pushButtonCut_clicked(self):
        self.minimize()
        self.capture = CaptureScreen()
        self.capture.signal_complete_capture.connect(self.__slot_screen_capture)

    @pyqtSlot()
    def on_pushButtonView_clicked(self):
        self.widgetUpload.hide()
        self.widgetConfig.hide()
        self.widgetView.show()

    @pyqtSlot()
    def on_pushButtonConfig_clicked(self):
        self.widgetConfig.show()
        self.widgetUpload.hide()
        self.widgetView.hide()

    @pyqtSlot(str)
    def __slot_showTip(self, msg):
        self.parent().showTip(msg, 'red')

    @pyqtSlot(QPixmap)
    def __slot_screen_capture(self, pixmap):
        temp_img_path = 'screenShot.png'
        pixmap.save(temp_img_path, 'png')
        self.widgetUpload.run_upload_async(temp_img_path)
        self.widgetUpload.signal_img.emit(pixmap)

    def keyPressEvent(self, e):
        """
        ctrl+alt+shift+F8
        :param e:
        :return:
        """
        if (e.modifiers() == Qt.ControlModifier | Qt.AltModifier | Qt.ShiftModifier) \
                and (e.key() == Qt.Key_F8):
            self.minimize()
            self.on_pushButtonCut_clicked()

    def minimize(self):
        if self.widgetConfig.minWhenCut:
            self.parentWidget().showMinimized()
