'''
Created on 18/5/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

import elementtree.ElementTree as ET
from elementtree.ElementTree import ElementTree
from Settings import corpus_train1 , corpus_train2 , corpus_test1 , corpus_test2 , corpus_test3 , pcorpus_train1

class Reader(object):
    
    def __init__(self , file, type_xml):
        self.__file = file
        self.__type = type_xml
        self.__comments = self.read()        
                        
    def read(self):
        if self.__type == 1:
            return self.__readType1()
        elif self.__type == 2:
            return self.__readType2()
        elif self.__type == 3:
            return self.__readType3()
        elif self.__type == 4:
            return self.__readType4()
        elif self.__type == 5:
            return self.__readType5()
        elif self.__type == 6:
            return self.__readType6()
        else:
            return [] 
            
    def __readType1(self):
        tree = ET.parse(self.__file)
        root = tree.getroot()        
        dictionary = []        
        for child in root:
            content = child[2].text
            polarity = child[5][0][0].text
            values = (content , polarity)
            dictionary.append(values)                
        return dictionary
        
    def __readType2(self):
        tree = ET.parse(self.__file)
        root = tree.getroot()
        iter = root.getiterator()
        dictionary = []
        for element in iter:
            #print element.tag , element.attrib
            print element
                #dictionary.append(content)                                        
        return dictionary
    
    def __readType3(self):
        tree = ET.parse(self.__file)
        root = tree.getroot()
        ids = []
        dictionary = []        
        for child in root:
            tweet_id = child[0].text             
            content = child[2].text            
            dictionary.append(content)
            ids.append(tweet_id)          
        return [ids ,dictionary]
            
    def __readType4(self):
        tree = ET.parse(self.__file)
        root = tree.getroot()
        iter = root.getiterator()
        dictionary = []
        for element in iter:
            if element.text:
                content = element.text 
                dictionary.append(content)                                        
        return dictionary
    
    def __readType5(self):
        tree = ET.parse(self.__file)
        root = tree.getroot()
        dictionary = []
        for child in root:
            content = child[2].text            
            dictionary.append(content)          
        return dictionary
    
    def __readType6(self):
        tree = ET.parse(self.__file)
        root = tree.getroot()
        dictionary = []
        for child in root:
            content = child[1].text
            polarity = child[2].text
            values = (content , polarity)
            dictionary.append(values)              
        return dictionary
    
    def get_comments(self):
        return self.__comments
        
        
if __name__ == '__main__':

    obj = Reader(pcorpus_train1 , 6)
    comentarios = obj.get_comments()
    for i in comentarios:
        print i 