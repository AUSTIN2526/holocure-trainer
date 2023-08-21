import sys
import threading
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from UI import Ui_Form
from pymem import Pymem
from pymem.process import module_from_name
import base64
import os
import json
from config import load_data

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        
        func_name = self.ui.ui_text['group_names']
        title_name = self.ui.ui_text['group_titles']
        self.groups = self.ui.groups
        
        # Load modify data
        modify_data = load_data()
        self.modify_data = {
            title_name[i]: {
                func_name[i][j]: [self.groups[i][j]] + [modify_data[i][j]]
                for j in range(len(func_name[i]))
            }
            for i in range(len(func_name))
        }

        # System language
        info = {
            'zh_TW': {
                'scan': ['掃描', '已掃描到遊戲'],
                'error': ['錯誤', '請先開啟遊戲後再按偵測程式'],
                'data_error': ['存檔讀取失敗', '初次修改請先開啟HoloCure建立存檔後，才能開始修改'],
                'save_editor_success': ['修改成功', '存檔修改完畢'],
                'save_editor_openError': ['修改失敗', '請關閉遊戲後再進行修改'],
                'save_editor_error': ['修改失敗', '發生不明錯誤，請回報開發者來解決此問題']
            },
            'en': {
                'scan': ['Scan', 'Game scanned'],
                'error': ['Error', 'Please open the game before pressing the detect button'],
                'data_error': ['Save File Load Failed', 'For the first modification, please open HoloCure to create a save file before starting the modification'],
                'save_editor_success': ['Successful', 'Save file modification completed'],
                'save_editor_openError': ['Failed', 'Please make the save editor after closing the game.'],
                'save_editor_error': ['Failed', 'An unknown error occurred, please report to the developer to resolve this issue']
            },
        }
        self.info = info[self.ui.language]
        
        
        # Load game save
        self.game_data_path = f'{os.getenv("LOCALAPPDATA")}\HoloCure\save_n.dat'
        self.game_data = self.load_game_data(self.ui.groups[-1])

        # Find HoloCure windows
        self.ui.page_button.clicked.connect(self.find_windows) 

        # Connect QCheckBox with modify function
        for idx in range(len(self.ui.groups)):        
            for fucn_ID in range(len(self.ui.groups[idx])):
                title = title_name[idx]
                name = func_name[idx][fucn_ID]
                checkbox = self.ui.groups[idx][fucn_ID]
                if len(self.ui.groups) != idx+1:
                    checkbox.clicked.connect(lambda state, x=(title, name): self.modify_thread(x))
                else:
                    checkbox.clicked.connect(lambda state, x=(title, name): self.save_editor(x))

        
        self.move(40, 40)
        self.show()
        
    
    def load_game_data(self, save_editor):
        try:
            with open(self.game_data_path, 'rb') as f:
                decode_data = base64.b64decode(f.read())

            for function in save_editor:
                function.setEnabled(True)

            return json.loads(decode_data)
            
        except:
            QMessageBox.critical(None, self.info['data_error'][0], self.info['data_error'][1])

    def find_windows(self):
        try:
            self.windows = Pymem("HoloCure.exe")
            self.game_module = module_from_name(self.windows.process_handle, "HoloCure.exe").lpBaseOfDll
            for functions in self.ui.groups[:-1]:
                for function in functions:
                    function.setEnabled(True)
            
            QMessageBox.information(None, self.info['scan'][0], self.info['scan'][1])
            
        except:
            QMessageBox.critical(None, self.info['error'][0], self.info['error'][1])
            
        

    def modify_thread(self, parameter):
        t = threading.Thread(target=self.dynamic_modify, args=(parameter,))
        t.setDaemon(True)
        t.start()

    def dynamic_modify(self, parameter):
        title, name = parameter
        checkbox, modify_data = self.modify_data[title][name]
        value, address, offsets, interlock = modify_data.values()

        # Interlock function
        if interlock:
            lock = [item for item in self.groups[1] if item is not checkbox][0]
            lock.setChecked(False)

        # Modify memory
        while checkbox.isChecked():
            try:
                addr = self.calculate_address(self.game_module + address, offsets)
                if self.windows.read_longlong(addr) != value:
                    self.windows.write_longlong(addr, value)
            except:
                pass
           
    
    def save_editor(self, parameter):
        title, name = parameter
        checkbox, data = self.modify_data[title][name]
        
        # Save editor need to close the game
        try:
            is_game_open = Pymem("HoloCure.exe")
        except:
            is_game_open = None
        
        try:
            if checkbox.isChecked():
                # Replace game save
                for modify_name, val in data.items():
                    self.game_data[modify_name] = val

                # Save editor result
                with open(self.game_data_path, 'wb') as f:
                    game_data_json = json.dumps(self.game_data).encode('UTF-8')
                    encoded_data = base64.b64encode(game_data_json)
                    f.write(encoded_data)
                  
                if  is_game_open != None:
                    QMessageBox.critical(None, self.info['save_editor_openError'][0], self.info['save_editor_openError'][1])
                else:
                    QMessageBox.information(None, self.info['save_editor_success'][0], self.info['save_editor_success'][1])

        except:
            QMessageBox.critical(None, self.info[self.ui.language][0], self.info['save_editor_error'][1])

            

            
    def calculate_address(self, address, offsets):
        addr = self.windows.read_longlong(address)
        for cnt,offset in enumerate(offsets):
            if cnt+1 != len(offsets):
                addr = self.windows.read_longlong(addr + offset)           
        return addr + offsets[-1]
        
   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
