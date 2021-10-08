class Item():
    def __init__(self, name: str, gold_value: int, modifications: dict, equip_slot: str):
        """Generic Item"""
        self.name = name
        self.gold_value = gold_value

        self.attribte_modifications = modifications
        self.equip_slot = equip_slot