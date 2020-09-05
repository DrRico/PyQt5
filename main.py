# -*- coding:utf-8 -*-
# author: DrRico time:2020/6/29
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog,QMessageBox
from PyQt5.QtGui import *
from position_btn import Ui_Form
sys.path.append(r'D:\Python_Shit\My_shit\TXEDU\Learning_SVM\My_HOG_LBP_SVM')
from MyCore import MyCore
fname = ''
class DetailUI(Ui_Form,QMainWindow):
    def __init__(self):
        super(DetailUI, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('室内定位系统')
        self.sig_img_btn.clicked.connect(self.openImage)
        self.mul_img_btn.clicked.connect(self.openFolder)
        self.exit_btn.clicked.connect(self.close)
        self.start_location_btn.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        global fname
        if fname == '':
            print("输入不能为空")
            self.messageDialog()
        else:
            a = MyCore(fname)
            a.mkdir()
            a.extra_feat()
            p, angle, showImg, isSingle = a.Predict()  # 进行预测
            if isSingle:
                self.x_text.setText(str(p[0]))
                self.y_text.setText(str(p[1]))
                self.angle_test.setText(angle)
            else:
                self.x_text.setText('')
                self.y_text.setText('')
                self.angle_test.setText('')

            self.result_img_show.setPixmap(QPixmap(str(showImg)))

    def messageDialog(self):
        msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有图像被选中')
        msg_box.exec_()

    def openImage(self):
        try:
            global fname
            fname , _ = QFileDialog.getOpenFileName(self, 'open file', r'D:\Python_Shit\My_shit\TXEDU\Learning_SVM\My_HOG_LBP_SVM\mate1283',"Image files (*.jpg *.gif *.png)")
            self.test_img_show.setPixmap(QPixmap(fname))
            self.test_img_show.setScaledContents(True)
        except:
            print('打开文件失败，可能是文件内型错误')
            self.test_img_show.setText("打开文件失败，可能是文件内型错误")

    def openFolder(self):
        try:
            global fname
            fname = QFileDialog.getExistingDirectory(self,"选取文件夹","./")  # 起始路径
            self.test_img_show.setText("你选择了\n"+fname+"内所有的图像")
            self.test_img_show.setWordWrap(True)

        except:
            self.test_img_show.setText("无法打开文件夹")
            # pass

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '警告', '退出后系统将停止,\n你确认要退出吗？',QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def runModel(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DetailUI()
    ex.show()
    # ex.pushButton_2.clicked.connect(DetailUI.openImage)
    sys.exit(app.exec_())

