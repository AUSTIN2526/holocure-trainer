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
        ('S2', 0x395270, 'Fail'),
        ('S3', 0xF58, 'complet'),
        ('S4', 0xA00, 'complet'),
        ('S1H', 0x53f098, 'Fail'),
        ('S2H', 0x1716b8, 'Fail'),
        ('S3H', 0xFD8, 'complet'),
        ('S4H', 0xAC2B0, 'Fail')
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
        if status != 'Fail':
            for name, value, offset in parameters:
                full_name = f'{name} ({stage})'
                create_parameter(full_name, value, base_address, offset, ui_texts, dynamic_data)

    # Static data definitions
    static_functions = [
    # Infinite Coin
    ('Infinite Coin', lambda name: {
        'holoCoins': 9999999999,
        'randomMoneyKey': 0,
        'fishSand': 9999999999,
        'holoChips': 9999999999,
        'tears': [[group, 1000000] for group in ['myth', 'councilHope', 'gamers', 'gen0', 'gen1', 'gen2', 'id1', 'id2', 'id3', 'gen3', 'gen4']]
    }),

    # Unlock Weapons
    ('Unlock Weapons', lambda name: {
        'unlockedItems': ['BodyPillow', 'FullMeal', 'PikiPikiPiman', 'SuccubusHorn', 'Headphones', 'UberSheep', 'HolyMilk', 'Sake', 'FaceMask', 'CreditCard', 'SuperChattoTime', 'IdolCostume', 'BlacksmithsGear', 'Breastplate', 'StudyGlasses', 'GorillasPaw', 'Halu', 'InjectionAsacoco', 'Membership', 'PiggyBank', 'Bandaid', 'ChickensFeather', 'EnergyDrink', 'GWSPill', 'Plushie', 'DevilHat', 'Limiter', 'NinjaHeadband', 'FocusShades', 'Candy', 'Beetle', 'Shacklesss', 'HopeSoda', 'LabCoat', 'PromiseTiara', 'RavenFeather', 'CorporationPin'],
        'unlockedWeapons': ['PsychoAxe', 'Glowstick', 'SpiderCooking', 'Tailplug', 'BLBook', 'EliteLava', 'HoloBomb', 'HoloLaser', 'WamyWater', 'CEOTears', 'CuttingBoard', 'BounceBall', 'ENCurse', 'IdolSong', 'XPotato', 'Sausage', 'OwlDagger'],
        'seenCollabs': ['BLLover', 'BreatheInAsacoco', 'BrokenDreams', 'EliteCooking', 'SnowSake', 'SnowQueen', 'DragonBeam', 'KanaCoco', 'LightBeam', 'MiComet', 'RingOfFitness', 'BoneBros', 'AbsoluteWall', 'BLFujoshi', 'CurseBall', 'DragonFire', 'EldritchHorror', 'IdolConcert', 'LegendarySausage', 'MiKorone', 'RapDog', 'SnowFlowerSake', 'StreamOfTears', 'ImDie', 'Jingisukan', 'HolyFire', 'IdolLive', 'FlatBoard', 'LightningWeiner', 'StarHalberd', 'MariLamy', 'BlackPlague', 'InfiniteBL', 'BloodLust']
    }),

    # Unlock Achievements
    ('Unlock Achievements', lambda name: {
        'achievements': {
            ach: {'flags': {}, 'unlocked': 1.0}
            for ach in ['irysGachikoi', 'allcomplete', 'justRNG', 'robocoClear', 'guraClear', 'suiseiClear', 'shinyfish', 'mumeiGachikoi', 'haatoClear', 'trueRNG', 'firstboss', 'mumeiClear', 'thankYou', 'akiClear', 'stealfish', 'inaGachikoi', 'hardcoreGamer', 'secondboss', 'huh', 'bae10', 'robocoGachikoi', 'sana10', 'ameClear', 'iDidIt', 'shionGachikoi', 'painPeko', 'ameGachikoi', 'guraGachikoi', 'matsuriGachikoi', 'sanaGachikoi', '2hard', 'idolPower', '1000damage', 'SCT', 'nothoughts', 'faunaClear', 'reineGachikoi', 'bullethell', 'inaClear', 'welcomehome', 'hallucinated', 'suiseiGachikoi', 'harvest', 'lookImOnTV', 'freeStickers', 'artblock', 'payDay', 'rhythmmaster', 'calliClear', 'moonaGachikoi', 'koroneClear', 'idolgroup', 'moonaClear', 'lv100', 'mikoGachikoi', 'safeISwear', 'chocoClear', 'baeClear', 'risuGachikoi', 'buyingPower', 'subaruGachikoi', 'couchPotato', 'digin', 'anyaGachikoi', 'skillissue', '50hamburgers', 'tankclass', 'fubukiGachikoi', 'notTakingAnyChances', 'mioClear', 'wamy', 'koboGachikoi', 'speedrunner', 'kaelaClear', 'boing', 'obliterated', 'petDog', 'howcouldyou', 'irys10', 'welltrained', 'dontNeed', 'faunaGachikoi', 'koroneGachikoi', 'melGachikoi', 'yagoostatue', 'oraora', 'shionClear', 'calli10', 'ollie10', 'rawstrength', 'soraClear', 'midboss', 'koboClear', 'aquaGachikoi', 'delusional', 'timeToUpgrade', 'risuClear', 'kaelaGachikoi', 'payToWin', 'subaruClear', 'heyhey', 'akiGachikoi', 'soraGachikoi', 'ayameClear', 'luckyDay', 'iofiClear', 'fubukiClear', 'kiaraGachikoi', 'matsuriClear', 'soloBeater', 'azkiClear', 'zeta10', 'lv50', 'millionaire', '3hard', 'ayameGachikoi', 'fourthboss', 'anyaClear', 'haatoGachikoi', 'barebones', 'donttouch', 'melClear', 'mioGachikoi', 'aquaClear', 'fishfearme', 'powerLevelling', 'fired', '1hard', 'nomain', 'fullCollab', 'thirdboss', 'dontFail', 'azkiGachikoi', 'plentyoffish', 'fleshWound', 'baeGachikoi', 'reineClear', 'kiara10', 'lovenature', 'kiaraClear', 'korone10', 'hammertime', 'okayuGachikoi', 'toohalu', 'watameClear', 'gambling', 'zenLoss', 'noelClear', 'scammed', 'stampHunting', 'watameGachikoi', 'legalRight', 'queen', 'CEOnow', 'lunaClear', 'fifthboss', 'jackpot', 'pekoraClear', '4hard', 'marineGachikoi', 'pekoraGachikoi', 'lunaGachikoi', 'cocoGachikoi', 'companion', 'operations', 'findLetters', 'flareGachikoi', 'oneMore', 'kanataGachikoi', 'cocoClear', 'towaClear', 'bigger', 'flareClear', 'towaGachikoi', 'kanataClear', 'faster', 'marineClear', 'noelGachikoi', 'zetaGachikoi', 'employee', 'muscle', 'ina10', '10000damage', 'ollieGachikoi', 'mikoClear', 'irysClear', 'grind', 'zetaClear', 'chocoGachikoi', 'okayuClear', 'fullyLoaded', 'pacifist', 'sanaClear', 'shion10', 'iofiGachikoi', 'calliGachikoi', 'kroniiClear', 'highwayrobbery', 'firstclear', 'kroniiGachikoi', 'ollieClear']
        },
        'fanletters': ['Kobokerz', 'Zecretary', 'Udin', 'Zomrade', 'Moonafic', 'Shiokko', 'Nakirigumi', 'FubuChun', 'Oruyanke', 'Miteiru', 'Kintoki', 'Robosa', 'Hoshiyomi', 'Miofa', 'Yatagarasu', 'Kenzoku', 'Tatsunoko', 'GuyRys', 'Hoomans', 'Brats', 'SmollAme', 'CursedBubba', 'SSRB', 'Sanalites', 'Kronies', 'KFP', 'Nodoka', 'Area15', 'Heimin', 'Pemaloe', 'Bazo', 'Cilus', 'Merakyat', 'Melfriend', 'Risuner', 'Aquacrew', 'Chocomate', 'Subatomo', 'Rosetai', 'Kapumin', 'Achan', 'Sukonbu', 'DeadbeatQ', 'Takodachi', 'Saplings', 'Haaton', 'Matsurisu', 'Pioneer', 'Soratomo', 'BloomGloom', 'Deadbeat', 'Moonabito', 'Spiderchama', 'Shrimp', 'Ioforia', 'Riscot', 'Watamate', 'Nousagi', 'Ichimi', 'ShiroganeKnight', 'Elfriend', 'Otaku', 'Nanoraaa', 'Fubuzilla', 'HalloweenBae', 'Mikodanye', 'Shubangelion', 'Teamate', 'ShrimpQ', 'HalloweenMyth', 'ObakeChan', 'Mikopi', 'Staff', 'GoriEla', 'Pekodam', 'Onigiriya', 'Koronesuki', 'Upao', 'Luknight', 'Chocolat', 'Irystocrats', 'Payoyo']
    }),

    # Unlock Characters & Costumes
    ('Unlock Characters & Costumes', lambda name: {
        'characters': [[char, 30] for char in ['kronii', 'fubuki', 'calli', 'mel', 'kobo', 'suisei', 'matsuri', 'choco', 'ayame', 'haato', 'random', 'reine', 'none', 'roboco', 'fauna', 'sora', 'miko', 'empty', 'gura', 'sana', 'okayu', 'aki', 'irys', 'kaela', 'shion', 'bae', 'azki', 'kiara', 'aqua', 'ina', 'iofi', 'korone', 'moona', 'ollie', 'mio', 'ame', 'subaru', 'mumei', 'risu', 'anya', 'zeta', 'flare', 'luna', 'pekora', 'kanata', 'watame', 'noel', 'marine', 'coco', 'towa']],
        'unlockedOutfits': ['default', 'ameAlt3', 'ameAlt1', 'ameAlt2', 'inaAlt1', 'inaAlt2', 'inaAlt3', 'guraAlt1', 'guraAlt2', 'guraAlt3', 'calliAlt1', 'calliAlt2', 'calliAlt3', 'kiaraAlt1', 'kiaraAlt2', 'kiaraAlt3', 'sanaAlt1', 'faunaAlt2', 'irysAlt2', 'okayuAlt1', 'mioAlt2', 'koroneAlt1', 'mikoAlt2', 'robocoAlt2', 'haatoAlt1', 'matsuriAlt1', 'akiAlt1', 'shionAlt1', 'ayameAlt1', 'chocoAlt1', 'subaruAlt1', 'irysAlt3', 'irysAlt1', 'baeAlt1', 'baeAlt2', 'faunaAlt1', 'mumeiAlt1', 'mumeiAlt2', 'kroniiAlt2', 'kroniiAlt1', 'kurokami', 'fubukiAlt1', 'fubukiAlt2', 'mioAlt1', 'koroneAlt2', 'okayuAlt2', 'soraAlt1', 'soraAlt2', 'azkiAlt1', 'azkiAlt2', 'robocoAlt1', 'suiseiAlt1', 'suiseiAlt2', 'mikoAlt1', 'melAlt1', 'aquaAlt1', 'marineAlt1', 'noelAlt1', 'pekoraAlt1', 'lunaAlt1', 'watameAlt1', 'cocoAlt1', 'kanataAlt1', 'towaAlt1', 'flareAlt1'],
        'fandomEXP': [[char, 100] for char in ['kronii', 'fubuki', 'calli', 'mel', 'kobo', 'suisei', 'matsuri', 'choco', 'ayame', 'haato', 'reine', 'none', 'roboco', 'fauna', 'sora', 'miko', 'gura', 'sana', 'okayu', 'aki', 'irys', 'kaela', 'shion', 'bae', 'azki', 'kiara', 'aqua', 'ina', 'iofi', 'korone', 'moona', 'ollie', 'mio', 'ame', 'subaru', 'mumei', 'risu', 'anya', 'zeta', 'flare', 'luna', 'pekora', 'kanata', 'watame', 'noel', 'marine', 'coco', 'towa']]
    }),

# Unlock Levels
('Unlock Levels', lambda name: {
    'unlockedStages': ['STAGE 1', 'HOLO HOUSE', 'STAGE 2', 'STAGE 3', 'STAGE 4', 'STAGE 1 (HARD)', 'STAGE 2 (HARD)', 'STAGE 3 (HARD)', 'TIME STAGE 1', 'TIME STAGE 2', 'TIME STAGE 3', 'TIME STAGE 4', 'TIME STAGE 5', 'STAGE 5', 'STAGE 4 (HARD)', 'STAGE 5 (HARD)', 'USADA CASINO'],
    'timeModeUnlocked': True
}),

    # Max Passive Skills
    ('Max Passive Skills', lambda name: {
      "selectedArmor": 5.0,
      "skillDamage": 10.0,
      "food": 5.0,
      "growth": 3.0,
      "usingAxe": 8.0,
      "woodLevel": 10.0,
      "specUnlock": 1.0,
      "GROff": 0.0,
      "haste": 5.0,
      "canDisable": 1.0,
      "mobUp": 5.0,
      "materialDrops": 1.0,
      "usingPick": 8.0,
      "moneyGain": 10.0,
      "reroll": 10.0,
      "regen": 5.0,
      "specCDR": 5.0,
      "enhanceUp": 5.0,
      "mineLevel": 10.0,
      "EXP": 5.0,
      "fandom": 1.0,
      "itemLimit": 0.0,
      "weaponLimit": 0.0,
      "pickUnlock": 1.0,
      "DR": 5.0,
      "SPD": 10.0,
      "crit": 5.0,
      "HP": 10.0,
      "manageLevel": 4.0,
      "towerFalls": 1.0,
      "ATK": 10,
      "stamps": 1,
      "enchantments": 1,
      "eliminate": 10,
      "pickupRange": 10,
      'supports': 1.0,
      'fanLetterUnlock': 1.0,
    }),


    # Unlock Furniture
    ('Unlock Furniture', lambda name: {
        'unlockedFurniture': ['tatamiFloor', 'oceanWall', 'tiledFloor', 'pinkCarpetFloor', 'concreteFloor', 'marbleFloor', 'easternWall', 'stoneWall', 'modernWall', 'polkaWallC', 'polkaWallB', 'polkaWallA', 'skyWall', 'stripedWall', 'flatWall', 'woodenWall', 'blueCarpetFloor', 'redCarpetFloor', 'stoneFloor', 'woodenFloor2', 'woodenFloor', 'window', 'demonSword', 'mountedSword', 'hangingvine', 'lantern', 'wallmirror', 'paintingD', 'paintingB', 'paintingC', 'paintingA', 'kroniclock', 'clock', 'woodendoor', 'marblecolumn', 'woodencolumn', 'woodenhalfwall', 'woodenwall', 'easterndivider', 'marblepartition', 'woodendivider', 'nekoplush', 'sharkplush', 'KFPbucket', 'shrinebox', 'taikodrums', 'baegemite', 'vampirecoffin', 'boxingdummy', 'exerciseball', 'dumbell', 'berryplant', 'plantpotC', 'plantpotB', 'plantpotA', 'TreasureChestA', 'marblestump', 'BoxB', 'boxA', 'woodenbarrel', 'woodenCrate', 'laundrybasket', 'washingmachine', 'toilet', 'bathtub', 'sink', 'bathstool', 'woodenDiningTable', 'marbleTable', 'woodenDiningChair', 'marblechair', 'stoolA1', 'kitchenCounterA', 'Microwave', 'marbleCounter', 'marblesink', 'fridge', 'stove', 'marblebookshelf', 'woodenbookshelf', 'vrset', 'retroconsole', 'crttv', 'TVStand', 'fireplace', 'standinglampA', 'woodentallcabinet', 'floorcushion', 'easterntable', 'glasstable', 'marbletable', 'woodentable', 'foxburger', 'couchA', 'bodypillow', 'vanity', 'gamerchairH', 'gamerchairg', 'gamerchairf', 'gamerchaire', 'gamerchaird', 'gamerchairc', 'gamerchairb', 'gamerchaira', 'officechair', 'beanbag', 'marblelaptopdesk', 'marbledesk', 'woodenPCdesk', 'woodendesk', 'woodenDresserA', 'nightstandB', 'nightstandA', 'futon', 'marblebed', 'woodenBedD', 'woodenBedC', 'woodenBedB', 'woodenBed', 'displaycase', 'completegrass', 'achandoll', 'hardcoretrophy'],
        'rodUnlock': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    }),

    # Infinite House Items
    ('Infinite House Items', lambda name: {
        'inventory': [[item, 9999, 9999] for item in ['shrimp', 'turtle', 'tuna', 'standardsoil', 'expeditedsoil', 'enhancedsoil', 'wheatSeed', 'tomatoSeed', 'potatoSeed', 'riceSeed', 'onionseed', 'carrotseed', 'greenbeansseed', 'peppersseed', 'strawberryseed', 'cornseed', 'radishseed', 'garlicseed', 'clownfish', 'lobster', 'eel', 'squid', 'mantaray', 'shark', 'koifish', 'pufferfish', 'wheat', 'tomato', 'potato', 'rice', 'onion', 'carrot', 'greenbeans', 'peppers', 'strawberry', 'corn', 'radish', 'garlic', 'stick', 'stone', 'leadbar', 'hardwood', 'plank', 'ironbar', 'cedarwood', 'mythrilbar', 'maplewood', 'diamond', 'acaciawood', 'adamantitebar', 'teakwood', 'bamboowood', 'hololite', 'platinumbar', 'axolotl']]
    })
]


    # Update static data using helper functions
    for name, func in static_functions:
        translated_name = translate_text(name, language)
        update_static_data(translated_name, func(translated_name), ui_texts, static_data)

    return dynamic_data, static_data
