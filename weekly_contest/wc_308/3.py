from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        mpg_d = {'M': [],
                 'G': [],
                 'P': []}
        for i in range(len(garbage)):
            for j in range(len(garbage[i])):
                mpg_d[garbage[i][j]].append(i)

        print(mpg_d)
        prev = {'M': 0,
                'G': 0,
                'P': 0}

        total_m = 0
        total_g = 0
        total_p = 0

        for i in range(len(mpg_d['M'])):
            total_m += 1
            if mpg_d['M'][i] != prev['M']:
                diff = mpg_d['M'][i]-prev['M']
                for j in range(diff):
                    total_m += travel[mpg_d['M'][i] - 1 -j]
            prev['M'] = mpg_d['M'][i]

        for j in range(len(mpg_d['G'])):
            total_g += 1
            if mpg_d['G'][j] != prev['G']:
                diff = mpg_d['G'][j]-prev['G']
                for k in range(diff):
                    total_g += travel[mpg_d['G'][j] - 1 -k]
            prev['G'] = mpg_d['G'][j]

        for k in range(len(mpg_d['P'])):
            total_p += 1
            if mpg_d['P'][k] != prev['P']:
                diff = mpg_d['P'][k]-prev['P']
                for j in range(diff):
                    total_p += travel[mpg_d['P'][k] - 1 -j]
            prev['P'] = mpg_d['P'][k]

        print(total_m, total_p, total_g)

        return total_m + total_g + total_p


if __name__ == '__main__':
    print(Solution().garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]))
