"""

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

"""


class Solution:
    def reverse(self, x: int) -> int:
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        return r*s*(r < 2**31)


def main():
    i1 = -8463847412
    i2 = -123
    i3 = 120

    s = Solution()
    print(s.reverse(i1))
    print(s.reverse(i2))
    print(s.reverse(i3))


if __name__ == '__main__':
    main()
