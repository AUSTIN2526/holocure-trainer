def main_info():
    return (
        {'value': 1090021872, 'address': 0x0312E610, 'offset': [0x70, 0x18, 0x170, 0x98, 0x48, 0x10, 0x9F0, 0x04], 'interlock':False},     # HP
        {'value': 1090021872, 'address': 0x0312E610, 'offset': [0x70, 0x18, 0x170, 0x98, 0x48, 0x10, 0x16C0, 0x04], 'interlock': False},  # Pick Range
        {'value': 1090021872, 'address': 0x0312E610, 'offset': [0x70, 0x18, 0x170, 0x98, 0x48, 0x10, 0x1EB0, 0x04], 'interlock': False},  # ATK
        {'value': 1083127808, 'address': 0x0312E610, 'offset': [0x70, 0x18, 0x170, 0x98, 0x48, 0x10, 0x1BB0, 0x04], 'interlock': False},  # Haste
        {'value': 1079558144, 'address': 0x0312E610, 'offset': [0x70, 0x18, 0x170, 0x98, 0x48, 0x10, 0x710, 0x04], 'interlock': False}    # EX
    )

def LV_info():
    return (
        [1072693248, 0x008007B0, [0x30,0x2A90,0x4], True],                             # Level up
        [1083127808, 0x008007B0, [0x30,0x2A90,0x4], True]                             # Stop Level up 
    )
    
