# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\ptqt\PyqtCode\excel\my_excel.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 420)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 431, 321))
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(60, 350, 351, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 451, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.actiondakai = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icon/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiondakai.setIcon(icon)
        self.actiondakai.setObjectName("actiondakai")
        self.actionguanbi = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionguanbi.setIcon(icon1)
        self.actionguanbi.setObjectName("actionguanbi")
        self.actiontuichu = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/icon/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiontuichu.setIcon(icon2)
        self.actiontuichu.setObjectName("actiontuichu")
        self.actionshiyong = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionshiyong.setIcon(icon3)
        self.actionshiyong.setObjectName("actionshiyong")
        self.actionguanyu = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/icon/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionguanyu.setIcon(icon4)
        self.actionguanyu.setObjectName("actionguanyu")
        self.menu.addAction(self.actiondakai)
        self.menu.addAction(self.actionguanbi)
        self.menu.addAction(self.actiontuichu)
        self.menu_2.addAction(self.actionshiyong)
        self.menu_2.addAction(self.actionguanyu)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "关键词："))
        self.pushButton.setText(_translate("MainWindow", "选定文件夹"))
        self.pushButton_2.setText(_translate("MainWindow", "开始搜索"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.actiondakai.setText(_translate("MainWindow", "打开"))
        self.actionguanbi.setText(_translate("MainWindow", "关闭"))
        self.actiontuichu.setText(_translate("MainWindow", "退出"))
        self.actionshiyong.setText(_translate("MainWindow", "使用说明"))
        self.actionguanyu.setText(_translate("MainWindow", "关于我们"))

import my_pic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

