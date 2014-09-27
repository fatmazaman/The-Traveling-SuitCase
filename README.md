The Traveling SuitCase
#######################

Travis (Creator of Numpy) traveled to Chicago and took the clark street #22 bus upto Dave's office.

Problem: He just left his suitcase on the bus.

Task: GET IT BACK!!!!

Hacking Transit Data: Many major cities provide a transit API for developers.
example: Chicago transit Authority(cta)

http://www.transitchicago.com/developers/

Available Data: * Real- time gps tracking
                * Stop prediction
                * Alert

TASK1: Travis doesn't know the number of the bus he was riding.Find likely candidates by parsing the data just downloaded and identifying vehicles traveling northbound of Dave's office.

Dave's office located at 
                 Latitude = 41.980262
                 Longitude = -87.668452  

TASK2: Write a program that periodically monitors the identified buses and reports their current distance from Dave's office.

When the bus gets closer tha 0.5miles, have the program issue an alert by popping up a web-page showing the bus location on a map.

Travis will meet bus and get his suitcase.                               