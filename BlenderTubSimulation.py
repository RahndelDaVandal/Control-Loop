# BlenderTubSimulation.py
import time
import random
import matplotlib.pyplot as plt
import controller
import indicator
import actuator
import controlloop


def plot(data, title:str) -> None:
	plt.title(title)

	plt.show()
	


if __name__ == '__main__':
	data = []
	
	CL = controlloop.ControlLoop()
	
	print(f'{CL}')

	gains = (0.06, 0.0, 0.0)
	
	CL.setController(controller.PID())
	CL.controller.gains = gains
	CL.controller.setpoint = 85.0
	CL.controller.mode = 'Auto'
	CL.controller.output_limits = (4.0,20.0)
	CL.setIndicator(indicator.LevelSensor())
	CL.max_volume = 10.0
	CL.setActuator(actuator.CPump())

	print(gains)

	title = (f'P:{gains[0]}|'
	         f'I:{gains[1]}|'
			 f'D:{gains[2]}|'
			 f'Setpoint:{CL.controller.setpoint}|'
			 f'Samples:{CL.controller.samples}')
	
	print(f'{CL}')

	sim_data = CL.simulate(30, -2, verbose=True)

	print()

	plot(sim_data, title)

