"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""
from template import *

print("Entrance, electric")
output = ""
output = output + add_signal_direction('electric/entrance', 'electric_signal_NE', 5082, 5083) + "\n"
output = output + add_signal_direction('electric/entrance', 'electric_signal_SW', 5084, 5085) + "\n"
output = output + add_signal_direction('electric/entrance', 'electric_signal_SE', 5086, 5087) + "\n"
output = output + add_signal_direction('electric/entrance', 'electric_signal_NW', 5088, 5089) + "\n"
output = output + add_signal_direction('electric/entrance', 'electric_signal_W',  5090, 5091) + "\n"
output = output + add_signal_direction('electric/entrance', 'electric_signal_E',  5092, 5093) + "\n"
output = output + add_signal_direction('electric/entrance', 'electric_signal_N',  5094, 5095) + "\n"
output = output + add_signal_direction('electric/entrance', 'electric_signal_S',  5096, 5097) + "\n"
