import MapReduce
import sys

"""
Mutiply matrix  using the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
N = 5
def mapper(record):
    if record[0] == 'a':
        for i in range(N):
            mr.emit_intermediate((record[1],i),('a',record[2],record[3]))
    else:
        for i in range(N):
            mr.emit_intermediate((i,record[2]),('b',record[1],record[3]))

def reducer(key, list_of_values):
    values_a = [0] * N
    values_b = [0] * N
    for value in list_of_values:
        if(value[0] == 'a'):
            values_a[value[1]] = value[2]
        else:
            values_b[value[1]] = value[2]
    value = sum([values_a[i] * values_b[i] for i in range(N)])
    mr.emit((key[0],key[1],value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
