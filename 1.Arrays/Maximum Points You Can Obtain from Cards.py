class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) 
        add = 0
        for i in range(k,0,-1):
            if sum(cardPoints[:i]) > sum(cardPoints[n-i:n]):
                add += cardPoints[0]
                cardPoints.pop(0)
                n -= 1
            else:
                add += cardPoints[-1]
                cardPoints.pop()
                n -= 1
        return add