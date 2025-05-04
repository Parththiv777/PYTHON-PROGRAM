class Solution(object):
    def plusOne(self, digits):
        sum = 0
        for i in range(len(digits)):
            sum = (sum * 10) + digits[i]
        sum = sum + 1
        return [int(digit) for digit in str(sum)]    
