#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 25/5/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''
from XMLReader import Reader
from XMLWritter import Writter
from TextCleaner import TextCleaner
from Settings import corpus_train1 as train1 , corpus_train2 as train2 , corpus_train1a as train1a   
from Settings import corpus_test1 as test1 , corpus_test2 as test2 , corpus_test3 as test3 , labeled2 , labeled3 , labeled
from Settings import  pcorpus_train1 as ptrain1
from Settings import allVectorizer, allVectorizerTFIDF, allModelTFIDF 
from Settings import allSVM, allNB, allME, allDT, allRF  
from Utils import compress , expand , get_polarity_from_file , show_classification_report , get_comments_from_file
from VectorModel import VectorModel as VM
from Classifier import SupervisedClassifier as SC
from Utils import write_data_to_disk , load_data_from_disk , generate_resultsFile
import os.path

from Settings import pnneuVectorizer, pnneuVectorizerTFIDF, pnneuModelTFIDF 
from Settings import pnnoneVectorizer, pnnoneVectorizerTFIDF, pnnoneModelTFIDF  
from Settings import pnnoneSVM, pnnoneNB, pnnoneME, pnnoneDT, pnnoneRF
from Settings import pnneuSVM, pnneuNB, pnneuME, pnneuDT, pnneuRF  
from Settings import firstResultsSVM1000 , firstResultsNB1000, firstResultsME1000, firstResultsDT1000, firstResultsRF1000
from Settings import secondResultsSVM1000, secondResultsNB1000, secondResultsME1000, secondResultsDT1000, secondResultsRF1000  
from Settings import firstResultsSVM60000, firstResultsNB60000, firstResultsME60000, firstResultsDT60000, firstResultsRF60000
class Manager(object):
    
    def __init__(self):
        self.__trainData = self.getTrainData()
        self.__labelsPNNEU = []
        self.__labelsPNEUNONE = []
                                
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
    
    def prepareModelsFirstStage(self):
        train_comments = []
        for i in self.__trainData:
            train_comments.append(i[0])
        
        model = VM(train_comments)
        vectorModelData = model.prepare_models()
        
        modelVectorizer = vectorModelData[0]
        modelVectorizerTFIDF = vectorModelData[1]
        modelTFIDF = vectorModelData[2]
        write_data_to_disk(allVectorizer, modelVectorizer)
        write_data_to_disk(allVectorizerTFIDF, modelVectorizerTFIDF)
        write_data_to_disk(allModelTFIDF, modelTFIDF)
    
    def prepareModelsSecondStage(self):
        train_commentsP_N_NEU = []
        train_commentsP_N_NONE = []
        for i in self.__trainData:
            if i[1]=="NEU":
                train_commentsP_N_NEU.append(i[0])
                self.__labelsPNNEU.append(i[1])
            elif i[1]=="NONE":
                train_commentsP_N_NONE.append(i[0])
                self.__labelsPNEUNONE.append(i[1])
            else :
                train_commentsP_N_NEU.append(i[0])
                train_commentsP_N_NONE.append(i[0])
                self.__labelsPNNEU.append(i[1])
                self.__labelsPNEUNONE.append(i[1])
        
        model = VM(train_commentsP_N_NEU)
        vectorModelData = model.prepare_models()
        modelVectorizer = vectorModelData[0]
        modelVectorizerTFIDF = vectorModelData[1]
        modelTFIDF = vectorModelData[2]
        write_data_to_disk(pnneuVectorizer, modelVectorizer)
        write_data_to_disk(pnneuVectorizerTFIDF, modelVectorizerTFIDF)
        write_data_to_disk(pnneuModelTFIDF, modelTFIDF)
        
        model2 = VM(train_commentsP_N_NONE)
        vectorModelData2 = model2.prepare_models()
        modelVectorizer2 = vectorModelData2[0]
        modelVectorizerTFIDF2 = vectorModelData2[1]
        modelTFIDF2 = vectorModelData2[2]
        write_data_to_disk(pnnoneVectorizer, modelVectorizer2)
        write_data_to_disk(pnnoneVectorizerTFIDF, modelVectorizerTFIDF2)
        write_data_to_disk(pnnoneModelTFIDF, modelTFIDF2)
    
    def prepareModelsFirstStage3C(self):
        pass 
    
    def prepareModelsSecondStage3C(self):
        pass
    
                                                      
    def trainClassifiersFirstStage(self):
        data = load_data_from_disk(allModelTFIDF)
        data_expanded = []
        for i in data:
            vec =  expand(i)
            data_expanded.append(vec)                 
        labels = []
        for i in self.__trainData:
            labels.append(i[1])            
        fileClassifiers = [allSVM, allNB, allME, allDT, allRF]
                
        for i in range(5):            
            classifier = SC(data_expanded, labels, i+1)
            fClass = classifier.train()                                 
            write_data_to_disk(fileClassifiers[i], fClass)
                    
    def trainClassifiersSecondStage(self):
        data = load_data_from_disk(pnneuModelTFIDF)
        data2 = load_data_from_disk(pnnoneModelTFIDF)
        data_expanded = []
        data_expanded2 = []
        for i in data:
            vec = expand(i)
            data_expanded.append(vec)
        for i in data2:
            vec = expand(i)
            data_expanded2.append(vec)
        
        fileClassifiers = [pnneuSVM, pnneuNB, pnneuME, pnneuDT, pnneuRF]
        fileClassifiers2 = [pnnoneSVM, pnnoneNB, pnnoneME, pnnoneDT, pnnoneRF]
        
        
        for i in range(5):
            print "first classifier: "
            classifier = SC(data_expanded, self.__labelsPNNEU, i+1)
            fClass = classifier.train()
            write_data_to_disk(fileClassifiers[i], fClass)
            print "second classifier"
            classifier2 = SC(data_expanded2, self.__labelsPNEUNONE, i+1)
            fClass2 = classifier2.train()
            write_data_to_disk(fileClassifiers2[i], fClass2)
    
    def trainClassifiersFirstStage3C(self):
        pass 
    
    def trainClassifiersSecondStage3C(self):
        pass
                    
    def testClassifiersFirstStage(self, test_data):
        vectorizer = load_data_from_disk(allVectorizer)
        transformer = load_data_from_disk(allVectorizerTFIDF)
        model = VM()
        model.set_models(vectorizer, transformer)    
        reader = Reader(test_data, 3)
        allDataTest = reader.read()
        test_ids = allDataTest[0]
        test_comments = allDataTest[1]                        
        fileClassifiers = [allSVM, allNB, allME, allDT, allRF]        
        #true_labels = get_polarity_from_file(labeled)        
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
            #show_classification_report(true_labels, labels)
            print "ok"
            all_labels_predicted.append(labels)
        
        fileResults = [firstResultsSVM1000, firstResultsNB1000, firstResultsME1000, firstResultsDT1000, firstResultsRF1000]
        for i in range(len(fileResults)):
            generate_resultsFile(fileResults[i], test_ids, all_labels_predicted[i])
        return all_labels_predicted    
        
    
    def classReduction(self, typeClassifier, test_data):
        predicted = []
        vectorizer = load_data_from_disk(pnneuVectorizer)
        transformer = load_data_from_disk(pnneuVectorizerTFIDF)
        model = VM()
        model.set_models(vectorizer, transformer)
        
        vectorizer2 = load_data_from_disk(pnnoneVectorizer)
        transformer2 = load_data_from_disk(pnnoneVectorizerTFIDF)
        model2 = VM()
        model2.set_models(vectorizer2, transformer2)
        
        reader = Reader(test_data, 3)
        allDataTest = reader.read()
        test_ids = allDataTest[0]
        test_comments = allDataTest[1]            
        #true_labels = get_polarity_from_file(labeled)            
        #true_labels = get_polarity_from_file(labeled2)
        fileClassifiers = [pnneuSVM, pnneuNB, pnneuME, pnneuDT, pnneuRF]
        fileClassifiers2 = [pnnoneSVM, pnnoneNB, pnnoneME, pnnoneDT, pnnoneRF]
        
        labelsPNNEU = []
        labelsPNNONE = []
        
        supClass = load_data_from_disk(fileClassifiers[typeClassifier-1])
        classifier = SC()
        classifier.set_classifier(supClass)
        
        supClass2 = load_data_from_disk(fileClassifiers2[typeClassifier-1])
        classifier2 = SC()
        classifier2.set_classifier(supClass2)
        
        
                
        #for j in range(len(true_labels)):
        for j in range(len(test_comments)):
            proc = TextCleaner(test_comments[j])
            text_cleaned = proc.get_processed_comment()
            
            vector = model.get_comment_tf_idf_vector([text_cleaned])
            result = classifier.classify(vector)            
            labelsPNNEU.append(result[0][0])
            
            vector2 = model2.get_comment_tf_idf_vector([text_cleaned])
            result2 = classifier2.classify(vector2)
            labelsPNNONE.append(result2[0][0])
        
        for i in range(len(labelsPNNEU)):
            label = labelsPNNEU[i]
            label2 = labelsPNNONE[i]
            if label == "P" and label2 == "P":
                predicted.append("P")
            elif label == "P" and label2 == "N":
                predicted.append("NEU")
            elif label == "P" and label2 == "NONE":
                predicted.append("NONE")
            elif label == "N" and label2 == "P":
                predicted.append("NEU")
            elif label == "N" and label2 == "N":
                predicted.append("N")
            elif label == "N" and label2 == "NONE":
                predicted.append("NONE")
            elif label == "NEU" and label2 == "P":
                predicted.append("NEU")
            elif label == "NEU" and label2 == "N":
                predicted.append("NEU")
            elif label == "NEU" and label2 == "NONE":
                predicted.append("NONE")                                                
        return predicted
    
    def testClassifiersSecondStage(self, test_data):
        all_labels = []
        reader = Reader(test_data, 3)
        allDataTest = reader.read()
        test_ids = allDataTest[0]
        for i in range(5):
            labels = self.classReduction(i+1, test_data)
            all_labels.append(labels)
            print "ok" 
        
        fileResults = []
        if len(test_ids)==1000:        
            fileResults = [secondResultsSVM1000, secondResultsNB1000, secondResultsME1000, secondResultsDT1000, secondResultsRF1000]
        else:
            fileResults = [firstResultsSVM60000, firstResultsNB60000, firstResultsME60000, firstResultsDT60000, firstResultsRF60000]
            
        for i in range(len(fileResults)):
            generate_resultsFile(fileResults[i], test_ids, all_labels[i])           
        return all_labels
    
    def testClassifiersFirstStage3C(self, test_data):
        pass
    
    def testClassifiersSecondStage3C(self, test_data):
        pass 
    
                    
if __name__ == '__main__':
    
    obj = Manager()        
    #obj.testClassifiersFirstStage(test1)
    
    true_labels = get_polarity_from_file(labeled)
    labels =  obj.testClassifiersSecondStage(test1)
    for i in labels:
        show_classification_report(true_labels, i)
    
        
    
    
    
    
    ''' Training first stage'''
    #obj.prepareModelsFirstStage()
    #obj.trainClassifiersFirstStage()
    
    ''' Training second stage '''
    #obj.prepareModelsSecondStage()
    #obj.trainClassifiersSecondStage() 
    
