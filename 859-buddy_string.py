class Solution(object):
    def buddyStrings(self, s: str, goal: str) -> bool:
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s):
            return True

        diff_indices_s = []
        diff_indices_goal = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_indices_s.append(s[i])
                diff_indices_goal.append(goal[i])

        return len(diff_indices_s) == 2 and diff_indices_s == diff_indices_goal[::-1]


