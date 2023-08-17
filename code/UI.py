from PyQt5 import QtCore, QtWidgets, QtGui
import locale


class Ui_Form:
    def __init__(self):
        # System language
        language = locale.getdefaultlocale()[0]
        language_mapping = {
            'zh_TW': 'zh_TW',
            'zh': 'zh_TW',
            'en': 'en'
        }
        self.language = language_mapping.get(language, 'en')

        # UI text
        ui_data = {
            'zh_TW': {
                'windows_name': 'HoloCure修改器 by AUSTIN2526',
                'info': '【啟動遊戲後按偵測按鈕遊戲即可啟用功能】',
                'detect_button': '偵測遊戲',
                'group_titles': ['♠ 動態修改區 ♠', '♥ 升級效果區 ♥', '♣ 修改存檔區 ♣'],
                'group_names': [
                    ['鎖血無敵', '全圖吸物', '秒殺怪物', '超高攻速', '無限技能'],
                    ['無限升級', '停止升級'],
                    ['無限貨幣', '全武器庫解鎖', '全成就解鎖', '全角色與服裝', '全關卡解鎖', '被動技能全滿','全小屋家具', '無限小屋道具']
                ]
            },
            'en':{
                'windows_name': 'HoloCure Modifier by AUSTIN2526',
                'info': '【Activate features by pressing the detection button after starting the game】',
                'detect_button': 'Detect Game',
                'group_titles': ['♠ Dynamic Function ♠', '♥ Upgrade Effects ♠', '♣ Save Editor ♣'],
                'group_names': [
                    ['God Mode', 'Full Map Magnet', 'One-Hit Kills', 'Super High Attack Speed', 'Unlimited Skills'],
                    ['Unlimited Level Up', 'Stop Level Up'],
                    ['Unlimited Currency', 'Unlock All Weapons', 'Unlock All Achievements', 'Unlock All Characters and Outfits', 'Unlock All Stages', 'Max Upgrades', 'Unlock All Furniture', 'Unlimited Inventory']
                ]
            }
        }
        self.ui_text = ui_data[self.language]
        
        # UI size
        self.object_size = {
            'zh_TW': (500, 280, 120),
            'en': (780, 280, 180)
        }
        self.w, self.h, self.space = self.object_size[self.language]

                
        self.groups = []
    def setupUi(self, page):   
        # Set window
        page.resize(self.w, self.h)
        page.setWindowTitle(self.ui_text['windows_name'])

        # Set detect button
        self.makelabel(page, 110, 10, 2000, 30, self.ui_text['info'])
        self.page_button = QtWidgets.QPushButton(page)
        self.page_button.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.page_button.setText(self.ui_text['detect_button'])


        for idx in range(len(self.ui_text['group_titles'])):
            checkboxes = [QtWidgets.QCheckBox(page) for _ in self.ui_text['group_names'][idx]]
            self.groups.append(checkboxes)
        
        x, y = 10, 50
        for idx, (group_title, checkboxes) in enumerate(zip(self.ui_text['group_titles'], self.groups)):
            self.makelabel(page, 10, y, 2000, 30, group_title)
            y += 25

            for position, checkbox in enumerate(checkboxes):
                col_count = position % 4
                row_count = position // 4

                checkbox_x = x + col_count * self.space
                checkbox_y = y + row_count * 30

                checkbox.setGeometry(QtCore.QRect(checkbox_x, checkbox_y, 2000, 30))
                checkbox.setText(self.ui_text['group_names'][idx][position])
                checkbox.setEnabled(False)

            # Next group position
            y += (row_count + 1) * 30 

                
    def makelabel(self, page, x=10, y=10, w=10, h=20, text='', s=True):
        font = QtGui.QFont()                       
        font.setPointSize(10) 
        self.label = QtWidgets.QLabel(page)
        self.label.setGeometry(QtCore.QRect(x, y, w, h))
        self.label.setText(text)
        self.label.setEnabled(s)
        self.label.setFont(font)
