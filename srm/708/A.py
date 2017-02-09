class SafeBetting:
    def minRounds(self, a, b, c):
        cnt = 0
        while b < c:
            b += (b - a)
            cnt += 1

        return cnt
