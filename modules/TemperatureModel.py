from datetime import datetime
from meteostat import Point, Monthly
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

class TemperatureModel:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        start = datetime(1970, 1, 1)
        end = datetime(2021, 12, 31)
        testLocation = Point(lat, long)
        data = Monthly(testLocation, start, end)
        data = data.fetch()
        data.plot(y=['tavg'])
        plt.show()
        poly = PolynomialFeatures(degree=2)
        poly_features = poly.fit_transform([*range(1970, 2021, (1/12))].reshape(-1, 1))
        poly_reg_model = LinearRegression()
        poly_reg_model.fit(poly_features, data['tavg'])
        y_predicted = poly_reg_model.predict(poly_features)
        plt.scatter(data['time'], data['tavg'])
        plt.plot(data['time'], y_predicted, c="red")
        plt.show()

tm = TemperatureModel(48.404244, -4.484974)
