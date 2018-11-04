#Set3Problem2
from Classes.vehicle import vehicle
from Classes.weather import weather
from Classes.orbit import orbit
from Functions.functions import print_the_fastest
from Functions.functions import fastest_vehicle
from Functions.functions import vehicles_allowed
from Functions.functions import decide_route

if __name__ == '__main__':
	'''
	the driver function to print the fastest vehicle 
	Input: the weather and the max speed in each orbit1_speed
	Output: the fastest vehicle and in which orbit number
	'''

	'''
	set all the values of the classes as per requirement
	'''
	orbit1=orbit(18,20)
	orbit2=orbit(20,10)
	orbit3=orbit(30,15)
	orbit4=orbit(15,18)

	sunny=weather(-.1,"Sunny")
	rainy=weather(.2,"Rainy")
	windy=weather(0,"Windy")

	bike=vehicle(10,2,"Bike")
	tuktuk=vehicle(12,1,"TukTuk")
	car=vehicle(20,3,"Car")

	'''
	get the list of weather,vehicle names
	'''
	weather_names=[]
	weather_names.extend([sunny.getname(),rainy.getname(),windy.getname()])

	vehicle_names=[]
	vehicle_names.extend([bike.getname(),tuktuk.getname(),car.getname()])

	'''
	get the list of vehicle,weather,orbit objects
	'''
	vehicles_object_list=[]
	vehicles_object_list.extend([bike,tuktuk,car])

	weathers_object_list=[]
	weathers_object_list.extend([sunny,rainy,windy])

	orbits_object_list=[]
	orbits_object_list.extend([orbit1,orbit2,orbit3,orbit4])

	'''
	get the inputted weather
	'''
	weather=input().split()
	weather=weather[2]
	
	'''
	finding the index of the weather to know
	which weather object to use
	'''
	for i in weather_names:
		if(i==weather):
			weather_index=weather_names.index(i)
			break

	'''
	input the four orbit speeds
	'''
	orbit_speed=[]
	for i in range(4):
		'''
		extract out and store the orbit speeds
		'''
		orb_spd=input().split()
		orbit_speed.append(int(orb_spd[5]))
	
	
	'''
	find out the vehicles allowed in the inputted weather
	'''
	vehicles_allowed=vehicles_allowed(weather_names[weather_index])

	vehicles_allowed_objects=[]
	'''
	get a list of all the allowed vehicle's objects in the particular weather
	from the vehicle objects list
	'''
	for x in vehicles_allowed:	
		vehicles_allowed_objects.append(vehicles_object_list[vehicle_names.index(x)])

	'''
	pass the orbit objects,orbit1 speed, orbit2 speed, allowed vehicles' object list,weather object of inputted weather
 	'''
	fastest_vehicle,fastest_orbit=fastest_vehicle(orbits_object_list,orbit_speed,vehicles_allowed_objects,weathers_object_list[weather_index])
	
	'''
	finally print the fastest vehicle in which orbit number
	and the starting and ending destinations
	along with the first chosen orbit number and the 
	second chosen orbit number
	'''
	dest1,dest2,orbit2=decide_route(fastest_orbit,fastest_vehicle)
	print("Vehicle {vehicle} to {dest1} via Orbit{orbit_no1} and {dest2} via Orbit{orbit_no2}".
		format(vehicle=fastest_vehicle,dest1=dest1,orbit_no1=fastest_orbit,dest2=dest2,orbit_no2=orbit2))
	