class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0 # running sum
        tank = 0 # current
        start = 0 # current best guess

        for i in range(len(gas)):
            diff = gas[i] - cost[i] # net

            tank += diff
            total += diff
            
            if tank < 0:
                start = i + 1
                tank = 0
    
        if total < 0:
            return -1
    
        return start