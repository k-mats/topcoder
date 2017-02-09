class BuildingStrings:
    m = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx'
    mp = 50 * 26
    n = 'abcdefghijklmnopqrstuvwxyz'
    np = 26 * 26
    o = 'abcdefghijklmno'
    op = 15 * 15
    p = 'abcdefghij'
    pp = 10 * 10
    q = 'abcdefg'
    qp = 7 * 7
    r = 'abcde'
    rp = 5 * 5
    s = 'abc'
    sp = 3 * 3
    t = 'ab'
    tp = 2 * 2
    def findAny(self, k):
        answers = []
        while k > 0:
            if k > self.mp:
                answers.append(self.m)
                k -= self.mp
            elif k > self.np:
                answers.append(self.n)
                k -= self.np
            elif k > self.op:
                answers.append(self.o)
                k -= self.op
            elif k > self.pp:
                answers.append(self.p)
                k -= self.pp
            elif k > self.qp:
                answers.append(self.q)
                k -= self.qp
            elif k > self.rp:
                answers.append(self.r)
                k -= self.rp
            elif k > self.sp:
                answers.append(self.s)
                k -= self.sp
            elif k > self.tp:
                answers.append(self.t)
                k -= self.tp
            else:
                answers.append('a')
                k -= 1

        return answers