def save_editor_info():

    achievements_format = {'flags': {}, 'unlocked': 'True'}
    achievements_list = [
        'haatoClear', 'azkiGachikoi', 'hardcoreGamer', 'suiseiClear', 'kiaraClear', 'lv50', 'zeta10', 'ollieGachikoi', 'speedrunner', 'iofiGachikoi', 'soloBeater', 'reineGachikoi', 'rhythmmaster', 'okayuClear', '2hard', '3hard', 'huh', 'mumeiClear', 'fullyLoaded', 'irysGachikoi', 'shionClear', '1hard', 'mikoClear', 'melClear', 'dontFail', 'subaruClear', 'safeISwear', 'powerLevelling', 'boing', '10000damage', 'robocoGachikoi', 'kroniiClear', 'obliterated', 'risuClear', 'mumeiGachikoi', 'koboGachikoi', 'SCT', 'freeStickers', 'lv100', 'moonaClear', 'heyhey', 'akiGachikoi', 'thankYou', 'shinyfish', 'digin', 'ina10', 'calliClear', 'timeToUpgrade', 'hallucinated', 'matsuriClear', 'koroneClear', 'firstclear', 'millionaire', 'mikoGachikoi', 'payToWin', 'calli10', 'anyaClear', 'kaelaClear', 'koboClear', 'mioGachikoi', 'skillissue', 'shion10', 'donttouch', 'nomain', 'painPeko', 'irysClear', 'oraora', 'ollieClear', 'soraGachikoi', 'payDay', 'baeGachikoi', 'idolgroup', 'sanaClear', 'inaGachikoi', 'baeClear', 'grind', 'CEOnow', 'notTakingAnyChances', 'faunaGachikoi', 'justRNG', 'inaClear', 'bullethell', 'melGachikoi', 'shionGachikoi', 'suiseiGachikoi', 'chocoClear', 'kaelaGachikoi', 'kroniiGachikoi', 'barebones', 'wamy', 'ameClear', 'ollie10', 'iofiClear', 'faunaClear', 'fubukiGachikoi', 'idolPower', '1000damage', 'korone10', 'thirdboss', 'sana10', 'aquaClear', 'dontNeed', 'fullCollab', 'trueRNG', 'muscle', 'zetaClear', 'okayuGachikoi', 'haatoGachikoi', 'plentyoffish', 'employee', 'anyaGachikoi', 'nothoughts', 'petDog', 'howcouldyou', 'bae10', 'hammertime', 'highwayrobbery', 'delusional', 'robocoClear', 'guraClear', 'matsuriGachikoi', 'azkiClear', 'ameGachikoi', 'yagoostatue', 'lookImOnTV', 'sanaGachikoi', 'mioClear', 'aquaGachikoi', 'chocoGachikoi', 'welltrained', 'kiara10', 'ayameGachikoi', 'risuGachikoi', 'artblock', 'akiClear', 'toohalu', 'koroneGachikoi', 'fired', 'luckyDay', 'welcomehome', 'allcomplete', 'harvest', 'ayameClear', 'buyingPower', 'firstboss', '50hamburgers', 'secondboss', 'fleshWound', 'couchPotato', 'soraClear', 'calliGachikoi', 'tankclass', 'pacifist', 'reineClear', 'midboss', 'iDidIt', 'fourthboss', 'lovenature', 'kiaraGachikoi', 'subaruGachikoi', 'zetaGachikoi', 'fishfearme', 'rawstrength', 'stealfish', 'guraGachikoi', 'moonaGachikoi', 'irys10', 'fubukiClear'
    ]
            
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
    
    outfits_list = ['default', 'ameAlt1', 'kiaraAlt1', 'inaAlt1', 'guraAlt1', 'calliAlt1', 'irysAlt1', 'baeAlt1', 'sanaAlt1', 'faunaAlt1', 'mumeiAlt1', 'kroniiAlt1', 'kurokami', 'ameAlt2', 'inaAlt2', 'guraAlt2', 'calliAlt2', 'kiaraAlt2', 'irysAlt2', 'faunaAlt2', 'kroniiAlt2', 'fubukiAlt1', 'mioAlt1', 'koroneAlt1', 'okayuAlt1', 'soraAlt1', 'azkiAlt1', 'robocoAlt1', 'suiseiAlt1', 'mikoAlt1', 'inaAlt3', 'ameAlt3', 'guraAlt3', 'kiaraAlt3', 'calliAlt3', 'mumeiAlt2', 'irysAlt3', 'baeAlt2', 'okayuAlt2', 'fubukiAlt2', 'mioAlt2', 'koroneAlt2', 'suiseiAlt2', 'soraAlt2', 'azkiAlt2', 'mikoAlt2', 'robocoAlt2', 'haatoAlt1', 'melAlt1', 'matsuriAlt1', 'akiAlt1', 'subaruAlt1', 'chocoAlt1', 'shionAlt1', 'ayameAlt1', 'aquaAlt1']
    
    characters = [
        'kronii', 'fubuki', 'calli', 'mel', 'suisei', 'matsuri', 'choco', 'ayame', 'haato', 'roboco', 'fauna', 'sora', 
        'miko', 'gura', 'sana', 'okayu', 'aki', 'irys', 'shion', 'bae', 'azki', 'kiara', 'aqua', 'ina', 'korone', 'mio', 
        'ame', 'subaru', 'mumei', 'reine', 'kaela', 'iofi', 'moona', 'ollie', 'risu', 'anya', 'zeta','kobo'
    ]

    
    stage_list = [
        'STAGE 1', 'STAGE 2', 'STAGE 1 [HARD]','STAGE 3','STAGE 2 [HARD]','TIME STAGE 1', 'STAGE 4', 'HOLO HOUSE'
    ]
    
    



    return (
        
        {'holoCoins': 99999999, 'randomMoneyKey': 0},                                              
        {'unlockedItems': items_list, 'unlockedWeapons': weapons_list, 'seenCollabs':collabs_list}, 
        {'achievements':{name:achievements_format for name in achievements_list}},
        {'characters': [[name, 30] for name in characters], 'unlockedOutfits':outfits_list, 'fandomEXP':[[name, 100] for name in characters]},
        {'unlockedStages':stage_list, 'timeModeUnlocked':True},
        {
            'food': 5, 'growth': 1, 'specUnlock': 1, 'haste': 5, 'mobUp': 5, 'ATK': 10, 'stamps': 1, 'regen': 5,
            'specCDR': 5, 'enhanceUp': 5, 'EXP': 5, 'moneyGain': 10, 'reroll': 10, 'enchantments': 1, 'fandom': 1, 'eliminate': 10,
            'pickupRange': 10, 'DR': 5, 'SPD': 10, 'HP': 10.0, 'crit': 5.,'growth':3.,'skillDamage':10
        }
        
    )
    

def load_data():
    return (
        main_info(),
        LV_info(),
        save_editor_info()
    )
        
        
        
        
    