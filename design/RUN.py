import untitled
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()    #定义主窗口
    ui=untitled.Ui_MainWindow()     #生成对象
    ui.setupUi(mainWindow)   #向主窗口添加控件
    mainWindow.show()
    sys.exit(app.exec_())