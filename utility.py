from apread import APReader
import numpy as np
import os
import matplotlib.pyplot as plt
from settings import *
from matplotlib_visualization import*
from scipy.fft import fft, fftfreq, rfft, rfftfreq
from scipy.signal import welch, find_peaks
plot_scale(1, title=1.5)


class VIV_files:
    def __init__(self, filename, starttimes, endtimes, title, samplingfreq=200):
        self.filename = filename
        self.measurements = APReader(path+filename)
        self.title = title
        self.starttimes = starttimes
        self.endtimes = endtimes
        self.means = {}
        self.std_devs = {}
        self.maxes = {}
        self.meanpeaks = {}
        self.sfreq = samplingfreq
        try:
            os.mkdir(towing_results)
        except FileExistsError:
            pass
    def plot_all_timeseries(self):
        for i in range(1, self.measurements.numChannels):
            fig = plt.figure()
            ax = plt.subplot(111)
            ax.plot(self.measurements.Channels[i].Time.data, self.measurements.Channels[i].data)
            fig.suptitle(self.title+"\n"+self.measurements.Channels[i].Name+" measurement - Full section")
            ax.set_xticks(np.arange(min(self.measurements.Channels[i].Time.data), max(self.measurements.Channels[i].Time.data) + 1, 5.0))
            ax.set_xlabel("Time [s]")
            ax.set_ylabel(self.measurements.Channels[i].unit)
            if self.measurements.Channels[i].Name != "Wave":
                ax.axvline(self.starttimes, ls="dotted", c="green", label="Data start")
                ax.axvline(self.endtimes, ls="dotted", c="red", label="Data end")
                ax.hlines(y=self.means[self.measurements.Channels[i].Name+" - Mean"], xmin=self.starttimes, xmax=self.endtimes, colors="red", label="Mean value \n ={} {}".format(round(self.means[self.measurements.Channels[i].Name+" - Mean"],2), self.measurements.Channels[i].unit))
                plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05), fancybox=True, shadow=True)
            plt.tight_layout()
            plt.savefig(towing_results+self.filename.lower().replace(".bin", "_")+self.measurements.Channels[i].Name+"_full_measurement.png")
            if show_plots:
                plt.show()
            else:
                plt.cla()
                fig.clear()
                plt.close('all')

    def plot_section_timeseries(self):
        for i in range(1, self.measurements.numChannels):
            fig = plt.figure()
            ax = plt.subplot(111)
            data = self.measurements.Channels[i].data[int(self.starttimes*self.sfreq):int(self.endtimes*self.sfreq)]
            time = self.measurements.Channels[i].Time.data[int(self.starttimes*self.sfreq):int(self.endtimes*self.sfreq)]
            peaks = find_peaks(data, height=np.mean(self.measurements.Channels[i].data[int(self.starttimes*self.sfreq):int(self.endtimes*self.sfreq)]))[0]
            ax.plot(self.measurements.Channels[i].Time.data[int(self.starttimes*self.sfreq):int(self.endtimes*self.sfreq)], self.measurements.Channels[i].data[int(self.starttimes*self.sfreq):int(self.endtimes*self.sfreq)])
            ax.scatter(time[peaks], data[peaks], color="red", alpha=0.5, s=25)
            fig.suptitle(self.title+"\n"+self.measurements.Channels[i].Name+" measurement - Utilized section")
            ax.set_xlabel("Time [s]")
            ax.set_ylabel(self.measurements.Channels[i].unit)

            mean = np.mean(self.measurements.Channels[i].data[int(self.starttimes*self.sfreq):int(self.endtimes*self.sfreq)])
            std_dev = np.std(self.measurements.Channels[i].data[int(self.starttimes*self.sfreq):int(self.endtimes*self.sfreq)], ddof=1)
            ax.axhline(y=mean, label="Mean value \n ={} {}".format(round(self.means[self.measurements.Channels[i].Name+" - Mean"],2), self.measurements.Channels[i].unit), c="red")
            plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05), fancybox=True, shadow=True)
            plt.tight_layout()
            plt.savefig(towing_results+self.filename.lower().replace(".bin", "_")+self.measurements.Channels[i].Name+"_valid_section.png")
            if show_plots:
                plt.show()
            else:
                fig.clear()
                plt.close(fig)
    def write_statistics(self):
        with open(towing_results+self.filename.lower().replace(".bin", ".txt"),"w") as f:
            f.write("\n -------------------\n"+self.title+"\n -------------------\n")
            f.write("Start time: {}\n".format(self.starttimes))
            f.write("End time: {}\n -------------------\n".format(self.endtimes))
            for i in range(1, self.measurements.numChannels):
                data_section = self.measurements.Channels[i].data[int(self.starttimes*self.sfreq):int(self.endtimes*self.sfreq)]
                f.write(self.measurements.Channels[i].Name+"\n -------------------\n")
                mean = np.mean(data_section)
                self.means[self.measurements.Channels[i].Name+" - Mean"] = mean
                f.write("Mean: {}\n".format(mean))
                std_dev = np.std(data_section, ddof=1)
                self.std_devs[self.measurements.Channels[i].Name+" - Std.dev"] = std_dev
                self.maxes[self.measurements.Channels[i].Name+" - abs(max)"] = np.max(np.abs(data_section))
                self.meanpeaks[self.measurements.Channels[i].Name+" - mean(peaks)"] = np.mean(data_section[find_peaks(data_section, height=mean)[0]])
                f.write("Std.dev: {}\n".format(std_dev))
                f.write("\n -------------------\n")

    def get_valid_measurements(self):
        data = [channel.data[int(self.starttimes*self.sfreq):int(self.endtimes*self.sfreq)] for channel in self.measurements.Channels]
        peaks = find_peaks(data)[0]
        name = [channel.Name for channel in self.measurements.Channels]
        return name, data, peaks



    def FFT(self, name_fft, plot=False, save=True):
        name = np.array([channel.Name for channel in self.measurements.Channels])
        idx = np.where(name==name_fft)[0][0]
        timeseries = self.measurements.Channels[idx].data
        dt = 1/self.sfreq
        norm_timeseries = timeseries-np.mean(timeseries)
        yf = rfft(norm_timeseries)
        xf = rfftfreq(n=len(norm_timeseries), d=dt)
        max_idx = np.argmax(xf)
        max_freq = np.abs(yf[max_idx])
        fig, ax = plt.subplots()
        ax.stem(xf, np.abs(yf), markerfmt=" ", label="Max freq: {:.2f}Hz".format(max_freq))
        ax.set_xlim(0, 10)
        plt.legend(loc="best")
        plt.title("Discrete fast fourier - {} \n V: {} m/s".format(name_fft, round(self.means["Speed - Mean"],2)))
        plt.ylabel("Frequency [Hz]")
        plt.tight_layout()
        if save:
            plt.savefig(towing_results+self.filename.lower().replace(".bin", "_")+name_fft+"_DFFT.png")
            if plot:
                plt.show()
            plt.close()
            plt.cla()
            plt.clf()

        return yf, xf

    def spectral_density(self, name_fft, plot=False, save=True):
        name = np.array([channel.Name for channel in self.measurements.Channels])
        idx = np.where(name == name_fft)[0][0]
        timeseries = self.measurements.Channels[idx].data
        norm_timeseries = timeseries-np.mean(timeseries)
        f, Pxx = welch(norm_timeseries, fs=self.sfreq, return_onesided=True, scaling="density", nperseg=2048)
        plt.plot(f, Pxx)
        #plt.ylim(0.5e-3, 10)
        plt.xlim(0, 10)
        plt.title("Spectral density - {} \n V: {} m/s".format(name_fft, round(self.means["Speed - Mean"],2)))
        plt.ylabel("Frequency [Hz]")
        plt.tight_layout()
        if save:
            plt.savefig(towing_results+self.filename.lower().replace(".bin", "_")+name_fft+"_spectrum.png")
            if plot:
                plt.show()
            plt.close()
            plt.cla()
            plt.clf()

        return Pxx, f


