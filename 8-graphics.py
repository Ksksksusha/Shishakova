import matplotlib.pyplot as plt
import numpy as np

with open("settings.txt", "r") as settings:
    sett = [float(i) for i in settings.read().split("\n")]

#print(sett)

dac_v = np.loadtxt("data_volts.txt", dtype=int)
tmes  = np.loadtxt("data_times.txt", dtype=float)

volts = dac_v * sett[1]
#print(volts)
#print(tmes)

fig, ax = plt.subplots(figsize=[10, 8], dpi=400)

ax.set_title("Зарядка и разрядка конденсатора от времени в RC цепи")
#plt.scatter(tmes, volts, 5, 'r', 'D', label='Экспериментальные точки')
ax.set(xlabel='Время, с', ylabel='Напряжение, В')
#ax.plot(tmes, volts, markevery=0.01, label='')
#ax.plot(tmes, volts, 'D', markevery=0.04, label='Экспериментальные точки', markersize=4, color='r')

#plt.plot(x, y1, 'o-r', label='Экспериментальные точки')


ax.plot(tmes, volts, 'D-b',  markevery=0.04, label='Экспериментальные точки', markersize=4, markerfacecolor='r', mec = 'r')


ax.text(20,0.5,"Время зарядки  = 53.17 сек")
ax.text(20,0.4,"Время разрядки = 56.43 сек")


ax.grid(which='major')
ax.minorticks_on()
ax.grid(which='minor', linestyle=':')

ax.legend()
fig.savefig("test.png")
#fig.savefig("test.svg")
#plt.show()