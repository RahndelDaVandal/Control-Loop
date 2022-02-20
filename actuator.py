# actuator.py
from abc import ABC, abstractmethod
from dataclasses import dataclass,field

@dataclass
class Actuator(ABC):
	
	@abstractmethod
	def update(self, input:float()) -> float():
		pass

@dataclass		
class CPump(Actuator):
	_output_min:float() = field(default=0.0, repr=False)
	_output_max:float() = field(default=100.0, repr=False)
	_input_min:float() = field(default=4, repr=False)
	_input_max:float() = field(default=20, repr=False)
	_input:float() = field(default=4, repr=False)
	_output:float() = field(default=0)
			
	def __repr__(self):
		return f'{self.__class__.__name__}({self._output} bbls/min)'
		
	def update(self, input) -> float():
		'''
		Update self.output with scaled output
		
		input:float() mA input 4-20mA
		
		return: self.output bbl/min
		
		'''
		o = (self._output_max - self._output_min)
		i = (self._input_max - self._input_min)
		
		o_over_i = o / i
		
		output = o_over_i * (input - self._input_min)
		
		self._output = output
		return self._output
		
	@property
	def output_limits(self) -> tuple():
		return (self._output_min, self._output_max)
		
	@output_limits.setter
	def output_limits(self, new_limits:tuple()) -> None:
		if isinstance(new_limits, tuple):
			if len(new_limits) == 2:
				if isinstance(new_limits[0], float) and isinstance(new_limits[1], float):
					if new_limits[0] < new_limits[1]:
						self._output_min, self._output_max = new_limits
					elif new_limits[0] > new_limits[1]:
						self._output_max, self._output_min = new_limits
					else: print('INVALID INPUT: Must enter a minimum value and a maximum value')
				else: print('INVALID INPUT: Cpump.output_limits must be floats')
			else: print('INVALID INPUT: Cpump.output_limits must be a tuple with a length of 2')
		else: print('INVALID INPUT: Cpump.output_limits must be of type tuple')
		
	@property
	def input_limits(self) -> tuple():
		return (self._input_min, self._input_max)
		
	@input_limits.setter
	def input_limits(self, new_limits:tuple()) -> None:
		if isinstance(new_limits, tuple):
			if len(new_limits) == 2:
				if isinstance(new_limits[0], float) and isinstance(new_limits[1], float):
					if new_limits[0] < new_limits[1]:
						self._input_min, self._input_max = new_limits
					elif new_limits[0] > new_limits[1]:
						self._input_max, self._input_max = new_limits
					else: print('INVALID INPUT: Must enter a minimum value and a maximum value')
				else: print('INVALID INPUT: Cpump.input_limits must be floats')
			else: print('INVALID INPUT: Cpump.input_limits must be a tuple with a length of 2')
		else: print('INVALID INPUT: Cpump.input_limits must be of type tuple')
		
	@property
	def output(self) -> float():
		return self._output
		
	@property
	def input(self) -> float():
		return self._input
		
