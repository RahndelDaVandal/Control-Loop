# actuator.py
from abc import ABC, abstractmethod
from dataclasses import dataclass,field

@dataclass
class Actuator(ABC):
	
	@abstractmethod
	def __post_init__(self):
		pass
	
	@abstractmethod
	def update(self, input:float()) -> float():
		pass

@dataclass		
class CPump(Actuator):
	max_out:float() = field(default=100, repr=False)
	min_out:float() = field(default=0, repr=False)
	max_mA:float() = field(default=20, repr=False)
	min_mA:float() = field(default=4, repr=False)
	input:float() = field(default=4, repr=False)
	output:float() = field(default=0)
	
	def __post_init__(self):
		self.update(self.input)
			
	def __repr__(self):
		return f'{self.__class__.__name__}({self.output} bbls/min)'
		
	def update(self, input) -> float():
		'''
		Update self.output with scaled output
		
		input:float() mA input 4-20mA
		
		return: self.output bbl/min
		
		'''
		output = self.max_out - self.min_out
		output /= self.max_mA - self.min_mA
		output *= self.input - self.min_mA
		return self.output
