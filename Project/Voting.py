
'''
Created on 2/6/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

import random
from SupervisedManager import Manager
from Settings import corpus_test1 as test1 , labeled2 , labeled , labeled3c
from Utils import get_polarity_from_file , show_classification_report, generate_resultsFile
from Settings import thirdResultsNaiveVoting1000 , thirdResultsNaiveVoting60000
from XMLReader import Reader
from Settings import threeClassThirdResultsNaiveVoting1000, threeClassThirdResultsNaiveVoting60000

class VotingSystem(object):
    
    def __init__(self, test_data, svm, nb, me, dt, rf):        
        self.__predictedSVM = svm
        self.__predictedNB = nb
        self.__predictedME = me
        self.__predictedDT = dt
        self.__predictedRF = rf
        self.__matrix = [self.__predictedSVM, self.__predictedNB, self.__predictedME, self.__predictedDT, self.__predictedRF]
        self.__predicted = []
        reader = Reader(test_data, 3)
        self.__allDataTest = reader.read()
        self.__test_ids = self.__allDataTest[0]
        
    
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
        
        fileResults = ""
        if len(self.__test_ids)==1000:        
            fileResults = thirdResultsNaiveVoting1000 
        else:
            fileResults = thirdResultsNaiveVoting60000
                    
        generate_resultsFile(fileResults, self.__test_ids, self.__predicted)
                        
        return self.__predicted 
    
    def naiveVoting3C(self):
        positives = []
        negatives = []
        neutral = []
        
        for i in range(len(self.__predictedSVM)):
            positives.append(0)
            negatives.append(0)
            neutral.append(0)
            
        for i in range(len(self.__matrix)):
            for j in range(len(self.__predictedSVM)):
                if self.__matrix[i][j] == "P":
                    positives[j]+=1
                elif self.__matrix[i][j] == "N":
                    negatives[j]+=1
                elif self.__matrix[i][j] == "NEU":
                    neutral[j]+=1
                
    
        for i in range(len(positives)):
            if positives[i]>=3:                
                self.__predicted.append("P")
            elif negatives[i]>=3:                
                self.__predicted.append("N")
            elif neutral[i]>=3:                
                self.__predicted.append("NEU")            
            elif positives[i]==1 and negatives[i]==1 and neutral[i]==1:      
                self.__predicted.append("NEU")                                 
            elif positives[i]==2 and negatives[i]==2:
                flag = random.randrange(2)
                if flag==0:                     
                    self.__predicted.append("P")
                if flag==1:                     
                    self.__predicted.append("N")                
            elif positives[i]==2 and neutral[i]==2:                
                self.__predicted.append("NEU")            
            elif negatives[i]==2 and neutral[i]==2:                
                self.__predicted.append("NEU")            
            elif positives[i]==2:                
                self.__predicted.append("P")
            elif negatives[i]==2:                
                self.__predicted.append("N")
            elif neutral[i]==2:                
                self.__predicted.append("NEU")            
            else:
                print "Nose!"
                print str(positives[i]) + " " + str(negatives[i]) + " " + str(neutral[i])
        
        
        
        
        fileResults = ""
        if len(self.__test_ids)==1000:        
            fileResults = threeClassThirdResultsNaiveVoting1000 
        else:
            fileResults = threeClassThirdResultsNaiveVoting60000
                    
        generate_resultsFile(fileResults, self.__test_ids, self.__predicted)
        
                        
        return self.__predicted 
            
    
if __name__ == '__main__':
    
    obj = Manager()
    labels = obj.testClassifiersSecondStage3C(test1)
    predictedSVM = labels[0]
    predictedNB = labels[1]
    predictedME = labels[2]
    predictedDT = labels[3]
    predictedRF = labels[4]
    trueLabels = get_polarity_from_file(labeled3c)
    
    voting = VotingSystem(test1, predictedSVM, predictedNB, predictedME, predictedDT, predictedRF)
    naive = voting.naiveVoting3C()
    show_classification_report(trueLabels, naive)
    
    
    #naive = obj.naiveVoting()
    #print naive
