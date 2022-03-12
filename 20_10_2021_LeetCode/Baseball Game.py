class Solution:
    def calPoints(self, ops) -> int:
        result = []
        operations = {"C": lambda x: x.pop(),
                      "D": lambda x: x.append(x[-1]*2),
                      "+": lambda x: x.append(x[-1]+x[-2])}
        for i in ops:
            if i in operations:
                operations[i](result)
            else:
                result.append(int(i))
        return sum(result)


if __name__ == "__main__":
    ops = ["5","-2","4","C","D","9","+","+"]
    print(Solution().calPoints(ops))