# -*- coding: utf-8 -*-
__author__ = 'XingKaiXin.me'

import copy


class ResolveSmash:
    int1 = []
    int2 = []
    int3 = []
    int4 = []
    int5 = []
    int6 = []
    int7 = []
    int8 = []

    intall = []

    def __init__(self):
        """

        :rtype : object
        """
        self.int1 = range(1, 5)
        self.int2 = copy.deepcopy(self.int1)
        self.int3 = copy.deepcopy(self.int1)
        self.int4 = copy.deepcopy(self.int1)
        self.int5 = range(5, 9)
        self.int6 = copy.deepcopy(self.int5)
        self.int7 = copy.deepcopy(self.int5)
        self.int8 = copy.deepcopy(self.int5)
        self.intall = [self.int1, self.int2, self.int3, self.int4,
                       self.int5, self.int6, self.int7, self.int8]

    def getNextGuessPre(self, lastguess, lastresult):
        NextGuessPre = ""
        for i in range(4):
            if lastresult[i] == 1:
                NextGuessPre += str(lastguess)[i]
            else:
                NextGuessPre += "0"
        return NextGuessPre

    def getNexGuess(self, prenum, int1, int2, int3, int4, count):
        if count > 0:
            for i in range(4):
                s = int(prenum[i])
                if s == 0:
                    if i == 0:
                        new_s = self.getNumFromint(prenum, int1, i)
                        prenum = prenum[0:i] +str(new_s) + prenum[i+1:4]
                    elif i == 1:
                        new_s = self.getNumFromint(prenum, int2, i)
                        prenum = prenum[0:i] +str(new_s) + prenum[i+1:4]
                    elif i == 2:
                        new_s = self.getNumFromint(prenum, int3, i)
                        prenum = prenum[0:i] +str(new_s) + prenum[i+1:4]
                    else:
                        new_s = self.getNumFromint(prenum, int4, i)
                        prenum = prenum[0:i] +str(new_s) + prenum[i+1:4]
        print prenum
        return int(prenum)

    def getNumFromint(self, prenum, int, loc):
        for i in int:
            s = str(i)
            if prenum.count(s) == 0:
                return s
                break

s = ResolveSmash()
ss = s.getNextGuessPre(5234, [1, 1, 0, 1])

s.getNexGuess(ss, s.int1, s.int2, s.int3, s.int4, 4)


