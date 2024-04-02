UI_TEXTS = {
    'zh_TW': {
        'window_title': 'HoloCure Trainer by AUSTIN2526',
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
        'window_title': 'HoloCure Trainer by AUSTIN2526',
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

UI_SETTINGS = {
    'zh_TW': {
        'window_size': (500, 300),
        'checkbox_spacing': 120,
        'row_spacing': 30,
        'label_font_size': 10,
        'max_columns': 4
    },
    'en': {
        'window_size': (780, 300),
        'checkbox_spacing': 180,
        'row_spacing': 30,
        'label_font_size': 10,
        'max_columns': 4
    }
}

LANGUAGE_MAP = {
    'zh_TW': 'zh_TW',
    'zh': 'zh_TW',
    'en': 'en'
}

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


import locale

def get_ui_data(language=None):
    if not language:
        system_language = locale.getdefaultlocale()[0]
        language = LANGUAGE_MAP.get(system_language, 'en')

    return UI_TEXTS[language], UI_SETTINGS[language], INFO_MESSAGES[language]