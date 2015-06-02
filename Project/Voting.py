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
    
    def naiveVoting(self):
        pass
    
    def weightedVoting(self):
        pass 


if __name__ == '__main__':
    
    predictedSVM = []
    predictedNB = []
    predictedME = []
    predictedDT = []
    trueLabels = []
