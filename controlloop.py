# control-loop.py
from dataclasses import dataclass, field
from typing import List
from controller import Controller
from indicator import Indicator
from actuator import Actuator

@dataclass
class Data:
	time:list() = field(defaultfactory=[])
	process_value:float() = field(default=0.0)
	indicator_output:float() = field(default=0.0)
	indicator_volume:float() = field(default=0.0)
	controller_output:float() = field(default=0.0)
	actuator_output:float() = field(default=0.0)
	

@dataclass
class ControlLoop:
	controller: List[Controller] = field(default=None)
	indicator: List[Controller] = field(default=None)
	actuator: List[Actuator] = field(default=None)
	
	def __post_init__(self):
		self.data = Data()
	
	def __repr__(self):
		return(
			f'{self.__class__.__name__}(\n'
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
		print(f'\nprocess_value = {process_value}')
		indicator_output = self.indicator.update(process_value)
		indicator_volume = self.indicator.current_volume
		print(f'indicator_output = {indicator_output}')
		controller_output = self.controller.update(indicator_output)
		print(f'controller_output = {controller_output}')
		actuator_output = self.actuator.update(controller_output)
		print(f'actuator_output = {actuator_output}\n')
		
		self.data.process_value = process_value
		self.data.indicator_output = indicator_output
		self.data.indicator_volume = indicator_volume
		self.data.controller_output = controller_output
		self.data.actuator_output = actuator_output
		
		return self.data
		
	def simulate(self, iter_num:int, pv_affect:float) -> Data():
		output_data = []
		
		self.data.time
		self.data.process_value
		self.data.indicator_output
		self.data.indicator_volume
		self.data.controller_output
		self.data.actuator_output
