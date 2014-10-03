#Find_north.py
#Find all the buses that are traveling northbound of Dave's office

Dave_latitude = 41.98062
Dave_longitude = -87.668452

from Xml.etree.ElemenTree import parse
doc = parse ('rt22.xml')
for bus in doc.findall('bus'):
	lat = float (bus.findtext('lat'))
	if lat > Dave_latitude:
		direction = bus.findtext('d')
		if direction.startswirch('North'):
			busid = bud.findtext('id')
			print busid, lat
