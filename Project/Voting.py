'''
Created on 2/6/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

class VotingSystem(object):
    
    def __init__(self, y_true, svm, nb, me, dt):
        self.__trueLabels = y_true
        self.__predictedSVM = svm
        self.__predictedNB = nb
        self.__predictedME = me
        self.__predictedDT = dt
        self.__matrix = [self.__predictedSVM, self.__predictedNB, self.__predictedME, self.__predictedDT]
        
    
    def naiveVoting(self):
        positives = []
        negatives = []
        neutral = []
        nones = []
        
        for i in range(len(self.__trueLabels)):
            positives.append(0)
            negatives.append(0)
            neutral.append(0)
            nones.append(0)
            
        for i in range(len(self.__matrix)):
            for j in range(len(self.__trueLabels)):
                if self.__matrix[i][j] == "P":
                    positives[j]+=1
                elif self.__matrix[i][j] == "N":
                    negatives[j]+=1
                elif self.__matrix[i][j] == "NEU":
                    neutral[j]+=1
                elif self.__matrix[i][j] == "NONE":
                    nones[j]+=1
        
        
        
        print "P: " + str(positives)
        print "N: " +  str(negatives)
        print "NEU: " + str(neutral)
        print "NONE: " + str(nones) 
            
    
    def weightedVoting(self):
        pass 


if __name__ == '__main__':
    
    predictedSVM = ["P" , "P", "P",   "N",  "NEU", "NONE"]
    predictedNB = ["N" , "P",  "N",   "P",  "NEU", "NONE"]
    predictedME = ["P" , "N",  "NEU", "N",  "NEU", "P"]
    predictedDT = ["P" , "N",  "P", " NONE", "NEU", "P"]
    
    '''
                   P  N  NEU  NONE           -> random(NEU,NONE)
                   P P   N    N              -> random(P,N)
                   P P  NEU  NEU             -> NEU
                   P P  NONE NONE            -> NONE
                   
                   N N  NEU  NEU             -> NEU
                   N N NONE  NONE            -> NONE
                   
                   NEU NEU NONE NONE         -> random(NEU,NONE)
                   
                   P P P x                    -> P
                   N N N x                    -> N
                   NEU NEU NEU x              -> NEU
                   NONE NONE NONE x           -> NONE
                   
                   PPPP                       -> P
                   NNNN                       -> N
                   NEUNEUNEUNEU               -> NEU
                   NONENONENONENONE           -> NONE
    
    '''
    
    trueLabels = ["P" , "P", "P", "N", "NEU", "NEU"]
    
    obj = VotingSystem(trueLabels, predictedSVM, predictedNB, predictedME, predictedDT)
    
    obj.naiveVoting()
