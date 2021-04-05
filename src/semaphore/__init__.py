"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""
from template import *

output = ""

# Semaphore, block
# We don't define semaphore block signal here since it could be changed as TVM sign.
print("Semaphore, block (skip)")
# output = output + replace_semaphore_signal('block', 5130)

# Semaphore, entrance
print("Semaphore, entrance")
output = output + replace_semaphore_signal('entrance', 5146)

# Semaphore, exit
print("Semaphore, exit")
output = output + replace_semaphore_signal('exit', 5162)

# Semaphore, combo
print("Semaphore, combo")
output = output + replace_semaphore_signal('combo', 5178)

# Semaphore, path
print("Semaphore, path")
output = output + replace_semaphore_signal('path', 5258)

# Semaphore, oneway_path
print("Semaphore, oneway path")
output = output + replace_semaphore_signal('oneway_path', 5274)

# Semaphore, programmable
print("Semaphore, programmable")
output = output + replace_semaphore_signal('programmable', 6159)
