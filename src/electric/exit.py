"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""
from template import *

print("Exit, electric")
output = ""
output = output + add_signal_direction('electric/exit', 'electric_signal_NE', 5098, 5099) + "\n"
output = output + add_signal_direction('electric/exit', 'electric_signal_SW', 5100, 5101) + "\n"
output = output + add_signal_direction('electric/exit', 'electric_signal_SE', 5102, 5103) + "\n"
output = output + add_signal_direction('electric/exit', 'electric_signal_NW', 5104, 5105) + "\n"
output = output + add_signal_direction('electric/exit', 'electric_signal_W',  5106, 5107) + "\n"
output = output + add_signal_direction('electric/exit', 'electric_signal_E',  5108, 5109) + "\n"
output = output + add_signal_direction('electric/exit', 'electric_signal_N',  5110, 5111) + "\n"
output = output + add_signal_direction('electric/exit', 'electric_signal_S',  5112, 5113) + "\n"
