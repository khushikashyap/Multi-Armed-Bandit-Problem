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
file='Sample2.csv'

dataset=pd.read_csv(path+file)
DataArray=dataset.values
DAshape=np.shape(DataArray)
ntrails=DAshape[0]
narms=DAshape[1]

uniform=np.random.beta(1,1,10000)
plt.hist(uniform, normed=True)
RSArray_trewards=[]

for k in range(1000):
    total_reward=0
    selected_arm=[]
    arm_win=[0]*narms
    arm_luz=[0]*narms

    for j in range(ntrails):
        s_arm= np.random.randint(0,10,1)
        selected_arm.append(s_arm)
        reward=DataArray[j][s_arm]
        total_reward=total_reward+reward[0]
    RSArray_trewards.append(total_reward)

plt.hist(RSArray_trewards,normed=True)
max(RSArray_trewards)


plt.hist(selected_arm)
print(total_reward)

dataset.sum(axis=0)
print(np.sum(DataArray,axis=0))