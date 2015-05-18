'''
Created on 18/5/2015

@author: ucsp
'''

import elementtree.ElementTree as ET
from elementtree.ElementTree import ElementTree

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
        return [1,2,3]
    
    def __readType2(self):
        pass
    
    def __readType3(self):
        pass
    
    def __readType4(self):
        pass
    
    def __readType5(self):
        pass
    
    def get_comments(self):
        return self.__comments
        
        
if __name__ == '__main__':
    
    obj = Reader("lala.xml" , 1)
    comentarios = obj.get_comments()
    print comentarios

