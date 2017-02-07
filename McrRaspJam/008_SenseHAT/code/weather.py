#setup the sense HAT
from sense_hat import SenseHat
hat = SenseHat()

#Write your code below

#Say hello
print("Manchester Raspberry Jam weather station")

#get the temperature
temperature = hat.get_temperature()
temperature = round(temperature, 1)
temperature = str(temperature)
print("Temperature: "+temperature+" Celsius")

#get the humidity
humidity = hat.get_humidity()
humidity = round(humidity, 1)
humidity = str(humidity)
print("Humidity: "+humidity+"% RH")

#get the atmoshpheric pressure
hat.get_pressure()
pressure = hat.get_pressure()
pressure = round(pressure, 1)
print("Pressure: "+str(pressure)+" millibars")
