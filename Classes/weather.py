class weather:
	'''
	class weather with crater crater_percentage(increase or decrease)
	and name of the weather
	'''
	def __init__(self,crater_percentage=0,name=""):
		self.__crater_percentage=crater_percentage
		self.__name=name

	def getname(self):
		return self.__name

	def get_details(self):
		return(self.__crater_percentage)
