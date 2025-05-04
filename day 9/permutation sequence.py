class Solution:
    def getPermutation(self, n, k):
        # Create a list of numbers as strings for easier concatenation later
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Precompute factorials up to n
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        # Convert k to 0-indexed
        k -= 1
        
        result = []
        for i in range(n, 0, -1):
            # Determine the index of the current digit
            index = k // factorial[i - 1]
            result.append(numbers.pop(index))
            # Reduce k for the next iteration
            k %= factorial[i - 1]
            
        return ''.join(result)

# Example usage:
if __name__ == '__main__':
    solution = Solution()
    print(solution.getPermutation(3, 3))  # Expected output: "213"
    print(solution.getPermutation(4, 9))  # Expected output: "2314"
    print(solution.getPermutation(3, 1))  # Expected output: "123"
