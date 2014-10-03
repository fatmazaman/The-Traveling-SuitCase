#Find_north.py
#Find all the buses that are traveling northbound of Dave's office

Dave_latitude = 41.98062
Dave_longitude = -87.668452


import xml.etree.ElementTree as ET
doc= ET.parse('rt22.xml')
#doc = parse ('rt22.xml')
for bus in doc.findall('bus'):
	lat = float (bus.findtext('lat'))
	if lat > Dave_latitude:
		direction = bus.findtext('d')
		if direction.startswith('North'):
			busid = bus.findtext('id')
			print (busid, lat)

#import xml.etree.ElementTree as ET
#tree = ET.parse('country_data.xml')
#root = tree.getroot()



