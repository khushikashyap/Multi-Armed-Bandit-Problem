#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:55:09 2019

@author: khushi
"""


import matplotlib.pyplot as plt
import numpy as np

z=np.random.beta(1,1,10000)
mean=z.mean()
var=z.var()
def betadis(x, a, b):
    from scipy.special import beta
    numfx=x**(a-1)*(1-x)**(b-1)
    denfx=beta(a,b)
    return numfx/denfx
    mean=beta(a/a+b)
    var=beta(a*b)/(a+b)**2*(a+b+1)
    return mean,var
    
eps=0.0000001
zz=np.linspace(eps,1-eps,1000)
BetaFunc=betadis(zz,1,1)
plt.hist(z,bins=49,normed=True)
plt.plot(zz,BetaFunc)
plt.ylim(0,2.5)
