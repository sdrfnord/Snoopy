#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# Samuel Cozannet: Added logger, Feb 2014
# License: GPL 2.0
 
import os
from gps import *
from time import *
import time
import threading

if len(sys.argv) < 2:
    sys.stderr.write('Usage:' + sys.argv[0] +' <file_to_write_gps_position_to> <log_prepend_text>\n')
    sys.exit(1)

# Setting the global variable
gpsd = None 
# logfile = "gpsd.log"
# prepend_text="prepend"
prepend_text = sys.argv[2]
logfile = sys.argv[1]

# Clear the terminal (optional, because it's nicer, only for debugging)
# os.system('clear') 
 
class GpsPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		# Call global variable into scope
		global gpsd 
		# Starting datastream from GPS
		gpsd = gps(mode=WATCH_ENABLE) 
		self.current_value = None
		# Setting the thread running to true
		self.running = True 
 
	def run(self):
		global gpsd
		while gpsp.running:
			# This will continue to loop and grab EACH set of gpsd info 
			# to clear the buffer. 
			gpsd.next() 
 
if __name__ == '__main__':
	# Create a new thread
	gpsp = GpsPoller() 
	try:
		gpsp.start() # start it up
		while True:
			# It may take a second or two to get good data
			# print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
			os.system('clear')
			f = open(logfile, "a")

			# print
			# print ' GPS reading'
			# print '----------------------------------------'
			# print 'latitude    ' , gpsd.fix.latitude
			# print 'longitude   ' , gpsd.fix.longitude
			# print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
			# print 'altitude (m)' , gpsd.fix.altitude
			# print 'eps         ' , gpsd.fix.eps
			# print 'epx         ' , gpsd.fix.epx
			# print 'epv         ' , gpsd.fix.epv
			# print 'ept         ' , gpsd.fix.ept
			# print 'speed (m/s) ' , gpsd.fix.speed
			# print 'climb       ' , gpsd.fix.climb
			# print 'track       ' , gpsd.fix.track
			# print 'mode        ' , gpsd.fix.mode
			# print
			# print 'sats        ' , gpsd.satellites

			# sats = ', '.join([str(s) for s in gpsd.satellites])
			# pos = "%s,%f,%f,%s,%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%s" %(prepend_text, gpsd.fix.latitude, gpsd.fix.longitude, gpsd.utc, gpsd.fix.time, gpsd.fix.altitude, gpsd.fix.eps, gpsd.fix.epx, gpsd.fix.epv, gpsd.fix.ept, gpsd.fix.speed, gpsd.fix.climb, gpsd.fix.track, gpsd.fix.mode, sats)

			# Cannot get precision from gpsd hence hardcoding for now
			pos ="%s,%f,%f,%f,%f" %(prepend_text,time.time(),gpsd.fix.latitude,gpsd.fix.longitude,50.0)

			f.write(pos)
			f.write("\n")
			f.close()

			# To Do: publish data to API with JSON format

			time.sleep(5) #set to whatever
			 
	except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
		print "\nKilling Thread..."
		gpsp.running = False
		gpsp.join() # wait for the thread to finish what it's doing

	print "Done.\nExiting."
