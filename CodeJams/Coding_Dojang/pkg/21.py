# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 10:07:42 2014

@author: choonghyun.jeon
"""

units_inch = ["2.54 cm","72 pt", "96 px"]
units_othersDic = {"cm":"10 mm", "pt":"20 dxa", "dxa":"635 emu"}

inParams = raw_input()
tempL = inParams.split('"')

print tempL[1], tempL[3]