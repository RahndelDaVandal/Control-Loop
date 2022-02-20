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
}

CL.setController(controller.PID(**pid_config))

CL.controller.auto(True)

CL.setActuator(actuator.CPump())
CL.setIndicator(indicator.LevelSensor())

print(CL)

test = CL.run(1.0)

print(type(test))
print(test)
