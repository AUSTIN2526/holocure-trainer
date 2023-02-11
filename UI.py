from PyQt5 import QtCore, QtWidgets
import locale


class Ui_Form(object):
    def setupUi(self, page):   
        
        #get language
        self.language = locale.getdefaultlocale()[0]
        #setting different language parameters 
        if self.language =='zh_TW' or self.language =='zh':
            self.language = 'zh_TW'
            self.w, self.h, self.space = 410, 300, 90
        else:
            self.language = 'en'
            self.w, self.h, self.space = 450, 300, 110
            

        #different language text
        self.UI_text = {'zh_TW':{'ui_name':'HoloCure修改器 by AUSTIN2526',
                                 'info':'【啟動遊戲後按偵測按鈕遊戲即可啟用功能】',
                                 'detect_button':'偵測遊戲',
                                 
                                 #if you want to add a row modify here(format func_name_ + "num")
                                 'func_name_1':['鎖血無敵', '全圖撿物', '秒殺怪物', '999 攻速'],
                                 'func_name_2':['無限技能','無限技能(Ame)'],
                                 'func_name_3':['無限升級', '停止升級'],
                                 'func_name_4':['無限金幣'],
                                 
                                 #if you want to add a row modify here(format func_title_ + "num")
                                 'func_title_1':'主要功能',
                                 'func_title_2':'特殊技能',
                                 'func_title_3':'升級',
                                 'func_title_4':'其他'},
                          
                        'en':{'ui_name':'HoloCure Trainer  by AUSTIN2526',
                              'info':'【Pleas click the detection button to enable function】',
                              'detect_button':'Detect',
                              
                              #if you want to add a row modify here(format func_name_ + "num")
                              'func_name_1':['Unlimited HP', 'EX Pick Range', 'Spike Monster', '999 Haste'],
                              'func_name_2':['Unlimited SP','Unlimited SP(Ame)'],
                              'func_name_3':['Unlimited EXP', 'Stop Level Up'],
                              'func_name_4':['Unlimited Coin'],
                                 
                               #if you want to add a row modify here(format func_title_ + "num")
                              'func_title_1':'Main Function',
                              'func_title_2':'Special Skill',
                              'func_title_3':'Level Up',
                              'func_title_4':'Other'},
        
                          
        }
        
        #QCheckBox group
        self.func_group_1, self.func_group_2, self.func_group_3, self.func_group_4 = [], [], [], []
        self.all_group = [self.func_group_1, self.func_group_2, self.func_group_3, self.func_group_4]
        
        #setting window
        page.resize(self.w, self.h)
        page.setWindowTitle(self.UI_text[self.language]['ui_name'])
        
        
        #detect button
        self.makelabel(page, 110, 10, 2000, 30, self.UI_text[self.language]['info'])
        self.page_button = QtWidgets.QPushButton(page)
        self.page_button.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.page_button.setText(self.UI_text[self.language]['detect_button'])
        
        #creat QCheckBox
        for cnt, group_ID in enumerate(self.all_group,1):
            for _ in self.UI_text[self.language][f'func_name_{cnt}']:
                group_ID.append(QtWidgets.QCheckBox(page))
        
        
        
        #set QCheckBox
        for cnt, group_ID in enumerate(self.all_group, 1):
            #stage 1~3
            self.makelabel(page, 10, 50+(cnt-1)*60, 2000, 30, self.UI_text[self.language][f'func_title_{cnt}'])
            for index in range(len(self.UI_text[self.language][f'func_name_{cnt}'])):
                group_ID[index].setGeometry(QtCore.QRect(10 + self.space*index, 80+(cnt-1)*60, 2000, 30))
                group_ID[index].setText(self.UI_text[self.language][f'func_name_{cnt}'][index])
                group_ID[index].setEnabled(False)
                
    

                  
       
    def makelabel(self, page, x=10, y=10, w=10, h=20, text='', s=True):
        self.label = QtWidgets.QLabel(page)
        self.label.setGeometry(QtCore.QRect(x, y, w, h))
        self.label.setObjectName('label')
        self.label.setText(text)
        self.label.setEnabled(s)

