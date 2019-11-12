class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(n):
            num = i + 1
            if (num%3 == 0 and num%5 == 0):
                res.append("FizzBuzz")
            elif (num%3 == 0):
                res.append("Fizz")
            elif (num%5 == 0):
                res.append("Buzz")
            else:
                res.append(str(num))
        return res