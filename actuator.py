# actuator.py
from abc import ABC, abstractmethod
from dataclasses import dataclass,field

@dataclass
class Actuator(ABC):
	
	@abstractmethod
	def update(self, input:float()) -> float():
		pass
		
class CPump(Actuator):
	max_out:float()
	min_out:float()
	max_mA:float()
	min_mA:float()
	output:float()
	
	def __post_init__(self):
		pass
		
	def update(self, input) -> float():
		'''
		Update self.output with scaled output
		
		input:float() mA input 4-20mA
		
		return: self.output bbl/min
		
		'''
		return self.output
