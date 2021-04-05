"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""
from template import *

print("Oneway Path, electric")
output = ""
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_NE', 5194, 5195) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_SW', 5196, 5197) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_SE', 5198, 5199) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_NW', 5200, 5201) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_W',  5202, 5203) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_E',  5204, 5205) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_N',  5206, 5207) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_S',  5208, 5209) + "\n"
