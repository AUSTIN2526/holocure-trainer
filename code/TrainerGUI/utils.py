# Constants
DEFAULT_OFFSETS = [0x1A0, 0x48, 0x10]
BASE_ADDRESS = 0x052CB8E0

# Translation dictionary
def get_translations():
    return {
        'Infinite Coin': {'zh_TW': '無限貨幣'},
        'Unlock Weapons': {'zh_TW': '全武器解鎖'},
        'Unlock Achievements': {'zh_TW': '全成就解鎖'},
        'Unlock Characters & Costumes': {'zh_TW': '全角色與服裝'},
        'Unlock Levels': {'zh_TW': '全關卡解鎖'},
        'Max Passive Skills': {'zh_TW': '被動技能全滿'},
        'Unlock Furniture': {'zh_TW': '全小屋家具'},
        'Infinite House Items': {'zh_TW': '無限小屋道具'},
        'Invincible': {'zh_TW': '鎖血無敵'},
        'Infinite Skills': {'zh_TW': '無限技能'},
        'Map-wide Collection': {'zh_TW': '全圖吸物'},
        'One-Hit Kill': {'zh_TW': '秒殺怪物'},
        'Ultra Attack Speed': {'zh_TW': '超高攻速'}
    }

# Translate text
def translate_text(text: str, language: str) -> str:
    translations = get_translations()
    return translations.get(text, {}).get(language, text)

# Create parameter helper function
def create_parameter(name: str, value: float, stage_offset: int, offset_suffix: int, ui_texts: dict, dynamic_data) -> None:
    offset = [stage_offset] + DEFAULT_OFFSETS + [offset_suffix, 0x00]
    ui_texts['group_names'][0].append(name)
    dynamic_data.update({name: {'value': value, 'address': BASE_ADDRESS, 'offset': offset}})

# Create a helper function for updating static_data
def update_static_data(name: str, data: dict, ui_texts: dict, static_data) -> None:
    ui_texts['group_names'][1].append(name)
    static_data.update({name: data})

