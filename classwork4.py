# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:55:07 2024

@author: Micaiah
"""
import numpy as np
import matplotlib.pyplot as plt


means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_men = [4, 3, 4, 1, 5]
std_women = [3, 5, 2, 3, 3]
ind = np.arange(len(means_men))
width = 0.35
fig, ax = plt.subplots()
bars_men = ax.bar(ind,means_men, width, label='Men', color='blue')
bars_women = ax.bar(ind, means_women, width, bottom=means_men,  label='Women', color='orange')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'))
ax.legend()

plt.show()


