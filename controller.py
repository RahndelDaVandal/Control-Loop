import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Controller(ABC):
	
	@abstractmethod
	def update(self, input:float()) -> float():
		pass

@dataclass
class PID(Controller):
	_Kp:float() = field(default = 0.0)
	_Ki:float() = field(default = 0.0)
	_Kd:float() = field(default = 0.0)
	
	def __post_init__(self):
		self.reset()
		
	def __repr__(self):
		return (
			f'{self.__class__.__name__}'
			f'(Kp={self._Kp}, '
			f'Ki={self._Ki}, '
			f'Kd={self._Kd}, '
			f'setpoint={self._setpoint}, '
			f'samples={self._samples}, '
			f'mode={self.mode}, '
			f'direction={self.direction})'
			)
	
	def reset(self) -> None:
		self._curr_time = time.monotonic()
		self._last_time = self._curr_time
		self._P = 0.0
		self._I = 0.0
		self._D = 0.0
		self._setpoint = 0.0
		self._output_max = 0.0
		self._output_min = 0.0
		self._error = 0.0
		self._samples = 1.0
		self._last_error = 0.0
		self._windup_val = 20.0
		self._output = 0.0
		self._last_output = self._output
		self._in_auto = False
		self._in_reverse = False
	
	def update(self, process_value:float()) -> float():
		'''
		Update PID Output Value
		
		process_value:float()
		'''
		self._output = 0.0
		
		self._curr_time = time.monotonic()
		delta_time = self._curr_time - self._last_time
		
		if self._in_auto:
			if delta_time > self._samples:	
				self._error = self._setpoint - process_value
				delta_error = self._error - self._last_error
					
				if delta_time >= self._samples:
					self._P = self._Kp * self._error
					self._I += self._error - self._last_error
						
					if self._I < -self._windup_val: self._I = -self._windup_val
					elif self._I > self._windup_val: self._I = self._windup_val
						
					self._D = 0.0
					if delta_time > 0: self._D = delta_error / delta_time
						
					self._last_time = self._curr_time
					self._last_error = self._error
						
					output = self._P + (self._Ki * self._I) + (self._Kd * self._D)
					
					self._output = self._clamp_output(output)
			
			if self._output == None: 
					print('Output is None')
					self._output = 0.0
					print(f'Output = {self.output}')
											
			return self._output
		
	@property
	def gains(self) -> tuple():
		return (self._Kp, self._Ki, self._Kd)
		
	@gains.setter 
	def gains(self, new_gain:tuple()) -> None:
		if isinstance(new_gain, tuple):
			if len(new_gain) == 3:
				self._Kp, self._Ki, self._Kd = new_gain
			else: print(f'INVALID INPUT: PID.gains must have a length of 3')
		else: print(f'INVALID INPUT: PID.gains must be a tuple()')
		
	@property
	def samples(self) -> float():
		return self._samples
		
	@samples.setter
	def samples(self, new_samples:float()) -> None:
		if isinstance(new_samples, float):
			if new_samples > 0:
				self._samples = new_samples
			else: 
				print(f'INVALID INPUT: PID.samples must be greater than 0')
		else: 
			print(f'INVALID INPUT: PID.gains must be a float()')
	
	@property
	def setpoint(self) -> float():
		return self._setpoint
		
	@samples.setter
	def setpoint(self, new_setpoint:float()) -> None:
		if isinstance(new_setpoint, float):
			if new_setpoint < 0:
				print('WARNING: Entered setpoint is negative!')
				self._setpoint = new_setpoint
			elif new_setpoint == 0:
				print('WARNING: Entered setpoint is equal to 0.0!')
				self._setpoint = new_setpoint
			else:
				self._setpoint = new_setpoint
		else:
			print('INVALID INPUT: PID.setpoint must be a float')
						
	@property
	def mode(self) -> str():
		if self._in_auto:
			return 'auto'
		else:
			return 'manual'
			
	@mode.setter
	def mode(self, new_mode:str()) -> None:
		if isinstance(new_mode, str):
			if new_mode.lower() in ['auto','automatic','a']:
				self._in_auto = True
			elif new_mode.lower() in ['manual', 'm']:
				self._in_auto = False
			else:
				print(f'INVALID INPUT: Must enter ("auto","automatic","a") or ("manual","m")')
		else:
			print(f'INVALID INPUT: PID.mode must be a str()')
			
	@property
	def direction(self) -> str():
		if self._in_reverse:
			return 'reverse'
		else:
			return 'direct'
			
	@direction.setter
	def direction(self, new_direction:str()) -> None:
		if isinstance(new_direction, str):
			if new_direction.lower() in ['direct','d']:
				self._in_reverse = False
			elif new_direction.lower() in ['reverse', 'r']:
				self._in_reverse = True
			else:
				print(f'INVALID INPUT: Must enter ("direct","d") or ("reverse","r")')
		else:
			print(f'INVALID INPUT: PID.direction must be a str()')
			
	@property
	def windup_val(self) -> float():
		return self._windup_val
		
	@windup_val.setter
	def windup_val(self, new_val:float()) -> None:
		if isinstance(new_val, float):
			if new_val < 0:
				print(
					'WARNING: Entered windup_val is less than 0! '
					'May cause controller to run different than expected!'
					)
			self._windup_val = new_val
		else:
			print('INVALID INPUT: PID.windup_val must be a float()')
			
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
					else:
						print(f'INVALID INPUT: Please enter limits (minimum, maximum)')
				else: print('INVALID IMPUT: output minimum and maximum must be type float')
			else: print('INVALID INPUT: PID.output_limits must be a tuple with a length of 2')
		else: print('INVALID INPUT: PID.output_limits must be type tuple')
	
	def _clamp_output(self, output:float()):
		if self._output_min:
			if self._output_max:
				if output < self._output_min:
					return self._output_min
				elif	output > self._output_max:
					return self._output_max
				else: return output
			else: return output
		else:return output
		
