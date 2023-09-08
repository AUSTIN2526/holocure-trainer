def main_info():
    return (
        {'value': 99999.0, 'address': 0x0314EE10, 'offset': [0x70, 0x18, 0x170, 0x98, 0x48, 0x10, 0xEB0, 0x00], 'interlock':False},     # HP
        {'value': 99999.0, 'address': 0x0314EE10, 'offset': [0x70, 0x18, 0x170, 0x98, 0x48, 0x10, 0x1F80, 0x00], 'interlock': False},  # Pick Range
        {'value': 99999.0, 'address': 0x0314EE10, 'offset': [0x70, 0x18, 0x170, 0x98, 0x48, 0x10, 0x340, 0x00], 'interlock': False},  # ATK
        {'value': 999.0, 'address': 0x0314EE10, 'offset': [0x70, 0x18, 0x170, 0x98, 0x48, 0x10, 0xCB0, 0x00], 'interlock': False},  # Haste
        {'value': 76.0, 'address': 0x0314EE10, 'offset': [0x70, 0x18, 0x170, 0x98, 0x48, 0x10, 0x1A80, 0x00], 'interlock': False}    # EX
    )

def LV_info():
    return (
        {'value': 1.0, 'address': 0x0314EB98, 'offset': [0x48,0x10,0xEC20, 0x00], 'interlock': True},    # Level up
        {'value': 999.0, 'address': 0x0314EB98, 'offset': [0x48,0x10,0xEC20, 0x00], 'interlock': True}    # Stop Level up                           
    )
    
