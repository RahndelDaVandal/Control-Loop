# main.py
import controller
import indicator
import actuator
import controlloop

CL = controlloop.ControlLoop()

print(CL)

pid_config = {
	'Kp' : 0.75,
	'Ki' : 0.075,
	'Kd' : 0.0075,
	'in_auto' : True
}

CL.setController(controller.PID(**pid_config))

print(CL)

CL.controller.setSetpoint(85)

print(CL)
