__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import random


# 生成一个4位不重复数字
def genSmash():
    single_smash = range(1, 9)
    smash = []
    for i in range(0, 4):
        randint = random.choice(single_smash)
        single_smash.remove(randint)
        smash.append(randint)
    return smash


# 单个数字在Smash中存在与否，位置多少
def findnum(onenum, smash):
    if smash.count(onenum) > 0:
        return [1, smash.index(onenum) + 1]
    else:
        return [0, 0]


# 4位数字猜中了Smash多少
def complareSmash(guessnum):
    exist = 0
    result = []
    smash = genSmash()
    print smash
    for i in range(4):
        a = int(str(guessnum)[i])
        b = findnum(a, smash)
        exist += b[0]
        if b[1] == i + 1:
            result.append(1)
        else:
            result.append(0)
    result.append(exist)
    return result


print complareSmash(1234)