"""该代码用于生成表示单位区域node总数的.npz文件（精度可自行设定），须在服务器上运行"""

import pandas as pd
import numpy as np
import os
import math
import geopandas as gp
from shapely.geometry import Point

matrix = np.zeros((128, 292))
lv = 0.2
boundary_path = "world-administrative-boundaries-countries.geojson"
calif = gp.read_file(boundary_path)
polygon = calif["geometry"].iloc[0]
loadpath = '/workspace/aggregate_data/america_nodes'
file_dir = os.listdir(loadpath) 

for file in file_dir:
    file1 = pd.read_csv(loadpath + '/' + file)
    for i in range(len(file1)):
        if type(file1.loc[i][4]) == str or type(file1.loc[i][5]) == str:
            continue
        elif math.isnan(file1.loc[i][4]) or math.isnan(file1.loc[i][5]):
            continue
        else:
            col = int((file1.loc[i][4] + 125.2) // lv)
            row = int((49.6 - file1.loc[i][5]) // lv)
            if col > 292 or row > 128:
                continue
            elif not Point(file1.loc[i][4], file1.loc[i][5]).within(polygon):
                matrix[row][col] = -1
            else:
                matrix[row][col] = matrix[row][col] + 1
                print(row, col, os.path.basename(file))


np.savez('node_0.2', matrix)
print('finished!')
