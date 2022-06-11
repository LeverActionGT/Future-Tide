from datetime import datetime

import pandas as pd
from meteostat import Point, Monthly
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

class TemperatureModel:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        #start = datetime(1970, 1, 1)
        #end = datetime(2021, 12, 31)
        #testLocation = Point(lat, long)
        #data = Monthly(testLocation, start, end)
        #data = data.fetch()
        #data.plot(y=['tavg'])
        #plt.show()
        df = pd.read_csv('Brest.csv')
        poly = PolynomialFeatures(degree=2)
        x = np.arange(1, 624, 1)
        y = df['tavg']
        print(len(x))
        print(len(y))
        x = np.array(x).reshape(-1, 1)
        y = np.array(np.nan_to_num(df['tavg'])).reshape(624, 1)
        print(x.shape)
        print(y.shape)
        poly_features = poly.fit_transform(np.array(x).reshape(1, -1))
        
        poly_reg_model = LinearRegression()
        poly_reg_model.fit(poly_features, y)
        y_predicted = poly_reg_model.predict(poly_features)
        plt.scatter(poly_features, y)
        plt.plot(poly_features, y_predicted, c="red")
        plt.show()

tm = TemperatureModel(48.404244, -4.484974)
