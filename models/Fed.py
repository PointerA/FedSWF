#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import copy
import torch
from torch import nn
import numpy as np
import random

def FedAvg(w):
    w_avg = copy.deepcopy(w[0])
    for k in w_avg.keys():
        for i in range(1, len(w)):
            w_avg[k] += w[i][k]
        w_avg[k] = torch.div(w_avg[k], len(w))
    return w_avg

def FedSideWindow(w):
    w_temp = copy.deepcopy(w)
    s = len(w)
    for i in range(1,s):
        w_i_temp = []
    
        random_choice = np.random.choice(range(s), 9, replace=False)
        if i not in set(random_choice):
            random_choice[8] = i
        random_choice = set(random_choice)
        random_choice.remove(i)
        random_choice = list(random_choice)
        
        for t in range(4):
            temp = copy.deepcopy(w[i])
            for k in temp.keys():
                for j in range(3):
                    temp[k] += w[random_choice[j]][k]
                temp[k] = torch.div(temp[k], 4)
            w_i_temp.append(temp)
            random.shuffle(random_choice)
        for t in range(4):
            temp = copy.deepcopy(w[i])
            for k in temp.keys():
                for j in range(5):
                    temp[k] += w[random_choice[j]][k]
                temp[k] = torch.div(temp[k], 6)
            w_i_temp.append(temp)
            random.shuffle(random_choice)
        
        divs = []
        vector1 = torch.tensor([]) 
        for k in w[0].keys():
            vector1 = torch.cat((vector1, torch.flatten(w_temp[0][k].cpu())))
        for t in range(8):
            vector2 = torch.tensor([])
            for k in w_i_temp[t].keys():
                vector2 = torch.cat((vector2, torch.flatten(w_i_temp[t][k].cpu())))
            divs.append(np.linalg.norm(vector1 - vector2,ord=2))

        min_idx = np.argmin(divs)
        w_temp[i] = copy.deepcopy(w_i_temp[min_idx])
    
    return FedAvg(w_temp)
    
