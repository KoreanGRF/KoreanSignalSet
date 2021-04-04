"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""
from template import *

print("Block, electric")
output = ""
output = output + add_signal_direction('electric/block', 'electric_signal_NE', 1275, 1276) + "\n"
output = output + add_signal_direction('electric/block', 'electric_signal_SW', 1277, 1278) + "\n"
output = output + add_signal_direction('electric/block', 'electric_signal_SE', 1279, 1280) + "\n"
output = output + add_signal_direction('electric/block', 'electric_signal_NW', 1281, 1282) + "\n"
output = output + add_signal_direction('electric/block', 'electric_signal_W',  1283, 1284) + "\n"
output = output + add_signal_direction('electric/block', 'electric_signal_E',  1285, 1286) + "\n"
output = output + add_signal_direction('electric/block', 'electric_signal_N',  1287, 1288) + "\n"
output = output + add_signal_direction('electric/block', 'electric_signal_S',  1289, 1290) + "\n"
