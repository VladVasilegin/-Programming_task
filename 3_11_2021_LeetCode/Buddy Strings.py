class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        differences = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                differences.append(s[i]+goal[i])
        if len(differences) == 0 and len(s) > len(set(list(s))):
            return True
        if len(s) != len(goal) or len(differences) != 2:
            return False
        if differences[0] != differences[1][::-1]:
            return False
        return True

if __name__ == "__main__":
    s = "aa"
    goal = "aa"
    print(Solution().buddyStrings(s,goal))