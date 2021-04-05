"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""
from template import *

print("Oneway Path, electric")
output = ""
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_NE', 5210, 5211) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_SW', 5212, 5213) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_SE', 5214, 5215) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_NW', 5216, 5217) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_W',  5218, 5219) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_E',  5220, 5221) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_N',  5222, 5223) + "\n"
output = output + add_signal_direction('electric/oneway_path', 'electric_signal_S',  5224, 5225) + "\n"
