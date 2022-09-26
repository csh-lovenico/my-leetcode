

# https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/2597256/Python-Readable-solution-with-short-explanation
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # check whether is has to be negative
        result = "" if numerator * denominator >= 0 else "-"

        # make the absolute values
        numerator = abs(numerator)
        denominator = abs(denominator)

        # make the number before the comma
        number, numerator = divmod(numerator, denominator)
        result += str(number)

        # check whether we are finished
        if not numerator:
            return result

        # attach the point and make it a list, as we now will
        # append a lot of numbers and python is way faster
        # appending to a list versus adding to a string
        result += "."
        result = [result]

        # now make a dict to save which numbers we already encountered
        found = {}
        position = len(result)

        # now compute the numbers after comma and break, if we have zero
        # or already encountered the number
        while numerator and numerator not in found:
            # put current value in the dict
            found[numerator] = position

            # get the new number
            number, numerator = divmod(numerator * 10, denominator)

            # attach the number
            result.append(str(number))

            # increase digit coutner
            position += 1

        # make the brackets
        if numerator in found:
            result.insert(found[numerator], '(')
            result.append(')')

        # construct the result
        return "".join(result)