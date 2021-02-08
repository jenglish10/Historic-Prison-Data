import csv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def is_int(num):
    try:
        int(num)
        return True
    except ValueError as e:
        return False

filename = "files/AdmissionBookA.csv"
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if not is_int(row[2]) or row[10] == '' or row[9] == '' or 'mos' in row[9]:
            continue
        x = int(row[2])
        y = int(row[10][0:1])
        z = row[9]
        if row[9][0::1] == ' ':
            z = z[1::]
        index = z.index('yr') - 1
        z = int(row[9][0:index])
        ax.scatter(x,y,z)

ax.set_xlabel('Age (yrs)')
ax.set_ylabel('Number of Convictions')
ax.set_zlabel('Sentence (yrs)')
plt.show()