#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:26:39 2019

@author: khushi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path= '/home/khushi/Desktop/Work/PYTHON/'
file='Sample2.csv'

dataset=pd.read_csv(path+file)
DataArray=dataset.values
DAshape=np.shape(DataArray)
ntrails=DAshape[0]
narms=DAshape[1]


uniform=np.random.beta(1,1,10000)
plt.hist(uniform, normed=True)
import time
start_time=time.clock()
Array_trewards=[]

for k in range(1000):
    total_reward=0
    selected_arm=[]
    arm_win=[0]*narms
    arm_luz=[0]*narms
    
    for j in range(ntrails):
        maxprob=0
        for k in range(narms):
            prob=np.random.beta(arm_win[k]+1,arm_luz[k]+1,1)
            if prob>maxprob:
                maxprob=prob
                s_arm=k
        selected_arm.append(s_arm)
        reward=DataArray[j][s_arm]
        if reward==1:
            arm_win[s_arm]=arm_win[s_arm]+1
        else:
            arm_luz[s_arm]=arm_luz[s_arm]+1
            
        total_reward=total_reward+reward
    Array_trewards.append(total_reward)
end_time=time.clock() 
print(-start_time+end_time)

plt.hist(Array_trewards,normed=True)
plt.hist(RSArray_trewards,normed=True) 
max(Array_trewards)

sum()
plt.hist(selected_arm)
print(total_reward)
 
dataset.sum(axis=0)
print(np.sum(DataArray,axis=0))
