# Constants
DEFAULT_OFFSETS = [0x1A0, 0x48, 0x10]
BASE_ADDRESS = 0x052CB8E0

def get_trainer_data(ui_texts: dict) -> list:
    """
    Generate trainer data with given parameters.

    Args:
        ui_texts (dict): Contains UI-related data, including 'group_names'.

    Returns:
        list: A list of parameter dictionaries with value, address, and offset.
    """
    def create_parameter(name: str, value: float, stage_offset: int, offset_suffix: int, ui_texts: dict, dynamic_data) -> dict:
        """
        Create a parameter dictionary.

        Args:
            name (str): Name of the parameter.
            value (float): Value for the parameter.
            stage_offset (int): Stage offset for the parameter.
            offset_suffix (int): Offset suffix for the parameter.
            ui_texts (dict): UI text data to update.

        Returns:
            dict: A dictionary containing the parameter data.
        """
        offset = [stage_offset] + DEFAULT_OFFSETS + [offset_suffix, 0x00]
       
        ui_texts['group_names'][0].append(name)
        dynamic_data.update({name:{'value': value, 'address': BASE_ADDRESS, 'offset': offset}})
    
    def infinite_currency(name, static_data):  # 無限貨幣
        MAX_HOLO_COINS = 9999999999
        MAX_TEARS = 1000000
        tears = ['myth', 'councilHope', 'gamers', 'gen0', 'gen1', 'gen2', 'id1', 'id2', 'id3']
        currency_data = {'holoCoins': MAX_HOLO_COINS, 'randomMoneyKey': 0, 'fishSand': MAX_HOLO_COINS, 'tears': [[name, MAX_TEARS] for name in tears]}
        ui_texts['group_names'][1].append(name)

        static_data.update({name:currency_data})

    def unlock_all_weapons(name, static_data):  # 全武器庫解鎖
        items = ['BodyPillow', 'FullMeal', 'PikiPikiPiman', 'SuccubusHorn', 'Headphones', 'UberSheep', 'HolyMilk', 'Sake', 'FaceMask', 'CreditCard', 'GorillasPaw', 'InjectionAsacoco', 'IdolCostume', 'Plushie', 'StudyGlasses', 'SuperChattoTime', 'EnergyDrink', 'Halu', 'Membership', 'GWSPill', 'ChickensFeather', 'Bandaid', 'Limiter', 'PiggyBank', 'DevilHat', 'BlacksmithsGear', 'Breastplate', 'HopeSoda', 'Shacklesss', 'Candy', 'NinjaHeadband', 'FocusShades', 'Beetle', 'LabCoat']
        weapons = ['PsychoAxe', 'Glowstick', 'SpiderCooking', 'Tailplug', 'BLBook', 'EliteLava', 'HoloBomb', 'HoloLaser', 'CuttingBoard', 'IdolSong', 'CEOTears', 'WamyWater', 'XPotato', 'BounceBall', 'ENCurse', 'Sausage']
        collabs = ['BreatheInAsacoco', 'DragonBeam', 'EliteCooking', 'FlatBoard', 'MiComet', 'BLLover', 'LightBeam', 'IdolConcert', 'StreamOfTears', 'MariLamy', 'BrokenDreams', 'RapDog', 'BoneBros', 'RingOfFitness', 'MiKorone', 'SnowSake', 'ImDie', 'AbsoluteWall', 'EldritchHorror', 'StarHalberd', 'CurseBall', 'KanaCoco', 'LegendarySausage', 'Jingisukan', 'LightningWeiner', 'SnowQueen', 'IdolLive']
        unlocked_items = {'unlockedItems': items, 'unlockedWeapons': weapons, 'seenCollabs': collabs}
        ui_texts['group_names'][1].append(name)

        static_data.update({name:unlocked_items})
    
    def unlock_all_achievements(name, static_data):  # 全成就解鎖
        achievements = ['haatoClear', 'azkiGachikoi', 'hardcoreGamer', 'suiseiClear', 'kiaraClear', 'lv50', 'zeta10', 'ollieGachikoi', 'speedrunner', 'iofiGachikoi', 'soloBeater', 'reineGachikoi', 'rhythmmaster', 'okayuClear', '2hard', '3hard', 'huh', 'mumeiClear', 'fullyLoaded', 'irysGachikoi', 'shionClear', '1hard', 'mikoClear', 'melClear', 'dontFail', 'subaruClear', 'safeISwear', 'powerLevelling', 'boing', '10000damage', 'robocoGachikoi', 'kroniiClear', 'obliterated', 'risuClear', 'mumeiGachikoi', 'koboGachikoi', 'SCT', 'freeStickers', 'lv100', 'moonaClear', 'heyhey', 'akiGachikoi', 'thankYou', 'shinyfish', 'digin', 'ina10', 'calliClear', 'timeToUpgrade', 'hallucinated', 'matsuriClear', 'koroneClear', 'firstclear', 'millionaire', 'mikoGachikoi', 'payToWin', 'calli10', 'anyaClear', 'kaelaClear', 'koboClear', 'mioGachikoi', 'skillissue', 'shion10', 'donttouch', 'nomain', 'painPeko', 'irysClear', 'oraora', 'ollieClear', 'soraGachikoi', 'payDay', 'baeGachikoi', 'idolgroup', 'sanaClear', 'inaGachikoi', 'baeClear', 'grind', 'CEOnow', 'notTakingAnyChances', 'faunaGachikoi', 'justRNG', 'inaClear', 'bullethell', 'melGachikoi', 'shionGachikoi', 'suiseiGachikoi', 'chocoClear', 'kaelaGachikoi', 'kroniiGachikoi', 'barebones', 'wamy', 'ameClear', 'ollie10', 'iofiClear', 'faunaClear', 'fubukiGachikoi', 'idolPower', '1000damage', 'korone10', 'thirdboss', 'sana10', 'aquaClear', 'dontNeed', 'fullCollab', 'trueRNG', 'muscle', 'zetaClear', 'okayuGachikoi', 'haatoGachikoi', 'plentyoffish', 'employee', 'anyaGachikoi', 'nothoughts', 'petDog', 'howcouldyou', 'bae10', 'hammertime', 'highwayrobbery', 'delusional', 'robocoClear', 'guraClear', 'matsuriGachikoi', 'azkiClear', 'ameGachikoi', 'yagoostatue', 'lookImOnTV', 'sanaGachikoi', 'mioClear', 'aquaGachikoi', 'chocoGachikoi', 'welltrained', 'kiara10', 'ayameGachikoi', 'risuGachikoi', 'artblock', 'akiClear', 'toohalu', 'koroneGachikoi', 'fired', 'luckyDay', 'welcomehome', 'allcomplete', 'harvest', 'ayameClear', 'buyingPower', 'firstboss', '50hamburgers', 'secondboss', 'fleshWound', 'couchPotato', 'soraClear', 'calliGachikoi', 'tankclass', 'pacifist', 'reineClear', 'midboss', 'iDidIt', 'fourthboss', 'lovenature', 'kiaraGachikoi', 'subaruGachikoi', 'zetaGachikoi', 'fishfearme', 'rawstrength', 'stealfish', 'guraGachikoi', 'moonaGachikoi', 'irys10', 'fubukiClear']
        achievements_data = {'achievements': {name: {'flags': {}, 'unlocked': 'True'} for name in achievements}}
        ui_texts['group_names'][1].append(name)
        static_data.update({name:achievements_data})

    def unlock_all_characters_and_costumes(name, static_data):  # 全角色與服裝
        outfits = ['default', 'ameAlt1', 'kiaraAlt1', 'inaAlt1', 'guraAlt1', 'calliAlt1', 'irysAlt1', 'baeAlt1', 'sanaAlt1', 'faunaAlt1', 'mumeiAlt1', 'kroniiAlt1', 'kurokami', 'ameAlt2', 'inaAlt2', 'guraAlt2', 'calliAlt2', 'kiaraAlt2', 'irysAlt2', 'faunaAlt2', 'kroniiAlt2', 'fubukiAlt1', 'mioAlt1', 'koroneAlt1', 'okayuAlt1', 'soraAlt1', 'azkiAlt1', 'robocoAlt1', 'suiseiAlt1', 'mikoAlt1', 'inaAlt3', 'ameAlt3', 'guraAlt3', 'kiaraAlt3', 'calliAlt3', 'mumeiAlt2', 'irysAlt3', 'baeAlt2', 'okayuAlt2', 'fubukiAlt2', 'mioAlt2', 'koroneAlt2', 'suiseiAlt2', 'soraAlt2', 'azkiAlt2', 'mikoAlt2', 'robocoAlt2', 'haatoAlt1', 'melAlt1', 'matsuriAlt1', 'akiAlt1', 'subaruAlt1', 'chocoAlt1', 'shionAlt1', 'ayameAlt1', 'aquaAlt1']
        characters = ['kronii', 'fubuki', 'calli', 'mel', 'suisei', 'matsuri', 'choco', 'ayame', 'haato', 'roboco', 'fauna', 'sora', 'miko', 'gura', 'sana', 'okayu', 'aki', 'irys', 'shion', 'bae', 'azki', 'kiara', 'aqua', 'ina', 'korone', 'mio',  'ame', 'subaru', 'mumei', 'reine', 'kaela', 'iofi', 'moona', 'ollie', 'risu', 'anya', 'zeta','kobo']
        
        characters_data = {
            'characters': [[name, 30] for name in characters],
            'unlockedOutfits': outfits,
            'fandomEXP': [[name, 100] for name in characters],
        }
        ui_texts['group_names'][1].append(name)
        static_data.update({name:characters_data})

    def unlock_all_levels(name, static_data):  # 全關卡解鎖
        stage = ['STAGE 1', 'STAGE 2', 'STAGE 1 (HARD)', 'STAGE 3', 'STAGE 2 (HARD)', 'TIME STAGE 1', 'STAGE 4', 'STAGE 3 (HARD)', 'HOLO HOUSE']
        stages_data = {'unlockedStages': stage, 'timeModeUnlocked': True}
        ui_texts['group_names'][1].append(name)
        static_data.update({name:stages_data})
        
    def max_passive_skills(name, static_data):  # 被動技能全滿
        buffs_data = {
            'food': 5, 'growth': 1, 'specUnlock': 1, 'haste': 5, 'mobUp': 5, 'ATK': 10, 'stamps': 1, 'regen': 5,
            'specCDR': 5, 'enhanceUp': 5, 'EXP': 5, 'moneyGain': 10, 'reroll': 10, 'enchantments': 1, 'fandom': 1, 'eliminate': 10,
            'pickupRange': 10, 'DR': 5, 'SPD': 10, 'HP': 10.0, 'crit': 5., 'growth': 3., 'skillDamage': 10
        }
        ui_texts['group_names'][1].append(name)
        static_data.update({name:buffs_data})
        
    def unlock_all_furniture(name, static_data):  # 全小屋家具
        furniture = ['bodypillow', 'vanity', 'gamerchairH', 'gamerchairg', 'gamerchairf', 'gamerchaire', 'gamerchaird', 'gamerchairc', 'gamerchairb', 'gamerchaira', 'officechair', 'beanbag', 'marblelaptopdesk', 'marbledesk', 'woodenPCdesk', 'woodendesk', 'woodenDresserA', 'nightstandB', 'nightstandA', 'futon', 'marblebed', 'woodenBedD', 'woodenBedC', 'woodenBedB', 'woodenBed', 'couchA', 'foxburger', 'woodentable', 'marbletable', 'glasstable', 'easterntable', 'floorcushion', 'woodentallcabinet', 'standinglampA', 'fireplace', 'TVStand', 'crttv', 'retroconsole', 'vrset', 'woodenbookshelf', 'marblebookshelf', 'displaycase', 'woodenDiningTable', 'marbleTable', 'woodenDiningChair', 'marblechair', 'stoolA1', 'kitchenCounterA', 'Microwave', 'marbleCounter', 'marblesink', 'fridge', 'stove', 'bathstool', 'sink', 'bathtub', 'toilet', 'washingmachine', 'laundrybasket', 'woodenCrate', 'woodenbarrel', 'boxA', 'BoxB', 'TreasureChestA', 'plantpotA', 'plantpotB', 'plantpotC', 'berryplant', 'marblestump', 'dumbell', 'exerciseball', 'boxingdummy', 'vampirecoffin', 'baegemite', 'taikodrums', 'shrinebox', 'KFPbucket', 'sharkplush', 'nekoplush', 'achandoll', 'completegrass', 'woodendivider', 'marblepartition', 'easterndivider', 'woodenwall', 'woodenhalfwall', 'woodencolumn', 'marblecolumn', 'woodendoor', 'clock', 'kroniclock', 'paintingA', 'paintingC', 'paintingB', 'paintingD', 'wallmirror', 'lantern', 'hangingvine', 'mountedSword', 'demonSword', 'window', 'hardcoretrophy', 'woodenFloor', 'woodenFloor2', 'stoneFloor', 'redCarpetFloor', 'blueCarpetFloor', 'pinkCarpetFloor', 'concreteFloor', 'marbleFloor', 'tiledFloor', 'tatamiFloor', 'woodenWall', 'flatWall', 'stripedWall', 'skyWall', 'polkaWallA', 'polkaWallB', 'polkaWallC', 'oceanWall', 'modernWall', 'stoneWall', 'easternWall', 'goldenfish1', 'goldenfish2', 'goldenfish3', 'goldenfish4', 'goldenfish5', 'goldenfish6', 'goldenfish7', 'goldenfish8', 'goldenfish9', 'goldenfish10', 'goldenfish11', 'goldenfish12']
        furniture_data = {'unlockedFurniture': furniture, 'rodUnlock': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}
        ui_texts['group_names'][1].append(name)
        static_data.update({name:furniture_data})

    def infinite_house_items(name, static_data):  # 無限小屋道具
        inventory = ['shrimp', 'clownfish', 'tuna', 'standardsoil', 'expeditedsoil', 'enhancedsoil', 'wheatSeed', 'tomatoSeed', 'potatoSeed', 'riceSeed', 'onionseed', 'carrotseed', 'greenbeansseed', 'peppersseed', 'strawberryseed', 'cornseed', 'radishseed', 'garlicseed', 'eel', 'koifish', 'lobster', 'wheat', 'tomato', 'potato', 'rice', 'peppers', 'greenbeans', 'carrot', 'onion', 'strawberry', 'corn', 'radish', 'garlic', 'pufferfish', 'mantaray', 'turtle', 'squid', 'shark', 'axolotl','goldenshrimp', 'goldenclownfish', 'goldentuna', 'goldeneel', 'goldenkoifish', 'goldenlobster', 'goldenpufferfish', 'goldenmantaray', 'goldenturtle', 'goldensquid', 'goldenshark', 'goldenaxolotl']
        inventory_data = {'inventory': [[name, 9999, 9999] for name in inventory]}
        ui_texts['group_names'][1].append(name)
        static_data.update({name:inventory_data})

    ui_texts.setdefault('group_names', [[] for _ in ui_texts['group_titles']])
    dynamic_data = {}
    static_data = {}
    create_parameter('鎖血無敵(S1)', 99999.0, 0x3470, 0x1C20, ui_texts, dynamic_data)
    create_parameter('無限技能(S1)', 99999.0, 0x3470, 0x0B60, ui_texts, dynamic_data)
    create_parameter('全圖吸物(S1)', 99999.0, 0x3470, 0x1B20, ui_texts, dynamic_data)
    create_parameter('秒殺怪物(S1)', 99999.0, 0x3470, 0x19A0, ui_texts, dynamic_data)
    create_parameter('超高攻速(S1)', 999.0, 0x3470, 0x1630, ui_texts, dynamic_data)

    create_parameter('鎖血無敵(S3)', 99999.0, 0xF58, 0x1C20, ui_texts, dynamic_data)
    create_parameter('無限技能(S3)', 99999.0, 0xF58, 0x0B60, ui_texts, dynamic_data)
    create_parameter('全圖吸物(S3)', 99999.0, 0xF58, 0x1B20, ui_texts, dynamic_data)
    create_parameter('秒殺怪物(S3)', 99999.0, 0xF58, 0x19A0, ui_texts, dynamic_data)
    create_parameter('超高攻速(S3)', 999.0, 0xF58, 0x1630, ui_texts, dynamic_data)

    create_parameter('鎖血無敵(S4)', 99999.0, 0xA00, 0x1C20, ui_texts, dynamic_data)
    create_parameter('無限技能(S4)', 99999.0, 0xA00, 0x0B60, ui_texts, dynamic_data)
    create_parameter('全圖吸物(S4)', 99999.0, 0xA00, 0x1B20, ui_texts, dynamic_data)
    create_parameter('秒殺怪物(S4)', 99999.0, 0xA00, 0x19A0, ui_texts, dynamic_data)
    create_parameter('超高攻速(S4)', 999.0, 0xA00, 0x1630, ui_texts, dynamic_data)



    infinite_currency('無限Coin', static_data)
    unlock_all_weapons('全武器解鎖', static_data)
    unlock_all_achievements('全成就解鎖', static_data)
    unlock_all_characters_and_costumes('全角色與服裝', static_data)
    unlock_all_levels('全關卡解鎖', static_data)
    max_passive_skills('被動技能全滿', static_data)
    unlock_all_furniture('全小屋家具', static_data)
    infinite_house_items('無限小屋道具', static_data)
    return dynamic_data, static_data    
