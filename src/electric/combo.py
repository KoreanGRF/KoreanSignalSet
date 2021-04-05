"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""
from template import *

print("Combo, electric")
output = ""
output = output + add_signal_direction('electric/combo', 'electric_signal_NE', 5114, 5115) + "\n"
output = output + add_signal_direction('electric/combo', 'electric_signal_SW', 5116, 5117) + "\n"
output = output + add_signal_direction('electric/combo', 'electric_signal_SE', 5118, 5119) + "\n"
output = output + add_signal_direction('electric/combo', 'electric_signal_NW', 5120, 5121) + "\n"
output = output + add_signal_direction('electric/combo', 'electric_signal_W',  5122, 5123) + "\n"
output = output + add_signal_direction('electric/combo', 'electric_signal_E',  5124, 5125) + "\n"
output = output + add_signal_direction('electric/combo', 'electric_signal_N',  5126, 5127) + "\n"
output = output + add_signal_direction('electric/combo', 'electric_signal_S',  5128, 5129) + "\n"
