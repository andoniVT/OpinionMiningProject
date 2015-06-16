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
        labels = self.__supManager.testClassifiersFirstStage(test_data)
        predictedSVM = labels[0]
        predictedNB = labels[1]
        predictedME = labels[2]
        predictedDT = labels[3]
        predictedRF = labels[4]        
        voting = VotingSystem(test_data, predictedSVM, predictedNB, predictedME, predictedDT, predictedRF)
        naive = voting.naiveVoting() 
    
    
    
    
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
    obj.testFirstStage(test60798)
    obj.testSecondStage(test60798)
    obj.testVotingSystemFS(test60798)
        
    
  
  
    
    
        