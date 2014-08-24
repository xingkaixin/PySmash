#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


__author__ = 'XingKaiXin.me'
import unittest
import Smash
import ResolveSmash
import time


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # self.s = Smash.Smash()
        # print "本轮要竞猜的数字是",self.s.smash
        # self.r = ResolveSmash.ResolveSmash()
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def testsmash(self):
        turntime = 0
        alltrytime = 0
        start = time.clock()
        while turntime < 2000000:
            s = Smash.Smash()
            #print "本轮要竞猜的数字是",s.smash
            r = ResolveSmash.ResolveSmash()
            trytime = 0
            nextprenum = 0
            step1 = s.complareSmash(r.FIRSTSTEP)
            flag = step1[0]+step1[1]+step1[2]+step1[3]
            trytime += 1
            if flag == 4:
                #print "猜对了！", r.FIRSTSTEP,trytime
                alltrytime += trytime
                turntime += 1
            else:
                r.delNumsFromintall(r.FIRSTSTEP)
                step2 = s.complareSmash(r.SECONDSTEP)
                flag = step2[0]+step2[1]+step2[2]+step2[3]
                trytime += 1
                if flag == 4:
                    #print "猜对了！", r.SECONDSTEP,trytime
                    alltrytime += trytime
                    turntime += 1
                else:
                    r.delNumsFromintall(r.SECONDSTEP)
                    part1 = step1[4]-step1[0]-step1[1]-step1[2]-step1[3]
                    part2 = step2[4]-step2[0]-step2[1]-step2[2]-step2[3]
                    nextprenum = r.getNextGuessAfterFirstandSecondStep(step1, step2)
                    while flag < 4:
                        nextprenum = r.getNexGuess(nextprenum, r.int1, r.int2, r.int3, r.int4, part1)
                        nextprenum = r.getNexGuess(nextprenum, r.int5, r.int6, r.int7, r.int8, part2)
                        nextresult = s.complareSmash(int(nextprenum))
                        flag = nextresult[0]+nextresult[1]+nextresult[2]+nextresult[3]
                        trytime += 1
                        if flag == 4:
                            #print "猜对了！", nextprenum, trytime
                            alltrytime += trytime
                            turntime += 1
                        else:
                            r.delNumsFromintall(int(nextprenum))
                            nextprenum = r.getNextGuessPre(int(nextprenum), nextresult)
        end = time.clock()
        print end-start, turntime, alltrytime, alltrytime/turntime


    def testresolve(self):
        pass

if __name__ =='__main__':
    unittest.main()