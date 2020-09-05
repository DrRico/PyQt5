# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPixmap, QIcon


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1445, 780)
        Form.setMouseTracking(False)
        self.sig_img_btn = QtWidgets.QPushButton(Form)
        self.sig_img_btn.setEnabled(True)
        self.sig_img_btn.setGeometry(QtCore.QRect(80, 40, 130, 25))
        self.sig_img_btn.setObjectName("sig_img_btn")
        self.result_img_show = QtWidgets.QLabel(Form)
        self.result_img_show.setGeometry(QtCore.QRect(10, 210, 1430, 560))
        self.result_img_show.setText("")
        self.result_img_show.setPixmap(QtGui.QPixmap("newestMap.png"))
        self.result_img_show.setObjectName("result_img_show")
        self.label_angle = QtWidgets.QLabel(Form)
        self.label_angle.setGeometry(QtCore.QRect(630, 150, 51, 16))
        self.label_angle.setObjectName("label_angle")
        self.label_x = QtWidgets.QLabel(Form)
        self.label_x.setGeometry(QtCore.QRect(630, 30, 41, 16))
        self.label_x.setObjectName("label_x")
        self.label_y = QtWidgets.QLabel(Form)
        self.label_y.setGeometry(QtCore.QRect(630, 90, 41, 16))
        self.label_y.setObjectName("label_y")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(670, 0, 134, 201))
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
        # self.test_img_show = QtWidgets.QGraphicsView(Form)
        self.test_img_show = QtWidgets.QLabel(Form)
        self.test_img_show.setGeometry(QtCore.QRect(260, 10, 161, 191))
        self.test_img_show.setObjectName("test_img_show")

        # 设置颜色等信息
        col = QColor(255, 255, 255)
        self.test_img_show.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())

        self.mul_img_btn = QtWidgets.QPushButton(Form)
        self.mul_img_btn.setGeometry(QtCore.QRect(80, 100, 130, 25))
        self.mul_img_btn.setObjectName("mul_img_btn")
        self.start_location_btn = QtWidgets.QPushButton(Form)
        self.start_location_btn.setGeometry(QtCore.QRect(480, 60, 80, 80))
        self.start_location_btn.setObjectName("start_location_btn")
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(80, 160, 130, 25))
        self.exit_btn.setObjectName("exit_btn")
        # self.exit_btn.setStyleSheet("background-color: red")  # 设置按钮的风格和颜色
        #一些个性化的设置
        self.sig_img_btn.setIcon(QIcon("./pic.jpg"));
        self.mul_img_btn.setIcon(QIcon("./folder.jpg"));
        self.exit_btn.setIcon(QIcon("./exit.jpg"));
        self.start_location_btn.setStyleSheet("QPushButton{border-radius:20px; "
                                              "background:rgb(110, 190, 10); "
                                              "color:white;"
                                              "font-weight: bold;}"
                                              "QPushButton:hover{background:rgb(140, 220, 35);}")  # 设置按钮的风格和颜色

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sig_img_btn.setText(_translate("Form", "选择单个图像"))
        self.label_angle.setText(_translate("Form", "方位"))
        self.label_x.setText(_translate("Form", "经度"))
        self.label_y.setText(_translate("Form", "维度"))
        self.mul_img_btn.setText(_translate("Form", "选择文件夹"))
        self.start_location_btn.setText(_translate("Form", "开始定位"))
        self.exit_btn.setText(_translate("Form", "退出系统"))
