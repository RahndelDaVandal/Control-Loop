# controller.py
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Controller(ABC):
	
	@abstractmethod
	def __post_init__(self):
		pass
	
	@abstractmethod
	def update(self, input:float()) -> float():
		pass

@dataclass
class PID(Controller):
	Kp:float()
	Ki:float()
	Kd:float()
	#out_min:float()
	#out_max:float()
	in_auto:bool() = field(default=False)
	#in_reverse:bool()
		
	def __post_init__(self):
		self.samples = 1
		self.curr_time = time.monotonic()
		self.last_time = self.curr_time
		self.clear()
		
	def __repr__(self):
		return (
			f'{self.__class__.__name__}'
			f'(Kp={self.Kp}, '
			f'Ki={self.Ki}, '
			f'Kd={self.Kd}, '
			f'setpoint={self.setpoint}, '
			f'samples={self.samples}, '
			f'in_auto={self.in_auto})'
			)
		
	def clear(self):
		self.P = 0.0
		self.I = 0.0
		self.D = 0.0
		self.setpoint = 0.0
		self.error = 0.0
		self.last_error = 0.0
		self.windup_val = 100.0
		self.output = 0.0
			
	def update(self, process_value:float()) -> float():
		'''
		Update PID Output Value
		
		process_value:float()
		'''
		self.curr_time = time.monotonic()
		delta_time = self.curr_time - self.last_error
		time_diff = self.curr_time - self.last_time
		
		if self.in_auto:
			if time_diff > self.samples:	
				self.error = self.setpoint - process_value
				delta_error = self.error - self.last_error
					
				if delta_time >= self.samples:
					self.P = self.Kp * self.error
					self.I += self.error - self.last_error
						
					if self.I < -self.windup_val: self.I = -self.windup_val
					elif self.I > self.windup_val: self.I = self.windup_val
						
					self.D = 0.0
					if delta_time > 0: self.D = delta_error / delta_time
						
					self.last_time = self.curr_time
					self.last_error = self.error
						
					self.output = self.P + (self.Ki * self.I) + (self.Kd * self.D)
					
					#if self.output > self.out_max: self.output = self.out_max
					#if self.output < self.out_min: self.output = self.out_min
					
					return self.output
			
	def setGains(self, gains:list(tuple())) -> None:
		'''
		Sets PID Gains
			
		gains: list(tuple(str(), float()))
						 i.e. [('Kp', 0.75)] or [('p', 0.75), ('Ki', 0.075)]
		'''
		for gain in gains:
			if isinstance(gain[0], str):
				gain_name = gain[0]
					
				if isinstance(gain[1], float):
					value = gain[1]
						
					if gain_name.upper() in ['KP','P']:
						self.Kp = value
					elif gain_name.upper() in ['KI','I']:
						self.Ki = value
					elif gain_name.upper() in ['KD','D']:
						self.Kd = value
					else:
						print(f'INVALID GAIN: "{gain_name}" ("Kp"/"p", "Ki"/"i", "Kd"/"d")')
							
				else:
					print(f'INVALID GAIN VALUE: {gain[1]} must be type float')
				
			else:
				print(f'gain_name {gain[0]} is not type str()')
					
		print(f'\nKp:{self.Kp} Ki:{self.Ki} Kd:{self.Kd}\n')
				
	def setSamples(self, value:float()) -> None:
		'''
		Sets Samples 
		
		value:float()
		'''
		value = float(value)
		if isinstance(value, float):
			self.samples = value
			print(f'samples: {self.samples}')
		else:
			print(f'INVALID INPUT: {value} not type float')
		
	def setWindup(self, value:float()):
		'''
		Sets windup_val to clamp "Integral Wind Up"
		
		value:float()
		'''
		value = float(value)
		if isinstance(value, float):
			self.windup_val = value
			print(f'windup_val: {self.windup_val}')
		else:
			print(f'INVALID INPUT: {value} not type float')
		
	def setSetpoint(self, value:float()):
		'''
		Sets PID Setpoint
		
		value:float()
		'''
		value = float(value)
		if isinstance(value, float):
			self.setpoint = value
			print(f'setpoint: {self.setpoint}')
		else:
			print(f'INVALID INPUT: {value} not type float')
		
	def setMode(self, in_auto:bool()):
		'''
		Sets PID Mode
		
		mode:bool() (Auto = True, Manual = False)
		'''
		if isinstance(in_auto, bool):
			self.in_auto = in_auto
		else:
			print(f'INVALID INPUT: in_auto {in_auto} not type bool')
		
	def setDirection(self, in_reverse:bool()):
		'''
		Sets PID Mode
		
		mode:bool() (Auto = True, Manual = False)
		'''
		if isinstance(in_reverse, bool):
			self.in_reverse = in_reverse
			print(f'in_reverse: {self.in_reverse}')
		else:
			print(f'INVALID INPUT: in_reverse {in_reverse} not type bool')
	