# Main function to get trainer data
def get_trainer_data(ui_texts: dict, language: str) -> tuple:
    ui_texts.setdefault('group_names', [[] for _ in ui_texts['group_titles']])
    dynamic_data = {}
    static_data = {}

    # Define stages and parameters
    stages = [
        ('S1', 0x3470, 'complet'),
        ('S2', 0x395270, 'complet'),
        ('S3', 0xF58, 'complet'),
        ('S4', 0xA00, 'complet'),
        ('S1H', 0x53f098, 'complet'),
        ('S2H', 0x1716b8, 'complet'),
        ('S3H', 0xFD8, 'complet'),
        ('S4H', 0xAC2B0, 'complet')
    ]

    parameters = [
        (translate_text('Invincible', language), 99999.0, 0x1C20),
        (translate_text('Infinite Skills', language), 99999.0, 0x0B60),
        (translate_text('Map-wide Collection', language), 99999.0, 0x1B20),
        (translate_text('One-Hit Kill', language), 99999.0, 0x19A0),
        (translate_text('Ultra Attack Speed', language), 999.0, 0x1630)
    ]

    # Create parameters for each stage
    for stage, base_address, status in stages:
        if status != 'unknow':
            for name, value, offset in parameters:
                full_name = f'{name} ({stage})'
                create_parameter(full_name, value, base_address, offset, ui_texts, dynamic_data)

    # Static data definitions
    static_functions = [
        ('Infinite Coin', lambda name: {'holoCoins': 9999999999, 'randomMoneyKey': 0, 'fishSand': 9999999999, 'tears': [[name, 1000000] for name in ['myth', 'councilHope', 'gamers', 'gen0', 'gen1', 'gen2', 'id1', 'id2', 'id3']]}),
        ('Unlock Weapons', lambda name: {'unlockedItems': ['BodyPillow', 'FullMeal', 'PikiPikiPiman', 'SuccubusHorn', 'Headphones', 'UberSheep', 'HolyMilk', 'Sake', 'FaceMask', 'CreditCard', 'GorillasPaw', 'InjectionAsacoco', 'IdolCostume', 'Plushie', 'StudyGlasses', 'SuperChattoTime', 'EnergyDrink', 'Halu', 'Membership', 'GWSPill', 'ChickensFeather', 'Bandaid', 'Limiter', 'PiggyBank', 'DevilHat', 'BlacksmithsGear', 'Breastplate', 'HopeSoda', 'Shacklesss', 'Candy', 'NinjaHeadband', 'FocusShades', 'Beetle', 'LabCoat'], 'unlockedWeapons': ['PsychoAxe', 'Glowstick', 'SpiderCooking', 'Tailplug', 'BLBook', 'EliteLava', 'HoloBomb', 'HoloLaser', 'CuttingBoard', 'IdolSong', 'CEOTears', 'WamyWater', 'XPotato', 'BounceBall', 'ENCurse', 'Sausage'], 'seenCollabs': ['BreatheInAsacoco', 'DragonBeam', 'EliteCooking', 'FlatBoard', 'MiComet', 'BLLover', 'LightBeam', 'IdolConcert', 'StreamOfTears', 'MariLamy', 'BrokenDreams', 'RapDog', 'BoneBros', 'RingOfFitness', 'MiKorone', 'SnowSake', 'ImDie', 'AbsoluteWall', 'EldritchHorror', 'StarHalberd', 'CurseBall', 'KanaCoco', 'LegendarySausage', 'Jingisukan', 'LightningWeiner', 'SnowQueen', 'IdolLive']}),
        ('Unlock Achievements', lambda name: {'achievements': {ach: {'flags': {}, 'unlocked': 'True'} for ach in ['haatoClear', 'azkiGachikoi', 'hardcoreGamer', 'suiseiClear', 'kiaraClear', 'lv50', 'zeta10', 'ollieGachikoi', 'speedrunner', 'iofiGachikoi', 'soloBeater', 'reineGachikoi', 'rhythmmaster', 'okayuClear', '2hard', '3hard', 'huh', 'mumeiClear', 'fullyLoaded', 'irysGachikoi', 'shionClear', '1hard', 'mikoClear', 'melClear', 'dontFail', 'subaruClear', 'safeISwear', 'powerLevelling', 'boing', '10000damage', 'robocoGachikoi', 'kroniiClear', 'obliterated', 'risuClear', 'mumeiGachikoi', 'koboGachikoi', 'SCT', 'freeStickers', 'lv100', 'moonaClear', 'heyhey', 'akiGachikoi', 'thankYou', 'shinyfish', 'digin', 'ina10', 'calliClear', 'timeToUpgrade', 'hallucinated', 'matsuriClear', 'koroneClear', 'firstclear', 'millionaire', 'mikoGachikoi', 'payToWin', 'calli10', 'anyaClear', 'kaelaClear', 'koboClear', 'mioGachikoi', 'skillissue', 'shion10', 'donttouch', 'nomain', 'painPeko', 'irysClear', 'oraora', 'ollieClear', 'soraGachikoi', 'payDay', 'baeGachikoi', 'idolgroup', 'sanaClear', 'inaGachikoi', 'baeClear', 'grind', 'CEOnow', 'notTakingAnyChances', 'faunaGachikoi', 'justRNG', 'inaClear', 'bullethell', 'melGachikoi', 'shionGachikoi', 'suiseiGachikoi', 'chocoClear', 'kaelaGachikoi', 'kroniiGachikoi', 'barebones', 'wamy', 'ameClear', 'ollie10', 'iofiClear', 'faunaClear', 'fubukiGachikoi', 'idolPower', '1000damage', 'korone10', 'thirdboss', 'sana10', 'aquaClear', 'dontNeed', 'fullCollab', 'trueRNG', 'muscle', 'zetaClear', 'okayuGachikoi', 'haatoGachikoi', 'plentyoffish', 'employee', 'anyaGachikoi', 'nothoughts', 'petDog', 'howcouldyou', 'bae10', 'hammertime', 'highwayrobbery', 'delusional', 'robocoClear', 'guraClear', 'matsuriGachikoi', 'azkiClear', 'ameGachikoi', 'yagoostatue', 'lookImOnTV', 'sanaGachikoi', 'mioClear', 'aquaGachikoi', 'chocoGachikoi', 'welltrained', 'kiara10', 'ayameGachikoi', 'risuGachikoi', 'artblock', 'akiClear', 'toohalu', 'koroneGachikoi', 'fired', 'luckyDay', 'welcomehome', 'allcomplete', 'harvest', 'ayameClear', 'buyingPower', 'firstboss', '50hamburgers', 'secondboss', 'fleshWound', 'couchPotato', 'soraClear', 'calliGachikoi', 'tankclass', 'pacifist', 'reineClear', 'midboss', 'iDidIt', 'fourthboss', 'lovenature', 'kiaraGachikoi', 'subaruGachikoi', 'zetaGachikoi', 'fishfearme', 'rawstrength', 'stealfish', 'guraGachikoi', 'moonaGachikoi', 'irys10', 'fubukiClear']}}),
        ('Unlock Characters & Costumes', lambda name: {'characters': [[char, 30] for char in ['kronii', 'fubuki', 'calli', 'mel', 'suisei', 'matsuri', 'choco', 'ayame', 'haato', 'roboco', 'fauna', 'sora', 'miko', 'gura', 'sana', 'okayu', 'aki', 'irys', 'shion', 'bae', 'azki', 'kiara', 'aqua', 'ina', 'korone', 'mio',  'ame', 'subaru', 'mumei', 'reine', 'kaela', 'iofi', 'moona', 'ollie', 'risu', 'anya', 'zeta','kobo']], 'unlockedOutfits': ['default', 'ameAlt1', 'kiaraAlt1', 'inaAlt1', 'guraAlt1', 'calliAlt1', 'irysAlt1', 'baeAlt1', 'sanaAlt1', 'faunaAlt1', 'mumeiAlt1', 'kroniiAlt1', 'kurokami', 'ameAlt2', 'inaAlt2', 'guraAlt2', 'calliAlt2', 'kiaraAlt2', 'irysAlt2', 'faunaAlt2', 'kroniiAlt2', 'fubukiAlt1', 'mioAlt1', 'koroneAlt1', 'okayuAlt1', 'soraAlt1', 'azkiAlt1', 'robocoAlt1', 'suiseiAlt1', 'mikoAlt1', 'inaAlt3', 'ameAlt3', 'guraAlt3', 'kiaraAlt3', 'calliAlt3', 'mumeiAlt2', 'irysAlt3', 'baeAlt2', 'okayuAlt2', 'fubukiAlt2', 'mioAlt2', 'koroneAlt2', 'suiseiAlt2', 'soraAlt2', 'azkiAlt2', 'mikoAlt2', 'robocoAlt2', 'haatoAlt1', 'melAlt1', 'matsuriAlt1', 'akiAlt1', 'subaruAlt1', 'chocoAlt1', 'shionAlt1', 'ayameAlt1', 'aquaAlt1'], 'fandomEXP': [[char, 100] for char in ['kronii', 'fubuki', 'calli', 'mel', 'suisei', 'matsuri', 'choco', 'ayame', 'haato', 'roboco', 'fauna', 'sora', 'miko', 'gura', 'sana', 'okayu', 'aki', 'irys', 'shion', 'bae', 'azki', 'kiara', 'aqua', 'ina', 'korone', 'mio',  'ame', 'subaru', 'mumei', 'reine', 'kaela', 'iofi', 'moona', 'ollie', 'risu', 'anya', 'zeta','kobo']]}),
        ('Unlock Levels', lambda name: {'unlockedStages': ['STAGE 1', 'STAGE 2', 'STAGE 1 (HARD)', 'STAGE 3', 'STAGE 2 (HARD)', 'TIME STAGE 1', 'STAGE 4', 'STAGE 3 (HARD)', 'HOLO HOUSE', 'STAGE 4 (HARD)'], 'timeModeUnlocked': True}),
        ('Max Passive Skills', lambda name: {'food': 5, 'growth': 1, 'specUnlock': 1, 'haste': 5, 'mobUp': 5, 'ATK': 10, 'stamps': 1, 'regen': 5, 'specCDR': 5, 'enhanceUp': 5, 'EXP': 5, 'moneyGain': 10, 'reroll': 10, 'enchantments': 1, 'fandom': 1, 'eliminate': 10, 'pickupRange': 10, 'DR': 5, 'SPD': 10, 'HP': 10.0, 'crit': 5., 'growth': 3., 'skillDamage': 10}),
        ('Unlock Furniture', lambda name: {'unlockedFurniture': ['bodypillow', 'vanity', 'gamerchairH', 'gamerchairg', 'gamerchairf', 'gamerchaire', 'gamerchaird', 'gamerchairc', 'gamerchairb', 'gamerchaira', 'officechair', 'beanbag', 'marblelaptopdesk', 'marbledesk', 'woodenPCdesk', 'woodendesk', 'woodenDresserA', 'nightstandB', 'nightstandA', 'futon', 'marblebed', 'woodenBedD', 'woodenBedC', 'woodenBedB', 'woodenBed', 'couchA', 'foxburger', 'woodentable', 'marbletable', 'glasstable', 'easterntable', 'floorcushion', 'woodentallcabinet', 'standinglampA', 'fireplace', 'TVStand', 'crttv', 'retroconsole', 'vrset', 'woodenbookshelf', 'marblebookshelf', 'displaycase', 'woodenDiningTable', 'marbleTable', 'woodenDiningChair', 'marblechair', 'stoolA1', 'kitchenCounterA', 'Microwave', 'marbleCounter', 'marblesink', 'fridge', 'stove', 'bathstool', 'sink', 'bathtub', 'toilet', 'washingmachine', 'laundrybasket', 'woodenCrate', 'woodenbarrel', 'boxA', 'BoxB', 'TreasureChestA', 'plantpotA', 'plantpotB', 'plantpotC', 'berryplant', 'marblestump', 'dumbell', 'exerciseball', 'boxingdummy', 'vampirecoffin', 'baegemite', 'taikodrums', 'shrinebox', 'KFPbucket', 'sharkplush', 'nekoplush', 'achandoll', 'completegrass', 'woodendivider', 'marblepartition', 'easterndivider', 'woodenwall', 'woodenhalfwall', 'woodencolumn', 'marblecolumn', 'woodendoor', 'clock', 'kroniclock', 'paintingA', 'paintingC', 'paintingB', 'paintingD', 'wallmirror', 'lantern', 'hangingvine', 'mountedSword', 'demonSword', 'window', 'hardcoretrophy', 'woodenFloor', 'woodenFloor2', 'stoneFloor', 'redCarpetFloor', 'blueCarpetFloor', 'pinkCarpetFloor', 'concreteFloor', 'marbleFloor', 'tiledFloor', 'tatamiFloor', 'woodenWall', 'flatWall', 'stripedWall', 'skyWall', 'polkaWallA', 'polkaWallB', 'polkaWallC', 'oceanWall', 'modernWall', 'stoneWall', 'easternWall', 'goldenfish1', 'goldenfish2', 'goldenfish3', 'goldenfish4', 'goldenfish5', 'goldenfish6', 'goldenfish7', 'goldenfish8', 'goldenfish9', 'goldenfish10', 'goldenfish11', 'goldenfish12'], 'rodUnlock': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}),
        ('Infinite House Items', lambda name: {'inventory': [[item, 9999, 9999] for item in ['shrimp', 'clownfish', 'tuna', 'standardsoil', 'expeditedsoil', 'enhancedsoil', 'wheatSeed', 'tomatoSeed', 'potatoSeed', 'riceSeed', 'onionseed', 'carrotseed', 'greenbeansseed', 'peppersseed', 'strawberryseed', 'cornseed', 'radishseed', 'garlicseed', 'eel', 'koifish', 'lobster', 'wheat', 'tomato', 'potato', 'rice', 'peppers', 'greenbeans', 'carrot', 'onion', 'strawberry', 'corn', 'radish', 'garlic', 'pufferfish', 'mantaray', 'turtle', 'squid', 'shark', 'axolotl','goldenshrimp', 'goldenclownfish', 'goldentuna', 'goldeneel', 'goldenkoifish', 'goldenlobster', 'goldenpufferfish', 'goldenmantaray', 'goldenturtle', 'goldensquid', 'goldenshark', 'goldenaxolotl']]})
    ]

    # Update static data using helper functions
    for name, func in static_functions:
        translated_name = translate_text(name, language)
        update_static_data(translated_name, func(translated_name), ui_texts, static_data)

    return dynamic_data, static_data
