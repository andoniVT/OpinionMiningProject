'''
Created on 15/5/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

from SupervisedManager import Manager
from Voting import VotingSystem
from Settings import corpus_test1 as test1000 , corpus_test2 as test60798

class SentimentManager(object):
    
    def __init__(self):
        self.__supManager = Manager()
    
    def trainFirstStage(self):
        self.__supManager.prepareModelsFirstStage()
        self.__supManager.trainClassifiersFirstStage()
    
    def trainSecondStage(self):
        self.__supManager.prepareModelsSecondStage()
        self.__supManager.trainClassifiersSecondStage()
            
    def testFirstStage(self, test_data):
        self.__supManager.testClassifiersFirstStage(test_data)
    
    def testSecondStage(self, test_data):
        pass
    
    def testVotingSystemFS(self, test_data):
        pass 
    
    def testVotingSystemSS(self, test_data):
        pass
    
    
    def trainFirstStage3classes(self):
        pass
    
    def trainSecondStage3classes(self):
        pass 
    
    def testFirstStage3classes(self, test_data):
        pass 
    
    def testSecondStage3classes(self, test_data):
        pass 
    
    def testVotingSystem3classes(self, test_data):
        pass  
    
    

if __name__ == '__main__':
    
    obj = SentimentManager()
    obj.testFirstStage(test1000)    
    
  
  
    
    
        