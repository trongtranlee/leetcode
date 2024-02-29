from collections import deque



class Solution(object):
    def rotateString(self, s:str, goal:str)-> bool:
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        queueList = deque(s)
        for _ in range(len(s)):
            if ''.join(queueList) == goal:
                return True
            # Kiểm tra nếu hàng đợi không rỗng trước khi thực hiện popleft()
            if queueList:
                element = queueList.popleft()
                queueList.append(element)

        return False
