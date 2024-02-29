from typing import List


class Solution(object):
    def destCity(self, paths:List[List[str]])-> str:
        """
        Input: paths = [["B","C"],["D","B"],["C","A"]]
        Output: "A"
        Explanation: All possible trips are:
        "D" -> "B" -> "C" -> "A".
        "B" -> "C" -> "A".
        "C" -> "A".
        "A".
        Clearly the destination city is "A".
        """
        start_cities = set()
        end_cities = set()

        for path in paths:
            start_cities.add(path[0])
            end_cities.add(path[1])

        for city in end_cities:
            if city not in start_cities:
                return city
