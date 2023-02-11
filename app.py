import sys
import threading
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from UI import Ui_Form
from pymem import *
from pymem.process import *
from time import sleep

class AppWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        #info language
        self.info = {'zh_TW':{'scan':['掃描', '已掃描到遊戲',],
                        'error':['錯誤', '請先開啟遊戲後再按偵測程式']},
                             
                        'en':{'scan':['Scen','Scan Success'],
                        'error':['Error','Please start the game first, then click the detection button']}
                          
        }
        
        #modeify data(format function_name:[QCheckBox object, value, base address, offsets])
        self.modify_data = {
                             #if you want to add a row modify here(format func_name_ + "num" + _ + "name")
                             'func_name_1_hP':[self.ui.func_group_1[0], 1090021872, 0x00A1EFD8,[0x70,0x18,0x170,0x98,0x48,0x10,0x1F70,0x04]],
                             'func_name_1_range':[self.ui.func_group_1[1], 1090021872, 0x00A1EFD8,[0x70,0x18,0x170,0x98,0x48,0x10,0x1670,0x04]],
                             'func_name_1_atk':[self.ui.func_group_1[2], 1090021872, 0x00A1EFD8,[0x70,0x18,0x170,0x98,0x48,0x10,0x480,0x04]],
                             'func_name_1_haste':[self.ui.func_group_1[3], 1083127808, 0x00A1EFD8,[0x70,0x18,0x170,0x98,0x48,0x10,0x1F0,0x04]],

                             'func_name_2_ex':[self.ui.func_group_2[0], 1079558144, 0x00A1EFD8,[0x70,0x18,0x170,0x98,0x48,0x10,0x1B30,0x04]],
                             'func_name_2_ex_ame':[self.ui.func_group_2[1], 1079558144, 0x00A1EFD8,[0x70,0x18,0x170,0x98,0x48,0x10,0x1B50,0x04]],
                             
                             'func_name_3_level_up':[self.ui.func_group_3[0], 1072693248, 0x00800B60, [0x48,0x10,0x1840,0x4]],
                             'func_name_3_stop_level_up':[self.ui.func_group_3[1], 1083127808, 0x00800B60, [0x48,0x10,0x1840,0x4]],
                             
                             'func_name_4_coin_1':[self.ui.func_group_4[0], 1100470147, 0x00A1EFC8, [0x1A8, 0x0, 0x0, 0x280, 0x34]],
                             
                             #this data not in QCheckBox this data will enable in modify function
                             'func_name_4_coin_2':[self.ui.func_group_4[0], 1100470147, 0x007D37E0, [0x148,0x18B4]],
                             
        }
        
        
        
        #detect button
        self.ui.page_button.clicked.connect(self.find_windows) 
        
        #connect QCheckBox object
        func_index = 0
        for group_ID in self.ui.all_group:
            for function in group_ID:
                name = list(self.modify_data.keys())[func_index]
                func_index+=1
                function.clicked.connect(lambda state, x=name: self.thread(x))

        
        self.move(40, 40)
        self.show()
        
    def find_windows(self):
        
        #get game dll
        try:
            self.windows = Pymem("HoloCure.exe")
            self.game_module = module_from_name(self.windows.process_handle, "HoloCure.exe").lpBaseOfDll
            
            #enable function
            for functions in self.ui.all_group:
                for function in functions:
                    function.setEnabled(True)
                    
            #success
            QMessageBox.information(None, self.info[self.ui.language]['scan'][0], self.info[self.ui.language]['scan'][1])
            
        except:
        
            #error
            QMessageBox.critical(None, self.info[self.ui.language]['error'][0], self.info[self.ui.language]['error'][1])
            
    def thread(self, text):
        print(text)
        t = threading.Thread(target = self.modify, args = (text,))
        t.setDaemon(True)
        t.start()
    
    def modify(self,text):
        
        #Mistake Proofing
        if text == 'func_name_2_ex':
            self.ui.func_group_2[1].setChecked(False)
        elif text =='func_name_2_ex_ame':
            self.ui.func_group_2[0].setChecked(False)
        elif text=='func_name_3_level_up':
            self.ui.func_group_3[1].setChecked(False)
        elif text=='func_name_3_stop_level_up':
             self.ui.func_group_3[0].setChecked(False)
            
        #get modeify data
        function, value, address, offsets = self.modify_data[text]
        
        #modeify
        while(1):
            if function.isChecked():
                try:
                    addr  = self.calculate_address(self.game_module + address, offsets)
                    
                    #coin have 2 address
                    if text == 'func_name_4_coin_1' and self.windows.read_int(addr) == 0:
                        function, value, address, offsets = self.modify_data['func_name_4_coin_2']
                        addr  = self.calculate_address(self.game_module + address, offsets)
                    
                    #write data
                    if self.windows.read_int(addr) != value:
                        self.windows.write_int(addr, value)
                        
                except:
                    pass
            else:
                break
    
   
     
    
    
    def calculate_address(self, address, offsets):
        addr = self.windows.read_int(address)
        for cnt,offset in enumerate(offsets):
            if cnt+1 != len(offsets):
                addr = self.windows.read_int(addr + offset)           
        return addr + offsets[-1]
        



app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
