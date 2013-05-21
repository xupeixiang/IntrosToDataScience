import MapReduce
import sys

"""
Join in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    line_items = [value for value in list_of_values if value[0] == 'line_item']
    orders = [value for value in list_of_values if value[0] == 'order']
    for order in orders:
        for line_item in line_items:
            mr.emit(order + line_item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
