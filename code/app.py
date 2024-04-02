import os
import sys
import json
import base64
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from pymem import Pymem
from pymem.process import module_from_name
from TrainerGUI.UI import UiForm
from TrainerTool.TrainerData import get_trainer_data
from TrainerTool.TrainerThread import ModifyThread

# 程式主視窗類別
class TrainerWindow(QWidget):
    # 遊戲存檔路徑
    SAVE_PATH = os.path.join(os.getenv("LOCALAPPDATA"), 'HoloCure', 'save_n.dat')

    def __init__(self):
        super().__init__()
        # 初始化使用者介面
        self.ui = UiForm()
        self.ui.setup_ui(self)
        self.message = self.ui.ui_message
        self.checkbox_groups = self.ui.checkbox_groups
        self.game_data = get_trainer_data()
        
        # 計算動態修改的索引值
        self.setup_checkbox()

        
        # 路徑與資料
        self.save_data = self.load_game_save()
        # 執行緒與遊戲資訊
        self.threads = []

        # 連接訊號
        self.ui.detect_button.clicked.connect(self.find_windows)
        
        self.windows = None
        
       
        
    # 載入遊戲存檔
    def load_game_save(self):
        try:
            with open(self.SAVE_PATH, 'rb') as f:
                decode_data = base64.b64decode(f.read())
                for checkbox in self.ui.checkbox_groups[-1]:
                    checkbox.setEnabled(True)
            return json.loads(decode_data)
        except FileNotFoundError:
            self.show_error_message(self.message['data_error'][0], self.message['data_error'][1])
        except Exception as e:
            self.show_error_message(self.message['error'][0], self.message['error'][1])
            
    
    # 尋找遊戲視窗
    def find_windows(self):
        try:
            self.windows = Pymem("HoloCure.exe")
            self.game_module = module_from_name(self.windows.process_handle, "HoloCure.exe").lpBaseOfDll
            for checkbox_group in self.ui.checkbox_groups:
                for checkbox in checkbox_group:
                    if self.ui.checkbox_groups[-1] == checkbox_group:
                         checkbox.setEnabled(False)
                    else:
                         checkbox.setEnabled(True)  
            self.show_info_message(self.message['scan'][0], self.message['scan'][1])
            
        except Exception as e:
            self.show_error_message(self.message['error'][0], self.message['error'][1])
            
   
        
            
    # 設定執行緒
    def setup_checkbox(self):
        idx = 0
       
        for checkboxes in self.checkbox_groups[:-1]:
            for checkbox in checkboxes:
                idx += 1
                try:
                    data = self.game_data[idx]
                    thread = self.create_modify_thread(checkbox, data)
                    self.threads.append(thread)
                    checkbox.clicked.connect(thread.run)
                
                except Exception as e:
                    print(e)
        
        for checkbox in self.checkbox_groups[-1]:
            data = self.game_data[idx]
            checkbox.clicked.connect(lambda state, x=(checkbox, data): self.save_editor(*x))
            idx += 1
                
               
       
    
    def save_editor(self, checkbox, data):
        if checkbox.isChecked() and self.windows == None:
            for modify_name, val in data.items():
               print(modify_name, val)
               self.save_data[modify_name] = val
        
        with open(self.SAVE_PATH, 'wb') as f:
            game_data_json = json.dumps(self.save_data).encode('UTF-8')
            encoded_data = base64.b64encode(game_data_json)
            f.write(encoded_data)
            self.show_info_message(self.message['save_editor_success'][0], self.message['save_editor_success'][1])
            return 
        self.show_error_message(self.message['save_editor_openError'][0], self.message['save_editor_openError'][1])
        
    
                
        

    # 建立修改執行緒
    def create_modify_thread(self, checkbox, data):
        return ModifyThread(checkbox=checkbox, data=data, game_module=self.game_module, windows=self.windows)

    # 顯示資訊訊息
    def show_info_message(self, title, message):
        QMessageBox.information(None, title, message)

    # 顯示錯誤訊息
    def show_error_message(self, title, message):
        QMessageBox.critical(None, title, message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    window = TrainerWindow()
    window.show()
    sys.exit(app.exec_())
