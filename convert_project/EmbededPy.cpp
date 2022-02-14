

#include "RocketPy.hpp"
#include "vehicle.h"
#include <string>
using namespace std;

#include <Python.h>




int main(int argc, char* argv[])
{
    RocketPy rckt;
    string str;
    rckt.initialize("params_config.xml",str);
    rckt.move(0.8);
    rckt.get_states();
    return 0;
}