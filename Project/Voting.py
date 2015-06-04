import random
from SupervisedManager import Manager
from Settings import corpus_test1 as test1 , labeled2
from Utils import get_polarity_from_file , show_classification_report

'''
Created on 2/6/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

'''
    P  N  NEU  NONE  [1,1,1,1]         -> random(NEU,NONE) 
    P P   N    N     [2,2,0,0]         -> random(P,N)
    P P  NEU  NEU    [2,0,2,0]         -> NEU
    P P  NONE NONE   [2,0,0,2]         -> NONE
    N N  NEU  NEU    [0,2,2,0]         -> NEU
    N N NONE  NONE   [0,2,0,2]         -> NONE                   
    NEU NEU NONE NONE   [0,0,2,2]        -> random(NEU,NONE)                   
    P P P x          [3,,,]          -> P
    N N N x          [,3,,]          -> N
    NEU NEU NEU x    [,,3,]          -> NEU
    NONE NONE NONE x [,,,3]          -> NONE                   
    PPPP             [4,0,0,0]          -> P
    NNNN             [0,4,0,0]          -> N
    NEUNEUNEUNEU     [0,0,4,0]          -> NEU
    NONENONENONENONE [0,0,0,4]          -> NONE                   
    P P N NEU     [2,1,1,0]    -> P
    P P N NONE    [2,1,0,1]    -> P
    P P NEU NONE  [2,0,1,1]    -> P                   
    N N P NEU    [1,2,1,0]     -> N
    N N NEU NONE [0,2,1,1]     -> N
    N N P NONE   [1,2,0,1]     -> N                   
    NEU NEU  [] -> NEU                   
    NONE NONE -> NONE                   
'''

class VotingSystem(object):
    
    def __init__(self, svm, nb, me, dt):        
        self.__predictedSVM = svm
        self.__predictedNB = nb
        self.__predictedME = me
        self.__predictedDT = dt
        self.__matrix = [self.__predictedSVM, self.__predictedNB, self.__predictedME, self.__predictedDT]
        self.__predicted = []
        
    
    def naiveVoting(self):
        positives = []
        negatives = []
        neutral = []
        nones = []
        
        for i in range(len(self.__predictedSVM)):
            positives.append(0)
            negatives.append(0)
            neutral.append(0)
            nones.append(0)
            
        for i in range(len(self.__matrix)):
            for j in range(len(self.__predictedSVM)):
                if self.__matrix[i][j] == "P":
                    positives[j]+=1
                elif self.__matrix[i][j] == "N":
                    negatives[j]+=1
                elif self.__matrix[i][j] == "NEU":
                    neutral[j]+=1
                elif self.__matrix[i][j] == "NONE":
                    nones[j]+=1
        
        for i in range(len(positives)):
            if positives[i]>=3:                
                self.__predicted.append("P")
            elif negatives[i]>=3:                
                self.__predicted.append("N")
            elif neutral[i]>=3:                
                self.__predicted.append("NEU")
            elif nones[i]>=3:                
                self.__predicted.append("NONE")
            elif positives[i]==1 and negatives[i]==1 and neutral[i]==1 and nones[i]==1:
                flag = random.randrange(2)
                if flag==0:                     
                    self.__predicted.append("NEU")
                if flag==1:                     
                    self.__predicted.append("NONE")                 
            elif positives[i]==2 and negatives[i]==2:
                flag = random.randrange(2)
                if flag==0:                     
                    self.__predicted.append("P")
                if flag==1:                     
                    self.__predicted.append("N")                
            elif positives[i]==2 and neutral[i]==2:                
                self.__predicted.append("NEU")
            elif positives[i]==2 and nones[i]==2:                
                self.__predicted.append("NONE")
            elif negatives[i]==2 and neutral[i]==2:                
                self.__predicted.append("NEU")
            elif negatives[i]==2 and nones[i]==2:                
                self.__predicted.append("NONE")
            elif neutral[i]==2 and nones[i]==2:
                flag = random.randrange(2)
                if flag==0:                     
                    self.__predicted.append("NEU")
                if flag==1:                     
                    self.__predicted.append("NONE")
            elif positives[i]==2:                
                self.__predicted.append("P")
            elif negatives[i]==2:                
                self.__predicted.append("N")
            elif neutral[i]==2:                
                self.__predicted.append("NEU")
            elif nones[i]==2:                
                self.__predicted.append("NONE")
            else:
                print "Nose!" 
                        
        return self.__predicted 
            
    
    def weightedVoting(self):
        pass 


if __name__ == '__main__':
    
    '''
    predictedSVM = ["P" , "P", "P",   "N",  "NEU", "NONE"]
    predictedNB = ["N" , "P",  "N",   "P",  "NONE", "NEU"]
    predictedME = ["P" , "N",  "NEU", "N",  "NEU", "P"]
    predictedDT = ["P" , "N",  "P", " NONE", "NONE", "P"]    
    trueLabels = ["P" , "P", "P", "N", "NEU", "NEU"]
    '''
    
    obj = Manager()
    labels = obj.testClassifiersFirstStage(test1)
    predictedSVM = labels[0]
    predictedNB = labels[1]
    predictedME = labels[2]
    predictedDT = labels[3]
    trueLabels = get_polarity_from_file(labeled2)
    
    voting = VotingSystem(predictedSVM, predictedNB, predictedME, predictedDT)
    naive = voting.naiveVoting()
    show_classification_report(trueLabels, naive)
    
    
    
    
    
    
    
    
    #naive = obj.naiveVoting()
    #print naive
