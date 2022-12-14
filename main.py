##
import os
import matplotlib.pyplot as plt

from utility import *
from matplotlib_visualization import *

plt.style.use("seaborn")
plt.rcParams["figure.figsize"] = (15, 3)
plot_scale(1, title=1.5)

try:
    os.mkdir(results)
except FileExistsError:
    pass

##
# VIV velocity 0.2 m/s - 1st run
viv_0_2_n1 = VIV_files("viv_0_2_n1.bin", starttimes=29.8, endtimes=111.6, title="Velocity: 0.2 m/s")
viv_0_2_n1.write_statistics()
viv_0_2_n1.plot_all_timeseries()
viv_0_2_n1.plot_section_timeseries()
viv_0_2_n1_time = viv_0_2_n1.measurements.Channels[0]


##
# VIV velocity 0.3 m/s - 1st run
viv_0_3_n1 = VIV_files("viv_0_3_n1.bin", starttimes=10.1, endtimes=65.2, title="Velocity: 0.3 m/s")
viv_0_3_n1.write_statistics()
viv_0_3_n1.plot_all_timeseries()
viv_0_3_n1.plot_section_timeseries()

##
# VIV velocity 0.4 m/s - 1st run
viv_0_4_n1 = VIV_files("viv_0_4_n1.bin", starttimes=15, endtimes=55, title="Velocity: 0.4 m/s")
viv_0_4_n1.write_statistics()
viv_0_4_n1.plot_all_timeseries()
viv_0_4_n1.plot_section_timeseries()

##
# VIV velocity 0.5 m/s - 1st run
viv_0_5_n1 = VIV_files("viv_0_5_n1.bin", starttimes=12, endtimes=44.5, title="Velocity: 0.5 m/s")
viv_0_5_n1.write_statistics()
viv_0_5_n1.plot_all_timeseries()
viv_0_5_n1.plot_section_timeseries()

##
# VIV velocity 0.6 m/s - 1st run
viv_0_6_n1 = VIV_files("viv_0_6_n1.bin", starttimes=20, endtimes=39.7, title="Velocity: 0.6 m/s")
viv_0_6_n1.write_statistics()
viv_0_6_n1.plot_all_timeseries()
viv_0_6_n1.plot_section_timeseries()

##
# VIV velocity 0.7 m/s - 1st run
viv_0_7_n1 = VIV_files("viv_0_7_n1.bin", starttimes=18, endtimes=35.4, title="Velocity: 0.7 m/s")
viv_0_7_n1.write_statistics()
viv_0_7_n1.plot_all_timeseries()
viv_0_7_n1.plot_section_timeseries()

##
# VIV velocity 0.75 m/s - 1st run
viv_0_75_n1 = VIV_files("viv_0_75_n1.bin", starttimes=17.0, endtimes=33.62, title="Velocity: 0.75 m/s")
viv_0_75_n1.write_statistics()
viv_0_75_n1.plot_all_timeseries()
viv_0_75_n1.plot_section_timeseries()

##
# VIV velocity 0.8 m/s - 1st run
viv_0_8_n1 = VIV_files("viv_0_8_n1.bin", starttimes=19, endtimes=33.5, title="Velocity: 0.8 m/s")
viv_0_8_n1.write_statistics()
viv_0_8_n1.plot_all_timeseries()
viv_0_8_n1.plot_section_timeseries()

##
# VIV velocity 0.83 m/s - 1st run
viv_0_83_n1 = VIV_files("viv_0_83_n1.bin", starttimes=19, endtimes=31.5, title="Velocity: 0.83 m/s")
viv_0_83_n1.write_statistics()
viv_0_83_n1.plot_all_timeseries()
viv_0_83_n1.plot_section_timeseries()

##
# VIV velocity 0.84 m/s - 1st run
viv_0_84_n1 = VIV_files("viv_0_84_n1.bin", starttimes=18, endtimes=29.5, title="Velocity: 0.84 m/s")
viv_0_84_n1.write_statistics()
viv_0_84_n1.plot_all_timeseries()
viv_0_84_n1.plot_section_timeseries()
viv_0_84_n1.spectral_density("1Y", plot=True)
viv_0_84_n1.spectral_density("1X", plot=True)
viv_0_84_n1.spectral_density("2Y", plot=True)
viv_0_84_n1.spectral_density("2X", plot=True)
viv_0_84_n1.spectral_density("3Y", plot=True)
viv_0_84_n1.spectral_density("3X", plot=True)
viv_0_84_n1.FFT("1Y", plot=True)
viv_0_84_n1.FFT("1X", plot=True)
viv_0_84_n1.FFT("2Y", plot=True)
viv_0_84_n1.FFT("2X", plot=True)
viv_0_84_n1.FFT("3Y", plot=True)
viv_0_84_n1.FFT("3X", plot=True)


