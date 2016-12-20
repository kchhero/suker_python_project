# -*- coding: utf-8 -*-

import locale

def aaa() :
    ab = []
    r = ''
    lll = "10,23,29,33,37,40+16"
    
    ab = lll.split(',')
    templ = ab[-1].split('+')[0]
    bonus = ab[-1].split('+')[1]
    ab[-1] = templ
    print ab
    print bonus
    
    for i in ab:        
        r += i+' '
                  
    print r
#    print "bonus = " + ab[-1].split('+')[1]

def bbb() :
    nnn,stt = aaa()
    print nnn,stt

aaa()

