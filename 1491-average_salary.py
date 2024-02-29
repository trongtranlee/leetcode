from typing import List


class Solution(object):
    def average(self, salary: List[int]) -> float:
        """
        Input: salary = [4000,3000,1000,2000]
        Output: 2500.00000
        Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
        Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
        """
        max_salary = max(salary)
        min_salary = min(salary)
        res = []
        for sal in salary:
            if sal == max_salary or sal == min_salary:
                continue
            else:
                res.append(sal)
        return float(sum(res))/len(res)