##
# VIV velocity 0.84 m/s - 2nd run
viv_0_84_n2 = VIV_files("viv_0_84_n2_001.bin", starttimes=21.5, endtimes=31.5, title="Velocity: 0.84 m/s")
viv_0_84_n2.write_statistics()
viv_0_84_n2.plot_all_timeseries()
viv_0_84_n2.plot_section_timeseries()

##
# VIV velocity 0.84 m/s - 3rd run
viv_0_84_n3 = VIV_files("viv_0_84_n3.bin", starttimes=22.5, endtimes=31, title="Velocity: 0.84 m/s")
viv_0_84_n3.write_statistics()
viv_0_84_n3.plot_all_timeseries()
viv_0_84_n3.plot_section_timeseries()

##
# VIV velocity 0.84 m/s - 4th run
viv_0_84_n4 = VIV_files("viv_0_84_n4.bin", starttimes=22, endtimes=32, title="Velocity: 0.84 m/s")
viv_0_84_n4.write_statistics()
viv_0_84_n4.plot_all_timeseries()
viv_0_84_n4.plot_section_timeseries()

##
# VIV velocity 0.84 m/s - 5th run
viv_0_84_n5 = VIV_files("viv_0_84_n5.bin", starttimes=23, endtimes=31, title="Velocity: 0.84 m/s")
viv_0_84_n5.write_statistics()
viv_0_84_n5.plot_all_timeseries()
viv_0_84_n5.plot_section_timeseries()

##

# VIV velocity 0.84 m/s - 1st freq. change run
viv_0_84_5hz = VIV_files("viv_0_84_5Hz_BE0_5Hz.bin", starttimes=20, endtimes=31, title="Velocity: 0.84 m/s", samplingfreq=5)
viv_0_84_5hz.write_statistics()
viv_0_84_5hz.plot_all_timeseries()
viv_0_84_5hz.plot_section_timeseries()

##

# VIV velocity 0.84 m/s - 2nd freq. change run
viv_0_84_10hz = VIV_files("viv_0_84_10Hz_BE1_25Hz.bin", starttimes=18, endtimes=31, title="Velocity: 0.84 m/s", samplingfreq=10)
viv_0_84_10hz.write_statistics()
viv_0_84_10hz.plot_all_timeseries()
viv_0_84_10hz.plot_section_timeseries()

##

# VIV velocity 0.84 m/s - 3rd freq. change run
viv_0_84_20hz = VIV_files("viv_0_84_20Hz_BE2_5Hz.bin", starttimes=23, endtimes=32, title="Velocity: 0.84 m/s", samplingfreq=20)
viv_0_84_20hz.write_statistics()
viv_0_84_20hz.plot_all_timeseries()
viv_0_84_20hz.plot_section_timeseries()

##

# VIV velocity 0.84 m/s - 4th freq. change run
viv_0_84_50 = VIV_files("viv_0_84_50Hz_BU5Hz.bin", starttimes=22, endtimes=32, title="Velocity: 0.84 m/s", samplingfreq=50)
viv_0_84_50.write_statistics()
viv_0_84_50.plot_all_timeseries()
viv_0_84_50.plot_section_timeseries()

##

# VIV velocity 0.84 m/s - 5th freq. change run
viv_0_84_100Hz = VIV_files("viv_0_84_100Hz_BU10Hz.bin", starttimes=18, endtimes=29.5, title="Velocity: 0.84 m/s", samplingfreq=100)
viv_0_84_100Hz.write_statistics()
viv_0_84_100Hz.plot_all_timeseries()
viv_0_84_100Hz.plot_section_timeseries()

##
# VIV velocity 0.85 m/s - 1st run
viv_0_85_n1 = VIV_files("viv_0_85_n1.bin", starttimes=24, endtimes=31.4, title="Velocity: 0.85 m/s")
viv_0_85_n1.write_statistics()
viv_0_85_n1.plot_all_timeseries()
viv_0_85_n1.plot_section_timeseries()


