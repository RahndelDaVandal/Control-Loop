# cpump.py
'''
Math for Scaled Value

Scaled Value = ( ((max_scaled - min_scaled)/(max_mA - min_mA))*(raw_mA - min_mA) + offset ) * fine_adjust
'''

from dataclasses import dataclass, field

@dataclass
class Cpump:
	max_out:float() = field(default=100.0)
	min_out:float()	= field(default=0.0)
	max_mA:float() = field(default=20.0)
	min_mA:float() = field(default=4.0)
	input:float() = field(default=4)
	scaled_out:float() = field(init=False)
	
	def __post_init__(self):
		self.update(self.min_mA)
		
	def __repr__(self):
		return f'{self.__class__.__name__}({self.scaled_out} bbls/min)'
		
	def calc_scaled_value(self):
		sv = ((self.max_out - self.min_out)/(self.max_mA-self.min_mA))*(self.input-self.min_mA)
		self.scaled_out = sv
		
	def update(self, input):
		self.input = input
		self.calc_scaled_value()
