"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""
from template import *

output = ""

# Electric, block
print("Electric, block")
output = output + replace_electric_signal('block', 1275)
output = output + replace_electric_signal('block', 6262)   # Restricted signal (with blue pole)

# Electric, entrance
print("Electric, entrance")
output = output + replace_electric_signal('entrance', 5082)
output = output + replace_electric_signal('entrance', 6278)   # Restricted signal (with blue pole)

# Electric, exit
print("Electric, exit")
output = output + replace_electric_signal('exit', 5098, 'Y')
output = output + replace_electric_signal('exit', 6294, 'Y')   # Restricted signal (with blue pole)

# Electric, combo
print("Electric, combo")
output = output + replace_electric_signal('combo', 5114, 'YG')
output = output + replace_electric_signal('combo', 6310, 'YG')   # Restricted signal (with blue pole)

# Electric, path
print("Electric, path")
output = output + replace_electric_signal('path', 5210)
output = output + replace_electric_signal('path', 5226)   # Seems like dummy, (with purple pole)
output = output + replace_electric_signal('path', 6389)   # Restricted signal (with blue pole)

# Electric, oneway path
print("Electric, oneway path")
output = output + replace_electric_signal('oneway_path', 5194)
output = output + replace_electric_signal('oneway_path', 5242)   # Seems like dummy (with purple pole)
output = output + replace_electric_signal('oneway_path', 6405)   # Restricted signal (with blue pole)

# Electric, programmable
print("Electric, programmable")
output = output + replace_electric_signal('programmable', 6175)
output = output + replace_electric_signal('programmable', 6207)   # Restricted signal (with blue pole)
