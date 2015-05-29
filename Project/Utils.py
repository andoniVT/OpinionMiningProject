'''
Created on 22/5/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''
import cPickle
from Settings import labeled , labeled2
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
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

def get_polarity_from_file(file):
    lines = []
    with open(file) as f:
        content = f.readlines()        
        for i in content:
            i = i.rstrip()
            begin = i.find("}")+1
            end = len(i)
            polarity = i[begin:end]                         
            lines.append(polarity)    
    return lines

def show_classification_report(y_true, y_predicted):
    print classification_report(y_true, y_predicted)
    print confusion_matrix(y_true, y_predicted)
    


if __name__ == '__main__':
    
    y_true = ["P" , "P" , "N" , "NONE" , "NEU"]
    y_predicted = ["P" , "P" , "N" , "NONE" , "NEU"]
    
    #y_true = [1.0 , 1.0 , -1.0 , 0.0 , 0.5]
    #y_predicted = [1.0 , -1.0 , 0.0 , 0.0 , -1.0]
    
    show_classification_report(y_true, y_predicted)
    
    