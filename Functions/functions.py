
def print_the_fastest(list_of_times):
	'''
	function to get the fastest vehicle and return based
	on priority chosen in case of many vehicles with same fastest time
	'''
	min_time=list_of_times[0][1]

	'''
	create a set of fastest vehicles
	'''
	vehicle_fastest=set()
	for i in list_of_times:
		if(i[1]==min_time):
			vehicle_fastest.add(i[2])

	'''
	the logic to get the fastest vehicle in case there
	are more than one vehicle with the same min_time
	the priority chosen is as follows
	bike>tuktuk>car
	'''
	sorted_vehicles=[]
	if("Bike" in vehicle_fastest):
		sorted_vehicles.append("Bike")
	if("TukTuk" in vehicle_fastest):
		sorted_vehicles.append("TukTuk")
	if("Car" in vehicle_fastest):
		sorted_vehicles.append("Car")
	'''
	return the vehicle with the most priority as mentioned above
	'''
	return(sorted_vehicles[0])

def fastest_vehicle(orbits,orbit_speed,vehicles,weather):
	'''
	the main piece of code where the logic to find the time 
	taken by each vehicle is written. The timing of each vehicle 
	is then stored onto a list,sorted and passed to print_the_fastest() to
	resolve disputes in case of same min_time of more than one vehicle.
	'''
	orbit_speed=orbit_speed[::-1]

	crater_percentage=weather.get_details()#to find the actual number of craters

	list_of_times=[]
	orbit_number=0

	last_orbit_object=orbits.pop(-1)
	for x in orbits:#iterate through the three orbits(1,2,3). We don't need to calc with orbit4
		distance,craters=x.get_details()
		craters=craters+(craters*crater_percentage)#increase or decrease no based on weather
				
		orbit_speed_popped=orbit_speed.pop()

		orbit_number+=1

		for y in vehicles:#iterate through every vehicle in that orbit
			vehicle_speed,vehicle_crater_time=y.get_details()
			'''
			choose the maximum speed as that of the vehicle 
			or the upper limit in that particular orbit
			'''
			vehicle_speed=orbit_speed_popped if orbit_speed_popped<vehicle_speed else vehicle_speed
			
			crater_covering_time=vehicle_crater_time*craters#time to cover craters in minutes
			distance_covering_time=(distance/vehicle_speed)*60#time to cover the distance in minutes
			total_time=crater_covering_time+distance_covering_time#total is just simple addition

			list_of_times.append([orbit_number,total_time,y.getname()])#make a list out of all


	list_of_times=sorted(list_of_times,key= lambda x:x[1])#sort in ascending order of times
	fastest_orbit=list_of_times[0][0]#get orbit no of the fastest vehicle

	fastest_vehicle=print_the_fastest(list_of_times)#send to function to resolve disputes if any
	return(fastest_vehicle,fastest_orbit)#return to main the fastest vehicle and the orbit number 

def vehicles_allowed(weather):
	'''
	simple method to determine
	which vehicle is available based on 
	any given weather
	'''
	if(weather=='Sunny'):
		return('Bike','TukTuk','Car')
	elif(weather=='Rainy'):
		return('TukTuk','Car')
	elif(weather=='Windy'):
		return('Bike','Car')

def decide_route(fastest_orbit,fastest_vehicle):
	'''
	A simple function to calculate dest1 and dest2
	and which orbit to choose first and which to choose 
	second. The second choice for an orbit will always be 
	orbit4
	'''
	orbit_list1=[1,2]

	if(fastest_orbit in orbit_list1):
		dest1="Hallitharam"
		dest2="R K Puram"
		orbit2=4
	else:
		dest1="R K Puram"
		dest2="Hallitharam"
		orbit2=4

	return(dest1,dest2,orbit2)