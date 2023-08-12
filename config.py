def main_info():
    return (
        [1090021872, 0x00A1EFD8, [0x70,0x18,0x170,0x98,0x48,0x10,0x11B0,0x04], False],  # HP
        [1090021872, 0x00A1EFD8, [0x70,0x18,0x170,0x98,0x48,0x10,0x500,0x04], False],   # Pick Range
        [1090021872, 0x00A1EFD8, [0x70,0x18,0x170,0x98,0x48,0x10,0x16C0,0x04], False],  # ATK
        [1083127808, 0x00A1EFD8, [0x70,0x18,0x170,0x98,0x48,0x10,0x1430,0x04], False],  # Haste
        [1079558144, 0x00A1EFD8, [0x70,0x18,0x170,0x98,0x48,0x10,0x9C0,0x04], False]   # EX
    )

def LV_info():
    return (
        [1072693248, 0x008007B0, [0x30,0x2A90,0x4], True],                             # Level up
        [1083127808, 0x008007B0, [0x30,0x2A90,0x4], True]                             # Stop Level up 
    )
    
def save_editor_info():

    
    achievements_list = [
        'pacifist', 'midboss', 'kiara10', 'okayuGachikoi', 'melGachikoi',
        'kroniiClear', 'speedrunner', 'soloBeater', 'iDidIt', 'ayameGachikoi',
        'haatoGachikoi', 'shionGachikoi', 'obliterated', 'mumeiGachikoi', 'SCT',
        'okayuClear', 'kiaraGachikoi', 'akiClear', 'suiseiGachikoi', 'mioGachikoi',
        'CEOnow', 'shion10', 'fired', 'lv100', '2hard', 'subaruGachikoi', 'toohalu',
        'chocoClear', 'kroniiGachikoi', 'wamy', 'payDay', 'painPeko', 'akiGachikoi',
        'mumeiClear', 'koroneGachikoi', 'petDog', 'bae10', 'ameClear', 'irysClear',
        'thankYou', 'fullyLoaded', 'luckyDay', 'allcomplete', 'ayameClear',
        'delusional', 'faunaClear', 'soraGachikoi', 'irysGachikoi', 'guraGachikoi',
        'irys10', 'buyingPower', 'robocoClear', 'fubukiGachikoi', 'baeGachikoi',
        'shionClear', 'mikoClear', 'fubukiClear', 'firstboss', 'freeStickers',
        'guraClear', 'idolPower', 'ina10', '1hard', 'melClear', 'haatoClear',
        '50hamburgers', 'matsuriGachikoi', '1000damage', 'calliClear', 'hallucinated',
        'dontFail', 'azkiGachikoi', 'secondboss', 'azkiClear', 'idolgroup',
        'timeToUpgrade', 'matsuriClear', 'subaruClear', 'hardcoreGamer', 'fleshWound',
        'ameGachikoi', 'sanaClear', 'baeClear', 'koroneClear', 'safeISwear',
        'suiseiClear', 'couchPotato', 'thirdboss', 'inaGachikoi', 'grind', 'firstclear',
        'powerLevelling', 'kiaraClear', 'korone10', 'sana10', 'dontNeed',
        'notTakingAnyChances', 'millionaire', 'boing', 'lv50', 'lookImOnTV',
        'aquaClear', 'fullCollab', 'faunaGachikoi', 'mikoGachikoi', '10000damage',
        'yagoostatue', 'sanaGachikoi', 'aquaGachikoi', 'trueRNG', 'justRNG',
        'payToWin', 'robocoGachikoi', 'calliGachikoi', 'mioClear', 'chocoGachikoi',
        'muscle', 'inaClear', 'calli10', 'soraClear'
    ]
    achievements_format = {'flags': {}, 'unlocked': 'True'}
            
    items_list = [ 
        'BodyPillow', 'FullMeal', 'PikiPikiPiman', 'SuccubusHorn', 'Headphones', 'UberSheep', 'HolyMilk',
        'Sake', 'FaceMask', 'CreditCard', 'GorillasPaw', 'InjectionAsacoco', 'IdolCostume', 'Plushie', 'StudyGlasses',
        'SuperChattoTime', 'EnergyDrink', 'Halu', 'Membership', 'GWSPill', 'ChickensFeather', 'Bandaid', 'Limiter',
        'PiggyBank', 'DevilHat', 'BlacksmithsGear', 'Breastplate', 'HopeSoda', 'Shacklesss'
    ]
    
    weapons_list = [
        'PsychoAxe', 'Glowstick', 'SpiderCooking', 'Tailplug', 'BLBook', 'EliteLava', 'HoloBomb', 'HoloLaser',
        'CuttingBoard', 'IdolSong', 'CEOTears', 'WamyWater', 'XPotato', 'BounceBall', 'ENCurse'
    ]
    
    collabs_list = [
        'BreatheInAsacoco', 'DragonBeam', 'EliteCooking', 'FlatBoard', 'MiComet', 'BLLover', 'LightBeam',
        'IdolConcert', 'StreamOfTears', 'MariLamy', 'BrokenDreams', 'RapDog', 'BoneBros', 'RingOfFitness',
        'MiKorone', 'SnowSake', 'ImDie', 'AbsoluteWall', 'EldritchHorror'
    ]
    
    outfits_list = [
        'default', 'ameAlt1', 'kiaraAlt1', 'inaAlt1', 'guraAlt1', 'calliAlt1', 'irysAlt1', 'baeAlt1',
        'sanaAlt1', 'faunaAlt1', 'mumeiAlt1', 'kroniiAlt1', 'kurokami', 'ameAlt2', 'inaAlt2', 'guraAlt2',
        'calliAlt2', 'kiaraAlt2', 'irysAlt2', 'faunaAlt2', 'kroniiAlt2', 'fubukiAlt1', 'mioAlt1', 'koroneAlt1', 'okayuAlt1',
        'soraAlt1', 'azkiAlt1', 'robocoAlt1', 'suiseiAlt1', 'mikoAlt1'
    ]
    
    characters = [
        'kronii', 'fubuki', 'calli', 'mel', 'suisei', 'matsuri', 'choco',
        'ayame', 'haato', 'random', 'none', 'roboco', 'fauna', 'sora',
        'miko', 'empty', 'gura', 'sana', 'okayu', 'aki', 'irys', 'shion',
        'bae', 'azki', 'kiara', 'aqua', 'ina', 'korone', 'mio',
        'ame', 'subaru', 'mumei'
    ]
    
    stage_list = [
        'STAGE 1', 'STAGE 2', 'STAGE 1 [HARD]','STAGE 3','STAGE 2 [HARD]','TIME STAGE 1'
    
    ]



    return (
        
        {'holoCoins': 99999999, 'randomMoneyKey': 0},               # Coin 
        {'unlockedItems': items_list, 'unlockedWeapons': weapons_list, 'seenCollabs':collabs_list}, # All Armorys 
        {'achievements':{name:achievements_format for name in achievements_list}},
        {'characters': [[name, 30] for name in characters], 'unlockedOutfits':outfits_list},
        {'unlockedStages':stage_list, 'timeModeUnlocked':True},
        {
            'food': 5, 'growth': 1, 'specUnlock': 1, 'haste': 5, 'mobUp': 5, 'ATK': 10, 'stamps': 1, 'regen': 5,
            'specCDR': 5, 'enhanceUp': 5, 'EXP': 5, 'moneyGain': 10, 'reroll': 10, 'enchantments': 1, 'fandom': 1, 'eliminate': 10,
            'pickupRange': 10, 'DR': 5, 'SPD': 10, 'HP': 10.0, 'crit': 5.0
        }
        
    )
    

def load_data():
    return (
        main_info(),
        LV_info(),
        save_editor_info()
    )
        
        
        
        
    