from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for v in bills:
            if v == 5:
                five += 1
            elif v == 10:
                if five <= 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                    continue
                if five >= 3:
                    five -= 3
                    continue
                return False
        return True