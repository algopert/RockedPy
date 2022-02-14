# RocketPy.py
# https://docs.rocketpy.org/en/latest/notebooks/getting_started.html

from vehicle import  objectstate
import xml.etree.ElementTree as ET
from rocketpy import Environment, SolidMotor, Rocket, Flight
import copy
         
class RocketPy:
	def __init__(self):
		self.__my_ptr = []
		self.__Calisto = None
		self.__Env = None
		self.__Flgt_inclination = 80
		self.__Flgt_heading = 0
		self.__cur_state = None

	def reinitialize(self):
		self.__my_ptr = []

	def move(self, xi_time=0.0):
		length = len(self.__my_ptr)

		for id in range(length - 1): #############################Only for Test ##############
			if 	xi_time>=self.__my_ptr[id].time  and xi_time<=self.__my_ptr[id+1].time:#############################Only for Test ##############
				print(self.__my_ptr[id].time, xi_time, self.__my_ptr[id+1].time)#############################Only for Test ##############
				break#############################Only for Test ##############
		ii = int(id)
		self.__cur_state = objectstate()
		print("ii = ", ii) #############################Only for Test ##############
		if id >= length:
			
			self.__cur_state.time = -1
			return
		print("time ii+1", self.__my_ptr[ii+1].time) #############################Only for Test ##############
		print("time ii", self.__my_ptr[ii].time)  #############################Only for Test ##############
		
		ratio = (xi_time - self.__my_ptr[ii].time) / (self.__my_ptr[ii+1].time - self.__my_ptr[ii].time)
		print("ratio = ", ratio) #############################Only for Test ##############
		self.__cur_state.state_in_geo = True
		self.__cur_state.attitude.z_up = False
		self.__cur_state.attitude.attitude_available = True

		self.__cur_state.time = xi_time
		self.__cur_state.x_or_lat = self.__my_ptr[ii].x_or_lat + (self.__my_ptr[ii+1].x_or_lat -self.__my_ptr[ii].x_or_lat) * ratio
		self.__cur_state.y_or_lon = self.__my_ptr[ii].y_or_lon + (self.__my_ptr[ii+1].y_or_lon -self.__my_ptr[ii].y_or_lon) * ratio
		self.__cur_state.z_or_alt = self.__my_ptr[ii].z_or_alt + (self.__my_ptr[ii+1].z_or_alt -self.__my_ptr[ii].z_or_alt) * ratio
		self.__cur_state.x_vel = self.__my_ptr[ii].x_vel + (self.__my_ptr[ii+1].x_vel -self.__my_ptr[ii].x_vel) * ratio
		self.__cur_state.y_vel = self.__my_ptr[ii].y_vel + (self.__my_ptr[ii+1].y_vel -self.__my_ptr[ii].y_vel) * ratio
		self.__cur_state.z_vel = self.__my_ptr[ii].z_vel + (self.__my_ptr[ii+1].z_vel -self.__my_ptr[ii].z_vel) * ratio
		self.__cur_state.x_acc = self.__my_ptr[ii].x_acc + (self.__my_ptr[ii+1].x_acc -self.__my_ptr[ii].x_acc) * ratio
		self.__cur_state.y_acc = self.__my_ptr[ii].y_acc + (self.__my_ptr[ii+1].y_acc -self.__my_ptr[ii].y_acc) * ratio
		self.__cur_state.z_acc = self.__my_ptr[ii].z_acc + (self.__my_ptr[ii+1].z_acc -self.__my_ptr[ii].z_acc) * ratio
		self.__cur_state.attitude.roll = self.__my_ptr[ii].attitude.roll + (self.__my_ptr[ii+1].attitude.roll -self.__my_ptr[ii].attitude.roll) * ratio
		self.__cur_state.attitude.pitch = self.__my_ptr[ii].attitude.pitch + (self.__my_ptr[ii+1].attitude.pitch -self.__my_ptr[ii].attitude.pitch) * ratio
		self.__cur_state.attitude.yaw = self.__my_ptr[ii].attitude.yaw + (self.__my_ptr[ii+1].attitude.yaw -self.__my_ptr[ii].attitude.yaw) * ratio
		self.__cur_state.attitude.roll_rate = self.__my_ptr[ii].attitude.roll_rate + (self.__my_ptr[ii+1].attitude.roll_rate -self.__my_ptr[ii].attitude.roll_rate) * ratio
		self.__cur_state.attitude.pitch_rate = self.__my_ptr[ii].attitude.pitch_rate + (self.__my_ptr[ii+1].attitude.pitch_rate -self.__my_ptr[ii].attitude.pitch_rate) * ratio
		self.__cur_state.attitude.yaw_rate = self.__my_ptr[ii].attitude.yaw_rate + (self.__my_ptr[ii+1].attitude.yaw_rate -self.__my_ptr[ii].attitude.yaw_rate) * ratio
		print("py-> x_or_lat: ", self.__cur_state.x_or_lat)#############################Only for Test ##############
		print("py-> y_or_lon: ", self.__cur_state.y_or_lon)#############################Only for Test ##############
		print("py-> z_or_alt: ", self.__cur_state.z_or_alt)#############################Only for Test ##############
		print("py-> x_vel: ", self.__cur_state.x_vel)#############################Only for Test ##############
		print("py-> y_vel: ", self.__cur_state.y_vel)#############################Only for Test ##############
		print("py-> z_vel: ", self.__cur_state.z_vel)#############################Only for Test ##############
		print("py-> x_acc: ", self.__cur_state.x_acc)#############################Only for Test ##############
		print("py-> y_acc: ", self.__cur_state.y_acc)#############################Only for Test ##############
		print("py-> z_acc: ", self.__cur_state.z_acc)#############################Only for Test ##############
			
		print("py-> attitude.roll: ", self.__cur_state.attitude.roll)#############################Only for Test ##############
		print("py-> attitude.pitch: ", self.__cur_state.attitude.pitch)#############################Only for Test ##############
		print("py-> attitude.yaw: ", self.__cur_state.attitude.yaw)#############################Only for Test ##############
		print("py-> attitude.roll_rate: ", self.__cur_state.attitude.roll_rate)#############################Only for Test ##############
		print("py-> attitude.pitch_rate: ", self.__cur_state.attitude.pitch_rate)#############################Only for Test ##############
		print("py-> attitude.yaw_rate: ", self.__cur_state.attitude.yaw_rate)#############################Only for Test ##############


		print(self.__cur_state.attitude.yaw_rate)#############################Only for Test ##############


	def get_states(self):
		print("get_states !!!!!!!!!!!!!!!!!")#############################Only for Test ##############
		return self.__cur_state



	def initialize(self, xi_config_file, xo_message):
		print("initialize start")
		myXMLtree = ET.parse(xi_config_file)
		x = myXMLtree.find('Environment')
		env_railLength = float(x.find('railLength').text)
		env_latitude = float(x.find('latitude').text)
		env_longitude = float(x.find('longitude').text)
		env_elevation = float(x.find('elevation').text)
		env_date = tuple(map(int, x.find('date').text.split(', ')))
		env_datum = x.find('datum').text

		x = myXMLtree.find('AtmosphericModel')
		atm_type = x.find('type').text.strip()
		atm_file = x.find('file').text.strip()
		atm_dictionary = x.find('dictionary').text.strip()
  
		x = myXMLtree.find('SolidMotor')
		mot_thrustSource = x.find('thrustSource').text.strip()
		mot_burnOut = float(x.find('burnOut').text)
		mot_grainNumber = int(x.find('grainNumber').text)
		mot_grainSeparation = float(x.find('grainSeparation').text)
		mot_grainDensity = float(x.find('grainDensity').text)
		mot_grainOuterRadius = float(x.find('grainOuterRadius').text)
		mot_grainInitialInnerRadius = float(x.find('grainInitialInnerRadius').text)
		mot_grainInitialHeight = float(x.find('grainInitialHeight').text)
		mot_nozzleRadius = float(x.find('nozzleRadius').text)
		mot_throatRadius = float(x.find('throatRadius').text)
		mot_interpolationMethod = x.find('interpolationMethod').text.strip()

		x = myXMLtree.find('Rocket')
		
		rkt_radius = float(x.find('radius').text)
		rkt_mass = float(x.find('mass').text)
		rkt_inertiaI = float(x.find('inertiaI').text)
		rkt_inertiaZ = float(x.find('inertiaZ').text)
		rkt_distanceRocketNozzle = float(x.find('distanceRocketNozzle').text)
		rkt_distanceRocketPropellant = float(x.find('distanceRocketPropellant').text)
		rkt_powerOffDrag = x.find('powerOffDrag').text.strip()
		rkt_powerOnDrag = x.find('powerOffDrag').text.strip()
		rkt_railButtons = tuple(map(float, x.find('railButtons').text.split(', ')))
		rkt_Nose_length = float(x.find('addNose').find('length').text)
		rkt_Nose_kind = x.find('addNose').find('kind').text.strip()
		rkt_Nose_distanceToCM = float(x.find('addNose').find('distanceToCM').text)
		rkt_Fins_n = int(x.find('addFins').find('n').text)
		rkt_Fins_span = float(x.find('addFins').find('span').text)
		rkt_Fins_rootChord = float(x.find('addFins').find('rootChord').text)
		rkt_Fins_tipChord = float(x.find('addFins').find('tipChord').text)
		rkt_Fins_distanceToCM = float(x.find('addFins').find('distanceToCM').text)
		rkt_Tail_topRadius = float(x.find('addTail').find('topRadius').text)
		rkt_Tail_bottomRadius = float(x.find('addTail').find('bottomRadius').text)
		rkt_Tail_length = float(x.find('addTail').find('length').text)
		rkt_Tail_distanceToCM = float(x.find('addTail').find('distanceToCM').text)
		rkt_ParacMain_CdS = float(x.find('addParachuteMain').find('CdS').text)
		rkt_ParacMain_samplingRate = float(x.find('addParachuteMain').find('samplingRate').text)
		rkt_ParacMain_lag = float(x.find('addParachuteMain').find('lag').text)
		rkt_ParacMain_noise = tuple(map(float, x.find('addParachuteMain').find('noise').text.split(', ')))
		rkt_ParacDrogue_CdS = float(x.find('addParachuteDrogue').find('CdS').text)
		rkt_ParacDrogue_samplingRate = float(x.find('addParachuteDrogue').find('samplingRate').text)
		rkt_ParacDrogue_lag = float(x.find('addParachuteDrogue').find('lag').text)
		rkt_ParacDrogue_noise = tuple(map(float, x.find('addParachuteDrogue').find('noise').text.split(', ')))

		x = myXMLtree.find('Fligt')
		self.__Flgt_inclination =  float(x.find('inclination').text)
		self.__Flgt_heading =  float(x.find('heading').text)
		###########################################################
		self.__Env = Environment(
			railLength=env_railLength,
			latitude=env_latitude,
			longitude=env_longitude,
			elevation=env_elevation,
			date=env_date,
			datum=env_datum,
		)
		self.__Env.setAtmosphericModel(
			type=atm_type,
			file=atm_file,
			dictionary=atm_dictionary,
		)
		#Env.info()

		Pro75M1670 = SolidMotor(
			thrustSource=mot_thrustSource,
			burnOut=mot_burnOut,
			grainNumber=mot_grainNumber,
			grainSeparation=mot_grainSeparation,
			grainDensity=mot_grainDensity,
			grainOuterRadius=mot_grainOuterRadius,
			grainInitialInnerRadius=mot_grainInitialInnerRadius,
			grainInitialHeight=mot_grainInitialHeight,
			nozzleRadius=mot_nozzleRadius,
			throatRadius=mot_throatRadius,
			interpolationMethod=mot_interpolationMethod,
		)

		#Pro75M1670.info()


		self.__Calisto = Rocket(
			motor=Pro75M1670,
			radius=rkt_radius,
			mass=rkt_mass,
			inertiaI=rkt_inertiaI,
			inertiaZ=rkt_inertiaZ,
			distanceRocketNozzle=rkt_distanceRocketNozzle,
			distanceRocketPropellant=rkt_distanceRocketPropellant,
			powerOffDrag=rkt_powerOffDrag,
			powerOnDrag=rkt_powerOnDrag,
		)

		self.__Calisto.setRailButtons(rkt_railButtons)

		NoseCone = self.__Calisto.addNose(
			length=rkt_Nose_length, 
			kind=rkt_Nose_kind, 
			distanceToCM=rkt_Nose_distanceToCM
		)

		FinSet = self.__Calisto.addFins(
			rkt_Fins_n,
			span=rkt_Fins_span,
			rootChord=rkt_Fins_rootChord,
			tipChord=rkt_Fins_tipChord,
			distanceToCM=rkt_Fins_distanceToCM
		)

		Tail = self.__Calisto.addTail(
			topRadius=rkt_Tail_topRadius, 
			bottomRadius=rkt_Tail_bottomRadius, 
			length=rkt_Tail_length, 
			distanceToCM=rkt_Tail_distanceToCM
		)


		def drogueTrigger(p, y):
			return True if y[5] < 0 else False

		def mainTrigger(p, y):
			return True if y[5] < 0 and y[2] < 800 else False

		Main = self.__Calisto.addParachute(
			'Main',
			CdS=rkt_ParacMain_CdS,
			trigger=mainTrigger,
			samplingRate=rkt_ParacMain_samplingRate,
			lag=rkt_ParacMain_lag,
			noise=rkt_ParacMain_noise
		)

		Drogue = self.__Calisto.addParachute(
			'Drogue',
			CdS=rkt_ParacDrogue_CdS,
			trigger=drogueTrigger,
			samplingRate=rkt_ParacDrogue_samplingRate,
			lag=rkt_ParacDrogue_lag,
			noise=rkt_ParacDrogue_noise
		)



		self.__Calisto.parachutes.remove(Drogue)
		self.__Calisto.parachutes.remove(Main)
		TestFlight = Flight(rocket=self.__Calisto, environment=self.__Env, inclination = self.__Flgt_inclination, heading=self.__Flgt_heading)
		print("initialize middle")#############################Only for Test ##############

		#TestFlight.allInfo()
		TestFlight.postProcess()
		my_TempObj = objectstate()
		length = len(TestFlight.x)
		
		my_TempObj.id = 1
		print("length", length)#############################Only for Test ##############
		self.__my_ptr = []
 
		for id in range(length):
			my_TempObj.time = TestFlight.x[:, 0][id]
			my_TempObj.state_in_geo = True
			my_TempObj.x_or_lat = TestFlight.x[:, 1][id]
			my_TempObj.y_or_lon = TestFlight.y[:, 1][id]
			my_TempObj.z_or_alt = TestFlight.z[:, 1][id]
			my_TempObj.x_vel = TestFlight.vx[:, 1][id]
			my_TempObj.y_vel = TestFlight.vy[:, 1][id]
			my_TempObj.z_vel = TestFlight.vz[:, 1][id]
			
			if id > 0:
				my_TempObj.x_acc = TestFlight.ax[:, 1][id-1]
				my_TempObj.y_acc = TestFlight.ay[:, 1][id-1]
				my_TempObj.z_acc = TestFlight.az[:, 1][id-1]
			else:
				my_TempObj.x_acc = 0
				my_TempObj.y_acc = 0
				my_TempObj.z_acc = 0

		
			my_TempObj.attitude.attitude_available = True
			my_TempObj.attitude.z_up = True
			my_TempObj.attitude.roll = TestFlight.psi[:, 1][id]
			my_TempObj.attitude.pitch = TestFlight.theta[:, 1][id]
			my_TempObj.attitude.yaw = TestFlight.phi[:, 1][id]
			my_TempObj.attitude.roll_rate = TestFlight.w3[:, 1][id]
			my_TempObj.attitude.pitch_rate = TestFlight.w2[:, 1][id]
			my_TempObj.attitude.yaw_rate = TestFlight.w1[:, 1][id]
			#print(my_TempObj.time, my_TempObj.x_or_lat, my_TempObj.y_or_lon, my_TempObj.z_or_alt)    #############################Only for Test ##############
   
			self.__my_ptr.append(copy.deepcopy(my_TempObj))
		print("initialize end")#############################Only for Test ##############
		












 

	







        