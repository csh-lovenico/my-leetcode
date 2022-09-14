from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            print(data[i] >> 7)
            print(data[i] >> 6)
            print(data[i] >> 4)
            print(data[i] >> 3)
            if data[i] >> 7 == 0:
                # 1 byte valid
                i += 1
                continue
            elif data[i] >> 5 == 6:
                # 2 bytes
                i += 1
                if i < len(data) and data[i] >> 6 == 2:
                    i += 1
                    continue
                else:
                    return False
            elif data[i] >> 4 == 14:
                # 3 bytes
                i += 1
                if i < len(data) and data[i] >> 6 == 2:
                    i += 1
                    if i < len(data) and data[i] >> 6 == 2:
                        i += 1
                        continue
                    else:
                        return False
                else:
                    return False
            elif data[i] >> 3 == 30:
                # 4 bytes
                i += 1
                if i < len(data) and data[i] >> 6 == 2:
                    i += 1
                    if i < len(data) and data[i] >> 6 == 2:
                        i += 1
                        if i < len(data) and data[i] >> 6 == 2:
                            i += 1
                            continue
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        return True
