# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

# Read data from text file
with open('/Users/brandonsamuelr/Downloads/b1_num_test.txt', 'r') as file:
    data = file.readlines()

# Extract variables from data
x = []
b1 = []
b1_est = []
for line in data:
    cols = line.split()
    x.append(float(cols[0]))
    b1.append(float(cols[1]))
    b1_est.append(float(cols[2]))

# Plot variables against x
plt.plot(x, b1, label='b1')
plt.plot(x, b1_est, label='b1_est')
plt.xlabel('2x')
plt.ylabel('b1 /b1 estimate')
plt.title('')
plt.legend()
plt.show()

#%% Polarization along the virtual photon
with open('/Users/brandonsamuelr/Downloads/qpol_data_highQ.txt', 'r') as file:
    data = file.readlines()

# Extract variables from data
x = []
b1 = []
b1_est = []
for line in data:
    cols = line.split()
    x.append(float(cols[0]))
    b1.append(float(cols[1]))
    b1_est.append(float(cols[2]))
    
with open('/Users/brandonsamuelr/Downloads/pole_data_highQ.txt', 'r') as file:
    data = file.readlines()

# Extract variables from data
x2 = []
b12 = []
b12_est = []
for line in data:
    cols = line.split()
    x2.append(float(cols[0]))
    b12.append(float(cols[1]))
    b12_est.append(float(cols[2]))

# Plot variables against x
plt.plot(x, b1, label='b1', color = 'b')
plt.plot(x, b1_est, label='b1 estimate polq')
plt.title('')
plt.plot(x2, b12, color = 'b' )
plt.plot(x2, b12_est, label='b1 estimate pole')
plt.xlabel('2x')
plt.ylabel('b1 /b1 estimate')
plt.title('')
plt.legend()



'''
plt.figure()
# high Q2
plt.figure()
with open('/Users/brandonsamuelr/Downloads/b1_compare_polq_highQ2.txt', 'r') as file:
    data = file.readlines()

# Extract variables from data
x_hiq = []
b1_hiq = []
b1_est_hiq = []
for line in data:
    cols = line.split()
    x_hiq.append(float(cols[0]))
    b1_hiq.append(float(cols[1]))
    b1_est_hiq.append(float(cols[2]))

# Plot variables against x
plt.plot(x_hiq, b1_hiq, label='b1')
plt.plot(x_hiq, b1_est_hiq, label='b1_est')
plt.xlabel('2x')
plt.ylabel('b1 /b1 estimate')
plt.title('')
plt.legend()
plt.show()
'''
#%%

'''

# high Q2
plt.figure()
with open('/Users/brandonsamuelr/Downloads/b1_compare_polq_highQ2100', 'r') as file:
    data = file.readlines()

# Extract variables from data
x_hiq = []
b1_hiq = []
b1_est_hiq = []
for line in data:
    cols = line.split()
    x_hiq.append(float(cols[0]))
    b1_hiq.append(float(cols[1]))
    b1_est_hiq.append(float(cols[2]))

# Plot variables against x
plt.plot(x_hiq, b1_hiq, label='b1')
plt.plot(x_hiq, b1_est_hiq, label='b1_est')
plt.xlabel('2x')
plt.ylabel('b1 /b1 estimate')
plt.title('')
plt.legend()
plt.show()
'''