class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        Input: command = "G()(al)"
        Output: "Goal"
        Explanation: The Goal Parser interprets the command as follows:
        G -> G
        () -> o
        (al) -> al
        The final concatenated result is "Goal".
        """
        return command.replace("()", "o").replace("(al)", "al")
