# -*- coding: utf-8 -*-

"""
实现根据关键词的查找到相应的文件目录，之后把含有关键词的文件复制到新的文件夹中。
"""

from PyQt5.QtCore import pyqtSlot
#from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_my_excel import Ui_MainWindow
from PyQt5.QtWidgets import *
from glob import glob
from os.path import join
import os
import re
from xlrd import open_workbook
import shutil
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    #把文件路径变成类的私有变量
    my_dir = ''
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_actiondakai_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("打开")
    
    @pyqtSlot()
    def on_actionguanbi_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("关闭")
    
    @pyqtSlot()
    def on_actiontuichu_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("退出")
    
    @pyqtSlot()
    def on_actionshiyong_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("使用")
    
    @pyqtSlot()
    def on_actionguanyu_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("关于")
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        选择文件夹
        """
        # TODO: not implemented yet
        #print("选定文件夹")
        #self.my_dir 的意思是，my_dir是一个全局变量，这就是用这个全局变量,因为后面也要用到这个
        self.my_dir = QFileDialog.getExistingDirectory(self,"选择文件夹","/")
        #print(self.my_dir)
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #print("开始搜索")  
        #print(self.my_dir)
        
        #1.找到相应的文件，用glob模块
        for my_file in glob(join(self.my_dir,'*.xlsx')):
            print(my_file)
        
        #2.获取用户输入的关键字
        words =self.lineEdit.text()
        
        #split翻译为分裂, split()就是将一个字符串分裂成多个字符串组成的列表。
        #split()当不带参数时以空格进行分割，当代参数时，以该参数进行分割。这里以空格分割
        words_list = re.split(' ', words) 
        #print(words_list) 
        
        num =0
        
        #读取该文件的每一个单元格里的内容
        for my_file in glob(join(self.my_dir,'*.xlsx')):
            print('a')
            print(my_file)
            
            wb = open_workbook(my_file.replace(u'/',u'\\'))
            for s in wb.sheets():
                for row in range(s.nrows):
                    for col in range(s.ncols):
                        file_contents = s.cell(row,col).value
                        if file_contents:  #如果表格不为空
                            print(file_contents)
                            for each_word in words_list:#对于输出的每个值，在表格中有时，
                                if each_word in file_contents:
                                    num = num + 1
                                    print(my_file)
                                    self.textBrowser.append(my_file)
                                    
                                    #把关键词所在的文件夹进行归类，复制到一个文件夹中
                                    
                                    #1.判断文件是否存在
                                    if not os.path.exists(self.my_dir + '\\符合条件文件'):
                                        os.mkdir(self.my_dir + '\\符合条件文件')
                                        self.textBrowser.append("创建文件夹成功：%s"%self.my_dir + '\\符合条件文件')
                                    else:
                                        self.textBrowser.append("该文件夹已存在")  
                                        
                                    self.textBrowser.append("开始复制文件。。。。。")
                                    #shutil.copy(src, dst) src指的是文件名称,dst指的是创建的文件夹路径
                                    #copy函数会把my_file文件复制到“self.my_dir + '\\符合条件文件'”这个文件目录下
                                    shutil.copy(my_file, self.my_dir + '\\符合条件文件')
                                    self.textBrowser.append("文件复制完成")
        self.textBrowser.append("一共处理了%s个文件"%str(num))                
                                    
             
            
                                   
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

