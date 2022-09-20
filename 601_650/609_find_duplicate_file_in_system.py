import collections
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result = []
        hashmap = collections.defaultdict(list)
        for path in paths:
            files = path.split(' ')
            folder = files[0]
            for i in range(1, len(files)):
                par = files[i].find('(')
                name = files[i][0:par]
                content = files[i][par + 1:-1]
                hashmap[content].append(folder + '/' + name)
        for k, v in hashmap.items():
            if len(v) > 1:
                result.append(v)
        return result
