from datetime import datetime
from meteostat import Point, Daily
import matplotlib.pyplot as plt

#class TemperatureModel:
 #   def __init__(self, lat, long):
  #      self.lat = lat
   #     self.long = long
    #    request = f''
lat = 40
long = 40
start = datetime(1970, 1, 1)
end = datetime(2021, 12, 31)
testLocation = Point(49.2497, -123.1193, 70)
data = Daily(testLocation, start, end)
data = data.fetch()
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()