##
# VIV velocity 0.88 m/s - 1st run
viv_0_88_n1 = VIV_files("viv_0_88_n1.bin", starttimes=23, endtimes=30.8, title="Velocity: 0.88 m/s")
viv_0_88_n1.write_statistics()
viv_0_88_n1.plot_all_timeseries()
viv_0_88_n1.plot_section_timeseries()


##
# VIV velocity 0.9 m/s - 1st run
viv_0_9_n1 = VIV_files("viv_0_9_n1.bin", starttimes=15.4, endtimes=31.5, title="Velocity: 0.9 m/s")
viv_0_9_n1.write_statistics()
viv_0_9_n1.plot_all_timeseries()
viv_0_9_n1.plot_section_timeseries()

##
# VIV velocity 1.0 m/s - 1st run
viv_1_0_n1 = VIV_files("viv_1_0_n1.bin", starttimes=21, endtimes=29.4, title="Velocity: 1.0 m/s")
viv_1_0_n1.write_statistics()
viv_1_0_n1.plot_all_timeseries()
viv_1_0_n1.plot_section_timeseries()

##
# VIV velocity 1.1 m/s - 1st run
viv_1_1_n1 = VIV_files("viv_1_1_n1.bin", starttimes=17.2, endtimes=29.5, title="Velocity: 1.1 m/s")
viv_1_1_n1.write_statistics()
viv_1_1_n1.plot_all_timeseries()
viv_1_1_n1.plot_section_timeseries()

##
# VIV velocity 1.2 m/s - 1st run
viv_1_2_n1 = VIV_files("viv_1_2_n1.bin", starttimes=24, endtimes=28.7, title="Velocity: 1.2 m/s")
viv_1_2_n1.write_statistics()
viv_1_2_n1.plot_all_timeseries()
viv_1_2_n1.plot_section_timeseries()

##
# VIV velocity 1.3 m/s - 1st run
viv_1_3_n1 = VIV_files("viv_1_3_n1.bin", starttimes=17.8, endtimes=24.9, title="Velocity: 1.3 m/s")
viv_1_3_n1.write_statistics()
viv_1_3_n1.plot_all_timeseries()
viv_1_3_n1.plot_section_timeseries()


##
# VIV velocity 1.4 m/s - 1st run
viv_1_4_n1 = VIV_files("viv_1_4_n1.bin", starttimes=16.2, endtimes=22.5, title="Velocity: 1.4 m/s")
viv_1_4_n1.write_statistics()
viv_1_4_n1.plot_all_timeseries()
viv_1_4_n1.plot_section_timeseries()

##
# VIV velocity 1.5 m/s - 1st run
viv_1_5_n1 = VIV_files("viv_1_5_n1.bin", starttimes=17.0, endtimes=23.4, title="Velocity: 1.5 m/s")
viv_1_5_n1.write_statistics()
viv_1_5_n1.plot_all_timeseries()
viv_1_5_n1.plot_section_timeseries()

runs = [viv_0_2_n1, viv_0_3_n1, viv_0_4_n1, viv_0_5_n1, viv_0_6_n1, viv_0_7_n1, viv_0_75_n1, viv_0_8_n1, viv_0_83_n1, viv_0_84_n1, viv_0_85_n1, viv_0_88_n1, viv_0_9_n1, viv_1_0_n1, viv_1_1_n1, viv_1_2_n1, viv_1_3_n1, viv_1_4_n1, viv_1_5_n1]

speed_means = np.array([run.means["Speed - Mean"] for run in runs])
X1_means = np.array([run.means["1X - Mean"] for run in runs])
X2_means = np.array([run.means["2X - Mean"] for run in runs])
X3_means = np.array([run.means["3X - Mean"] for run in runs])
Y1_meanpeaks = np.array([run.meanpeaks["1Y - mean(peaks)"] for run in runs])
Y2_meanpeaks = np.array([run.meanpeaks["2Y - mean(peaks)"] for run in runs])
Y3_meanpeaks = np.array([run.meanpeaks["3Y - mean(peaks)"] for run in runs])

fig, ax = plt.subplots()
ax.plot(speed_means, Y2_meanpeaks)
plt.show()


"""
To do list:
**
to lower p?? filenavn

**
Make plot of maximum moment versus reduced velocity

**
Make FFT showing that inline has twice the freq compared to cross-flow

**
Test application of different butterworth filters to isolate relevant freq. content

**
Finding steady state and finding amplitude from mean. Do testing on this amplitude
- Code for peak identification in Design of ocean structures
"""