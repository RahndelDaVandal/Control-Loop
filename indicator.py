# indicator.py

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Indicator(ABC):
	
	@abstractmethod
	def update(self, process_value:float()) -> float():
		pass
		
@dataclass
class LevelSensor(Indicator):
	
	max_vol:float() = field(repr=False,default=10)
	percent:float() = field(default=0)
	
	def __post_init__(self):
		self.percent = self.update(0)
		
	def __repr__(self):
		return f'{self.__class__.__name__}({self.percent}%)'
		
	def update(self, process_value:float()) -> float():
		self.percent = (process_value / self.max_vol) * 100
		return self.percent
		
