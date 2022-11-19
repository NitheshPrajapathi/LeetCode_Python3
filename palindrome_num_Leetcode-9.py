class Solution:
    def isPalindrome(self, x: int) -> bool:
        #consider the int read from left to right and palindrome we can check for positive int
        #121->121 ,but -121->121- so the x is greater than zero.
        num=x
        rev=0
        if num>0:
            while num:
                num,digit=divmod(num,10)
                rev=rev*10+digit
        return rev==x


