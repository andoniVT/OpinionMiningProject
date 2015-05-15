#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 15/5/2015

@author: ucsp
'''
import re
import unicodedata
from unicodedata import normalize
from split import separar
import snowballstemmer
from Settings import stop_words

stopWordFile = stop_words

class TextCleaner(object):
    
    def __init__(self, comment="" , flag=True):
        self.__comment = comment
        self.__remove_stop = flag
        self.__cleaned = ""
    
    def remove_accent(self , word):
        word= word.replace("á", "a")
        word= word.replace("é", "e")
        word= word.replace("í", "i") 
        word= word.replace("ó", "o")
        word= word.replace("ú", "u")
        word= word.replace("ä", "a")
        word= word.replace("ë", "e")
        word= word.replace("ï", "i")
        word= word.replace("ö", "o")
        word= word.replace("ü", "u")
        word= word.replace("Á", "a")
        word= word.replace("É", "e")
        word= word.replace("Í", "i") 
        word= word.replace("Ó", "o")
        word= word.replace("Ú", "u")
        return word 


if __name__ == '__main__':
    
    comentario = 'La comPUtadoRa no funciona #UnAsco'
    obj = TextCleaner(comentario)
    