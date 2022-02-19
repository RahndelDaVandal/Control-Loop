# indicator.py

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Indicator(ABC):
	
	@abstractmethod
	def __post_init__(self):
		pass
	
	@abstractmethod
	def update(self, input:float()) -> float():
		pass
		
@dataclass
class LevelSensor(Indicator):
	
	max_vol:float() = field(repr=False,default=10)
	curr_vol:float() = field(repr=False,default=0)
	percent:float() = field(default=0)
	
	def __post_init__(self):
		self.percent = self.update()
		
	def __repr__(self):
		return f'{self.__class__.__name__}({self.percent}%)'
		
	def update(self, inlet_rate:float(), outlet_rate:float()):
		return ((inlet_rate + outlet_rate)/self.max_vol) * 100
		
