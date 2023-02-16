import sys
import threading
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from UI import Ui_Form
from pymem import Pymem
from pymem.process import module_from_name
import base64
import os
import json

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        #info language
        self.info = {'zh_TW':{'scan':['掃描', '已掃描到遊戲',],
                              'error':['錯誤', '請先開啟遊戲後再按偵測程式'],
                              'data_error':['存檔讀取失敗', '初次下載請先開啟HoloCure，才能修改存檔'],
                              'save_editor_success':['修改成功','存檔修改完畢，重新啟動遊戲即可生效'],
                              'save_editor_error':['修改失敗','發生不明錯誤，請回報開發者來解決此問題']},
                             
                     'en':{'scan':['Scen','Scan Success'],
                           'error':['Error','Please start the game first, then click the detection button'],
                           'data_error':['Read Failed', 'For the first download, please open HoloCure before use save editor'],
                           'save_editor_success':['Success','Modify successful, please restart the game to take effect'],
                           'save_editor_error':['Fail','Unknow, please report to the developer to fix this program']},                     
        }
        
        #if you want to add new function modify here
        self.modify_data = {
                             #dynamic editor(format function_name:[QCheckBox object, interlock object, value, base address, offsets])
                            'func_name_1_hP':[self.ui.func_group_1[0], None, 1090021872, 0x00A1EFD8, [0x70,0x18,0x170,0x98,0x48,0x10,0x11A0,0x04]],
                            'func_name_1_range':[self.ui.func_group_1[1], None, 1090021872, 0x00A1EFD8, [0x70,0x18,0x170,0x98,0x48,0x10,0x500,0x04]],
                            'func_name_1_atk':[self.ui.func_group_1[2], None, 1090021872, 0x00A1EFD8, [0x70,0x18,0x170,0x98,0x48,0x10,0x16C0,0x04]],
                            'func_name_1_haste':[self.ui.func_group_1[3], None, 1083127808, 0x00A1EFD8, [0x70,0x18,0x170,0x98,0x48,0x10,0x1430,0x04]],
                            'func_name_1_ex':[self.ui.func_group_1[4], None, 1079558144, 0x00A1EFD8, [0x70,0x18,0x170,0x98,0x48,0x10,0x9C0,0x04]],
                             
                            'func_name_2_level_up':[self.ui.func_group_2[0],self.ui.func_group_2[1], 1072693248, 0x008007B0, [0x30,0x2A90,0x4]],
                            'func_name_2_stop_level_up':[self.ui.func_group_2[1],self.ui.func_group_2[0], 1083127808, 0x008007B0, [0x30,0x2A90,0x4]],
                                
                                
                             #save editor(format function_name:[QCheckBox object,{key:val}])
                            'save_editor_coin':[self.ui.save_editor_func_1[0], {'holoCoins':99999999, 'randomMoneyKey':0}],
                            
                            'save_editor_armory':[
                                                    self.ui.save_editor_func_1[1], 
                                                    {
                                                        'unlockedItems':[
                                                                        'BodyPillow', 'FullMeal', 'PikiPikiPiman', 'SuccubusHorn', 'Headphones', 'UberSheep', 'HolyMilk', \
                                                                        'Sake', 'FaceMask', 'CreditCard', 'GorillasPaw', 'InjectionAsacoco', 'IdolCostume', 'Plushie', 'StudyGlasses',  \
                                                                        'SuperChattoTime', 'EnergyDrink', 'Halu', 'Membership', 'GWSPill', 'ChickensFeather', 'Bandaid', 'Limiter', \
                                                                        'PiggyBank', 'DevilHat', 'BlacksmithsGear', 'Breastplate', 'HopeSoda', 'Shacklesss'
                                                        ],
                                             
                                                        'unlockedWeapons':[
                                                                            'PsychoAxe', 'Glowstick', 'SpiderCooking', 'Tailplug', 'BLBook', 'EliteLava', 'HoloBomb', 'HoloLaser', \
                                                                            'CuttingBoard', 'IdolSong', 'CEOTears', 'WamyWater', 'XPotato', 'BounceBall', 'ENCurse'
                                                        ],
                                                                           
                                                        'seenCollabs':[
                                                                        'BreatheInAsacoco', 'DragonBeam', 'EliteCooking', 'FlatBoard', 'MiComet', 'BLLover', 'LightBeam', \
                                                                        'IdolConcert', 'StreamOfTears', 'MariLamy', 'BrokenDreams', 'RapDog', 'BoneBros', 'RingOfFitness', \
                                                                        'MiKorone', 'SnowSake', 'ImDie', 'AbsoluteWall', 'EldritchHorror'
                                                        ],
                                                                        
                                                        'unlockedOutfits':[
                                                                            'default', 'ameAlt1', 'kiaraAlt1', 'inaAlt1', 'guraAlt1', 'calliAlt1', 'irysAlt1', 'baeAlt1', \
                                                                            'sanaAlt1', 'faunaAlt1', 'mumeiAlt1', 'kroniiAlt1', 'kurokami', 'ameAlt2', 'inaAlt2', 'guraAlt2', \
                                                                            'calliAlt2', 'kiaraAlt2', 'irysAlt2', 'faunaAlt2', 'kroniiAlt2', 'fubukiAlt1', 'mioAlt1', 'koroneAlt1', 'okayuAlt1', \
                                                                            'soraAlt1', 'azkiAlt1', 'robocoAlt1', 'suiseiAlt1', 'mikoAlt1'
                                                        ]
                            
                                                    }
                            ],
                            
                             #this option can use for loop modeify it, but will break the system architecture,so I don't use it
                            'save_editor_achievements':[
                                                        self.ui.save_editor_func_1[2], 
                                                        {
                                                            'achievements':{
                                                                            'pacifist': {'flags': {}, 'unlocked': 'True'}, 'midboss': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'kiara10': {'flags': {}, 'unlocked': 'True'}, 'okayuGachikoi': {'flags': {}, 'unlocked': 'True'}, 'melGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'kroniiClear': {'flags': {}, 'unlocked': 'True'}, 'speedrunner': {'flags': {}, 'unlocked': 'True'}, 'soloBeater': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'iDidIt': {'flags': {}, 'unlocked': 'True'}, 'ayameGachikoi': {'flags': {}, 'unlocked': 'True'}, 'haatoGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'shionGachikoi': {'flags': {}, 'unlocked': 'True'}, 'obliterated': {'flags': {}, 'unlocked': 'True'}, 'mumeiGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'SCT': {'flags': {}, 'unlocked': 'True'}, 'okayuClear': {'flags': {}, 'unlocked': 'True'}, 'kiaraGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'akiClear': {'flags': {}, 'unlocked': 'True'}, 'suiseiGachikoi': {'flags': {}, 'unlocked': 'True'}, 'mioGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'CEOnow': {'flags': {}, 'unlocked': 'True'}, 'shion10': {'flags': {}, 'unlocked': 'True'}, 'fired': {'flags': {}, 'unlocked': 'True'}, 'lv100': {'flags': {}, \
                                                                            'unlocked': 'True'}, '2hard': {'flags': {}, 'unlocked': 'True'}, 'subaruGachikoi': {'flags': {}, 'unlocked': 'True'}, 'toohalu': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'chocoClear': {'flags': {}, 'unlocked': 'True'}, 'kroniiGachikoi': {'flags': {}, 'unlocked': 'True'}, 'wamy': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'payDay': {'flags': {}, 'unlocked': 'True'}, 'painPeko': {'flags': {}, 'unlocked': 'True'}, 'akiGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'mumeiClear': {'flags': {}, 'unlocked': 'True'}, 'koroneGachikoi': {'flags': {}, 'unlocked': 'True'}, 'petDog': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'bae10': {'flags': {}, 'unlocked': 'True'}, 'ameClear': {'flags': {}, 'unlocked': 'True'}, 'irysClear': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'thankYou': {'flags': {}, 'unlocked': 'True'}, 'fullyLoaded': {'flags': {}, 'unlocked': 'True'}, 'luckyDay': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'allcomplete': {'flags': {}, 'unlocked': 'True'}, 'ayameClear': {'flags': {}, 'unlocked': 'True'}, 'delusional': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'faunaClear': {'flags': {}, 'unlocked': 'True'}, 'soraGachikoi': {'flags': {}, 'unlocked': 'True'}, 'irysGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'guraGachikoi': {'flags': {}, 'unlocked': 'True'}, 'irys10': {'flags': {}, 'unlocked': 'True'}, 'buyingPower': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'robocoClear': {'flags': {}, 'unlocked': 'True'}, 'fubukiGachikoi': {'flags': {}, 'unlocked': 'True'}, 'baeGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'shionClear': {'flags': {}, 'unlocked': 'True'}, 'mikoClear': {'flags': {}, 'unlocked': 'True'}, 'fubukiClear': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'firstboss': {'flags': {}, 'unlocked': 'True'}, 'freeStickers': {'flags': {}, 'unlocked': 'True'}, 'guraClear': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'idolPower': {'flags': {}, 'unlocked': 'True'}, 'ina10': {'flags': {}, 'unlocked': 'True'}, '1hard': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'melClear': {'flags': {}, 'unlocked': 'True'}, 'haatoClear': {'flags': {}, 'unlocked': 'True'}, '50hamburgers': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'matsuriGachikoi': {'flags': {}, 'unlocked': 'True'}, '1000damage': {'flags': {}, 'unlocked': 'True'}, 'calliClear': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'hallucinated': {'flags': {}, 'unlocked': 'True'}, 'dontFail': {'flags': {}, 'unlocked': 'True'}, 'azkiGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'secondboss': {'flags': {}, 'unlocked': 'True'}, 'azkiClear': {'flags': {}, 'unlocked': 'True'}, 'idolgroup': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'timeToUpgrade': {'flags': {}, 'unlocked': 'True'}, 'matsuriClear': {'flags': {}, 'unlocked': 'True'}, 'subaruClear': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'hardcoreGamer': {'flags': {}, 'unlocked': 'True'}, 'fleshWound': {'flags': {}, 'unlocked': 'True'}, 'ameGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'sanaClear': {'flags': {}, 'unlocked': 'True'}, 'baeClear': {'flags': {}, 'unlocked': 'True'}, 'koroneClear': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'safeISwear': {'flags': {}, 'unlocked': 'True'}, 'suiseiClear': {'flags': {}, 'unlocked': 'True'}, 'couchPotato': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'thirdboss': {'flags': {}, 'unlocked': 'True'}, 'inaGachikoi': {'flags': {}, 'unlocked': 'True'}, 'grind': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'firstclear': {'flags': {}, 'unlocked': 'True'}, 'powerLevelling': {'flags': {}, 'unlocked': 'True'}, 'kiaraClear': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'korone10': {'flags': {}, 'unlocked': 'True'}, 'sana10': {'flags': {}, 'unlocked': 'True'}, 'dontNeed': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'notTakingAnyChances': {'flags': {}, 'unlocked': 'True'}, 'millionaire': {'flags': {}, 'unlocked': 'True'}, 'boing': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'lv50': {'flags': {}, 'unlocked': 'True'}, 'lookImOnTV': {'flags': {}, 'unlocked': 'True'}, 'aquaClear': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'fullCollab': {'flags': {}, 'unlocked': 'True'}, 'faunaGachikoi': {'flags': {}, 'unlocked': 'True'}, 'mikoGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            '10000damage': {'flags': {}, 'unlocked': 'True'}, 'yagoostatue': {'flags': {}, 'unlocked': 'True'}, 'sanaGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'aquaGachikoi': {'flags': {}, 'unlocked': 'True'}, 'trueRNG': {'flags': {}, 'unlocked': 'True'}, 'justRNG': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'payToWin': {'flags': {}, 'unlocked': 'True'}, 'robocoGachikoi': {'flags': {}, 'unlocked': 'True'}, 'calliGachikoi': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'mioClear': {'flags': {}, 'unlocked': 'True'}, 'chocoGachikoi': {'flags': {}, 'unlocked': 'True'}, 'muscle': {'flags': {}, 'unlocked': 'True'}, \
                                                                            'inaClear': {'flags': {}, 'unlocked': 'True'}, 'calli10': {'flags': {}, 'unlocked': 'True'}, 'soraClear': {'flags': {}, 'unlocked': 'True'}
                                                            }
                                                        }
                            ],
                             
                            #this option can use for loop modeify it, but will break the system architecture,so I don't use it
                            'save_editor_characters':[
                                                        self.ui.save_editor_func_1[3],
                                                        {
                                                         'characters':[
                                                                        ['kronii', 30], ['fubuki', 30], ['calli', 30], ['mel', 30], ['suisei', 30], ['matsuri', 30], ['choco', 30], \
                                                                        ['ayame', 30], ['haato', 30], ['random', 0], ['none', 0], ['roboco', 30], ['fauna', 30], ['sora', 30], ['miko', 30], ['empty', 0], ['gura', 30], ['sana', 30], \
                                                                        ['okayu', 30], ['aki', 30], ['irys', 30], ['shion', 30], ['bae', 30], ['azki', 30], ['kiara', 30], ['aqua', 30], ['ina', 30], ['korone', 30], ['mio', 30], \
                                                                        ['ame', 30], ['subaru', 30], ['mumei', 30]
                                                         ],
                                                        'unlockedOutfits':['default', 'ameAlt1', 'kiaraAlt1', 'inaAlt1', 'guraAlt1', 'calliAlt1', 'irysAlt1', 'baeAlt1', 'sanaAlt1', 'faunaAlt1', 'mumeiAlt1', 'kroniiAlt1', 'kurokami', \
                                                                           'ameAlt2', 'inaAlt2', 'guraAlt2', 'calliAlt2', 'kiaraAlt2', 'irysAlt2', 'faunaAlt2', 'kroniiAlt2', 'fubukiAlt1', 'mioAlt1', 'koroneAlt1', 'okayuAlt1', 'soraAlt1', \
                                                                           'azkiAlt1', 'robocoAlt1', 'suiseiAlt1', 'mikoAlt1']
                                                         }
                            ],
                            
                            'save_editor_unlockedStages':[
                                                        self.ui.save_editor_func_1[4], 
                                                        {
                                                            'unlockedStages':['STAGE 1', 'STAGE 2', 'STAGE 1 (HARD)','STAGE 3','STAGE 2 (HARD)','TIME STAGE 1'],
                                                            'timeModeUnlocked':True
                                                        }
                                                                         
                            ],
                            
                            'save_editor_upgrades':[
                                                    self.ui.save_editor_func_1[5],
                                                    {
                                                        'food': 5, 'growth': 1, 'specUnlock': 1, 'haste': 5, 'mobUp': 5, 'ATK': 10, 'stamps': 1, 'regen': 5, \
                                                        'specCDR': 5, 'enhanceUp': 5, 'EXP': 5, 'moneyGain': 10, 'reroll': 10, 'enchantments': 1, 'fandom': 1, 'eliminate': 10, \
                                                        'pickupRange': 10, 'DR': 5, 'SPD': 10, 'HP': 10.0, 'crit': 5.0
                                                    }
                            ]
        }
       
        #load game data
        self.game_data_path = f'{os.getenv("LOCALAPPDATA")}\HoloCure\save_n.dat'
        self.game_data = self.load_game_data()

        #read HoloCure windows
        self.ui.page_button.clicked.connect(self.find_windows) 

        #connect QCheckBox with modify function
        func_index = 0
        for group_ID in self.ui.all_group:        
            for function in group_ID:
                name = list(self.modify_data.keys())[func_index]
                func_index+=1
                function.clicked.connect(lambda state, x=name: self.select_modify_type(x))

        
        self.move(40, 40)
        self.show()
    
    def load_game_data(self):
        try:
            #read HoloCure data file
            with open(self.game_data_path, 'rb') as f:
                #decode data
                decode_data = base64.b64decode(f.read())
                
            #enable save_editor_func
            for function in self.ui.all_group[-1]:
                function.setEnabled(True)
            
            return json.loads(decode_data)
            
        except:
            QMessageBox.critical(None, self.info[self.ui.language]['data_error'][0], self.info[self.ui.language]['data_error'][1])

    def find_windows(self):
        #get HoloCure dll file
        try:
            self.windows = Pymem("HoloCure.exe")
            self.game_module = module_from_name(self.windows.process_handle, "HoloCure.exe").lpBaseOfDll
            
            #enable func
            for functions in self.ui.all_group[:-1]:
                for function in functions:
                    function.setEnabled(True)
                    
            QMessageBox.information(None, self.info[self.ui.language]['scan'][0], self.info[self.ui.language]['scan'][1])
            
        except:
            QMessageBox.critical(None, self.info[self.ui.language]['error'][0], self.info[self.ui.language]['error'][1])
      
    def select_modify_type(self, text):
        #save editor
        if text.split('_')[0]== 'save':
            self.save_editor(text)       
        #dynamic modeify
        else:
            t = threading.Thread(target = self.dynamic_modify, args = (text,))
            t.setDaemon(True)
            t.start()
        

    
    def dynamic_modify(self, text): 
    
        function, interlock, value, address, offsets = self.modify_data[text]
        
        #interlock function
        if interlock != None:
            interlock.setChecked(False)
        
        #modify memory
        while(1):
            if function.isChecked():
                try:
                    addr  = self.calculate_address(self.game_module + address, offsets)
                    if self.windows.read_int(addr) != value:
                        self.windows.write_int(addr, value)
                        
                except:
                    pass
                    
            else:
                break
    
    def save_editor(self, text):
        function, data = self.modify_data[text]
        try:
            #modify game data
            if function.isChecked():
                for modify_name, val in data.items():
                    self.game_data[modify_name] = val
                
                #write game data
                with open(self.game_data_path, 'wb') as f:
                    res = base64.b64encode(json.dumps(self.game_data).encode('UTF-8'))
                    f.write(res)
                    
                QMessageBox.information(None, self.info[self.ui.language]['save_editor_success'][0], self.info[self.ui.language]['save_editor_success'][1])
                
        except:
            QMessageBox.critical(None, self.info[self.ui.language]['save_editor_error'][0], self.info[self.ui.language]['save_editor_error'][1])
            

            
    def calculate_address(self, address, offsets):
        addr = self.windows.read_int(address)
        for cnt,offset in enumerate(offsets):
            if cnt+1 != len(offsets):
                addr = self.windows.read_int(addr + offset)           
        return addr + offsets[-1]
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
