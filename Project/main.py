'''
Created on 15/5/2015

@author: ucsp
'''
from XMLReader import Reader
from TextCleaner import TextCleaner
from Settings import corpus_train1 as train1 , corpus_train2 as train2   
from Settings import corpus_test1 as test1 , corpus_test2 as test2 , corpus_test3 as test3

class Manager(object):
    
    def __init__(self):
        self.__train_data = []
    
    def getTrainData(self):
        reader = Reader(train1, 1)
        corpus = reader.get_comments()
        for i in corpus:
            if i[0] is not None:
                proc = TextCleaner(i[0])
                texto_procesado = proc.get_processed_comment()
                if texto_procesado!= "None!":
                    print texto_procesado + " - " + i[1]   


if __name__ == '__main__':
    
    obj = Manager()
    obj.getTrainData()    
    '''
    for i in corpus:         
        if i is not None:
            proc = TextCleaner(i)
            texto_procesado = proc.get_processed_comment()
            if texto_procesado == "None!":
                print "Nonee" + " -> " + i
            else:  
                print texto_procesado
    '''
         
    
    
