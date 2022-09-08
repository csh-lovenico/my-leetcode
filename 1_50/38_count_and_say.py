class Solution:
    def countAndSay(self, n: int) -> str:
        num_str = '1'
        for i in range(1, n):
            temp_str = ''
            curr = None
            count = 0
            for j in range(len(num_str)):
                if num_str[j] != curr:
                    if curr:
                        temp_str += (str(count) + curr)
                    curr = num_str[i]
                    count = 1
                else:
                    count += 1
            temp_str += (str(count) + curr)
            num_str = temp_str
        return num_str