def save_editor_info():
    # Achievements
    achievements_format = {'flags': {}, 'unlocked': 'True'}
    achievements = [
        'haatoClear', 'azkiGachikoi', 'hardcoreGamer', 'suiseiClear', 'kiaraClear', 'lv50', 'zeta10', 'ollieGachikoi', 'speedrunner', 'iofiGachikoi', 'soloBeater', 'reineGachikoi', 'rhythmmaster', 'okayuClear', '2hard', '3hard', 'huh', 'mumeiClear', 'fullyLoaded', 'irysGachikoi', 'shionClear', '1hard', 'mikoClear', 'melClear', 'dontFail', 'subaruClear', 'safeISwear', 'powerLevelling', 'boing', '10000damage', 'robocoGachikoi', 'kroniiClear', 'obliterated', 'risuClear', 'mumeiGachikoi', 'koboGachikoi', 'SCT', 'freeStickers', 'lv100', 'moonaClear', 'heyhey', 'akiGachikoi', 'thankYou', 'shinyfish', 'digin', 'ina10', 'calliClear', 'timeToUpgrade', 'hallucinated', 'matsuriClear', 'koroneClear', 'firstclear', 'millionaire', 'mikoGachikoi', 'payToWin', 'calli10', 'anyaClear', 'kaelaClear', 'koboClear', 'mioGachikoi', 'skillissue', 'shion10', 'donttouch', 'nomain', 'painPeko', 'irysClear', 'oraora', 'ollieClear', 'soraGachikoi', 'payDay', 'baeGachikoi', 'idolgroup', 'sanaClear', 'inaGachikoi', 'baeClear', 'grind', 'CEOnow', 'notTakingAnyChances', 'faunaGachikoi', 'justRNG', 'inaClear', 'bullethell', 'melGachikoi', 'shionGachikoi', 'suiseiGachikoi', 'chocoClear', 'kaelaGachikoi', 'kroniiGachikoi', 'barebones', 'wamy', 'ameClear', 'ollie10', 'iofiClear', 'faunaClear', 'fubukiGachikoi', 'idolPower', '1000damage', 'korone10', 'thirdboss', 'sana10', 'aquaClear', 'dontNeed', 'fullCollab', 'trueRNG', 'muscle', 'zetaClear', 'okayuGachikoi', 'haatoGachikoi', 'plentyoffish', 'employee', 'anyaGachikoi', 'nothoughts', 'petDog', 'howcouldyou', 'bae10', 'hammertime', 'highwayrobbery', 'delusional', 'robocoClear', 'guraClear', 'matsuriGachikoi', 'azkiClear', 'ameGachikoi', 'yagoostatue', 'lookImOnTV', 'sanaGachikoi', 'mioClear', 'aquaGachikoi', 'chocoGachikoi', 'welltrained', 'kiara10', 'ayameGachikoi', 'risuGachikoi', 'artblock', 'akiClear', 'toohalu', 'koroneGachikoi', 'fired', 'luckyDay', 'welcomehome', 'allcomplete', 'harvest', 'ayameClear', 'buyingPower', 'firstboss', '50hamburgers', 'secondboss', 'fleshWound', 'couchPotato', 'soraClear', 'calliGachikoi', 'tankclass', 'pacifist', 'reineClear', 'midboss', 'iDidIt', 'fourthboss', 'lovenature', 'kiaraGachikoi', 'subaruGachikoi', 'zetaGachikoi', 'fishfearme', 'rawstrength', 'stealfish', 'guraGachikoi', 'moonaGachikoi', 'irys10', 'fubukiClear'
    ]
    
    # Armorys
    items = [
        'BodyPillow', 'FullMeal', 'PikiPikiPiman', 'SuccubusHorn', 'Headphones', 'UberSheep', 'HolyMilk', 'Sake', 'FaceMask', 'CreditCard', 'GorillasPaw', 'InjectionAsacoco', 'IdolCostume', 'Plushie', 'StudyGlasses', 'SuperChattoTime', 'EnergyDrink', 'Halu', 'Membership', 'GWSPill', 'ChickensFeather', 'Bandaid', 'Limiter', 'PiggyBank', 'DevilHat', 'BlacksmithsGear', 'Breastplate', 'HopeSoda', 'Shacklesss', 'Candy', 'NinjaHeadband', 'FocusShades', 'Beetle', 'LabCoat'
    ]
    
    weapons = [
        'PsychoAxe', 'Glowstick', 'SpiderCooking', 'Tailplug', 'BLBook', 'EliteLava', 'HoloBomb', 'HoloLaser', 'CuttingBoard', 'IdolSong', 'CEOTears', 'WamyWater', 'XPotato', 'BounceBall', 'ENCurse', 'Sausage'
    ]
    
    collabs = [
        'BreatheInAsacoco', 'DragonBeam', 'EliteCooking', 'FlatBoard', 'MiComet', 'BLLover', 'LightBeam', 'IdolConcert', 'StreamOfTears', 'MariLamy', 'BrokenDreams', 'RapDog', 'BoneBros', 'RingOfFitness', 'MiKorone', 'SnowSake', 'ImDie', 'AbsoluteWall', 'EldritchHorror', 'StarHalberd', 'CurseBall', 'KanaCoco', 'LegendarySausage', 'Jingisukan', 'LightningWeiner', 'SnowQueen', 'IdolLive'
    ]
    
    # Characters
    outfits = [
        'default', 'ameAlt1', 'kiaraAlt1', 'inaAlt1', 'guraAlt1', 'calliAlt1', 'irysAlt1', 'baeAlt1', 'sanaAlt1', 'faunaAlt1', 'mumeiAlt1', 'kroniiAlt1', 'kurokami', 'ameAlt2', 'inaAlt2', 'guraAlt2', 'calliAlt2', 'kiaraAlt2', 'irysAlt2', 'faunaAlt2', 'kroniiAlt2', 'fubukiAlt1', 'mioAlt1', 'koroneAlt1', 'okayuAlt1', 'soraAlt1', 'azkiAlt1', 'robocoAlt1', 'suiseiAlt1', 'mikoAlt1', 'inaAlt3', 'ameAlt3', 'guraAlt3', 'kiaraAlt3', 'calliAlt3', 'mumeiAlt2', 'irysAlt3', 'baeAlt2', 'okayuAlt2', 'fubukiAlt2', 'mioAlt2', 'koroneAlt2', 'suiseiAlt2', 'soraAlt2', 'azkiAlt2', 'mikoAlt2', 'robocoAlt2', 'haatoAlt1', 'melAlt1', 'matsuriAlt1', 'akiAlt1', 'subaruAlt1', 'chocoAlt1', 'shionAlt1', 'ayameAlt1', 'aquaAlt1'
    ]
    
    characters = [
        'kronii', 'fubuki', 'calli', 'mel', 'suisei', 'matsuri', 'choco', 'ayame', 'haato', 'roboco', 'fauna', 'sora', 
        'miko', 'gura', 'sana', 'okayu', 'aki', 'irys', 'shion', 'bae', 'azki', 'kiara', 'aqua', 'ina', 'korone', 'mio', 
        'ame', 'subaru', 'mumei', 'reine', 'kaela', 'iofi', 'moona', 'ollie', 'risu', 'anya', 'zeta','kobo'
    ]

    # Stage
    stage = [
        'STAGE 1', 'STAGE 2', 'STAGE 1 (HARD)', 'STAGE 3', 'STAGE 2 (HARD)', 'TIME STAGE 1', 'STAGE 4', 'STAGE 3 (HARD)', 'HOLO HOUSE'
    ]
    
    # Tears
    tears = ['myth', 'councilHope', 'gamers', 'gen0', 'gen1', 'gen2', 'id1', 'id2', 'id3']
    
    
    
    furniture = [
        'bodypillow', 'vanity', 'gamerchairH', 'gamerchairg', 'gamerchairf', 'gamerchaire', 'gamerchaird', 'gamerchairc', 'gamerchairb', 'gamerchaira', 'officechair', 'beanbag', 'marblelaptopdesk', 'marbledesk', 'woodenPCdesk', 'woodendesk', 'woodenDresserA', 'nightstandB', 'nightstandA', 'futon', 'marblebed', 'woodenBedD', 'woodenBedC', 'woodenBedB', 'woodenBed', 'couchA', 'foxburger', 'woodentable', 'marbletable', 'glasstable', 'easterntable', 'floorcushion', 'woodentallcabinet', 'standinglampA', 'fireplace', 'TVStand', 'crttv', 'retroconsole', 'vrset', 'woodenbookshelf', 'marblebookshelf', 'displaycase', 'woodenDiningTable', 'marbleTable', 'woodenDiningChair', 'marblechair', 'stoolA1', 'kitchenCounterA', 'Microwave', 'marbleCounter', 'marblesink', 'fridge', 'stove', 'bathstool', 'sink', 'bathtub', 'toilet', 'washingmachine', 'laundrybasket', 'woodenCrate', 'woodenbarrel', 'boxA', 'BoxB', 'TreasureChestA', 'plantpotA', 'plantpotB', 'plantpotC', 'berryplant', 'marblestump', 'dumbell', 'exerciseball', 'boxingdummy', 'vampirecoffin', 'baegemite', 'taikodrums', 'shrinebox', 'KFPbucket', 'sharkplush', 'nekoplush', 'achandoll', 'completegrass', 'woodendivider', 'marblepartition', 'easterndivider', 'woodenwall', 'woodenhalfwall', 'woodencolumn', 'marblecolumn', 'woodendoor', 'clock', 'kroniclock', 'paintingA', 'paintingC', 'paintingB', 'paintingD', 'wallmirror', 'lantern', 'hangingvine', 'mountedSword', 'demonSword', 'window', 'hardcoretrophy', 'woodenFloor', 'woodenFloor2', 'stoneFloor', 'redCarpetFloor', 'blueCarpetFloor', 'pinkCarpetFloor', 'concreteFloor', 'marbleFloor', 'tiledFloor', 'tatamiFloor', 'woodenWall', 'flatWall', 'stripedWall', 'skyWall', 'polkaWallA', 'polkaWallB', 'polkaWallC', 'oceanWall', 'modernWall', 'stoneWall', 'easternWall', 'goldenfish1', 'goldenfish2', 'goldenfish3', 'goldenfish4', 'goldenfish5', 'goldenfish6', 'goldenfish7', 'goldenfish8', 'goldenfish9', 'goldenfish10', 'goldenfish11', 'goldenfish12'
    ]
    
    inventory = [
        'shrimp', 'clownfish', 'tuna', 'standardsoil', 'expeditedsoil', 'enhancedsoil', 'wheatSeed', 'tomatoSeed', 'potatoSeed', 'riceSeed', 'onionseed', 'carrotseed', 'greenbeansseed', 'peppersseed', 'strawberryseed', 'cornseed', 'radishseed', 'garlicseed', 'eel', 'koifish', 'lobster', 'wheat', 'tomato', 'potato', 'rice', 'peppers', 'greenbeans', 'carrot', 'onion', 'strawberry', 'corn', 'radish', 'garlic', 'pufferfish', 'mantaray', 'turtle', 'squid', 'shark', 'axolotl','goldenshrimp', 'goldenclownfish', 'goldentuna', 'goldeneel', 'goldenkoifish', 'goldenlobster', 'goldenpufferfish', 'goldenmantaray', 'goldenturtle', 'goldensquid', 'goldenshark', 'goldenaxolotl'
    ]

    return (
        
        {'holoCoins': 9999999999, 'randomMoneyKey': 0, 'fishSand':9999999999, 'tears':[[name, 1000000] for name in tears]},                                              
        {'unlockedItems': items, 'unlockedWeapons': weapons, 'seenCollabs':collabs}, 
        {'achievements':{name:achievements_format for name in achievements}},
        {'characters': [[name, 30] for name in characters], 'unlockedOutfits':outfits, 'fandomEXP':[[name, 100] for name in characters]},
        {'unlockedStages':stage, 'timeModeUnlocked':True},
        {
            'food': 5, 'growth': 1, 'specUnlock': 1, 'haste': 5, 'mobUp': 5, 'ATK': 10, 'stamps': 1, 'regen': 5,
            'specCDR': 5, 'enhanceUp': 5, 'EXP': 5, 'moneyGain': 10, 'reroll': 10, 'enchantments': 1, 'fandom': 1, 'eliminate': 10,
            'pickupRange': 10, 'DR': 5, 'SPD': 10, 'HP': 10.0, 'crit': 5.,'growth':3.,'skillDamage':10
        },
        {'unlockedFurniture':furniture,'rodUnlock': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],},
        {'inventory':[[name, 9999, 9999] for name in inventory]}
      
    )
    

def load_data():
    return (
        main_info(),
        LV_info(),
        save_editor_info()
    )
        
        
        
        
    