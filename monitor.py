#monitor.py
import urllib
import xml.etree.ElementTree as ET
candidates = ['4363','4154']
Dave_latitude = 41.98062

def distance(lat1,lat2):
	#return distance in miles between three lats
	    return 69*abs( lat1 - lat2)
def monitor():
	u = urllib.urlopen('http://www.ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
	doc = ET.parse(u)
	

'''    for bus in doc.findall('bus'): 
		busid = bus.findtext('id')
		if busid in candidates:
			lat = float (bus.findtext('lat'))
			dis = distance(lat, Dave_latitude)
			print (busid,dis,'miles')
	print ('_'*10)'''		

	
import time 
while True:
	monitor()
	time.sleep(60)
    