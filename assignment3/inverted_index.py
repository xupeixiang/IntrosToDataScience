import MapReduce
import sys

"""
Build inverted index using Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    doc_id = record[0]
    text = record[1]
    for word in text.split(' '):
        mr.emit_intermediate(word, doc_id)

def reducer(key, list_of_values):
    doc_list = []
    for doc_id in list_of_values:
        if doc_id not in doc_list:
            doc_list.append(doc_id);
    mr.emit((key, doc_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
