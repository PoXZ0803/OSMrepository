"""该代码用于生成表示单位区域edge总长度的.npz文件（精度为0.2），须在服务器上运行"""

import pandas as pd
import numpy as np
import os
import geopandas as gp
from shapely.geometry import Point

matrix = np.zeros((128, 292))
lv = 0.2
boundary_path = "world-administrative-boundaries-countries.geojson"
calif = gp.read_file(boundary_path)
polygon = calif["geometry"].iloc[0]
loadpath = '/workspace/aggregate_data/america_edges'
file_dir = os.listdir(loadpath)

for file in file_dir:
    lon = float(os.path.basename(file).split('_')[3]) - 0.1
    lat = float(os.path.basename(file).split('_')[1]) - 0.1
    col = int((lon + 125.2) // lv)
    row = int((49.6 - lat) // lv)
    if not Point(lon, lat).within(polygon):
        matrix[row][col] = -1  # 对于国境线以外的区域，将对应区域的值置为-1
        continue
    else:
        file1 = pd.read_csv(loadpath + '/' + file)
        edge_sum = 0
        for i in range(len(file1)):
            if col > 292 or row > 128:
                continue
            else:
                node = file1.loc[i]
                edge_sum = edge_sum + node['length']
    matrix[row][col] = edge_sum
    print(row, col, edge_sum, os.path.basename(file))
np.savez('edge_length_sum_0.2', matrix)

print('finished!')
