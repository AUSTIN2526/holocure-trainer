from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox
from PyQt5 import QtCore, QtWidgets, QtGui
from .utils import get_ui_data
import sys
class UiForm:
    def __init__(self):
        self.ui_texts, self.ui_settings, self.ui_message = get_ui_data()
        self.checkbox_groups = []

    def setup_ui(self, page):
        # 設定視窗
        page.resize(*self.ui_settings['window_size'])
        page.setWindowTitle(self.ui_texts['window_title'])

        # 設定偵測按鈕
        self.create_label(page, 110, 10, 2000, 30, self.ui_texts['info_text'])
        self.detect_button = QPushButton(page)
        self.detect_button.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.detect_button.setText(self.ui_texts['detect_button_text'])

        for idx, group_name in enumerate(self.ui_texts['group_names']):
            checkboxes = [QCheckBox(page) for _ in self.ui_texts['group_names'][idx]]
            self.checkbox_groups.append(checkboxes)

        x, y = 10, 50
        for idx, (group_title, checkboxes) in enumerate(zip(self.ui_texts['group_titles'], self.checkbox_groups)):
            self.create_label(page, 10, y, 2000, 30, group_title)
            y += self.ui_settings['row_spacing']

            for position, checkbox in enumerate(checkboxes):
                col_count = position % self.ui_settings['max_columns']
                row_count = position // self.ui_settings['max_columns']

                checkbox_x = x + col_count * self.ui_settings['checkbox_spacing']
                checkbox_y = y + row_count * self.ui_settings['row_spacing']
                print(checkbox)
                checkbox.setGeometry(QtCore.QRect(checkbox_x, checkbox_y, 2000, 30))
                checkbox.setText(self.ui_texts['group_names'][idx][position])
                checkbox.setEnabled(False)

            # 計算下一組位置
            y += (row_count + 1) * self.ui_settings['row_spacing']
            
            
    

    def create_label(self, parent, x=10, y=10, width=10, height=20, text='', enabled=True):
        font = QtGui.QFont()
        font.setPointSize(self.ui_settings['label_font_size'])
        label = QLabel(parent)
        label.setGeometry(QtCore.QRect(x, y, width, height))
        label.setText(text)
        label.setEnabled(enabled)
        label.setFont(font)

def main():
    app = QApplication(sys.argv)
    page = QMainWindow()

    # 實例化 UiForm 並呼叫 setup_ui
    ui_form = UiForm()
    ui_form.setup_ui(page)

    page.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
