# -*- coding: utf-8 -*- 
"""
Project: qt_skeleton
Creator: gezhipeng
Create time: 2022-10-22 08:37
IDE: PyCharm
Introduction:
"""
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from image_tool import Ui_MainWindow
from PyQt5.QtCore import Qt
import cv2
import sys
import os


class MainUi(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(MainUi, self).setupUi(MainWindow)
        self.action_file_open.triggered.connect(self.open_image)
        self.label_image.setScaledContents(True)
        self.max_width = 1200
        self.max_height = 900


    def open_image(self):
        image_path, _ = QFileDialog.getOpenFileName(
            None,
            "选择图片",
            os.path.expanduser("~"),
            "JPEG Files(*.jpg);;PNG Files(*.png)")
        self.label_image.setText(image_path)
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            w0, h0 = pixmap.width(), pixmap.height()
            if w0 > 10 and h0 > 10:
                w, h = w0, h0
                if w > self.max_width:
                    w, h = self.max_width, self.max_width * h // w
                if h > self.max_height:
                    w, h = self.max_height * w // h, self.max_height
                pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.label_image.setPixmap(pixmap)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())