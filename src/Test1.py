# -*- coding: utf-8 -*-


__author__ = 'XingKaiXin.me'

import unittest
import Smash
import ResolveSmash


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.s = Smash.Smash()
        print self.s.smash
        self.r = ResolveSmash.ResolveSmash()
        # pass

    @classmethod
    def tearDownClass(self):
        pass

    def testsmash(self):
        print self.s.complareSmash(1234)


    def testresolve(self):
        pass

if __name__ =='__main__':
    unittest.main()