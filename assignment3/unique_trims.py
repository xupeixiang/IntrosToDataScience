import MapReduce
import sys

"""
Manipulating string of nucleotides using the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[1]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    mr.emit(key[:len(key) - 10])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
