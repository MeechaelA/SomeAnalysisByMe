import numpy as np
import matplotlib.pyplot as plt
import spacepy
import magnetic

class MagnetAnalysis:
    xLviv = 0
    yLviv = 0
    zLviv = 0
    xBucharest = 0
    yBucharest = 0
    zBucharest = 0

    def load(self):
        ReadObj = magnetic.IAGA2002()
        ReadObj.read( "lvv20220808vmin.min" )
        self.xLviv = ReadObj.get('X')
        self.yLviv = ReadObj.get('Y')
        self.zLviv = ReadObj.get('Z')


        ReadObj2 = magnetic.IAGA2002()
        ReadObj2.read( "sua20220808pmin.min" )
        self.xBucharest = ReadObj2.get('X')
        self.yBucharest = ReadObj2.get('Y')
        self.zBucharest = ReadObj2.get('Z')

    def run(self):
        self.load()
        print(self.xLviv)


if __name__ == "__main__":
    analysis = MagnetAnalysis()
    analysis.run()
