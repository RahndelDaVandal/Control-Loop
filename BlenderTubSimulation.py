# BlenderTubSimulation.py

import controller
import indicator
import actuator
import controlloop

def simulate():
	pass

if __name__ == '__main__':
	data = []
	
	pid_config = {
		'Kp' : 0.75,
		'Ki' : 0.075,
		'Kd' : 0.0075,
	}
	
	CL = controlloop.ControlLoop()
	
	print(CL)
	
	CL.setController(controller.PID(**pid_config))
	CL.controller.setSetpoint(85)
	CL.setActuator(actuator.CPump())
	CL.setIndicator(indicator.LevelSensor())
	
	print(CL)
