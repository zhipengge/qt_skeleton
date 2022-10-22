# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_tool.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setObjectName("label_image")
        self.horizontalLayout.addWidget(self.label_image)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile_F = QtWidgets.QMenu(self.menubar)
        self.menuFile_F.setObjectName("menuFile_F")
        self.menuTool_T = QtWidgets.QMenu(self.menubar)
        self.menuTool_T.setObjectName("menuTool_T")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_file_new = QtWidgets.QAction(MainWindow)
        self.action_file_new.setObjectName("action_file_new")
        self.action_file_open = QtWidgets.QAction(MainWindow)
        self.action_file_open.setObjectName("action_file_open")
        self.action_file_save = QtWidgets.QAction(MainWindow)
        self.action_file_save.setObjectName("action_file_save")
        self.action_file_save_as = QtWidgets.QAction(MainWindow)
        self.action_file_save_as.setObjectName("action_file_save_as")
        self.action_tool_resize = QtWidgets.QAction(MainWindow)
        self.action_tool_resize.setObjectName("action_tool_resize")
        self.menuFile_F.addAction(self.action_file_new)
        self.menuFile_F.addAction(self.action_file_open)
        self.menuFile_F.addAction(self.action_file_save)
        self.menuFile_F.addAction(self.action_file_save_as)
        self.menuTool_T.addAction(self.action_tool_resize)
        self.menubar.addAction(self.menuFile_F.menuAction())
        self.menubar.addAction(self.menuTool_T.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ImageTool"))
        self.label_image.setText(_translate("MainWindow", "image_label"))
        self.menuFile_F.setTitle(_translate("MainWindow", "File(&F)"))
        self.menuTool_T.setTitle(_translate("MainWindow", "Tool(&T)"))
        self.action_file_new.setText(_translate("MainWindow", "New(N)"))
        self.action_file_open.setText(_translate("MainWindow", "Open(&O)"))
        self.action_file_save.setText(_translate("MainWindow", "Save(&S)"))
        self.action_file_save_as.setText(_translate("MainWindow", "Save As(&A)"))
        self.action_tool_resize.setText(_translate("MainWindow", "Resize(&R)"))

