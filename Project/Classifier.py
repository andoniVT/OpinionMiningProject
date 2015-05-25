'''
Created on 22/5/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''
from sklearn.svm import LinearSVC as SVM
from sklearn.naive_bayes import MultinomialNB as NB
from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.linear_model import LogisticRegression as ME


class SupervisedClassifier(object):
    
    def __init__(self, data=None, labels=None , type=None):
        self.__data = data
        self.__labels = labels
        self.__type = type
        self.__classifier = []
    
    def train(self):
        if self.__type == 1:
            return self.__trainSVM()
        elif self.__type == 2:
            return self.__trainNB()
        elif self.__type == 3:
            return self.__trainME()
        else:
            return self.__trainDT()
    
    def __trainSVM(self):
        print "Training Support Vector Machine"
        classifier = SVM()
        classifier = classifier.fit(self.__data, self.__labels)
        self.__classifier = classifier
        return classifier
        
    
    def __trainNB(self):
        print "Training Naive Bayes"
        classifier = NB()
        classifier = classifier.fit(self.__data, self.__labels)
        self.__classifier = classifier
        return classifier
    
    def __trainME(self):
        print "Training Max Entropy"
        classifier = ME()
        classifier = classifier.fit(self.__data, self.__labels)
        self.__classifier = classifier
        return classifier
    
    def __trainDT(self):
        print "Training Decision Tree"
        classifier = DT()
        classifier = classifier.fit(self.__data, self.__labels)
        self.__classifier = classifier
        return classifier
    
    def classify(self, test_data):
        predictions = []
        for i in test_data:
            value = self.__classifier.predict(i)
            predictions.append(value)
        return predictions
    
    def set_classifier(self, classifier):
        self.__classifier = classifier
                
         

if __name__ == '__main__':
    
    data = [[1,2,3], [4,5,6],[3,2,1],[6,5,4],[2,5,8]]
    labels = [1,1,0,0,1]
    
    obj = SupervisedClassifier(data, labels,1)
    obj.train()
    
    test = [[1,2,3],[3,2,1]]
    print obj.classify(test)
    
    
    