class Solution(object):
    def generateParenthesis(self, n):
        return self.genAlgorithm(n,n,[],"")

    def genAlgorithm(self,nOpen,nClose,result,str):
        if nOpen == 0 and nClose == 0:
            result.append(str)
            return
        if nClose == nOpen:
            self.genAlgorithm(nOpen-1, nClose, result, str+"(")
        else:
            if nOpen != 0:
                self.genAlgorithm(nOpen-1, nClose, result, str+"(")
            self.genAlgorithm(nOpen, nClose-1, result, str + ")")
        return result


if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))