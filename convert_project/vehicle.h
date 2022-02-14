#pragma once


struct objectattitude
{
	bool                   attitude_available = false;
	bool                   z_up = true;

	double                 roll = 0;
	double                 pitch = 0;
	double                 yaw = 0;

	double                 roll_rate = 0;
	double                 pitch_rate = 0;
	double                 yaw_rate = 0;
};

struct objectstate
{
	double                 time = 0;
	bool                   state_in_geo =  true;	
	
	double                 x_or_lat = 0;
	double                 y_or_lon = 0;
	double                 z_or_alt = 0;

	double                 x_vel = 0;
	double                 y_vel = 0;
	double                 z_vel = 0;

	double                 x_acc = 0;
	double                 y_acc = 0;
	double                 z_acc = 0;	

	objectattitude         attitude;

};
