"""该代码用于画表示美国单位区域节点个数的散点图，支持sum.xlsx和.npz文件格式的输入"""

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from openpyxl import load_workbook


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap


workbook = load_workbook(filename="node_0.2_alpha.xlsx")
sheet = workbook["Sheet1"]
x = sheet["B1:B19822"]
y = sheet["A1:A19822"]
alpha1 = sheet["C1:C19822"]
X = []
Y = []
COLOR = []
cmap = plt.get_cmap('Reds')
new_cmap = truncate_colormap(cmap, 0.15, 0.9)  # 可通过调整cmap画出不同颜色的散点图

for i in x:
    for j in i:
        X.append(j.value)
for k in y:
    for l in k:
        Y.append(l.value)
for m in alpha1:
    for n in m:
        COLOR.append(n.value)

# save_data = np.load("filter_0.02.npz")
# data = save_data['arr_0']
# data_row = np.size(data, 0)
# data_col = np.size(data, 1)
# lat = []
# lon = []
# color = []
#
# for i in range(data_row):
#     for j in range(data_col):
#         if data[i][j] < 0:
#             continue
#         else:
#             a = i * 0.02 - 125.2
#             b = j * 0.02 + 24.0
#             lon.append(a)
#             lat.append(b)
#             color.append(data[i][j])

plt.figure(figsize=(87.6, 38.4), dpi=600)
plt.scatter(X, Y, c=COLOR, s=64, cmap=new_cmap)  # 可在此调整散点大小

plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.xlim(-125.2, -66.8)
plt.ylim(24.0, 49.6)
plt.savefig('node_plot_0.2_s=64_red.pdf', bbox_inches='tight', pad_inches=0)  # 此处存在问题：无法保存为jpg或png格式
# plt.show()
