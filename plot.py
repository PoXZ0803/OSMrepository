import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook


workbook = load_workbook(filename="count2.xlsx")
sheet = workbook["Sheet1"]
x = sheet["B1:B1817"]
y = sheet["A1:A1817"]
alpha1 = sheet["H1:H1817"]
X = []
Y = []
ALPHA = []
for i in x:
    for j in i:
        X.append(j.value)
for k in y:
    for l in k:
        Y.append(l.value)
for m in alpha1:
    for n in m:
        ALPHA.append(n.value)
print(X)
print(Y)
print(ALPHA)
plt.figure(figsize=(6.2, 14.6))
for t in range(1817):
    plt.scatter(X[t], Y[t], s=36, c='b',alpha=ALPHA[t])


# plt.xlim(-76.2,-66.6)
# plt.ylim(24.0,49.6)
plt.xlim(-76.2,-70)
plt.ylim(35.0,49.6)

# my_x_ticks = np.arange(-76.2, -66.6, 0.4)
# x_ticks = np.linspace(-77, -66, 10)
# y_ticks = np.linspace(10, 50, 10)
# my_y_ticks = np.arange(24.0,49.2, 2)
# plt.xticks(x_ticks)
# plt.yticks(y_ticks)
plt.show()
