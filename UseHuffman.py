from HuffmanCode import HuffmanCode
from string import ascii_lowercase
from collections import Counter
import sys


path = "sample.txt"

with open(path) as f:
    print (Counter(letter for line in f
                  for letter in line.lower()
                  if letter in ascii_lowercase))

h = HuffmanCode(path)

output_path = h.compress()
print("Compressed file: " + output_path)


decom_path = h.decompress(output_path)
print("Decompressed file: " + decom_path)