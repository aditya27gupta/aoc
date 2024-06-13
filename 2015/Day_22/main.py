from itertools import count
from functools import reduce
from collections import namedtuple
from heapq import heappop, heappush


class Spell(namedtuple("BaseSpell", "name cost effect turns damage heal armor mana")):
    def __new__(
        cls, name, cost, effect=False, turns=None, damage=0, heal=0, armor=0, mana=0
    ):
        return super().__new__(
            cls, name, cost, effect, turns, damage, heal, armor, mana
        )


spells = (
    Spell("Magic Missile", 53, damage=4),
    Spell("Drain", 73, damage=2, heal=2),
    Spell("Shield", 113, effect=True, turns=6, armor=7),
    Spell("Poison", 173, effect=True, turns=6, damage=3),
    Spell("Recharge", 229, effect=True, turns=5, mana=101),
)


class State:
    def __init__(
        self,
        player_hp: int,
        player_mana: int,
        boss_hp: int,
        boss_damage: int,
        effects: tuple = None,
        mana_spent: int = 0,
        hard_mode: bool = False,
    ):
        self.player_hp = player_hp
        self.player_mana = player_mana
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.effects = effects or ()
        self.mana_spent = mana_spent
        self.hard_mode = hard_mode

    def __eq__(self, other) -> bool:
        if not isinstance(other, State):
            raise NotImplementedError
        return all([getattr(self, k) == getattr(other, k) for k in vars(self)])

    def __hash__(self):
        return reduce(lambda a, b: a ^ hash(b), (v for k, v in vars(self).items()), 0)

    def process_effects(self, player_mana, player_hp, boss_hp):
        remaining_effects = []
        armor = 0
        for timer, spell in self.effects:
            player_mana += spell.mana
            player_hp += spell.heal
            armor = max(spell.armor, armor)
            boss_hp -= spell.damage
            if timer > 1:
                remaining_effects.append((timer - 1, spell))

        return tuple(remaining_effects), player_mana, player_hp, armor, boss_hp

    def boss_turn(self):
        (
            self.effects,
            self.player_mana,
            self.player_hp,
            armor,
            self.boss_hp,
        ) = self.process_effects(
            self.player_mana, self.player_hp - int(self.hard_mode), self.boss_hp
        )
        if self.boss_hp > 0:
            self.player_hp -= max(1, self.boss_damage - armor)

    def turns(self):
        new_effects, player_mana, player_hp, _, boss_hp = self.process_effects(
            self.player_mana, self.player_hp, self.boss_hp
        )
        for spell in spells:
            if spell.cost > player_mana or any(spell is s for t, s in new_effects):
                continue

            new_state = State(
                player_hp,
                player_mana - spell.cost,
                boss_hp,
                self.boss_damage,
                new_effects,
                self.mana_spent + spell.cost,
                self.hard_mode,
            )

            if not spell.effect:
                new_state.player_hp += spell.heal
                new_state.boss_hp -= spell.damage
            else:
                new_state.effects += ((spell.turns, spell),)

            new_state.boss_turn()
            if new_state.player_hp > 0:
                yield new_state


def solve(state):
    open_states = {state}
    queue = [(state.mana_spent, state)]
    closed_state = set()
    counter = count()
    while open_states:
        current = heappop(queue)[-1]
        if current.boss_hp < 1:
            print("You won")
            return current
        open_states.remove(current)
        closed_state.add(current)
        for new_state in current.turns():
            if new_state not in open_states and new_state not in closed_state:
                open_states.add(new_state)
                heappush(queue, (new_state.mana_spent, next(counter), new_state))


def main():
    player_hp, player_mana = 50, 500
    boss_hp, boss_damage = 51, 9
    start_state = State(player_hp, player_mana, boss_hp, boss_damage)
    end_state = solve(start_state)
    print(end_state.mana_spent)

    start_state.hard_mode = True
    end_state = solve(start_state)
    print(end_state.mana_spent)


if __name__ == "__main__":
    main()
