import MapReduce
import sys

"""
Check whether friendship is symmetric using the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0];
    friend = record[1];
    mr.emit_intermediate(person, (friend,1))
    # not real 
    mr.emit_intermediate(friend, (person,0))


def reducer(key, list_of_values):
    # those who are key's friends
    friend_to = [x[0] for x in list_of_values if x[1] == 1]
    # those who's friend is key
    friend_from = [x[0] for x in list_of_values if x[1] == 0]
    for friend in friend_to:
        if friend not in friend_from:
            mr.emit((key, friend))
            mr.emit((friend, key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
