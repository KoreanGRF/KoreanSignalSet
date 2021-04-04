"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""
import sys
import os
import glob

sys.path.append(os.path.abspath("./src/electric/"))
sys.path.append(os.path.abspath("./src/semaphore/"))

# _ROOT path
_ROOT = os.path.dirname(os.path.abspath(__file__))[:-3]

# Import sub python files
import electric
import semaphore

output = electric.output + "\n" + semaphore.output

# Write a file
f = open(_ROOT + "generated/replace_blocks.pnml", "w")
f.write(output)
f.close()