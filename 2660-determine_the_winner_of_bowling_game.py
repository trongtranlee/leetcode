class Solution(object):
    def isWinner(self, player1, player2):

        def getScore(player):
            count, score = 0, 0

            for i in range(len(player)):
                if count > 0:
                    score += player[i] * 2
                    count -= 1
                else:
                    score += player[i]
                if player[i] == 10:
                    count = 2
            return score
        player1Score, player2Score = getScore(player1), getScore(player2)

        if player1Score > player2Score:
            return 1
        elif player1Score < player2Score:
            return 2
        else:
            return 0

