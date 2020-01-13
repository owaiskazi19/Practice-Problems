class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = set(J)
        count = 0
        for i in S:
            if i in res:
                count += 1
        return count
        