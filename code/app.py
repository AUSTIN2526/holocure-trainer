import os
import sys
import json
import base64
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtCore import QTimer
from pymem import Pymem
from pymem.process import module_from_name
from TrainerGUI.UI import HoloCureTrainerUI


class TrainerWindow(QWidget):
    SAVE_PATH = os.path.join(os.getenv("LOCALAPPDATA"), 'HoloCure', 'save_n.dat')

    def __init__(self):
        super().__init__()
        self.ui = HoloCureTrainerUI()
        self.ui.setup_ui(self)

        self.dynamic_checkboxes = self.ui.checkbox_groups[0]
        self.static_checkboxes = self.ui.checkbox_groups[1]
        self.dynamic_data = self.ui.data[0]
        self.static_data = self.ui.data[1]
        self.save_data = self.load_game_save()

        try:
            self.windows = Pymem("HoloCure.exe")
            self.game_module = module_from_name(self.windows.process_handle, "HoloCure.exe").lpBaseOfDll
            for i in self.dynamic_checkboxes:
                i.setEnabled(True)
        except Exception:
            self.windows = None
            self.game_module = None
            for i in self.static_checkboxes:
                i.setEnabled(True)
            
            

        for checkbox in self.dynamic_checkboxes:
            checkbox.clicked.connect(self.on_dynamic_checkbox_clicked)

        for checkbox in self.static_checkboxes:
            checkbox.clicked.connect(self.on_static_checkbox_clicked)

        self.ui.detect_button.clicked.connect(self.find_windows)

    def on_dynamic_checkbox_clicked(self):
        sender = self.sender()
        checkbox_name = sender.text()
        data = self.dynamic_data.get(checkbox_name, {})

        if sender.isChecked() and self.windows:
            timer = QTimer(self)
            timer.setInterval(10)  # 設置較長的間隔以降低 CPU 負擔
            timer.timeout.connect(lambda: self.modify_dynamic_data(sender, data))
            timer.start()

            sender.timer = timer  # 將計時器與 checkbox 綁定，方便後續管理
        elif hasattr(sender, 'timer'):
            sender.timer.stop()
            sender.timer.deleteLater()
            del sender.timer

    def modify_dynamic_data(self, checkbox, data):
        if not checkbox.isChecked():
            if hasattr(checkbox, 'timer'):
                checkbox.timer.stop()
                checkbox.timer.deleteLater()
                del checkbox.timer
            return

        value, address, offsets = data.values()
        try:
            addr = self.calculate_address(self.game_module + address, offsets)
            if self.windows.read_double(addr) != value:
                self.windows.write_double(addr, value)
        except Exception:
            pass

    def on_static_checkbox_clicked(self):
        sender = self.sender()
        checkbox_name = sender.text()
        new_value = self.static_data.get(checkbox_name, {})

        if self.windows is None and sender.isChecked():
            try:
                for name, val in new_value.items():
                    self.save_data[name] = val

                with open(self.SAVE_PATH, 'wb') as f:
                    game_data_json = json.dumps(self.save_data).encode('UTF-8')
                    encoded_data = base64.b64encode(game_data_json)
                    f.write(encoded_data)

                self.show_message_box("成功", "存檔已成功更新")
            except Exception as e:
                self.show_error_message("存檔錯誤", str(e))
        else:
            self.show_error_message("存檔修改錯誤", '請先關閉遊戲在進行存檔修改')

    def load_game_save(self):
        try:
            with open(self.SAVE_PATH, 'rb') as f:
                decode_data = base64.b64decode(f.read())
                return json.loads(decode_data)
        except FileNotFoundError:
            self.show_error_message("存檔錯誤", "找不到存檔文件")
        except Exception as e:
            self.show_error_message("載入錯誤", str(e))
            return {}

    def find_windows(self):
        try:
            self.windows = Pymem("HoloCure.exe")
            self.game_module = module_from_name(self.windows.process_handle, "HoloCure.exe").lpBaseOfDll
            for i in self.dynamic_checkboxes:
                i.setEnabled(True)
            for i in self.static_checkboxes:
                i.setEnabled(False)
            

            self.show_message_box(**self.ui.alert['scan'])
        except Exception as e:
            self.show_error_message(**self.ui.alert['error'])

    def calculate_address(self, address, offsets):
        addr = self.windows.read_longlong(address)
        for index, offset in enumerate(offsets):
            if index + 1 != len(offsets):
                addr = self.windows.read_longlong(addr + offset)
        return addr + offsets[-1]

    def show_message_box(self, title, text):
        QMessageBox.information(self, title, text, QMessageBox.Ok)

    def show_error_message(self, title, text):
        QMessageBox.critical(self, title, text, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    window = TrainerWindow()
    window.show()
    sys.exit(app.exec_())
