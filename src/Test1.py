# -*- coding: utf-8 -*-
__author__ = 'XingKaiXin.me'

import unittest
import Smash


class Test1(unittest.TestCase):
    def setUp(self):
        self.s = Smash.Smash()
        # pass

    def tearDown(self):
        pass

    def testsmash(self):
        print self.s.complareSmash(1234)


if __name__ =='__main__':
    unittest.main()