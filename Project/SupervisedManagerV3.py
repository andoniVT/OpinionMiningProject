'''
Created on 25/6/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

from XMLReader import Reader
from XMLWritter import Writter
from TextCleaner import TextCleaner
from Settings import corpus_train1 as train1    
from Settings import corpus_test1 as test1  , labeled , labeled3c
from Settings import  pcorpus_train1 as ptrain1
from Settings import allVectorizerA, allVectorizerTFIDFA, allModelTFIDFA 
from Settings import allSVMA, allNBA, allMEA, allDTA, allRFA  
from Utils import expand , get_polarity_from_file , show_classification_report 
from VectorModel import VectorModel as VM
from Classifier import SupervisedClassifier as SC
from Utils import write_data_to_disk , load_data_from_disk , generate_resultsFile
import os.path
from Utils import hasSentiments

from Settings import allFullVectorizer, allFullVectorizerTFIDF, allFullModelTFIDF  
from Settings import allFullSVM, allFullNB, allFullME, allFullDT, allFullRF 
from Settings import resultsSVM1000, resultsNB1000, resultsMEM1000, resultsDTM1000, resultsRFM1000 
from Settings import resultsSVM60000, resultsNB60000, resultsMEM60000, resultsDTM60000, resultsRFM60000 
from Project.Settings import corpus_test1

class Manager3(object):
    
    def __init__(self):
        self.__trainData = self.getTrainData()
        self.__labels = []
        
                                
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
    
    
    def prepareModelsFirstStage(self):
        train_comments = []
        for i in self.__trainData:
            train_comments.append(i[0])
            self.__labels.append(i[1])
        
        
        model = VM(train_comments)
        vectorModelData = model.prepare_models()
        
        modelVectorizer = vectorModelData[0]
        modelVectorizerTFIDF = vectorModelData[1]
        modelTFIDF = vectorModelData[2]

        
        write_data_to_disk(allFullVectorizer, modelVectorizer)
        write_data_to_disk(allFullVectorizerTFIDF, modelVectorizerTFIDF)
        write_data_to_disk(allFullModelTFIDF, modelTFIDF)
    
    
    
    def trainClassifiersFirstStage(self):
        data = load_data_from_disk(allFullModelTFIDF)
        data_expanded = []
        for i in data:
            vec =  expand(i)
            data_expanded.append(vec)                 
        labels = self.__labels
                 
        fileClassifiers = [allFullSVM, allFullNB, allFullME, allFullDT, allFullRF]
                
        for i in range(5):            
            classifier = SC(data_expanded, labels, i+1)
            fClass = classifier.train()                                 
            write_data_to_disk(fileClassifiers[i], fClass)
    
    def testClassifiersFirstStage(self, test_data):
        vectorizer = load_data_from_disk(allFullVectorizer)
        transformer = load_data_from_disk(allFullVectorizerTFIDF)
        model = VM()
        model.set_models(vectorizer, transformer)    
        reader = Reader(test_data, 3)
        allDataTest = reader.read()
        
        test_ids = allDataTest[0]
        test_comments = allDataTest[1]
                                
        fileClassifiers = [allFullSVM, allFullNB, allFullME, allFullDT, allFullRF]                        
        all_labels_predicted = []                            
        for i in fileClassifiers:
            supClass = load_data_from_disk(i)
            classifier = SC()
            classifier.set_classifier(supClass)
            labels = []
            #for j in range(len(true_labels)):
            for j in range(len(test_comments)):
                proc = TextCleaner(test_comments[j])
                text_cleaned = proc.get_processed_comment()
                vector = model.get_comment_tf_idf_vector([text_cleaned])
                result = classifier.classify(vector)            
                labels.append(result[0][0])
                
                
            
            print labels
            all_labels_predicted.append(labels)
        
        
         

         

        
        fileResults = []
        if len(test_ids)==1000:         
            fileResults = [resultsSVM1000, resultsNB1000, resultsMEM1000, resultsDTM1000, resultsRFM1000]
        else:
            fileResults = [resultsSVM60000, resultsNB60000, resultsMEM60000, resultsDTM60000, resultsRFM60000]
            
        for i in range(len(fileResults)):
            generate_resultsFile(fileResults[i], test_ids, all_labels_predicted[i])
        
            
        return all_labels_predicted 
         
    

from Settings import corpus_test1 as test1000 , corpus_test2 as test60798

if __name__ == '__main__':
    
    obj = Manager3()
    #obj.prepareModelsFirstStage()
    #obj.trainClassifiersFirstStage()
    
    obj.testClassifiersFirstStage(test1000)
    print "ok"
    obj.testClassifiersFirstStage(test60798)
    
    
