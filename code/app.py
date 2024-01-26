import os
import json
import base64
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QThread, QTimer, pyqtSignal
from pymem import Pymem
from pymem.process import module_from_name
from config import load_data
from UI import UiForm

# System lanagage
INFO_MESSAGES = {
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

class ModifyThread(QThread):
    modification_signal = pyqtSignal()

    def __init__(self, checkbox=None, data=None, game_module=None, windows=None):
        super(ModifyThread, self).__init__()
        self.checkbox = checkbox
        self.data = data
        self.game_module = game_module
        self.windows = windows
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.modify_data)

    def run(self):
        self.timer.start(1)  # Give a delay; too low a value may cause modification function to fail

    def modify_data(self):
        if not self.checkbox.isChecked():
            self.timer.stop()
            return

        value, address, offsets, interlock = self.data.values()
        
        try:
            addr = self.calculate_address(self.game_module + address, offsets)
            if self.windows.read_double(addr) != value:
                self.windows.write_double(addr, value)
                self.modification_signal.emit()
        except:
            pass

    def calculate_address(self, address, offsets):
        addr = self.windows.read_longlong(address)
        for index, offset in enumerate(offsets):
            if index + 1 != len(offsets):
                addr = self.windows.read_longlong(addr + offset)
        return addr + offsets[-1]

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_form = UiForm()
        self.ui_form.setup_ui(self)
        self.info = INFO_MESSAGES[self.ui_form.current_language]

        # Paths and data
        self.game_data_path = os.path.join(os.getenv("LOCALAPPDATA"), 'HoloCure', 'save_n.dat')
        self.game_data = self.load_game_data()

        # Threads and game info
        self.threads = []
        self.windows = None
        self.game_module = None
        self.setup_threads()

        self.enable_checkbox_groups()

        # Connect signals
        self.ui_form.page_button.clicked.connect(self.find_windows)
        
    def get_info(self):
        return INFO_MESSAGES[self.ui_form.current_language]

    def setup_threads(self):
        group_names = self.ui_form.ui_texts['group_names']
        checkbox_groups = self.ui_form.checkbox_groups
        all_data = load_data()

        for i, group in enumerate(checkbox_groups):
            for j, checkbox in enumerate(group):
                name = group_names[i][j]
                data = all_data[i][j]

                if i != len(checkbox_groups) - 1:
                    thread = ModifyThread(checkbox=checkbox, data=data, game_module=self.game_module, windows=self.windows)
                    self.threads.append(thread)
                    checkbox.clicked.connect(thread.run)
                else:
                    checkbox.clicked.connect(lambda state, x=(checkbox, data): self.save_editor(*x))

    def save_editor(self, checkbox, data):
        try:
            is_game_open = Pymem("HoloCure.exe")
        except:
            is_game_open = None

        if checkbox.isChecked():
            if is_game_open is None:
                for modify_name, val in data.items():
                    self.game_data[modify_name] = val

                with open(self.game_data_path, 'wb') as f:
                    game_data_json = json.dumps(self.game_data).encode('UTF-8')
                    encoded_data = base64.b64encode(game_data_json)
                    f.write(encoded_data)
                    self.show_info_message(self.info['save_editor_success'][0], self.info['save_editor_success'][1])
            else:
                self.show_error_message(self.info['save_editor_openError'][0], self.info['save_editor_openError'][1])

    def find_windows(self):
        try:
            self.windows = Pymem("HoloCure.exe")
            self.game_module = module_from_name(self.windows.process_handle, "HoloCure.exe").lpBaseOfDll
            self.enable_checkbox_groups()
            self.setup_threads()
            self.show_info_message(self.info['scan'][0], self.info['scan'][1])
        except Exception as e:
            self.show_error_message(self.info['error'][0], self.info['error'][1])

    def enable_checkbox_groups(self):
        if self.windows is None:
            for function in self.ui_form.checkbox_groups[-1]:
                function.setEnabled(True)
        else:
            for functions in self.ui_form.checkbox_groups[:-1]:
                for function in functions:
                    function.setEnabled(True)
            for function in self.ui_form.checkbox_groups[-1]:
                function.setEnabled(False)
            
    def load_game_data(self):
        if not hasattr(self, 'cached_game_data'):
            try:
                with open(self.game_data_path, 'rb') as f:
                    decode_data = base64.b64decode(f.read())
                self.cached_game_data = json.loads(decode_data)
                return self.cached_game_data
                
            except Exception as e:
                self.show_error_message(self.info['data_error'][0], self.info['data_error'][1])

        
    def show_info_message(self, title, message):
        QMessageBox.information(None, title, message)

    def show_error_message(self, title, message):
        QMessageBox.critical(None, title, message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
