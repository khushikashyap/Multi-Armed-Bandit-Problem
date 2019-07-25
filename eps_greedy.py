#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:31:29 2019

@author: khushi
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path= '/home/khushi/Desktop/Work/PYTHON/'
file='Sample1.csv'

dataset=pd.read_csv(path+file)
DataArray=dataset.values
DAshape=np.shape(DataArray)
ntrails=DAshape[0]
narms=DAshape[1]


uniform=np.random.beta(1,1,10000)
plt.hist(uniform, normed=True)
for k in range(1000):
    total_reward=0
    selected_arm=[]

    arm_win=[0]*narms
    arm_luz=[0]*narms
    eps=0.1

    s_arm= list(np.random.randint(0,10,1))

    selected_arm.append(s_arm)
    arm=list(range(0,10))

            
    for j in range(ntrails):
        reward=DataArray[j][s_arm[0]]
        if reward==1:
            x=np.random.uniform(0,1,1)   
            if x<eps:
                d_arm=list(set(arm)-set(s_arm))
                s_arm= [d_arm[np.random.randint(0,9,1).astype('int64')[0]]]
                if reward==0:
                    d_arm=list(set(arm)-set(s_arm)) 
                    s_arm= [d_arm[np.random.randint(0,9,1).astype('int64')[0]]]
        
        total_reward=total_reward+reward
        selected_arm.append(s_arm)
        
plt.hist(selected_arm)
print(total_reward)

dataset.sum(axis=0)
print(np.sum(DataArray,axis=0))