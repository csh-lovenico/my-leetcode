class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for i in range(len(sentence)):
            s.add(sentence[i])
        return len(s) == 26
