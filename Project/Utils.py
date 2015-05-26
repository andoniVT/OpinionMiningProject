'''
Created on 22/5/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''
from _dbus_bindings import Array
from array import array
import cPickle
testFile = "testFile.txt"

def compress(vector):
    result = {}
    pos = 0 
    for i in vector: 
        if i != 0:
            result[pos] = i
        pos+=1    
    return [result , pos]

def expand(vector):
    values = vector[0]
    size = vector[1]
    result = []
    
    for i in range(size):
        if values.has_key(i):
            result.append(values.get(i))
        else:
            result.append(0)
    return result

def write_data_to_disk(file, data):
    with open(file, 'wb') as fid:
        cPickle.dump(data, fid)

def load_data_from_disk(file):
    with open(file, 'rb') as fid:
        data = cPickle.load(fid)
    return data  

def parse_file(file):
    lines = []
    with open(file) as f:
        content = f.readlines()
        for i in content:
            lines.append(i)
    
    for i in lines:
        print i
    

     
    


if __name__ == '__main__':
    
    parse_file(testFile)