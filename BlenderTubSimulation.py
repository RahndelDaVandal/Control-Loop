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
	
	CL = controlloop.ControlLoop()
	
	print(CL)
	
	CL.setController(controller.PID())
	CL.controller.gains = (0.75, 0.075, 0.0075)
	CL.controller.setpoint = 85.0
	print(CL.controller)
	print(CL.controller.setpoint)
	CL.controller.mode = 'Auto'
	CL.controller.output_limits = (4.0,20.0)
	CL.setIndicator(indicator.LevelSensor())
	CL.max_volume = 10.0
	CL.setActuator(actuator.CPump())
	
	
	
	print(CL)
	
	input = 0.0
	
	for i in range(10):
		input -= 5 + random.uniform(-2,2)
		if input < 0: input = 0
		output = CL.run(input)
		data.append(output)
		input += output.actuator_output
		time.sleep(1)
		
	for i in data:
		print(
			f'SP:{CL.controller.setpoint}'
			f'PV:{i.process_value:.2f}'
			f'|LS:{i.indicator_output:.2f}'
			f'|CO:{i.controller_output:.2f}'
			f'|AO:{i.actuator_output:.2f}'
			)
	
