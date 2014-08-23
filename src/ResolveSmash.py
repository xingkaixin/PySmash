# -*- coding: utf-8 -*-
__author__ = 'XingKaiXin.me'

import copy

"""
解Smash,生成下轮要猜的数字，在数组集合中移除已竞猜过的数字~~~~~
"""
class ResolveSmash:
    FIRSTSTEP = 1234
    SECONDSTEP = 5678

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


    def getNextGuessAfterFirstandSecondStep(self, result1, result2):
        str1 = self.getNextGuessPre(self.FIRSTSTEP, result1)
        str2 = self.getNextGuessPre(self.SECONDSTEP, result2)
        nextstr = ""
        for i in range(0,4):
            if str1[i] != "0":
                nextstr += str1[i]
            elif str2[i] != "0":
                nextstr += str2[i]
            else:
                nextstr += "0"
        return nextstr

    def getNexGuess(self, prenum, int1, int2, int3, int4, count):
        if count > 0:
            for i in range(4):
                s = int(prenum[i])
                if s == 0:
                    if i == 0:
                        new_s = self.getNumFromint(prenum, int1)
                        prenum = prenum[0:i] +str(new_s) + prenum[i+1:4]
                    elif i == 1:
                        new_s = self.getNumFromint(prenum, int2)
                        prenum = prenum[0:i] +str(new_s) + prenum[i+1:4]
                    elif i == 2:
                        new_s = self.getNumFromint(prenum, int3)
                        prenum = prenum[0:i] +str(new_s) + prenum[i+1:4]
                    else:
                        new_s = self.getNumFromint(prenum, int4)
                        prenum = prenum[0:i] +str(new_s) + prenum[i+1:4]
        return prenum

    def getNumFromint(self, prenum, int):
        for i in int:
            s = str(i)
            if prenum.count(s) == 0:
                return s
                break

    def delNumsFromintall(self, num):
        for i in range(4):
            s = int(str(num)[i])
            if i == 0:
                self.int1 = self.delNumFromint(s, self.int1)
                self.int5 = self.delNumFromint(s, self.int5)
            elif i == 1:
                self.int2 = self.delNumFromint(s, self.int2)
                self.int6 = self.delNumFromint(s, self.int6)
            elif i == 2:
                self.int3 = self.delNumFromint(s, self.int3)
                self.int7 = self.delNumFromint(s, self.int7)
            elif i == 3:
                self.int4 = self.delNumFromint(s, self.int4)
                self.int8 = self.delNumFromint(s, self.int8)


    def delNumFromint(self, num, int):
        if int.count(num) > 0:
            int.remove(num)
        return int

