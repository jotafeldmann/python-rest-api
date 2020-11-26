from dataclasses import dataclass
from typing import Dict, List

from .utils import remove_empty_items

List_of_types_str = List[str]
Types = Dict[str, bool]


@dataclass
class Pokemon:
    name: str
    types: Types
    total: int
    hp: int
    attack: int
    defense: int
    speed_attack: int
    speed_defense: int
    speed: int
    generation: int
    legendary: bool

    @staticmethod
    def from_list_to_dict(list_types: List_of_types_str) -> Types:
        types = {}
        for t in remove_empty_items(list_types):
            types[t] = True

        return types

    def __init__(self,
                 name: str,
                 types: List_of_types_str,
                 total: int,
                 hp: int,
                 attack: int,
                 defense: int,
                 speed_attack: int,
                 speed_defense: int,
                 speed: int,
                 generation: int,
                 legendary: bool):
        self.name = name
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed_attack = speed_attack
        self.speed_defense = speed_defense
        self.speed = speed
        self.generation = generation
        self.legendary = legendary
        self.types = self.from_list_to_dict(types)
