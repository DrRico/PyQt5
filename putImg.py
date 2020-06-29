import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtGui as QtGui

class filedialogdemo(QWidget):

  def __init__(self, parent=None):
    super(filedialogdemo, self).__init__(parent)
    layout = QVBoxLayout()

    self.label = QLabel(self)
    self.label.setPixmap(QPixmap('./newestMap.png'))
    self.label.move(300, 20) # 起始的位置
    self.label.setFixedSize(1440, 560)  # 照片显示的位置 #'''



    '''self.setWindowTitle("设置背景图片")
    window_pale = QtGui.QPalette()
    window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./newestMap.png")))
    self.setPalette(window_pale)   # '''

    self.btn = QPushButton()
    self.btn.clicked.connect(self.loadFile)
    self.btn.setFixedSize(150, 30)

    self.btn.setText("获取照片")
    layout.addWidget(self.btn)

    self.label = QLabel()
    layout.addWidget(self.label)


    '''self.content = QTextEdit()
    layout.addWidget(self.content)'''
    self.setWindowTitle("室内图像定位系统")
    self.setWindowIcon(QIcon('web.png'))
    self.setLayout(layout)
    self.setGeometry(200, 200, 1650, 760)  # 设置窗口的位置和尺寸

  def loadFile(self):
    print("load--file")
    fname, _ = QFileDialog.getOpenFileName(self, '选择图片', './', 'Image files(*.jpg *.gif *.png)')
    self.label.setPixmap(QPixmap(fname))


if __name__ == '__main__':
  app = QApplication(sys.argv)
  fileload = filedialogdemo()
  fileload.show()
  sys.exit(app.exec_())