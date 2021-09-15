"""该代码用于画出横坐标为节点数/节点数区间，纵坐标为亮度的箱线图"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('crop_nightlight.png')
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # RGB 转为 HSV
H, S, V = cv2.split(HSV)

save_data = np.load("node_0.02.npz")
data = save_data['arr_0']
data_row = np.size(data, 0)
data_col = np.size(data, 1)


box1 = []
box2 = []
box3 = []
box4 = []
box5 = []
box6 = []
box7 = []
for i in range(data_row):
    for j in range(data_col):
        lon = j * 0.02 - 125.2
        lat = 49.6 - i * 0.02
        a = int(((lon - (-125.2)) / (125.2 - 66.8)) * 2190)
        b = int(((49.6 - lat) / (49.6 - 24.0)) * 960)
        if 0 <= data[i][j] < 10:
            box1.append(V[b][a])
        elif 10 <= data[i][j] < 20:
            box2.append(V[b][a])
        elif 20 <= data[i][j] < 50:
            box3.append(V[b][a])
        elif 50 <= data[i][j] < 100:
            box4.append(V[b][a])
        elif 100 <= data[i][j] < 200:
            box5.append(V[b][a])
        elif 200 <= data[i][j] < 400:
            box6.append(V[b][a])
        elif data[i][j] >= 400:
            box7.append(V[b][a])
        else:
            continue
        # if data[i][j] == 0:
        #     box1.append(V[b][a])
        # elif data[i][j] == 10:
        #     box2.append(V[b][a])
        # elif data[i][j] == 20:
        #     box3.append(V[b][a])
        # elif data[i][j] == 50:
        #     box4.append(V[b][a])
        # elif data[i][j] == 100:
        #     box5.append(V[b][a])
        # elif data[i][j] == 200:
        #     box6.append(V[b][a])
        # elif data[i][j] == 400:
        #     box7.append(V[b][a])
        # else:
        #     continue

plt.figure(figsize=(18, 10))  # 设置画布的尺寸
plt.title('Examples of boxplot', fontsize=20)  # 标题，并设定字号大小
plt.xlabel('nodes number per unit area')
plt.ylabel('luminance')
# labels = '0', '10', '20', '50', '100', '200', '400'
labels = '0-10', '10-20', '20-50', '50-100', '100-200', '200-400', '400+'  # 图例
plt.boxplot([box1, box2, box3, box4, box5, box6, box7], showfliers=False, labels=labels)
plt.show()

