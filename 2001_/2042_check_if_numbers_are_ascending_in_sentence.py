class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split(' ')
        last_num = float('-inf')
        for word in words:
            if word.isdigit():
                if int(word) > last_num:
                    last_num = int(word)
                else:
                    return False
        return True
