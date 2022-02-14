#ifndef _ROCKETPY_HPP_
#define _ROCKETPY_HPP_

#define PY_SSIZE_T_CLEAN

#include <Python.h>
#include "vehicle.h"
#include <string>


#define PY_FILE_NAME    "RocketPy"
#define PY_CLASS_NAME   "RocketPy"


#define FN_REINITIALIZE "reinitialize"
#define FN_MOVE         "move"
#define FN_GET_STATES   "get_states"
#define FN_INITIALIZE   "initialize"



class RocketPy
{
public:
	RocketPy();
	~RocketPy();

	bool initialize(std::string xi_config_file, std::string& xo_message);
	bool reinitialize();
	
    void move(double xi_time);
	
	objectstate* get_states();		
	
private:
	objectstate my_ptr;
	
	PyObject* pName, * pModule, * pDict, * pClass, * pInstance;
	PyObject* pValue;

};

#endif