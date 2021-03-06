#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'XingKaiXin.me'

import random


class Smash:
    smash = []

    # 生成一个4位不重复数字
    def __init__(self):
        self.smash = []
        single_smash = range(1, 9)
        for i in range(0, 4):
            randint = random.choice(single_smash)
            single_smash.remove(randint)
            self.smash.append(randint)


    # 单个数字在Smash中存在与否，位置多少
    def findnum(self, onenum):
        if self.smash.count(onenum) > 0:
            return [1, self.smash.index(onenum) + 1]
        else:
            return [0, 0]


    # 4位数字猜中了Smash多少
    def complareSmash(self, guessnum):
        exist = 0
        result = []
        for i in range(4):
            a = int(str(guessnum)[i])
            b = self.findnum(a)
            exist += b[0]
            if b[1] == i + 1:
                result.append(1)
            else:
                result.append(0)
        result.append(exist)
        return result
