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
	_max_vol:float() = field(repr=False, default=10.0)
	_cur_vol:float() = field(repr=False, default = 0)
	_percent:float() = field(default=0.0)
		
	def __repr__(self):
		return f'{self.__class__.__name__}({self.percent}%)'
		
	def update(self, actuator_output_volume:float) -> float:
		'''Updates and Returns Indicator Percent Value.

		Args:
			actuator_output_volume (float): input from actuator 

		Returns:
			Indicator percent value as a float

		'''
		self._cur_vol += actuator_output_volume
		self._percent = (self._cur_vol / self._max_vol) * 100
		return self._percent
		
	@property
	def max_volume(self) -> float:
		return self._max_vol
		
	@max_volume.setter
	def max_volume(self, new_volume: float) -> None:
		if isinstance(new_volume, flaot):
			self._max_vol = new_volume
		else: print('INVALID INPUT: LevelSensor.max_volume must be type float')
		
	@property
	def current_volume(self) -> float:
		return self._cur_vol
		
	@current_volume.setter
	def current_volume(self, new_volume:float) -> None:
		if isinstance(new_volume, float):
			if new_volume > 0:
				self._cur_vol = new_volume
			else: print('INVALID INPUT: LevelSensor.current_volume must be greater than 0')
		else: print('INVALID INPUT: LevelSensor.current_volume must be type float')
		
	@property
	def percent(self) -> float:
		return self._percent
