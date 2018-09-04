from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

import PicPong

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = PicPong.PicPong()
    mainWindow.setWindowTitle('PicPong')
    mainWindow.setWindowIcon(QIcon('shuoGG_re'))
    mainWindow.setStyleSheet("QWidget{background: #33CCCC;border:none}")
    mainWindow.show()
    sys.exit(app.exec_())