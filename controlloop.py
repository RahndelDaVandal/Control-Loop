# control-loop.py
import time
from dataclasses import dataclass, field
from typing import List, Optional
from controller import Controller
from indicator import Indicator
from actuator import Actuator

@dataclass
class Data:
	time:list = field(default_factory=list)
	process_value:list = field(default_factory=list)
	indicator_percent:list = field(default_factory=list)
	indicator_volume:list = field(default_factory=list)
	controller_output:list = field(default_factory=list)
	actuator_output:list = field(default_factory=list)
	

@dataclass
class ControlLoop:
	controller: List[Controller] = field(default=None)
	indicator: List[Controller] = field(default=None)
	actuator: List[Actuator] = field(default=None)
	
	def __repr__(self):
		return(f'{self.__class__.__name__}(\n'
			   f'controller({self.controller}),\n'
			   f'indicator({self.indicator}),\n'
			   f'actuator({self.actuator})\n)\n'
			  )

	def setController(self, controller:Controller=None) -> None:
		if controller is not None:
			self.controller = controller
		else:
			self.controller = Default()
			
	def setIndicator(self, indicator:Indicator=None) -> None:
		if indicator is not None:
			self.indicator = indicator
		else:
			self.indicator = Default()
			
	def setActuator(self, actuator:Actuator=None) -> None:
		if actuator is not None:
			self.actuator = actuator
		else:
			self.actuator = Default()

	def run(self, process_value) -> Data():
		data = Data()

		print(f'\nprocess_value = {process_value}')
		indicator_output = self.indicator.update(process_value)
		indicator_volume = self.indicator.current_volume
		print(f'indicator_output = {indicator_output}')
		controller_output = self.controller.update(indicator_output)
		print(f'controller_output = {controller_output}')
		actuator_output = self.actuator.update(controller_output)
		print(f'actuator_output = {actuator_output}\n')
		
		data.process_value = process_value
		data.indicator_output = indicator_output
		data.indicator_volume = indicator_volume
		data.controller_output = controller_output
		data.actuator_output = actuator_output
		
		return data
		
	def simulate(self, 
	             iter_num:int, 
				 pv_affect:float,
				 sim_samples:float = 1, 
				 pv_noise:tuple = (0.0,0.0), 
				 verbose:Optional = False
				 ) -> Data():
		"""Simulate Control Loop Output.

			Args:
				iter_num(int): integer number of iterations of simulation
				pv_affect(float): float effect change on process value 
				sim_samples(float): 
					float for pause in seconds inbetween iterations
				pv_noise(tuple(float,float)): 
					process value noise as tuple for rand.Uniform()
				verbose(bool): 
					whether to print values to console during each iteration

			Returns:
				Returns Data dataclass 
		"""
		data = Data()
		t = 0 
		affect = pv_affect
		process_value = 0.0
		indicator_percent = 0.0
		indicator_volume = 0.0
		controller_output = 0.0
		actuator_output = 0.0

		for i in range(iter_num):
			if process_value < 0:process_value = 0.0
			data.process_value.append(process_value)
			process_value = self.indicator.update(affect)
			if process_value < 0:process_value = 0.0
			controller_output = self.controller.update(process_value)
			actuator_output = self.actuator.update(controller_output)
			if verbose:
				print(f'|PV:{process_value:.2f}'
				      f'|R:{affect:.2f}'
					  f'|C:{controller_output:.2f}'
					  f'|A:{actuator_output:.2f}'
					  f'|E:{self.controller._error:.2f}'
					  )
			process_value = self.indicator.update(actuator_output)
			data.time.append(t)
			t += 1
			data.controller_output.append(controller_output)
			data.actuator_output.append(actuator_output)
			data.indicator_volume.append(self.indicator.current_volume)

			time.sleep(sim_samples)
		
		return data

