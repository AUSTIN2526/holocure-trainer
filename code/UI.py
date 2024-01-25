from PyQt5 import QtCore, QtWidgets, QtGui
import locale

class UiForm:
    # Language mapping dictionary as a class attribute
    LANGUAGE_MAPPING = {
        'zh_TW': 'zh_TW',
        'zh': 'zh_TW',
        'en': 'en'
    }

    # UI text and object size dictionaries
    UI_DATA = {
        'zh_TW': {
            'window_name': 'HoloCure Trainer by AUSTIN2526',
            'info_text': '【啟動遊戲後按偵測按鈕遊戲即可啟用功能】',
            'detect_button_text': '偵測遊戲',
            'group_titles': ['♠ 動態修改區 ♠', '♥ 升級效果區 ♥', '♣ 修改存檔區 ♣'],
            'group_names': [
                ['鎖血無敵', '全圖吸物', '秒殺怪物', '超高攻速', '無限技能'],
                ['無限升級', '停止升級'],
                ['無限貨幣', '全武器庫解鎖', '全成就解鎖', '全角色與服裝', '全關卡解鎖', '被動技能全滿', '全小屋家具', '無限小屋道具']
            ]
        },
        'en': {
            'window_name': 'HoloCure Trainer by AUSTIN2526',
            'info_text': '【Activate features by pressing the detection button after starting the game】',
            'detect_button_text': 'Detect Game',
            'group_titles': ['♠ Dynamic Function ♠', '♥ Upgrade Effects ♠', '♣ Save Editor ♣'],
            'group_names': [
                ['God Mode', 'Full Map Magnet', 'One-Hit Kills', 'Super High Attack Speed', 'Unlimited Skills'],
                ['Unlimited Level Up', 'Stop Level Up'],
                ['Unlimited Currency', 'Unlock All Weapons', 'Unlock All Achievements', 'Unlock All Characters and Outfits', 'Unlock All Stages', 'Max Upgrades', 'Unlock All Furniture', 'Unlimited Inventory']
            ]
        }
    }

    OBJECT_SIZE = {
        'zh_TW': (500, 300, 120),
        'en': (780, 300, 180)
    }

    # Constants for UI
    ROW_SPACING = 30
    LABEL_FONT_SIZE = 10
    MAX_COLUMNS = 4


    def __init__(self):
        # System language
        self.current_language = self.LANGUAGE_MAPPING.get(locale.getdefaultlocale()[0], 'en')
    
        # UI text
        self.ui_texts = self.UI_DATA[self.current_language]

        # UI size
        self.window_width, self.window_height, self.space = self.OBJECT_SIZE[self.current_language]

        # Initialize other attributes
        self.checkbox_groups = []

    def setup_ui(self, page):
        # Set window
        page.resize(self.window_width, self.window_height)
        page.setWindowTitle(self.ui_texts['window_name'])

        # Set detect button
        self.make_label(page, 110, 10, 2000, 30, self.ui_texts['info_text'])
        self.page_button = QtWidgets.QPushButton(page)
        self.page_button.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.page_button.setText(self.ui_texts['detect_button_text'])

        for idx, group_title in enumerate(self.ui_texts['group_titles']):
            checkboxes = [QtWidgets.QCheckBox(page) for _ in self.ui_texts['group_names'][idx]]
            self.checkbox_groups.append(checkboxes)

        x, y = 10, 50
        for idx, (group_title, checkboxes) in enumerate(zip(self.ui_texts['group_titles'], self.checkbox_groups)):
            self.make_label(page, 10, y, 2000, 30, group_title)
            y += self.ROW_SPACING

            for position, checkbox in enumerate(checkboxes):
                col_count = position % self.MAX_COLUMNS
                row_count = position // self.MAX_COLUMNS

                checkbox_x = x + col_count * self.space
                checkbox_y = y + row_count * self.ROW_SPACING

                checkbox.setGeometry(QtCore.QRect(checkbox_x, checkbox_y, 2000, 30))
                checkbox.setText(self.ui_texts['group_names'][idx][position])
                checkbox.setEnabled(False)
                

            # Next group position
            y += (row_count + 1) * self.ROW_SPACING

    def make_label(self, page, x=10, y=10, w=10, h=20, text='', s=True):
        font = QtGui.QFont()
        font.setPointSize(self.LABEL_FONT_SIZE)
        label = QtWidgets.QLabel(page)
        label.setGeometry(QtCore.QRect(x, y, w, h))
        label.setText(text)
        label.setEnabled(s)
        label.setFont(font)
