#!/usr/bin/python
# -*- coding: utf-8 -*-
#çalışacak gibi duruyor ancak anlayamadım matığını
#birden fazla sensörü çalıştırabiliyoruz
#çalışmaz ise 3. bir kod daha vardı ancak yazmadım, linki bulunuyor 
import os
import fnmatch
import time
import MySQLdb as mdb
import logging

logging.basicConfig(filename='/home/pi/DS18B20_error.log',
  level=logging.DEBUG,
  format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

# Load the modules (not required if they are loaded at boot) 
# os.system('modprobe w1-gpio')
# os.system('modprobe w1-therm')

# Function for storing readings into MySQL
def insertDB(IDs, temperature):

  try:

    con = mdb.connect('localhost',
                      'pi_insert',
                      'xxxxxxxxxx',
                      'measurements');
    cursor = con.cursor()

    for i in range(0,len(temperature)):
      sql = "INSERT INTO temperature(temperature, sensor_id) \
      VALUES ('%s', '%s')" % \
      ( temperature[i], IDs[i])
      cursor.execute(sql)
      sql = []
      con.commit()

    con.close()

  except mdb.Error, e:
    logger.error(e)

# Get readings from sensors and store them in MySQL

temperature = []
IDs = []

for filename in os.listdir("/sys/bus/w1/devices"):
  if fnmatch.fnmatch(filename, '28-*'):
    with open("/sys/bus/w1/devices/" + filename + "/w1_slave") as f_obj:
      lines = f_obj.readlines()
      if lines[0].find("YES"):
        pok = lines[1].find('=')
        temperature.append(float(lines[1][pok+1:pok+6])/1000)
        IDs.append(filename)
      else:
        logger.error("Error reading sensor with ID: %s" % (filename))

if (len(temperature)>0):
  insertDB(IDs, temperature)
