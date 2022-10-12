from apread import APReader
from utility import Decay_test
import matplotlib.pyplot as plt
from matplotlib_visualization import plot_scale
import numpy as np

plt.style.use("seaborn")
plt.rcParams["figure.figsize"] = (15, 3)
plot_scale(1, title=1.5)

sfreq = 200  # Hz

folder = "Decay\\"
filename_air = "decay_air.bin"
filename_water = "decay_water.bin"
##

d_air = Decay_test(folder+filename_air, starttimes=[20,240,590,1010,1510,1900], endtimes=[230, 590, 1000, 1520, 1800, 2190], title="Decay test air")

##
channels = [i for i in range(1,7)]

for channel in channels:
    plt.plot(d_air.measurements.Channels[0].data, d_air.measurements.Channels[channel].data, linewidth=0.5)
    plt.axvline(x=d_air.measurements.Channels[0].data[int(d_air.starttimes[channel-1]*sfreq)], ls="dotted", c="red")
    plt.axvline(x=d_air.measurements.Channels[0].data[int(d_air.endtimes[channel-1]*sfreq)], ls="dotted", c="red")
    plt.title(d_air.measurements.Channels[channel].Name + d_air.title)
    plt.show()

d_air.plot_valid_sections()

##
d_water = Decay_test(folder+filename_water, starttimes=[0,0,0,0,0,0], endtimes=[69, 69, 69, 69, 69, 69], title="Decay test water")

debug = True