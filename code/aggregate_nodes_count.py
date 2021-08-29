import os
import numpy as np
import csv
import codecs

sum_number = 0
for i in np.arange(24.0, 49.6, 0.2):
    i1 = format(i + 0.2, '.1f')
    i2 = format(i, '.1f')
    for j in np.arange(66.6, 125.4, 0.2):
        j1 = format(j, '.1f')
        j2 = format(j + 0.2, '.1f')
        if os.path.exists('nodes_{}000_{}000_-{}000_-{}000.csv'.format(i1, i2, j1, j2)):
            with open('nodes_{}000_{}000_-{}000_-{}000.csv'.format(i1, i2, j1, j2), 'r') as f:
                a = len(f.readlines())
                sum_number = sum_number + a
            #     ulist = [str(i1), ' ', str(i2), ' ', str(j1), ' ', str(j2), ' ', str(a), '\n']
            #     with open('count.txt', 'a', encoding='utf-8', newline='') as countfile:
            #         countfile.writelines(ulist)
            # f.close()

print(sum_number)