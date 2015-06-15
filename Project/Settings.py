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




''' results 4 classes'''
firstResultsSVM1000 = "Results/results_4classes/firstStage/run1-testSVM1000.txt"
firstResultsNB1000 = "Results/results_4classes/firstStage/run1-testNB1000.txt"
firstResultsME1000 = "Results/results_4classes/firstStage/run1-testME1000.txt"
firstResultsDT1000 = "Results/results_4classes/firstStage/run1-testDT1000.txt"
firstResultsRF1000 = "Results/results_4classes/firstStage/run1-testRF1000.txt"
secondResultsSVM1000 = "Results/results_4classes/secondStage/run2-testSVM1000.txt"
secondResultsNB1000 = "Results/results_4classes/secondStage/run2-testNB1000.txt"
secondResultsME1000 = "Results/results_4classes/secondStage/run2-testME1000.txt"
secondResultsDT1000 = "Results/results_4classes/secondStage/run2-testDT1000.txt"
secondResultsRF1000 = "Results/results_4classes/secondStage/run2-testRF1000.txt"
thirdResultsNaiveVoting1000 = "Results/results_4classes/thirdStage/run3-testNV1000.txt"

firstResultsSVM60000 = "Results/results_4classes/firstStage/run1-testSVM60000.txt"
firstResultsNB60000 = "Results/results_4classes/firstStage/run1-testNB60000.txt"
firstResultsME60000 = "Results/results_4classes/firstStage/run1-testME60000.txt"
firstResultsDT60000 = "Results/results_4classes/firstStage/run1-testDT60000.txt"
firstResultsRF60000 = "Results/results_4classes/firstStage/run1-testRF60000.txt"
secondResultsSVM60000 = "Results/results_4classes/secondStage/run2-testSVM60000.txt"
secondResultsNB60000 = "Results/results_4classes/secondStage/run2-testNB60000.txt"
secondResultsME60000 = "Results/results_4classes/secondStage/run2-testME60000.txt"
secondResultsDT60000 = "Results/results_4classes/secondStage/run2-testDT60000.txt"
secondResultsRF60000 = "Results/results_4classes/secondStage/run2-testRF60000.txt"
thirdResultsNaiveVoting60000 = "Results/results_4classes/thirdStage/run3-testNV60000.txt"

''' results 3 classes '''
threeClassFirstResultsSVM1000 = "Results/results_3classes/firstStage/run1-testSVM1000.txt"
threeClassFirstResultsNB1000 = "Results/results_3classes/firstStage/run1-testNB1000.txt"
threeClassFirstResultsME1000 = "Results/results_3classes/firstStage/run1-testME1000.txt"
threeClassFirstResultsDT1000 = "Results/results_3classes/firstStage/run1-testDT1000.txt"
threeClassFirstResultsRF1000 = "Results/results_3classes/firstStage/run1-testRF1000.txt"
threeClassSecondResultsSVM1000 = "Results/results_3classes/secondStage/run2-testSVM1000.txt"
threeClassSecondResultsNB1000 = "Results/results_3classes/secondStage/run2-testNB1000.txt"
threeClassSecondResultsME1000 = "Results/results_3classes/secondStage/run2-testME1000.txt"
threeClassSecondResultsDT1000 = "Results/results_3classes/secondStage/run2-testDT1000.txt"
threeClassSecondResultsRF1000 = "Results/results_3classes/secondStage/run2-testRF1000.txt"
threeClassThirdResultsNaiveVoting1000 = "results_3classes/thirdStage/run3-testNV1000.txt"

firstResultsSVM60000 = "Results/results_3classes/firstStage/run1-testSVM60000.txt"
firstResultsNB60000 = "Results/results_3classes/firstStage/run1-testNB60000.txt"
firstResultsME60000 = "Results/results_3classes/firstStage/run1-testME60000.txt"
firstResultsDT60000 = "Results/results_3classes/firstStage/run1-testDT60000.txt"
firstResultsRF60000 = "Results/results_3classes/firstStage/run1-testRF60000.txt"
secondResultsSVM60000 = "Results/results_3classes/secondStage/run2-testSVM60000.txt"
secondResultsNB60000 = "Results/results_3classes/secondStage/run2-testNB60000.txt"
secondResultsME60000 = "Results/results_3classes/secondStage/run2-testME60000.txt"
secondResultsDT60000 = "Results/results_3classes/secondStage/run2-testDT60000.txt"
secondResultsRF60000 = "Results/results_3classes/secondStage/run2-testRF60000.txt"
thirdResultsNaiveVoting60000 = "Results/Results/thirdStage/run3-testNV60000.txt"




