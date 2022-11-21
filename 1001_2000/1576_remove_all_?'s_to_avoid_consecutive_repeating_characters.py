import string


class Solution:
    def modifyString(self, s: str) -> str:
        if s == '?':
            return 'a'
        l = list(s)
        letters = list(string.ascii_lowercase)
        for i in range(len(l)):
            if l[i] == '?':
                if i == 0:
                    for ltr in letters:
                        l[i] = ltr
                        if l[i] == l[i + 1]:
                            continue
                        else:
                            break
                elif i == len(l) - 1:
                    for ltr in letters:
                        l[i] = ltr
                        if l[i] == l[i - 1]:
                            continue
                        else:
                            break
                else:
                    for ltr in letters:
                        l[i] = ltr
                        if l[i] == l[i - 1] or l[i] == l[i + 1]:
                            continue
                        else:
                            break
        return ''.join(l)
