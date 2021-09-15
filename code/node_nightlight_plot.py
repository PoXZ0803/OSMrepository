"""该代码用于画出横坐标为单位区域节点数，纵坐标为对应区域在nightlight图像上的亮度的散点图，用于观察二者之间的关系"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from openpyxl import load_workbook


image = cv2.imread('crop_nightlight_-125.2_-66.8_24.0_49.6.png')
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # RGB 转为 HSV
H, S, V = cv2.split(HSV)

save_data = np.load("node_0.02.npz")
data = save_data['arr_0']
data_row = np.size(data, 0)
data_col = np.size(data, 1)
X = []
Y = []

for i in range(data_row):
    for j in range(data_col):
        if data[i][j] < 0:
            continue
        else:
            lon = j * 0.02 - 125.2
            lat = 49.6 - i * 0.02
            a = int(((lon - (-125.2)) / (125.2 - 66.8)) * 2190)
            b = int(((49.6 - lat) / (49.6 - 24.0)) * 960)
            X.append(data[i][j])
            Y.append(V[b][a])

plt.figure(dpi=600)
plt.scatter(X, Y, s=1)
plt.show()

# workbook = load_workbook(filename="sum2.xlsx")
# sheet = workbook["Sheet1"]
# x = sheet["B1:B24904"]
# y = sheet["A1:A24904"]
# alpha1 = sheet["C1:C24904"]
# X = []
# Y = []
# ALPHA = []
# for i in x:
#     for j in i:
#         X.append(j.value)
# for k in y:
#     for l in k:
#         Y.append(l.value)
# for m in alpha1:
#     for n in m:
#         ALPHA.append(n.value)
#
# print(len(X), len(Y), len(ALPHA))
#
# xplot = []
# yplot = []
# for i in range(len(X)):
#     startx = int(((X[i] - (-125.2)) / (125.2 - 66.8)) * 2190)
#     starty = int(((49.6 - Y[i]) / (49.6 - 24.0)) * 960)
#     if startx > 2190 or starty > 960:
#         continue
#     xplot.append(ALPHA[i])
#     yplot.append(V[starty][startx])
#
# plt.figure(dpi=600)
# plt.scatter(xplot, yplot, s=1)
# plt.show()
