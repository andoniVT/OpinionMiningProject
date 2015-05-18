'''
Created on 18/5/2015

@author: ucsp
'''

import elementtree.ElementTree as ET
from elementtree.ElementTree import ElementTree
from Settings import corpus_train1 , corpus_train2 , corpus_test1 , corpus_test2 

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
        else:
            return [] 
            
    def __readType1(self):
        tree = ET.parse(self.__file)
        root = tree.getroot()
        dictionary = {}
        for child in root:
            content = child[2].text
            polarity = child[5][0][0].text
            dictionary[content] = polarity          
        return dictionary
    
    def __readType2(self):
        pass
    
    def __readType3(self):
        tree = ET.parse(self.__file)
        root = tree.getroot()
        dictionary = []
        for child in root:
            content = child[2].text            
            dictionary.append(content)          
        return dictionary
            
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
        pass
    
    def get_comments(self):
        return self.__comments
        
        
if __name__ == '__main__':

    obj = Reader(corpus_test2 , 4)
    comentarios = obj.get_comments()
    print comentarios[1]
    #for i in comentarios:
    #    print i 
    '''
    comentarios = obj.get_comments()
    for i in comentarios.items():
        print i
    ''' 