# tub.py
from dataclasses import dataclass, field

@dataclass
class Tub:
	max_vol:float() = field(repr=False,default=10)
	curr_vol:float() = field(repr=False,default=0)
	
	def __post_init__(self):
		self.percent = ((self.curr_vol/self.max_vol)*100)
		
	def __repr__(self):
		return f'{self.__class__.__name__}({self.percent}%)'
		
	def update(self, suction_rate:float(), discharge_rate:float()):
		self.curr_vol += (suction_rate + discharge_rate)
		self.percent = (self.curr_vol/self.max_vol) * 100

