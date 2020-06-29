# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'position_sys.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1445, 780)
        Form.setMouseTracking(False)
        self.sig_img_btn = QtWidgets.QPushButton(Form)
        self.sig_img_btn.setEnabled(True)
        self.sig_img_btn.setGeometry(QtCore.QRect(90, 60, 120, 25))
        self.sig_img_btn.setObjectName("sig_img_btn")
        self.result_img_show = QtWidgets.QLabel(Form)
        self.result_img_show.setGeometry(QtCore.QRect(10, 210, 1430, 560))
        self.result_img_show.setPixmap(QtGui.QPixmap("newestMap.png"))
        self.result_img_show.setObjectName("result_img_show")
        self.label_angle = QtWidgets.QLabel(Form)
        self.label_angle.setGeometry(QtCore.QRect(520, 160, 51, 16))
        self.label_angle.setObjectName("label_angle")
        self.label_x = QtWidgets.QLabel(Form)
        self.label_x.setGeometry(QtCore.QRect(530, 40, 41, 16))
        self.label_x.setObjectName("label_x")
        self.label_y = QtWidgets.QLabel(Form)
        self.label_y.setGeometry(QtCore.QRect(530, 100, 41, 16))
        self.label_y.setObjectName("label_y")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(570, 10, 134, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.y_text = QtWidgets.QLineEdit(self.layoutWidget)
        self.y_text.setObjectName("y_text")
        self.gridLayout.addWidget(self.y_text, 1, 0, 1, 1)
        self.angle_test = QtWidgets.QLineEdit(self.layoutWidget)
        self.angle_test.setObjectName("angle_test")
        self.gridLayout.addWidget(self.angle_test, 3, 0, 1, 1)
        self.x_text = QtWidgets.QLineEdit(self.layoutWidget)
        self.x_text.setObjectName("x_text")
        self.gridLayout.addWidget(self.x_text, 0, 0, 1, 1)
        #self.test_img_show = QtWidgets.QGraphicsView(Form)
        self.test_img_show = QtWidgets.QLabel(Form)
        self.test_img_show.setGeometry(QtCore.QRect(260, 10, 161, 191))
        # 设置颜色等信息
        col = QColor(255, 255, 255)
        self.test_img_show.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.test_img_show.setObjectName("test_img_show")
        self.mul_img_btn = QtWidgets.QPushButton(Form)
        self.mul_img_btn.setGeometry(QtCore.QRect(90, 120, 120, 25))
        self.mul_img_btn.setObjectName("mul_img_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sig_img_btn.setText(_translate("Form", "选择单个图像"))
        self.label_angle.setText(_translate("Form", "方位角"))
        self.label_x.setText(_translate("Form", "经度"))
        self.label_y.setText(_translate("Form", "维度"))
        self.mul_img_btn.setText(_translate("Form", "选择文件夹"))