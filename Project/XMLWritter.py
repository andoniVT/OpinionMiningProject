'''
Created on 20/5/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''
import elementtree.ElementTree as ET
from Settings import pcorpus_train1

class Writter(object):
    
    def __init__(self , data):
        self.__data = data
        self.__comments = self.__data[0]
        self.__labels = self.__data[1]
    
    def write(self , file):
        root = ET.Element("comments")
        id = 1
        for i in range(len(self.__comments)):            
            key = self.__comments[i]
            value = self.__labels[i]
            comment = ET.SubElement(root , "comment")
            comment_id = ET.SubElement(comment , "id")
            comment_id.text = str(id) 
            content = ET.SubElement(comment , "content")
            content.text = key 
            polarity = ET.SubElement(comment , "polarity")  
            polarity.text = value 
            id+=1
            print key , value
        tree = ET.ElementTree(root)
        tree.write(file)
         
    

if __name__ == '__main__':
    
    x = ["a","b","c","d","e"]
    y = ["False", "False", "True", "False", "True"]
    data = [x , y]
    
    obj = Writter(data)
    obj.write(pcorpus_train1)
    