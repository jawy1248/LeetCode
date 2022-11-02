class Solution:
    def isPalindrome(self, x):
        x2 = str(x)
        print(x2)
        if x2[0] != x2[-1]:
            return False
        elif len(x2) == 2:
            if x2[0] == x2[1]:
                return True
            else:
                return False
        elif len(x2) < 2:
            return True
        else:
            x2 = x2[1:-1]
            return self.isPalindrome(x2)