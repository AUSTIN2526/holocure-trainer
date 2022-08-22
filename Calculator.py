from PyQt5 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, page):
        form_w = 440
        form_h = 180
        page.resize(form_w, form_h)
        page.setWindowTitle('HoloCure修改器 by austin70915')
        
        self.makelabel(page, 10, 10, 2000, 30,'啟動遊戲後按偵測按鈕遊戲即可啟用功能')
        #偵測遊戲
        self.page_button = QtWidgets.QPushButton(page)
        self.page_button.setGeometry(QtCore.QRect(290,10,100,30))
        self.page_button.setText('偵測遊戲')
        
        #功能區
        func_name = ['鎖血無敵','無限特殊技能(我還沒寫好)','全圖撿物(我還沒寫好)','無限HoloCoin']
        self.data = []
        self.makelabel(page, 10, 50, 2000, 30,'功能選擇區:')
        for i in range(len(func_name)):
            self.data.append(QtWidgets.QCheckBox(page))
            self.data[i].setGeometry(QtCore.QRect(10, 70+i*20, 2000, 30))
            self.data[i].setText(func_name[i])
            self.data[i].setEnabled(False)
            
        
            
        

    def makelabel(self, page, x=10, y=10, w=10, h=20, text='', s=True):
        self.label = QtWidgets.QLabel(page)
        self.label.setGeometry(QtCore.QRect(x, y, w, h))
        self.label.setObjectName('label')
        self.label.setText(text)
        self.label.setEnabled(s)

