#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: feifan time:2019/5/21
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import *
from position import Ui_Form


class DetailUI(Ui_Form,QMainWindow):
    def __init__(self):
        super(DetailUI, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('室内定位系统')
        self.sig_img_btn.clicked.connect(self.openImage)


    def openImage(self):
        try:
            fname , _ = QFileDialog.getOpenFileName(self, 'open file', r'D:\Python_Shit\My_shit\TXEDU\Learning_SVM\My_HOG_LBP_SVM\mate1283',"Image files (*.jpg *.gif *.png)")
            #self.angle_test.setText(str(fname))
            #img = QPixmap(fname)
            #print(img)
            self.test_img_show.setPixmap(QPixmap(fname))
            self.test_img_show.setScaledContents(True)

        except:
            print('打开文件失败，可能是文件内型错误')
            self.test_img_show.setText("打开文件失败，可能是文件内型错误")

    def runModel(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DetailUI()
    ex.show()
    # ex.pushButton_2.clicked.connect(DetailUI.openImage)
    sys.exit(app.exec_())
