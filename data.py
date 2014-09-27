import urllib
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?routhe=22')
data=u.read()
f = open ('rt22.xml', 'wb')
f.write(data)
f.close()