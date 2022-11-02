class Solution:
    def oneMut(self, start, bank):
        assert len(start)==len(bank), 'Strings should be same length'
        diff = 0
        for i in range(len(start)):
            if start[i] != bank[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False
        
    def minMutation(self, start, end, bank):
        if start == end:
            return 0
        else:
            best = []
            for i in bank:
                if self.oneMut(start, i):
                    bank2 = bank[:]
                    bank2.remove(i)
                    best.append(self.minMutation(i, end, bank2))
            best = [i for i in best if i >= 0]
            if best == []:
                return -1
            else:
                return 1 + min(best)