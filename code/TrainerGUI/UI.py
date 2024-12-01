from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox
from PyQt5 import QtCore, QtGui
from typing import List
import sys
import locale
from .utils import get_trainer_data


class HoloCureTrainerUI:
    DEFAULT_LANGUAGE = 'zh_TW'

    # UI 文本與設定資料
    TEXTS = {
        'zh_TW': {
            'window_title': 'HoloCure Trainer by AUSTIN2526',
            'info_text': '【啟動遊戲後按偵測按鈕遊戲即可啟用功能】',
            'detect_button_text': '偵測遊戲',
            'group_titles': ['♠ 動態修改區 ♠', '♣ 修改存檔區 ♣'],
        }
    }

    SETTINGS = {
        'zh_TW': {
            'window_size': (700, 300),
            'checkbox_spacing': 140,
            'row_spacing': 30,
            'label_font_size': 10,
            'max_columns': 5
        }
    }

    ALERT_MESSAGES = {
        'zh_TW': {
            'scan': {'title': '掃描', 'text': '已掃描到遊戲'},
            'error': {'title': '錯誤', 'text': '請先開啟遊戲後再按偵測程式'},
            'data_error': {'title': '存檔讀取失敗', 'text': '初次修改請先開啟HoloCure建立存檔後，才能開始修改'},
            'save_editor_success': {'title': '修改成功', 'text': '存檔修改完畢'},
            'save_editor_openError': {'title': '修改失敗', 'text': '請關閉遊戲後再進行修改'},
            'save_editor_error': {'title': '修改失敗', 'text': '發生不明錯誤，請回報開發者來解決此問題'}
        }
    }


    def __init__(self):
        # 獲取系統語言並選擇相應的文本和設定
        language = locale.getdefaultlocale()[0]
        self.texts = self.TEXTS.get(language, self.TEXTS[self.DEFAULT_LANGUAGE])
        self.settings = self.SETTINGS.get(language, self.SETTINGS[self.DEFAULT_LANGUAGE])
        self.checkbox_groups: List[List[QCheckBox]] = []
        self.alert = self.ALERT_MESSAGES.get(language, self.SETTINGS[self.DEFAULT_LANGUAGE])
        self.data = get_trainer_data(self.texts)
    def setup_ui(self, window: QMainWindow):
        """
        設定主視窗的 UI。
        """
        # 設定視窗標題與大小
        window.resize(*self.settings['window_size'])
        window.setWindowTitle(self.texts['window_title'])

        # 加入提示標籤
        self._create_label(
            parent=window,
            x=110, y=10, width=2000, height=30,
            text=self.texts['info_text']
        )

        # 加入偵測遊戲按鈕
        self.detect_button = QPushButton(window)
        self.detect_button.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.detect_button.setText(self.texts['detect_button_text'])

        # 建立核取方塊群組
        for group_names in self.texts['group_names']:
            self.checkbox_groups.append([QCheckBox(window) for _ in group_names])

        # 動態生成核取方塊
        self._create_dynamic_checkboxes(window)

    def _create_label(self, parent, x: int, y: int, width: int, height: int, text: str, enabled: bool = True):
        """
        建立標籤元件。
        """
        font = QtGui.QFont()
        font.setPointSize(self.settings['label_font_size'])

        label = QLabel(parent)
        label.setGeometry(QtCore.QRect(x, y, width, height))
        label.setText(text)
        label.setEnabled(enabled)
        label.setFont(font)

    def _create_dynamic_checkboxes(self, parent):
        """
        動態建立核取方塊與群組標籤。
        """
        x_start, y_start = 10, 50
        y_offset = y_start

        for group_title, checkboxes, group_names in zip(self.texts['group_titles'], self.checkbox_groups, self.texts['group_names']):
            # 加入群組標題
            self._create_label(parent, x_start, y_offset, 2000, 30, group_title)
            y_offset += self.settings['row_spacing']

            # 排列核取方塊
            for index, (checkbox, name) in enumerate(zip(checkboxes, group_names)):
                column = index % self.settings['max_columns']
                row = index // self.settings['max_columns']

                checkbox_x = x_start + column * self.settings['checkbox_spacing']
                checkbox_y = y_offset + row * self.settings['row_spacing']

                checkbox.setGeometry(QtCore.QRect(checkbox_x, checkbox_y, 800, 30))
                checkbox.setText(str(name))
                checkbox.setEnabled(False)

            # 更新 Y 偏移量
            y_offset += (len(checkboxes) // self.settings['max_columns'] + 1) * self.settings['row_spacing']


def main():
    """
    主執行函式，啟動應用程式。
    """
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    ui = HoloCureTrainerUI()
    ui.setup_ui(main_window)

    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
