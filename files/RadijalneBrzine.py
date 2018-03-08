import numpy as np
from scipy.optimize import leastsq
import pylab as plt

c = 300000; P = 68.663; floor_P = np.floor(P)

JD, BC, HeI, Halfa = np.loadtxt('combi', usecols = (4, 5, 8, 9), unpack = True)
shift_Halfa = Halfa - 6562.8
shift_HeI = HeI - 6678.15

floor_JD = np.floor(JD)
faza2 = [0]*len(floor_JD)
faza = [0]*len(floor_JD)
for i in range(len(floor_JD)):
	n = int(floor_JD[i]/floor_P)
	faza[i] = (floor_JD[i] - n * floor_P) / floor_P
	faza2[i] = faza[i] + 1

vrad_Halfa = shift_Halfa / 6562.8 * c + BC
vrad_HeI = shift_HeI / 6678.15 * c + BC

plt.scatter(faza, vrad_Halfa, color = 'red')
plt.scatter(faza2, vrad_Halfa, color = 'red', label = 'H$_a$')
plt.scatter(faza, vrad_HeI, color = 'green')
plt.scatter(faza2, vrad_HeI, color = 'green', label = 'HeI')
plt.xlabel('Faza')
plt.ylabel('V$_{rad}$ [km/s]')
plt.legend(loc='upper right')

plt.savefig('./RadijalneBrzine.png')