# scratch_pad.py

from random import randint
from time import sleep
from dataclasses import dataclass

@dataclass
class Simulation:
    level: float
    inflow: float
    outflow: float
    constraint: float
    variance: float

    def rand_rate_change(curr_rate: float, constraint: float, vari_range: float, rand_range = (-5,5)) -> float:
        r = randint(*rand_range)
        new_rate = curr_rate + r
        if new_rate  >= (constraint + vari_range):
            return constraint + vari_range
        elif new_rate <= (constraint - vari_range):
            return constraint - vari_range
        else:
            return new_rate

if __name__ == "__main__":
   sim = Simulation(100, 0, 10, 10, 2)
   print(sim)
