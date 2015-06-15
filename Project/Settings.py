'''
Created on 15/5/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

'''resource '''
big_text =  'Resource/big2.txt'
stop_words = 'Resource/stopwords_spanish.txt'

''' original corpus '''
corpus_train1 = "Data/general-tweets-train-tagged.xml"
corpus_train1a =  "Data/nuevoTrainPrueba.xml"

corpus_train2 = "Data/socialtv-tweets-train-tagged.xml"

corpus_test1 = "Data/general-tweets-test1k.xml"
corpus_test2 = "Data/general-tweets-test.xml"
corpus_test3 = "Data/socialtv-tweets-test.xml"






''' corpus proccesed '''
pcorpus_train1 = "Data/general-tweets-train-tagged-proccesed.xml"

''' corpus manual labeled'''
labeled = "Data/manual-label-general-tweets-test1k.txt"
labeled2 = "Data/manual-label-general-tweets-test1k-500.txt"
labeled3 = "Data/manual-label-general-tweets-test1k-500_2.txt"


''' vector model '''
allVectorizer = "Models/all/simpleVectorizer.pk1"
allVectorizerTFIDF = "Models/all/tfidfVectorizer.pk1"
allModelTFIDF = "Models/all/tfidfModel.pk1"

pnneuVectorizer = "Models/p-n-neu/simpleVectorizer.pk1"
pnneuVectorizerTFIDF = "Models/p-n-neu/tfidfVectorizer.pk1"
pnneuModelTFIDF = "Models/p-n-neu/tfidfModel.pk1"

pnnoneVectorizer = "Models/p-n-none/simpleVectorizer.pk1"
pnnoneVectorizerTFIDF = "Models/p-n-none/tfidfVectorizer.pk1"
pnnoneModelTFIDF = "Models/p-n-none/tfidfModel.pk1"
  

''' classifiers '''
allSVM = "Classifiers/all/SVM.pk1"
allNB = "Classifiers/all/NB.pk1"
allME = "Classifiers/all/ME.pk1"
allDT = "Classifiers/all/DT.pk1"
allRF = "Classifiers/all/RF.pk1"
allAB = "Classifiers/all/AB.pk1"

pnneuSVM = "Classifiers/p-n-neu/SVM.pk1"
pnneuNB = "Classifiers/p-n-neu/NB.pk1"
pnneuME = "Classifiers/p-n-neu/ME.pk1"
pnneuDT = "Classifiers/p-n-neu/DT.pk1"

pnnoneSVM = "Classifiers/p-n-none/SVM.pk1"
pnnoneNB = "Classifiers/p-n-none/NB.pk1"
pnnoneME = "Classifiers/p-n-none/ME.pk1"
pnnoneDT = "Classifiers/p-n-none/DT.pk1"




''' results '''
firstResultsSVM1000 = "Results/firstStage/run1-testSVM1000.txt"
firstResultsNB1000 = "Results/firstStage/run1-testNB1000.txt"
firstResultsME1000 = "Results/firstStage/run1-testME1000.txt"
firstResultsDT1000 = "Results/firstStage/run1-testDT1000.txt"



