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
import elementtree.ElementTree as ET
from Settings import corpus_train1 as train1 , labeled3

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

def get_comments_from_file(file):
    lines = []
    with open(file) as f:
        content = f.readlines()
        for i in content:
            i = i.rstrip()
            end = i.find("}")
            lines.append(i[0:end])
    return lines 

def show_classification_report(y_true, y_predicted):
    print classification_report(y_true, y_predicted)
    print confusion_matrix(y_true, y_predicted)
    

def generar_xml(contenido, valores):
    root = ET.Element("tweets")
    id = 1
    for i in range(len(contenido)):                        
        comment = ET.SubElement(root , "tweet")
        
        comment_id = ET.SubElement(comment , "tweetid")
        comment_id.text = str(id)
        
        user = ET.SubElement(comment , "user")
        
        content = ET.SubElement(comment , "content")
        content.text = contenido[i]
        
        date = ET.SubElement(comment , "date")
        
        lang = ET.SubElement(comment , "lang")
        
        sentiments = ET.SubElement(comment , "sentiments")
        pol = ET.SubElement(sentiments , "polarity")
        value = ET.SubElement(pol , "value")
        value.text = valores[i]
         
        id+=1
        
    tree = ET.ElementTree(root)
    tree.write("nuevoTrainPrueba.xml")

def auxiliar():
    total_neu = 201
    total_none = 444
    aux_neu = 0
    aux_none = 0
    
    contenidos_train = []
    polaridades_train = []
    
    neutros_test = []
    nones_test = []
    
    tree = ET.parse(train1)
    root = tree.getroot()        
            
    for child in root:
        content = child[2].text
        polarity = child[5][0][0].text
        
        if polarity == "NEU" and aux_neu < total_neu:
            values = (content , polarity)
            neutros_test.append(values)
            aux_neu+=1 
        
        elif polarity == "NONE" and aux_none < total_none:
            values = (content , polarity)
            nones_test.append(values)
            aux_none+=1
        
        else:
            contenidos_train.append(content)
            polaridades_train.append(polarity)
    
    generar_xml(contenidos_train, polaridades_train)
    
    print "NEUTROS"
    for i in neutros_test:
        print i[0] + "}" + i[1]
    
    print "\n"
    print "NONES"
    for i in nones_test:
        print i[0] + "}" + i[1]

def generate_resultsFile(file,ids, labels):
    file_to_write = open(file, 'w')
    for i in range(len(ids)):
        line = ids[i] + "\t" + labels[i] + "\n"
        file_to_write.write(line)
    
if __name__ == '__main__':
    
    file = "testFile.txt"
    ids = ["123" , "456", "789"]
    labels = ["P" , "P", "N"]
    generate_resultsFile(file, ids, labels)
    
