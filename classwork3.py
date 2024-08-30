# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:53:05 2024

@author: Micaiah
"""
import numpy
import matplotlib.pyplot as plt
prog=(' Java', 'Python',' PHP', 'JavaScript', 'C#', 'C++')
larity=( 22.2, 17.6, 8.8, 8, 7.7, 6.7)
plt.barh(prog,larity)
plt.title("Popular programming languages")
plt.ylabel("Popularity amoung users")
plt.xlabel("Languages")