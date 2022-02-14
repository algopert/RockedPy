from RocketPy import RocketPy



#%matplotlib notebook

##################################################################

rocket = RocketPy()
rocket.initialize("params_config.xml", "")
rocket.move(0.8)
#print(rocket.get_states())





