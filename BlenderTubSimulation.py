# BlenderTubSimulation.py
import time
import random
import controller
import indicator
import actuator
import controlloop

def simulate() -> list():
	pass
	
def plot() -> None:
	pass

if __name__ == '__main__':
	data = []
	
	pid_config = {
		'Kp' : 0.1,
		'Ki' : 0.0,
		'Kd' : 0.0,
	}
	
	CL = controlloop.ControlLoop()
	
	print(CL)
	
	CL.setController(controller.PID(**pid_config))
	CL.controller.setSetpoint(85)
	CL.setActuator(actuator.CPump())
	CL.setIndicator(indicator.LevelSensor())
	CL.controller.setMode(True)
	
	print(CL)
	
	input = 0.0
	
	for i in range(10):
		input -= 5 + random.uniform(-2,2)
		if input < 0: input = 0
		output = CL.run(input)
		data.append(output)
		input += output.controller_output
		time.sleep(1)
		
	print(data)
	
# Clamp controller output 
# use @property and @property.setter
