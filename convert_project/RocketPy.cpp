#include "RocketPy.hpp"


#define PY_FILE_NAME    "RocketPy"
#define PY_CLASS_NAME   "RocketPy"


#define FN_REINITIALIZE "reinitialize"
#define FN_MOVE         "move"
#define FN_GET_STATES   "get_states"
#define FN_INITIALIZE   "initialize"

#define PARAM1  20
#define PARAM2  30


RocketPy::RocketPy()
{

    Py_Initialize();

    pName = PyUnicode_DecodeFSDefault(PY_FILE_NAME);
    pModule = PyImport_Import(pName);  //python_filename //ok
    Py_XDECREF(pName);
    //
    pDict = PyModule_GetDict(pModule);
    // Build the name of a callable class 
    Py_XDECREF(pModule);
    pClass = PyDict_GetItemString(pDict, PY_CLASS_NAME);
    Py_XDECREF(pDict);
    // Create an instance of the class
    if (!PyCallable_Check(pClass))
        return;

    pInstance = PyObject_CallObject(pClass, NULL);
    Py_XDECREF(pClass);
	
}
RocketPy::~RocketPy()
{
    // Clean up
    Py_XDECREF(pInstance);
    
    Py_FinalizeEx();
}

bool RocketPy::initialize(std::string xi_config_file, std::string& xo_message)
{
    PyObject* pValue;

    pValue = PyObject_CallMethod(pInstance, FN_INITIALIZE, "(ss)", xi_config_file.c_str(), xo_message.c_str());
    Py_XDECREF(pValue);

    // Need to modify minor with python
    // if (pValue != NULL)
    //{
    //   printf("Return of call : %d\n", PyLong_AsLong(pValue));
    //   Py_XDECREF(pValue);
    //}
    // else
    //{
    //  PyErr_Print();
    //}
    
 
    return 0;
}
	
bool RocketPy::reinitialize()
{
    PyObject* pValue;
    pValue = PyObject_CallMethod(pInstance, FN_REINITIALIZE, NULL);
    if (pValue != NULL)
        return PyLong_AsLong(pValue);
    
    return 0; // Need to modify minor with python
}
	
void RocketPy::move(double xi_time)
{
    PyObject_CallMethod(pInstance, FN_MOVE, "(d)" , xi_time);
}
	
objectstate* RocketPy::get_states()
{
    PyObject* pValue;
    pValue = PyObject_CallMethod(pInstance, FN_GET_STATES, NULL);
    
    //vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv  Only For Test  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\\
    printf("time =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("time")))); 
    printf("x_or_lat =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("x_or_lat"))));
    printf("y_or_lon =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("y_or_lon"))));
    printf("z_or_alt =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("z_or_alt"))));
    printf("x_vel =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("x_vel"))));
    printf("y_vel =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("y_vel"))));
    printf("z_vel =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("z_vel"))));
    printf("x_acc =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("x_acc"))));
    printf("y_acc =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("y_acc"))));
    printf("z_acc =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("z_acc"))));
    printf("attitude.roll =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("roll"))));
    printf("attitude.pitch =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("pitch"))));
    printf("attitude.yaw =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("yaw"))));
    printf("attitude.roll_rate =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("roll_rate"))));
    printf("attitude.pitch_rate =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("pitch_rate"))));
    printf("attitude.yaw_rate =   %f\n", PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("yaw_rate"))));
    printf("attitude.z_up =   %d\n", PyLong_AsLong(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("z_up"))));
    printf("attitude.attitude_available =   %d\n", PyLong_AsLong(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("attitude_available"))));
    printf("state_in_geo =   %d\n", PyLong_AsLong(PyObject_GetAttr(pValue, PyUnicode_InternFromString("state_in_geo"))));
    //^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  Only For Test  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//
    


    my_ptr.time = PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("time")));
    my_ptr.x_or_lat = PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("x_or_lat")));
    my_ptr.y_or_lon = PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("y_or_lon")));
    my_ptr.z_or_alt = PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("z_or_alt")));
    my_ptr.x_vel = PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("x_vel")));
    my_ptr.y_vel = PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("y_vel")));
    my_ptr.z_vel = PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("z_vel")));
    my_ptr.x_acc = PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("x_acc")));
    my_ptr.y_acc = PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("y_acc")));
    my_ptr.z_acc = PyFloat_AsDouble(PyObject_GetAttr(pValue, PyUnicode_InternFromString("z_acc")));
    my_ptr.attitude.roll = PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("roll")));
    my_ptr.attitude.pitch = PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("pitch")));
    my_ptr.attitude.yaw = PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("yaw")));
    my_ptr.attitude.roll_rate = PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("roll_rate")));
    my_ptr.attitude.pitch_rate = PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("pitch_rate")));
    my_ptr.attitude.yaw_rate = PyFloat_AsDouble(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("yaw_rate")));
    my_ptr.attitude.z_up = PyLong_AsLong(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("z_up")));
    my_ptr.attitude.attitude_available = PyLong_AsLong(PyObject_GetAttr(PyObject_GetAttr(pValue, PyUnicode_InternFromString("attitude")), PyUnicode_InternFromString("attitude_available")));
    my_ptr.state_in_geo = PyLong_AsLong(PyObject_GetAttr(pValue, PyUnicode_InternFromString("state_in_geo")));
    
    Py_XDECREF(pValue);
    
	return &my_ptr;
}