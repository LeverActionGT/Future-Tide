from datetime import datetime

import pandas as pd
from meteostat import Point, Daily
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

class TemperatureModel:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        start = datetime(2019, 1, 1)
        end = datetime(2019, 12, 31)
        testLocation = Point(lat, long)
        data = Daily(testLocation, start, end)
        data = data.fetch()
        sum1 = sum(data['tavg'])/len(data['tavg'])
        print(sum1)
        print(data['tavg'])

tm = TemperatureModel(48.404244, -4.484974)
