'''
Digital Root (GFG)

You are given a number n. You need to find the digital root of n. DigitalRoot of a number is the recursive sum of its digits until we get a single digit number.

Example 1:

Input:
n = 1
Output:  1
Explanation: Digital root of 1 is 1
Example 2:

Input:
n = 99999
Output: 9
Explanation: Sum of digits of 99999 is 45
which is not a single digit number, hence
sum of digit of 45 is 9 which is a single
digit number.
'''

class Solution:
    def digitalRoot(self, n):
        if len(str(n))==1:
            return n
            
        def sum_digit(N):
            if N==0:
                return 0
                
            return N%10+sum_digit(N//10)
            
        n=sum_digit(n)
        
        return self.digitalRoot(n)
