import smbus
import math
import time

# Guc yonetim register'lari
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
 return bus.read_byte_data(address, adr)

def read_word(adr):
 high = bus.read_byte_data(address, adr)
 low = bus.read_byte_data(address, adr+1)
 val = (high << 8) + low
 return val

def read_word_2c(adr):
 val = read_word(adr)
 if (val >= 0x8000):
 return -((65535 - val) + 1)
 else:
 return val

def dist(a,b):
 return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
 radians = math.atan2(x, dist(y,z))
 return -math.degrees(radians)

def get_x_rotation(x,y,z):
 radians = math.atan2(y, dist(x,z))
 return math.degrees(radians)


bus = smbus.SMBus(1)
address = 0x68 #MPU6050 I2C adresi

#MPU6050 ilk calistiginda uyku modunda oldugundan, calistirmak icin asagidaki komutu veriyoruz:
bus.write_byte_data(address, power_mgmt_1, 0)

while True:
 time.sleep(0.1)
 #Jiroskop register'larini oku
 gyro_xout = read_word_2c(0x43)
 gyro_yout = read_word_2c(0x45)
 gyro_zout = read_word_2c(0x47)

 print "Jiroskop X : ", gyro_xout, " olcekli: ", (gyro_xout / 131)
 print "Jiroskop Y : ", gyro_yout, " olcekli: ", (gyro_yout / 131)
 print "Jiroskop Z: ", gyro_zout, " olcekli: ", (gyro_zout / 131)
 
 #Ivmeolcer register'larini oku
 accel_xout = read_word_2c(0x3b)
 accel_yout = read_word_2c(0x3d)
 accel_zout = read_word_2c(0x3f)

 accel_xout_scaled = accel_xout / 16384.0
 accel_yout_scaled = accel_yout / 16384.0
 accel_zout_scaled = accel_zout / 16384.0

 print "Ivmeolcer X: ", accel_xout, " olcekli: ", accel_xout_scaled
 print "Ivmeolcer Y: ", accel_yout, " olcekli: ", accel_yout_scaled
 print "Ivmeolcer Z: ", accel_zout, " olcekli: ", accel_zout_scaled

 print "X dondurme: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
 print "Y dondurme: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

 time.sleep(0.5)
