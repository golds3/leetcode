from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        for i in range(1,len(people)):
            tmp = people[i]
            if tmp[1]!=i:
                index = tmp[1]
                people[index+1:i+1] = people[index:i]
                people[index] = tmp
        return people
