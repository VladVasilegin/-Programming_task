class Solution(object):
    def letterCombinations(self, digits):
        dict_Phone = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        if digits == "":
            return ""
        list_string_char = [dict_Phone[i] for i in list(map(int,list(digits)))]

        result = list(list_string_char[0])
        for i in range(1,len(list_string_char)):
            temp = []
            for j in list_string_char[i]:
                for n in result:
                    temp.append(n+j)
            result = temp
        return result



if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))