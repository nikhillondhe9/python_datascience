import numpy as np
import matplotlib.pyplot as plt


class MyPlot(object):

    def __init__(self):
        self.x = np.arange(0, 100)
        self.y = self.x*2
        self.z = self.x ** 2
        self.fig = plt.figure()

    def plot1(self):
        ax = self.fig.add_axes([0, 0, 1, 1])
        ax.set_title('Plot 1')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.plot(self.x, self.y)
        plt.tight_layout()
        plt.show()

    def internal_plot(self):
        ax1 = self.fig.add_axes([0, 0, 1, 1])
        ax2 = self.fig.add_axes([0.2, 0.5, 0.2, 0.2])
        ax1.set_title('External Plot ')
        ax1.set_xlabel('X axis')
        ax1.set_ylabel('Y axis')
        ax2.set_title('Internal Plot ')
        ax2.set_xlabel('X axis')
        ax2.set_ylabel('Y axis')
        ax1.plot(self.x, self.y)
        ax2.plot(self.x, self.y)
        plt.tight_layout()
        plt.show()

    def sub_plots(self):
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 2))
        ax[0].plot(self.x, self.y, lw=3, ls='--', color='red')
        ax[1].plot(self.x, self.z, lw=3, ls='--', color='blue')
        plt.show()


if __name__ == '__main__':
    myplot = MyPlot()
    while True:
        x = int(input('Enter number 1,2 or 3 for following plots: \n 1. Regular plot \n 2. Internal Plot \n 3. Sub plots'))  # NOQA
        if x not in range(1, 4):
            print('Enter number 1,2 & 3 only')
        else:
            if x == 1:
                myplot.plot1()
                break
            elif x == 2:
                myplot.internal_plot()
                break
            elif x == 3:
                myplot.sub_plots()
                break
