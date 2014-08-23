# -*- coding: utf-8 -*-


__author__ = 'XingKaiXin.me'

import unittest
import Smash
import ResolveSmash


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.s = Smash.Smash()
        print "本轮要竞猜的数字是",self.s.smash
        self.r = ResolveSmash.ResolveSmash()
        # pass

    @classmethod
    def tearDownClass(self):
        pass

    def testsmash(self):
        trytime = 0
        nextprenum = 0
        step1 = self.s.complareSmash(self.r.FIRSTSTEP)
        flag = step1[0]+step1[1]+step1[2]+step1[3]
        print 1, flag
        trytime += 1
        if flag == 4:
            print "猜对了！", self.r.FIRSTSTEP,trytime
        else:
            self.r.delNumsFromintall(self.r.FIRSTSTEP)
            step2 = self.s.complareSmash(self.r.SECONDSTEP)
            flag = step2[0]+step2[1]+step2[2]+step2[3]
            trytime += 1
            print 2, flag
            if flag == 4:
                print "猜对了！", self.r.SECONDSTEP,trytime
                self.r.delNumsFromintall(self.r.SECONDSTEP)
            else:
                part1 = step1[4]-step1[0]-step1[1]-step1[2]-step1[3]
                part2 = step2[4]-step2[0]-step2[1]-step2[2]-step2[3]
                print "step", step1, step2
                print "part", part1, part2
                nextprenum = self.r.getNextGuessAfterFirstandSecondStep(step1, step2)
                while flag < 4:
                    nextprenum = self.r.getNexGuess(nextprenum, self.r.int1, self.r.int2, self.r.int3, self.r.int4, part1)
                    nextprenum = self.r.getNexGuess(nextprenum, self.r.int5, self.r.int6, self.r.int7, self.r.int8, part2)
                    nextresult = self.s.complareSmash(int(nextprenum))
                    flag = nextresult[0]+nextresult[1]+nextresult[2]+nextresult[3]
                    trytime += 1
                    print 3, flag, nextprenum, self.r.intall
                    if flag == 4:
                        print "猜对了！", nextprenum, trytime
                    self.r.delNumsFromintall(int(nextprenum))
                    nextprenum = self.r.getNextGuessPre(int(nextprenum), nextresult)



    def testresolve(self):
        pass

if __name__ =='__main__':
    unittest.main()