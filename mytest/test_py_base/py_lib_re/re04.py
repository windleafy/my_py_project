#!/usr/bin/env python
"""re04"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 21:13
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
import re

tmp = '"url":"http://upos-hz-mirrorkodou.acgvideo.com/upgcxcode/77/07/10570777/10570777-1-15.flv?e=ig8euxZM2rNcNbRa7WdVhoM17zUVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1570199622&gen=playurl&os=kodou&oi=1780887262&trid=574fe176f124472ba97fade93991f3feu&platform=pc&upsig=4f749582ffd27c3a61a722674179d697&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0","backup_url":null}]}'

r = re.search('"url":"(.*?)".*?"', tmp, re.S).group(1)
print(r)
