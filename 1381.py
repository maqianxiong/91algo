###思路
###暴力法

代码
Python

 Class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.ina = [] 

    def push(self, x: int) -> None:
        if len(self.ina)<self.max:
            self.ina.append(x)

    def pop(self) -> int:
        if self.ina:
            return self.ina.pop()
        else:
            return -1


    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.ina))):
            self.ina[i]+=val
复杂度分析

时间复杂度：O(N)
空间复杂度：O(1)
