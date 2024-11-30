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

    ui_texts.setdefault('group_names', [[] for _ in ui_texts['group_titles']])
    dynamic_data = {}
    static_data = {}
    create_parameter('鎖血無敵(S1)', 99999.0, 0x3470, 0x1C20, ui_texts, dynamic_data)
    create_parameter('無限技能(S1)', 99999.0, 0x3470, 0x0B60, ui_texts, dynamic_data)
    create_parameter('鎖血無敵(S3)', 99999.0, 0xF58, 0x1C20, ui_texts, dynamic_data)
    create_parameter('無限技能(S3)', 99999.0, 0xF58, 0x0B60, ui_texts, dynamic_data)
    create_parameter('鎖血無敵(S4)', 99999.0, 0xA00, 0x1C20, ui_texts, dynamic_data)
    create_parameter('無限技能(S4)', 99999.0, 0xA00, 0x0B60, ui_texts, dynamic_data)

    infinite_currency('無限Coin', static_data)
    return dynamic_data, static_data
