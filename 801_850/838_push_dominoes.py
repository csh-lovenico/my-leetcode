class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d_l = list(dominoes)
        l_s = set()
        r_s = set()
        for i in range(len(dominoes)):
            if dominoes[i] == 'L':
                l_s.add(i - 1)
            elif dominoes[i] == 'R':
                r_s.add(i + 1)

        while l_s or r_s:
            pub = l_s.intersection(r_s)
            new_l_s = set()
            new_r_s = set()
            for i in pub:
                d_l[i] = '.'
            for i in l_s:
                if 0 <= i < len(d_l) and i not in pub:
                    if d_l[i] == '.':
                        d_l[i] = 'L'
                        new_l_s.add(i - 1)
            for i in r_s:
                if 0 <= i < len(d_l) and i not in pub:
                    if d_l[i] == '.':
                        d_l[i] = 'R'
                        new_r_s.add(i + 1)
            l_s = new_l_s
            r_s = new_r_s
        return ''.join(d_l)
