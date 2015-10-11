import json
import math
import sys

#Command line argument specifying each set of co-ordinates as one argument with a comma between
#just because 4 arguments are a lot more manageable than 8
#python LyftChallenge.py 54.0894797,-6.18671 53.1229599,-6.2705202 52.986375,-6.043701 51.8856167,-10.4240951

#This system could be significantly more efficient, but for a quickly typed solution I hope it's adequate

#I've put it in a class, no real reason why
class Driver:
	def __init__(self, source, destination):
		self.source = source
		self.dest = destination

class Location:
	def __init__(self, lat, lon):
		self.lat=float(lat)
		self.lon=float(lon)
		
#Great-circle distance
def GetDistance(sorc, dest):
	#converting to radians
	cLat = math.radians(sorc.lat)
	cLon = math.radians(sorc.lon)
	dLat = math.radians(dest.lat)
	dLon = math.radians(dest.lon)
	latDif = math.radians(dLat-cLat)
	lonDif = math.radians(dLon-cLon)
	
	centralAngle = math.acos (math.sin(cLat)*math.sin(dLat) + \
		math.cos(cLat)*math.cos(dLat)*math.cos(lonDif))
		
	distance = centralAngle*6371#mean earth radius in km
	
	return distance

def GetDetour(drive1, drive2):
	fullJourney = 0
	fullJourney += GetDistance(drive1.source, drive2.source)
	fullJourney += GetDistance(drive2.source, drive2.dest)
	fullJourney += GetDistance(drive2.dest, drive1.source)
	return fullJourney

def main():
	argues = []
	for x in sys.argv:
		argues.append(x.split(","))
	driver1 = Driver(Location(argues[1][0], sys.argv[1][1]), \
						Location(argues[2][0], argues[2][1]))
	driver2 = Driver(Location(argues[3][0], sys.argv[3][1]), \
						Location(argues[4][0], sys.argv[4][1]))
	
	detour1 = GetDetour(driver1, driver2)
	detour2 = GetDetour(driver2, driver1)
	if(detour1>detour2):	
		print("Driver one should do the detour")
	elif (detour2>detour1):
		print("Driver two should do the detour")
	else:
		print("Whoever has the most fuel efficient car should do the detour")
			
	return 0

if __name__ == '__main__':
	main()

