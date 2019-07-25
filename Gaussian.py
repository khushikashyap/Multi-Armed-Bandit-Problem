# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:28:46 2019

@author: Acer
"""
import numpy as np
import matplotlib.pyplot as plt

cc=np.random.normal(loc=2,scale=0.5,size=10000)

dd=np.linspace(np.min(cc),np.max(cc),1000)
mean=cc.mean()
sigma=cc.std()

def gauss(d, mean, sigma):
    pi=np.pi
    normd=2.*sigma*sigma
    cons=1./np.sqrt(normd*pi)
    func=cons*np.exp(-((d-mean)**2)/normd)
    return func

dis_Gaussian=gauss(dd,mean,sigma)

plt.plot(dd,dis_Gaussian)
plt.hist(cc, bins=49, normed=True)

