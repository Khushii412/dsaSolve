class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        tank=start=0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i+1
                tank = 0
        return start
       # calc sum for each iteration , if value of tank becomes -ve , change start index. 
