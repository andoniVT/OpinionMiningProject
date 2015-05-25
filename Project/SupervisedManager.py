'''
Created on 25/5/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''
from XMLReader import Reader
from XMLWritter import Writter
from TextCleaner import TextCleaner
from Settings import corpus_train1 as train1 , corpus_train2 as train2   
from Settings import corpus_test1 as test1 , corpus_test2 as test2 , corpus_test3 as test3
from Settings import  pcorpus_train1 as ptrain1
import os.path

class Manager(object):
    
    def __init__(self):
        self.__trainData = self.getTrainData()
        
    
    def getTrainData(self):
        flag = os.path.isfile(ptrain1)
        if flag:        
            return self.__readProccesedTrainData()
        else:            
            return self.__readTrainData()
            
    def __readData(self):
        comments = []
        labels = []
        reader = Reader(train1, 1)
        corpus = reader.get_comments()
        for i in corpus:
            if i[0] is not None:
                proc = TextCleaner(i[0])
                texto_procesado = proc.get_processed_comment()
                if texto_procesado!= "None!":
                    comments.append(texto_procesado)
                    if i[1] == "P+":                                            
                        labels.append("P")
                    elif i[1] == "N+":                                                                    
                        labels.append("N")                            
                    else:                                                 
                        labels.append(i[1])
        return [comments , labels]
    
    def __readTrainData(self):
        all_comments =  self.__readData()
        writ = Writter(all_comments)
        writ.write(ptrain1)
        obj = Reader(ptrain1 , 6)
        comentarios = obj.get_comments()
        return comentarios
    
    def __readProccesedTrainData(self):
        obj = Reader(ptrain1 , 6)
        comentarios = obj.get_comments()
        return comentarios  



if __name__ == '__main__':
    
    obj = Manager()
