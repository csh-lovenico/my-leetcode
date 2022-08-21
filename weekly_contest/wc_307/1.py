from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        required_energy = 0
        # if initialEnergy > sum(energy):
        #     required_energy = 0
        # else:
        #     required_energy = sum(energy) - initialEnergy + 1
        total_exp = initialExperience
        required_exp = 0
        total_energy = initialEnergy
        for i in range(0, len(energy)):
            if total_energy <= energy[i]:
                required_energy += (energy[i] - total_energy + 1)
                total_energy = 1
            else:
                total_energy -= energy[i]

        for i in range(0, len(experience)):
            if total_exp <= experience[i]:
                now_required = (experience[i] - total_exp + 1)
                required_exp += (experience[i] - total_exp + 1)
                total_exp = total_exp + now_required + experience[i]
            else:
                total_exp += experience[i]
        return required_energy + required_exp


if __name__ == '__main__':
    print(Solution().minNumberOfHours(11,
                                      23
                                      , [69, 22, 93, 68, 57, 76, 54, 72, 8, 78, 88, 15, 58, 61, 25, 70, 58, 91, 79, 22,
                                         91, 74, 90, 75, 31, 53, 31, 7, 51, 96, 76, 17, 64, 89, 83, 54, 28, 33, 32, 45,
                                         20],
                                      [51, 81, 46, 80, 56, 7, 46, 74, 64, 20, 84, 66, 13, 91, 49, 30, 75, 43, 74, 88,
                                       82, 51, 72, 4, 80, 30, 10, 19, 40, 27, 21, 71, 24, 94, 79, 13, 40, 28, 63, 85,
                                       70]))
    print(Solution().minNumberOfHours(5, 3, [1, 4, 3, 2], [2, 6, 3, 1]))
