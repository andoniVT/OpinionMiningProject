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
from Settings import allSVM, allNB, allME, allDT 
from Utils import compress , expand , get_polarity_from_file , show_classification_report , get_comments_from_file
from VectorModel import VectorModel as VM
from Classifier import SupervisedClassifier as SC
from Utils import write_data_to_disk , load_data_from_disk
import os.path

from Settings import pnneuVectorizer, pnneuVectorizerTFIDF, pnneuModelTFIDF 
from Settings import pnnoneVectorizer, pnnoneVectorizerTFIDF, pnnoneModelTFIDF  
from Settings import pnnoneSVM, pnnoneNB, pnnoneME, pnnoneDT
from Settings import pnneuSVM, pnneuNB, pnneuME, pnneuDT

class Manager(object):
    
    def __init__(self):
        self.__trainData = self.getTrainData()
                                
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
            elif i[1]=="NONE":
                train_commentsP_N_NONE.append(i[0])
            else :
                train_commentsP_N_NEU.append(i[0])
                train_commentsP_N_NONE.append(i[0])
        
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
                      
                                
    def trainClassifiersFirstStage(self):
        data = load_data_from_disk(allModelTFIDF)
        data_expanded = []
        for i in data:
            vec =  expand(i)
            data_expanded.append(vec)                 
        labels = []
        for i in self.__trainData:
            labels.append(i[1])            
        fileClassifiers = [allSVM, allNB, allME, allDT]
        for i in range(4):            
            classifier = SC(data_expanded, labels, i+1)
            fClass = classifier.train()                                 
            write_data_to_disk(fileClassifiers[i], fClass)
    
    def trainClassifiersSecondStage(self):
        data = load_data_from_disk(pnneuModelTFIDF)
        data2 = load_data_from_disk(pnnoneModelTFIDF)
        data_expanded = []
        data_expanded2 = []
        
        '''
        Continuara ...
        '''
        
         
        
        
    
    def testClassifiersFirstStage(self, test_data):
        vectorizer = load_data_from_disk(allVectorizer)
        transformer = load_data_from_disk(allVectorizerTFIDF)
        model = VM()
        model.set_models(vectorizer, transformer)
        
        reader = Reader(test_data, 3)
        test_comments = reader.read()
        
        
        fileClassifiers = [allSVM, allNB, allME, allDT]
        
        true_labels = get_polarity_from_file(labeled)
        
        all_labels_predicted = []
                    
        
        for i in fileClassifiers:
            supClass = load_data_from_disk(i)
            classifier = SC()
            classifier.set_classifier(supClass)
            labels = []
            for j in range(len(true_labels)):
                proc = TextCleaner(test_comments[j])
                text_cleaned = proc.get_processed_comment()
                vector = model.get_comment_tf_idf_vector([text_cleaned])
                result = classifier.classify(vector)            
                labels.append(result[0][0])
            show_classification_report(true_labels, labels)
            print "ok"
            all_labels_predicted.append(labels)
        return all_labels_predicted
    
        '''
        for i in test_comments:
            proc = TextCleaner(i)
            text_cleaned = proc.get_processed_comment()
            vector = model.get_comment_tf_idf_vector([text_cleaned])            
            print  i + "}"
             
            for i in fileClassifiers:
                supClass = load_data_from_disk(i)
                classifier = SC()
                classifier.set_classifier(supClass)
                result = classifier.classify(vector)
                print result[0][0]+"#" ,
            print ""
        '''
    
    def testClassifiersSecondStage(self, test_data):
        pass 
        
             
            
                            
        
        


if __name__ == '__main__':
    
    obj = Manager()
    test = ["Altozano tras la presentación de su libro 101 españoles y Dios. Divertido, emocionante y brillante." , "Mañana en Gaceta: TVE, la que pagamos tú y yo, culpa a una becaria de su falsa información sobre el cierre de @gaceta" , "Más mañana en Gaceta. Amaiur depende de Uxue Barkos para crear grupo propio. ERC no cumple el req. del 15% y el PNV no quiere competencia", "Dado q la deuda privada es superior a la publica, el recorte del gasto privado tiene q ser superior al del gasto publico. Xq nadie protesta?", "Portada El Mundo http://t.co/3EZnkcyL ...", "Tras un año, constato: a las 7 d la mañana, cuando paseo a la perra x mi barrio, 8 d cada 10 personas con las q me cruzo, son mujeres."]
    
    #obj.testClassifiersFirstStage(test1)
    
    
    ''' Training first stage'''
    #obj.prepareModelsFirstStage()
    #obj.trainClassifiersFirstStage()
    
    ''' Training second stage '''
    obj.prepareModelsSecondStage()
    #obj.trainClassifiersSecondStage(test1) 
    
