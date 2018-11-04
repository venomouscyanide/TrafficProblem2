class vehicle:
	'''
	class vehicle with speed, time to clear a crater and name 
	'''
	def __init__(self,speed=0,crater_time=0,name=""):
		self.__speed=speed
		self.__crater_time=crater_time
		self.__name=name

	def getname(self):
		'''
		simple method to get the vehicle name
		'''
		return self.__name

	def get_details(self):
		'''
		simple method to get the speed and time to clear a crater 
		of a particular vehicle
		'''
		return (self.__speed,self.__crater_time)