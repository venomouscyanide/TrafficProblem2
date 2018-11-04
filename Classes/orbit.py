class orbit:
	'''
	class orbit with distance and crater no in it
	'''
	def __init__(self,distance=0,craters=0):
		self.__distance=distance
		self.__craters=craters

	def get_details(self):
		'''
		simple function to get the orbit class contents
		'''
		return (self.__distance,self.__craters)