class objectattitude:
	def __init__(self):
		self.attitude_available= False
		self.z_up = True
		self.roll = 0
		self.pitch = 0
		self.yaw = 0
		self.roll_rate = 0
		self.pitch_rate = 0
		self.yaw_rate = 0
		

class objectstate:
	def __init__(self):
		self.id=1
		self.time=0.0
		self.state_in_geo=False
		self.x_or_lat=0.0
		self.y_or_lon=0.0
		self.z_or_alt=0.0
		self.x_vel=0.0
		self.y_vel=0.0
		self.z_vel=0.0
		self.x_acc=0.0
		self.y_acc=0.0
		self.z_acc=0.0
		self.attitude = objectattitude()