class Decay_test:
    def __init__(self, filename, starttimes, endtimes, title, sfreq=200):
        self.filename = filename
        self.measurements = APReader(filename)
        self.title = title
        self.starttimes = starttimes
        self.endtimes = endtimes
        self.sfreq = sfreq

        try:
            os.mkdir(towing_results)
        except FileExistsError:
            pass
    def plot_valid_sections(self):
        for i in range(1,7):
            plt.plot(self.measurements.Channels[0].data[int(self.starttimes[i-1]*self.sfreq):int(self.endtimes[i-1]*self.sfreq)], self.measurements.Channels[i].data[int(self.starttimes[i-1]*self.sfreq):int(self.endtimes[i-1]*self.sfreq)], linewidth=0.5)
            plt.title(self.measurements.Channels[i].Name + self.title)
            plt.show()
def ReducedVelocity(U, f, d):
    return U/(f*d)


import numpy as np
import matplotlib.pyplot as plt


def turningpoints(lst):
    dx = np.diff(lst)
    tps_dx = (dx[1:] * dx[:-1] < 0)
    tps = np.array([1], dtype=bool)
    tps1 = np.append(tps, tps_dx)
    tp = np.append(tps1, tps)
    return tp


def PQanalysisFun(t, x, plotflag):
    # PQ analysis
    # Inputs: time series t and motion history x. Note that x should have zero mean!
    # Outputs: coefficients P and Q, raw data xbar and dx, and indices tp for
    # all turning points (includes negatives!)

    if plotflag == 1:
        plt.figure()
        plt.subplot(1, 2, 1)
        plt.plot(t, x)
        plt.xlabel('t')
        plt.ylabel('x')

    tp = turningpoints(x)  # find turning point indices
    ttp1 = t[tp]
    xtp1 = x[tp]

    # select only positive turning points
    ttp = ttp1[xtp1 > 0]
    xtp = xtp1[xtp1 > 0]

    n = len(xtp)

    if n < 3:
        print('Error from PQanalysis: Not enough turning points identified')
        return 0

    if plotflag == 1:
        plt.plot(ttp, xtp, 'k.')

    # find the mean and differences
    xbar = 0.5 * (xtp[1:n - 1] + xtp[0:n - 2])
    dx = (xtp[0:n - 2] - xtp[1:n - 1]) / xbar

    # linear fit
    pcoeffs = np.polynomial.polynomial.polyfit(xbar, dx, 1)
    P = pcoeffs[0]  # P coefficient
    Q = pcoeffs[1]  # Q coefficient

    if plotflag == 1:
        plt.subplot(1, 2, 2)
        plt.plot(xbar, dx, 'b.')
        plt.plot(xbar, np.polynomial.polynomial.polyval(xbar, pcoeffs))
        plt.ylim(0, 0.3)

    return P, Q, xbar, dx, tp
