from typing import Dict
from math import ceil
from itertools import product, combinations


def fight_result(player_stats: Dict, enemy_stats: Dict) -> bool:
    player_damage = max(1, player_stats["Damage"] - enemy_stats["Armor"])
    enemy_damage = max(1, enemy_stats["Damage"] - player_stats["Armor"])

    enemy_dies_after = ceil(enemy_stats["Hit Points"] / player_damage)
    player_dies_after = ceil(player_stats["Hit Points"] / enemy_damage)

    result = enemy_dies_after <= player_dies_after
    return result


def use_equipments(equipments: Dict, player_stats: Dict, enemy_stats: Dict) -> int:
    min_cost = float("inf")
    max_cost = 0

    for weapon, armor, (ring1, ring2) in product(
        equipments["Weapons"], equipments["Armor"], combinations(equipments["Rings"], 2)
    ):
        new_player_stats = player_stats.copy()
        Weapons = equipments["Weapons"]
        Armor = equipments["Armor"]
        Rings = equipments["Rings"]
        new_player_stats["Damage"] += Weapons[weapon]["Damage"]
        new_player_stats["Armor"] += Armor[armor]["Armor"]
        cost = Weapons[weapon]["Cost"] + Armor[armor]["Cost"]

        new_player_stats["Damage"] += Rings[ring1]["Damage"] + Rings[ring2]["Damage"]
        new_player_stats["Armor"] += Rings[ring1]["Armor"] + Rings[ring2]["Armor"]
        cost += Rings[ring1]["Cost"] + Rings[ring2]["Cost"]

        if fight_result(new_player_stats, enemy_stats):
            if min_cost > cost:
                min_cost = cost
        elif max_cost < cost:
            max_cost = cost

    return min_cost, max_cost


def main() -> None:
    player_stats: Dict = {"Hit Points": 100, "Damage": 0, "Armor": 0}
    enemy_stats: Dict = {"Hit Points": 104, "Damage": 8, "Armor": 1}
    equipments: Dict = {
        "Weapons": {
            "Dagger": {"Cost": 8, "Damage": 4, "Armor": 0},
            "Shortsword": {"Cost": 10, "Damage": 5, "Armor": 0},
            "Warhammer": {"Cost": 25, "Damage": 6, "Armor": 0},
            "Longsword": {"Cost": 40, "Damage": 7, "Armor": 0},
            "Greataxe": {"Cost": 74, "Damage": 8, "Armor": 0},
        },
        "Armor": {
            "No Armor": {"Cost": 0, "Damage": 0, "Armor": 0},
            "Leather": {"Cost": 13, "Damage": 0, "Armor": 1},
            "Chainmail": {"Cost": 31, "Damage": 0, "Armor": 2},
            "Splintmail": {"Cost": 53, "Damage": 0, "Armor": 3},
            "Bandedmail": {"Cost": 75, "Damage": 0, "Armor": 4},
            "Platemail": {"Cost": 102, "Damage": 0, "Armor": 5},
        },
        "Rings": {
            "No Ring": {"Cost": 0, "Damage": 0, "Armor": 0},
            "Damage +1": {"Cost": 25, "Damage": 1, "Armor": 0},
            "Damage +2": {"Cost": 50, "Damage": 2, "Armor": 0},
            "Damage +3": {"Cost": 100, "Damage": 3, "Armor": 0},
            "Defense +1": {"Cost": 20, "Damage": 0, "Armor": 1},
            "Defense +2": {"Cost": 40, "Damage": 0, "Armor": 2},
            "Defense +3": {"Cost": 80, "Damage": 0, "Armor": 3},
        },
    }
    result = use_equipments(equipments, player_stats, enemy_stats)
    print(result)


if __name__ == "__main__":
    main()
