from PyQt5 import QtCore, QtWidgets, QtGui
import locale


class Ui_Form:
    def __init__(self):
    
        #get language
        self.language = locale.getdefaultlocale()[0]
        
        #set system language
        if self.language =='zh_TW' or self.language =='zh':
            self.language = 'zh_TW'
            self.w, self.h, self.space, self.row_space = 450, 270, 90, 30
            
        else:
            self.language = 'en'
            self.w, self.h, self.space, self.row_space = 620, 270, 140, 30
            

        #UI language (if you want add new function modify here【format func_name_ + "num"】)
        self.UI_text = {'zh_TW':{'ui_name':'HoloCure修改器 by AUSTIN2526',
                                 'info':'【啟動遊戲後按偵測按鈕遊戲即可啟用功能】',
                                 'detect_button':'偵測遊戲',
                                 
                                 #modify here
                                 'func_name_1':['鎖血無敵', '全圖撿物', '秒殺怪物', '999 攻速','無限技能'],
                                 'func_name_2':['無限升級','停止升級'],
                                 'func_name_3':['無限金幣', '解鎖裝備', '解鎖成就', '全角色與服裝', '解鎖關卡', '解鎖被動'],
                                 
                                 #modify here
                                 'func_title_1':'♠ 主要功能 ♠',
                                 'func_title_2':'♥ 升級 ♥',
                                 'func_title_3':'♣ 修改存檔 ♣'},
                          
                        'en':{'ui_name':'HoloCure Trainer  by AUSTIN2526',
                              'info':'【Pleas click the detection button to enable function】',
                              'detect_button':'Detect',
                              
                              #modify here
                              'func_name_1':['Unlimited HP', 'EX Pick Range', 'Spike Monster', '999 Haste', 'Unlimited SP'],
                              'func_name_2':['Unlimited EXP', 'Stop Level Up'],
                              'func_name_3':['Unlimited Coin', 'All Armorys', 'All Achievements', 'ALL Outfits and Characters', 'All Stages', 'Max Upgrades'],
                                 
                               #modify here
                              'func_title_1':'♠ Main Function ♠',
                              'func_title_2':'♦ Level Up ♦',
                              'func_title_3':'♣ Save Editor ♣'},          
        }
        
        #QCheckBox group(save_editor_func_1 need to be in the last)
        self.func_group_1, self.func_group_2, self.save_editor_func_1 = [], [], []
        self.all_group = [self.func_group_1, self.func_group_2, self.save_editor_func_1]
        
    def setupUi(self, page):   

        
        
        #set window
        page.resize(self.w, self.h)
        page.setWindowTitle(self.UI_text[self.language]['ui_name'])

        #set detect button
        self.makelabel(page, 110, 10, 2000, 30, self.UI_text[self.language]['info'])
        self.page_button = QtWidgets.QPushButton(page)
        self.page_button.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.page_button.setText(self.UI_text[self.language]['detect_button'])
        
        #creat QCheckBox
        for cnt, group_ID in enumerate(self.all_group,1):
            for _ in self.UI_text[self.language][f'func_name_{cnt}']:
                group_ID.append(QtWidgets.QCheckBox(page))
        
        #UI init position
        x, y =10, 50
        for cnt, group_ID in enumerate(self.all_group, 1):
            #title x position always 10
            self.makelabel(page, 10, y, 2000, 30, self.UI_text[self.language][f'func_title_{cnt}'])
            
            #calc length
            func_num = len(self.UI_text[self.language][f'func_name_{cnt}'])
            row_cnt = func_num//5
            col_cnt = func_num if func_num < 4 else 4
            
      
            for row in range(row_cnt+1):
                for col in range(col_cnt):
                    index = row * 4  + col
                    
                    #updat x and y position
                    x = 10 + self.space * index if index < 4 else 10 + self.space * (index-row_cnt*4)
                    y = y if index % 4 != 0 else y +25
                    
                    group_ID[index].setGeometry(QtCore.QRect(x, y, 2000, 30))
                    group_ID[index].setText(self.UI_text[self.language][f'func_name_{cnt}'][index])
                    group_ID[index].setEnabled(False)
                
                col_cnt = func_num if func_num <= 4 else func_num-row_cnt*4 
                
            #title space 
            y+=self.row_space
            
                
            
            
                
    def makelabel(self, page, x=10, y=10, w=10, h=20, text='', s=True):
        font = QtGui.QFont()                       
        font.setPointSize(10) 
        self.label = QtWidgets.QLabel(page)
        self.label.setGeometry(QtCore.QRect(x, y, w, h))
        self.label.setText(text)
        self.label.setEnabled(s)
        self.label.setFont(font)
