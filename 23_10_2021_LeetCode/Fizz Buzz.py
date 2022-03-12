class Solution:
    def fizzBuzz(self, n: int):
        list = [str(i) for i in range(1,n+1)]
        for i in range(2,n,3):
            list[i]="Fizz"
        for i in range(4,n,5):
            list[i]="Buzz"
        for i in range(14,n,15):
            list[i]="FizzBuzz"

        return list


if __name__ == "__main__":
    n = 15
    print(Solution().fizzBuzz(n))