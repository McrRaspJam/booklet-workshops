#setup the sense HAT
from sense_hat import SenseHat
hat = SenseHat()

#get acceleration data in G's
acceleration = hat.get_accelerometer_raw()
#round values to 1.d.p.
acceleration['x'] = round(acceleration['x'], 1)
acceleration['y'] = round(acceleration['y'], 1)
acceleration['z'] = round(acceleration['z'], 1)
print(acceleration)

