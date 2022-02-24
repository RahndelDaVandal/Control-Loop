# BlenderTubSimulation.py
import time
import random
import controller
import indicator
import actuator
import controlloop

def simulate(CL:controlloop.ControlLoop()) -> list():
	data = []
	for i in range(5):
		input_vol = CL.indicator.current_volume
		input_percent = CL.indicator.percent
		print(input_percent)
		print(CL.indicator)
		temp = CL.run(input_percent)
		data.append(temp)
		print(data[len(data)-1])
		CL.indicator.update(input_vol + temp.actuator_output)
		time.sleep(1)
	
	
def plot() -> None:
	pass


if __name__ == '__main__':
	data = []
	
	CL = controlloop.ControlLoop()
	
	print(CL)
	
	CL.setController(controller.PID())
	CL.controller.gains = (0.1, 0.0, 0.0)
	CL.controller.setpoint = 85.0
	print(CL.controller)
	print(f'CL.controller.setpoint = {CL.controller.setpoint}')
	CL.controller.mode = 'Auto'
	CL.controller.output_limits = (4.0,20.0)
	print(f'CL.controller.output_limits = {CL.controller.output_limits}')
	CL.setIndicator(indicator.LevelSensor())
	CL.max_volume = 10.0
	CL.setActuator(actuator.CPump())
	
	
	
	print(CL)
	
	simulate(CL)	
	
"""	
	for i in range(10):
		input = CL.indicator.current_volume
		input -= 5 + random.uniform(0,0)
		if input < 0: input = 0
		output = CL.run(input)
		data.append(output)
		input += output.actuator_output
		time.sleep(1)
		
	for i in data:
		print(
			f'|SP:{CL.controller.setpoint}'
			f'|PV:{i.process_value:.2f}'
			f'|LS:{i.indicator_output:.2f}'
			f'|CO:{i.controller_output:.2f}'
			f'|AO:{i.actuator_output:.2f}|'
			)
"""
