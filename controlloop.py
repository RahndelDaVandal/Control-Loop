# control-loop.py
from dataclasses import dataclass, field
from typing import List
from controller import Controller
from indicator import Indicator
from actuator import Actuator

@dataclass
class ControlLoop:
	controller: List[Controller] = field(default=None)
	indicator: List[Controller] = field(default=None)
	actuator: List[Actuator] = field(default=None)
	
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

	def run(self):
		pass
