"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""

print("Electric")

output = ""

import block
output = output + block.output

import entrance
output = output + entrance.output

import exit
output = output + exit.output

import combo
output = output + combo.output

import oneway_path
output = output + oneway_path.output

import path
output = output + path.output
