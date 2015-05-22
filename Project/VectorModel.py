'''
Created on 22/5/2015
@author: Jorge Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

from scipy import spatial
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


class VectorModel(object):
    
    def __init__(self , data=None):
        self.__data = data
        self.__vectorizer = []
        self.__corpus = []
        self.__transformer = []
        self.__corpus_tf_idf = [] 
    
    def prepare_models(self):
        self.__vectorizer = CountVectorizer()
        vector = self.__vectorizer.fit_transform(self.__data)
        self.__corpus = vector.toarray()
        self.__transformer = TfidfTransformer()
        tfidf = self.__transformer.fit_transform(self.__corpus)
        self.__corpus_tf_idf = tfidf.toarray()
        return [self.__vectorizer, self.__corpus, self.__transformer, self.__corpus_tf_idf]
    
    def set_models(self, vectorizer, transformer):
        self.__vectorizer = vectorizer
        self.__transformer = transformer
        
    def get_comment_frequency_vector(self, comments):
        vec_comments = []
        for i in comments:
            vec_comments.append(i)
        vectores = self.__vectorizer.transform(vec_comments).toarray()
        return vectores 
    
    def get_comment_tf_idf_vector(self, comments):
        vector = self.get_comment_frequency_vector(comments)
        result = self.__transformer.transform(vector).toarray()
        return result

if __name__ == '__main__':
    
    print "hello"
