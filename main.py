from tracemalloc import start
from xmlrpc.client import DateTime
import math
import numpy as np

import matplotlib as mpl

import matplotlib.pyplot as plt
import datetime
import spacepy
import magnetic

class MagnetAnalysis:
    datetimesLviv = []
    xLviv = []
    yLviv = []
    zLviv = []
    magLviv = []

    datetimesBucharest = []
    xBucharest = []
    yBucharest = []
    zBucharest = []
    magBucharest = []

    def load(self):
        ReadObj = magnetic.IAGA2002()
        ReadObj.read( "lvv20220808vmin.min" )
        self.datetimesLviv = ReadObj.get('DATETIME')
        self.xLviv = ReadObj.get('X')
        self.yLviv = ReadObj.get('Y')
        self.zLviv = ReadObj.get('Z')


        ReadObj2 = magnetic.IAGA2002()
        ReadObj2.read( "sua20220808pmin.min" )
        self.datetimesBucharest = ReadObj2.get('DATETIME')
        self.xBucharest = ReadObj2.get('X')
        self.yBucharest = ReadObj2.get('Y')
        self.zBucharest = ReadObj2.get('Z')

    def make_magnitudes(self):
        for i, x_component in enumerate(self.xLviv):
            mag = math.sqrt(x_component**2 + self.yLviv[i]**2 + self.zLviv[i]**2)
            self.magLviv.append(mag)

        for i, x_component in enumerate(self.xBucharest):
            mag = math.sqrt(x_component**2 + self.yBucharest[i]**2 + self.zBucharest[i]**2)
            self.magBucharest.append(mag)

    def make_datetime_succint(self):
        for i in range(len(self.datetimesLviv)):
            hourMinuteFormat = "%I-%M"
            self.datetimesLviv[i] = self.datetimesLviv[i].strftime(hourMinuteFormat)
        
        for i in range(len(self.datetimesBucharest)):
            hourMinuteFormat = "%I-%M"
            self.datetimesBucharest[i] = self.datetimesBucharest[i].strftime(hourMinuteFormat)
        
    def create_tick_spacing(self, every_x_amount):
        tickSpacing = []
        for i, datetime in enumerate(self.datetimesLviv):
            if i % every_x_amount == 0:
                tickSpacing.append(i)

        return tickSpacing


    def run(self):
        self.load()
        self.make_magnitudes()
        #self.make_datetime_succint()
        #tickSpacing = self.create_tick_spacing(120)

        fig, axs = plt.subplots(2,1)
        #start_time = datetime.datetime(2022, 8, 8, 0, 0)
        #end_time = datetime.datetime(2022, 8, 8, 12, 0)
        #axs[0].set_xlim(start_time.strftime("%I-%M"), end_time.strftime("%I-%M"))
        axs[0].set_title('Lviv, Ukraine (Variance)')
        axs[0].set_xlabel('Date Time')
        axs[0].set_ylabel('Magnetometer Magnitude')
        axs[0].plot(self.datetimesLviv, self.magLviv)
        #axs[1].set_xlim(start_time.strftime("%I-%M"), end_time.strftime("%I-%M"))
        axs[1].set_title('Bucharest, Romania (Provisional)')
        axs[1].set_xlabel('Date Time')
        axs[1].set_ylabel('Magnetometer Magnitude')
        axs[1].plot(self.datetimesBucharest, self.magBucharest)
        fig.savefig('full_figure.png')
        fig.show()
        plt.show()


if __name__ == "__main__":
    analysis = MagnetAnalysis()
    analysis.run()
