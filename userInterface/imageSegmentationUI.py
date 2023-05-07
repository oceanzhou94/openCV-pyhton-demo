"""
@Auth ： youngZ
@File ：imageSegmentationUI.py
图像分割和融合UI
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '图像分割.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_save_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_img.setGeometry(QtCore.QRect(1130, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_save_img.setFont(font)
        self.pushButton_save_img.setObjectName("pushButton_save_img")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(940, 340, 450, 400))
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setWidgetResizable(False)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 4000, 4000))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_dealt_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_dealt_img.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        self.label_dealt_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_dealt_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_dealt_img.setObjectName("label_dealt_img")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 340, 450, 400))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 4000, 4000))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_source_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_source_img.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        self.label_source_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_source_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_source_img.setObjectName("label_source_img")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton_choose_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose_img.setGeometry(QtCore.QRect(210, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_choose_img.setFont(font)
        self.pushButton_choose_img.setObjectName("pushButton_choose_img")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(210, 100, 500, 200))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_watershed = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_watershed.setGeometry(QtCore.QRect(260, 50, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_watershed.setFont(font)
        self.pushButton_watershed.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_watershed.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_watershed.setObjectName("pushButton_watershed")
        self.pushButton_grabCut = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_grabCut.setGeometry(QtCore.QRect(20, 120, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_grabCut.setFont(font)
        self.pushButton_grabCut.setObjectName("pushButton_grabCut")
        self.pushButton_distance = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_distance.setGeometry(QtCore.QRect(20, 50, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_distance.setFont(font)
        self.pushButton_distance.setObjectName("pushButton_distance")
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_clear.setGeometry(QtCore.QRect(260, 120, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_4.setGeometry(QtCore.QRect(470, 340, 450, 400))
        self.scrollArea_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setWidgetResizable(False)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 4000, 4000))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.label_mid_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_mid_img.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        self.label_mid_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_mid_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_mid_img.setObjectName("label_mid_img")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(740, 100, 500, 200))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_fusion_n = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_fusion_n.setGeometry(QtCore.QRect(20, 120, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_fusion_n.setFont(font)
        self.pushButton_fusion_n.setObjectName("pushButton_fusion_n")
        self.pushButton_fusion_g = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_fusion_g.setGeometry(QtCore.QRect(260, 120, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_fusion_g.setFont(font)
        self.pushButton_fusion_g.setObjectName("pushButton_fusion_g")
        self.pushButton_choose1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_choose1.setGeometry(QtCore.QRect(20, 50, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_choose1.setFont(font)
        self.pushButton_choose1.setObjectName("pushButton_choose1")
        self.pushButton_choose2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_choose2.setGeometry(QtCore.QRect(260, 50, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_choose2.setFont(font)
        self.pushButton_choose2.setObjectName("pushButton_choose2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_save_img.setText(_translate("MainWindow", "保存图片"))
        self.label_dealt_img.setText(_translate("MainWindow", "处理后图像"))
        self.label_source_img.setText(_translate("MainWindow", "原图像1"))
        self.pushButton_choose_img.setText(_translate("MainWindow", "选择图片"))
        self.groupBox.setTitle(_translate("MainWindow", "图像分割功能"))
        self.pushButton_watershed.setText(_translate("MainWindow", "分水岭算法分割图像"))
        self.pushButton_grabCut.setText(_translate("MainWindow", "前景提取"))
        self.pushButton_distance.setText(_translate("MainWindow", "距离转换"))
        self.pushButton_clear.setText(_translate("MainWindow", "画布清空"))
        self.label_mid_img.setText(_translate("MainWindow", "原图像2"))
        self.groupBox_2.setTitle(_translate("MainWindow", "图像融合功能"))
        self.pushButton_fusion_n.setText(_translate("MainWindow", "图像普通融合"))
        self.pushButton_fusion_g.setText(_translate("MainWindow", "金字塔融合"))
        self.pushButton_choose1.setText(_translate("MainWindow", "选择图像1"))
        self.pushButton_choose2.setText(_translate("MainWindow", "选择图像2"))
