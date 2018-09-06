from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

import PicPong

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = PicPong.PicPong()
    mainWindow.setWindowTitle('PicPong')
    mainWindow.setWindowIcon(QIcon('shuoGG_re'))
    mainWindow.setStyleSheet("QFrame#WindowWithTitleBar{background: #33CCCC}")
    mainWindow.setStyleSheet("QWidget#uploadWidget{background: #FFFFFF}")
    # fixSize
    mainWindow.setSupportStretch(False)
    mainWindow.setMaxEnable(False)
    # 不然快捷键失效
    mainWindow.mainwidget.setFocus()
    mainWindow.show()
    sys.exit(app.exec_())