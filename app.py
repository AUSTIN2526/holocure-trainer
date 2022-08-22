import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from Calculator import Ui_Form
from pymem import *
from pymem.process import *
import threading


class AppWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.page_button.clicked.connect(self.find_windows)
        
        self.ui.data[0].clicked.connect(self.threading_HP)
        self.ui.data[3].clicked.connect(self.threading_Coin)
        
           
        self.move(20, 20)
        self.show()
        
    def find_windows(self):
        try:
            self.windows = Pymem("HoloCure.exe")
            self.game_module = module_from_name(self.windows.process_handle, "Holocure.exe").lpBaseOfDll
            for i in self.ui.data:
                i.setEnabled(True)
            QMessageBox.information(None, '掃描', '已掃描到遊戲')
        except:
                 QMessageBox.critical(None, '錯誤', '請先開啟遊戲後再按偵測程式')
                 
    def threading_HP(self):
        HP_t = threading.Thread(target = self.HP)
        HP_t.start()
            
    def HP(self):
        while(1):
            if self.ui.data[0].isChecked():
                try:
                    offsets = [0x190C,0x144,0x140,0x140,0x140,0x140,0x24,0x10,0x2B8,0x4]
                    addr  = self.Hacking(self.game_module + 0x006FBD7C, offsets)
                    self.windows.write_int(addr, 1099214080)
                    
                except:
                    pass
            else:
                break
            
    def threading_Coin(self):
        conin_t = threading.Thread(target = self.Coin)
        conin_t.start()
        
    def Coin(self):
        while(1):
            if self.ui.data[3].isChecked():
                try:
                    offsets = [0x4,0x0,0x18,0xA4,0x334]
                    addr  = self.Hacking(self.game_module + 0x00705AB4, offsets)
                    self.windows.write_int(addr, 1099214080)
                    
                except:
                    pass
            else:
                break
        
        
    
        
    def Hacking(self, address, offsets):
        addr = self.windows.read_int(address)
        for offset in offsets:
            if offset != offsets[-1]:
                addr = self.windows.read_int(addr + offset)
        addr = addr + offsets[-1]
        return addr


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())