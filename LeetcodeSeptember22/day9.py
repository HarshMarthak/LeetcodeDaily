class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        max_defense_for_attacks = [0] * int(1e5 + 2)
        max_att = 0
        for att, defense in properties:
            if defense > max_defense_for_attacks[att]:
                max_defense_for_attacks[att] = defense
            if att > max_att:
                max_att = att
        current_max = 0
        for i in range(max_att, 0, -1):
            current_max = max(current_max, max_defense_for_attacks[i])
            max_defense_for_attacks[i] = current_max
        result = 0
        for att, defense in properties:
            if defense < max_defense_for_attacks[att + 1]:
                result += 1
        return result
