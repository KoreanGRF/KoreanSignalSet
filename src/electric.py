"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""
import os
from template import *

# _ROOT path
_ROOT = os.path.dirname(os.path.abspath(__file__))[:-3]

output = ""

# Electric, block
print("Electric, block")
output = output + replace_signal('electric/block', 1275)
output = output + replace_signal('electric/block', 6262)   # Restricted signal (with blue pole)

# Electric, entrance
print("Electric, entrance")
output = output + replace_signal('electric/entrance', 5082)
output = output + replace_signal('electric/entrance', 6278)   # Restricted signal (with blue pole)

# Electric, exit
print("Electric, exit")
output = output + replace_signal('electric/exit', 5098)
output = output + replace_signal('electric/exit', 6294)   # Restricted signal (with blue pole)

# Electric, combo
print("Electric, combo")
output = output + replace_signal('electric/combo', 5114)
output = output + replace_signal('electric/combo', 6310)   # Restricted signal (with blue pole)

# Electric, path
print("Electric, path")
output = output + replace_signal('electric/path', 5210)
output = output + replace_signal('electric/path', 5226)   # Seems like dummy, (with purple pole)
output = output + replace_signal('electric/path', 6389)   # Restricted signal (with blue pole)

# Electric, oneway path
print("Electric, oneway path")
output = output + replace_signal('electric/oneway_path', 5194)
output = output + replace_signal('electric/oneway_path', 5242)   # Seems like dummy (with purple pole)
output = output + replace_signal('electric/oneway_path', 6405)   # Restricted signal (with blue pole)

# Electric, programmable
print("Electric, programmable")
output = output + replace_signal('electric/programmable', 6175)
output = output + replace_signal('electric/programmable', 6207)   # Restricted signal (with blue pole)

# Write a file
f = open(_ROOT + "generated/electric.pnml", "w")
f.write(output)
f.close()
