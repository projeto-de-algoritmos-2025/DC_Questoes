class Solution(object):
    def multiply(self, num1, num2):
        def add_strings(n1, n2):
            res = []
            carry = 0
            i, j = len(n1) - 1, len(n2) - 1

            while i >= 0 or j >= 0 or carry:
                d1 = int(n1[i]) if i >= 0 else 0
                d2 = int(n2[j]) if j >= 0 else 0
                total = d1 + d2 + carry
                res.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1

            return ''.join(reversed(res))

        def subtract_strings(n1, n2):
            res = []
            carry = 0
            i, j = len(n1) - 1, len(n2) - 1

            while i >= 0:
                d1 = int(n1[i])
                d2 = int(n2[j]) if j >= 0 else 0
                diff = d1 - d2 - carry
                if diff < 0:
                    diff += 10
                    carry = 1
                else:
                    carry = 0
                res.append(str(diff))
                i -= 1
                j -= 1

            while len(res) > 1 and res[-1] == '0':
                res.pop()
            return ''.join(reversed(res))

        def karatsuba(x, y):
            x = x.lstrip('0') or '0'
            y = y.lstrip('0') or '0'
            if len(x) == 1 or len(y) == 1:
                return str(int(x) * int(y))

            n = max(len(x), len(y))
            n2 = n // 2
            x = x.zfill(n)
            y = y.zfill(n)

            a, b = x[:-n2], x[-n2:]
            c, d = y[:-n2], y[-n2:]

            ac = karatsuba(a, c)
            bd = karatsuba(b, d)
            ab_cd = karatsuba(add_strings(a, b), add_strings(c, d))
            ad_bc = subtract_strings(subtract_strings(ab_cd, ac), bd)

            part1 = ac + '0' * (2 * n2)
            part2 = ad_bc + '0' * n2
            result = add_strings(add_strings(part1, part2), bd)
            return result.lstrip('0') or '0'

        if num1 == '0' or num2 == '0':
            return '0'
        return karatsuba(num1, num2)
