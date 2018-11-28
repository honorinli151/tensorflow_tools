'''
File: /Users/lichenle/Desktop/MyProject/tensorflow_tools/datautils.py
Project: /Users/lichenle/Desktop/MyProject/tensorflow_tools
Created Date: Tuesday November 27th 2018
Author: Chenle Li
-----
Last Modified: 2018-11-27 11:22:23
Modified By: Chenle Li at <chenle.li@student.ecp.fr>
-----
Copyright (c) 2018 Chenle Li
-----
HISTORY:
Date               	  By     	Comments
-------------------	---------	---------------------------------------------------------
'''

import gensim 
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.test.utils import datapath

def load_pretrained_model(Word2VecPath):  
    model = Word2Vec.load_word2vec_format(Word2VecPath, binary=True)
    return model


def load_pretrained_keyvec(Word2VecPath):
    wv_from_bin = KeyedVectors.load_word2vec_format(datapath(Word2Vec), binary=True)  # C binary format
    return wv_from_bin