# -*- coding: utf-8 -*-
"""
Created on Thu Feb 06 14:14:52 2014

@author: choonghyun.jeon
"""

import sys

linuxMark = '/'
winMark = '\\'

def getDirMark() :
    if sys.platform=='linux2' :
        return linuxMark
    else :
        return winMark