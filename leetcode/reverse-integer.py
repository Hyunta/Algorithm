class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        numAsString = str(x)
        retrunNum = 0

        if numAsString[0] == '-':
            reverse = numAsString[:0:-1]
            returnNum = int(reverse)
            retrunNum = returnNum * -1

        else:
            reverse = numAsString[::-1]
            returnNum = int(reverse)
            retrunNum = returnNum

        return retrunNum if -(2 ** 31) - 1 < retrunNum < 2 ** 31 else 0