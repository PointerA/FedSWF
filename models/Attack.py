#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import copy
import torch
import numpy as np
import random



def attack_by_flip(w, idxs_users, attackers):
    w_attacked = copy.deepcopy(w)

    for i in range(len(w_attacked)):
        if(idxs_users[i] in set(attackers)):
            for k in w_attacked[i].keys():
                w_attacked[i][k] = -w_attacked[i][k]
                    
    return w_attacked